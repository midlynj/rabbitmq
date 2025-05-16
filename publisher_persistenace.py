import pika
import sys
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.confirm_delivery()

channel.exchange_declare(exchange='logs_exchange2', exchange_type='direct', durable=True)

severity = ["Error", "Warning", "Info", "Critical"]
messages = ["Error message", "Warning message", "Info message", "Critical message"]

for i in range(5):
    randomNum = random.randint(0, len(severity) - 1)
    message = messages[randomNum]
    rk = severity[randomNum]
    try:
        channel.basic_publish(exchange='logs_exchange2',
                              routing_key=rk,
                              body=message,
                              properties=pika.BasicProperties(
                                  delivery_mode=2  # Make Message Persistent
                              )
                              )
        print(f"[x] sent {message}")
    except pika.exceptions.ChannelClosed:
        print("Channel Closed")
    except pika.exceptions.ConnectionClosed:
        print("Connection Closed")

channel.exchange_delete(exchange='logs_exchange2', if_unused=False)

connection.close()
