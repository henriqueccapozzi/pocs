#!/usr/local/bin/python
import pika, os, json, sys

RABBIT_HOST = os.environ.get("RABBIT_HOST", "rabbit")
RABBIT_QUEUE = os.environ.get("RABBIT_HOST", "task_queue")


with pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST)) as connection:
    channel = connection.channel()
    channel.queue_declare(queue=RABBIT_QUEUE, durable=True)
    
    message = " ".join(sys.argv[1:]) or "Hello World!"

    channel.basic_publish(
            exchange="",
            routing_key=RABBIT_QUEUE,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode = 2, # make message persistent
            ))

    print(" [x] Sent %r" % message)
