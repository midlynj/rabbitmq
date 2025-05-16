import os
import pika
import sys

from log.custom_log import LOGGER


def main():
    # create connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    # create channel
    channel = connection.channel()
    # create queue if not exist
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        LOGGER.info(f"[x] received {body}")

        # associate callback method with message queue and delete message

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    # start consuming message
    LOGGER.info(" [*] waiting for the messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        LOGGER.info("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            LOGGER.warning("Exiting queue all data lost")
            os._exists(0)
