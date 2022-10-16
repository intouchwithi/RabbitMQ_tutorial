#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing = sys.argv[1] if len(sys.argv) > 1 else 'anonymus.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(
    exchange='topic_logs',
    routing_key=routing,
    body=message
    )
print(" [x] Sent %r, %r" % (routing, message))
connection.close()
