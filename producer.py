import pika
from log.custom_log import LOGGER

# create connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# create channel
channel = connection.channel()

# create queue if not exist
channel.queue_declare(queue="hello")


# publish message
channel.basic_publish(exchange="", routing_key="hello", body="hello_world msg #1")
LOGGER.info("[x] Sent hello World")

# close connection
# auto closes channel
connection.close()
