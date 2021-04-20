#!/usr/bin/python3
import pika, os, sys, time
import subprocess

RABBIT_HOST = os.environ.get("RABBIT_HOST", "rabbit")
RABBIT_QUEUE = os.environ.get("RABBIT_HOST", "task_queue")


def main():
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(5)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    with pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST)) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=RABBIT_QUEUE, durable=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        print(f" i'm worker {sys.argv[1] if len(sys.argv)>1 else '(no id received)'}")

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=RABBIT_QUEUE, on_message_callback=callback)
        channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
