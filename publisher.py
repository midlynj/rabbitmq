import pika
import random
from log.custom_log import LOGGER

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs_exchange', exchange_type='direct')

severity = ["Error", "Warning", "Info", "Critical"]
messages = ["Error message", "Warning message", "Info message", "Critical message"]

for i in range(10):
    randomNum = random.randint(0, len(severity) - 1)
    LOGGER.info(randomNum)
    message = messages[randomNum]
    rk = severity[randomNum]
    channel.basic_publish(exchange='logs_exchange', routing_key=rk, body=message)
    LOGGER.info(f"[x] sent {message}")

channel.exchange_delete(exchange='logs_exchange', if_unused=False)

connection.close()
