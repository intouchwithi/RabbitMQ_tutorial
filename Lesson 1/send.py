import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello_queue')

counter = 0
while True:
    time.sleep(random.randint(1,10))
    counter+=1
    msg = f'Message number {counter}'
    channel.basic_publish(exchange='',
                          routing_key='hello_queue',
                          body=msg)
    print(f"Sent '{msg}'")

connection.close()
