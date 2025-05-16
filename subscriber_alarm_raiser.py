import pika
from log.custom_log import LOGGER

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs_exchange', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs_exchange', queue=queue_name, routing_key="Error")

LOGGER.info('[*] waiting for the messages')


def callback(ch, method, properties, body):
    LOGGER.info(f"[x] Alarm:::: {body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
