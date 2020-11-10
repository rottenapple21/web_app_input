import pika
import sys
import json
from . import forms
import os

class Connect():
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://qqhlybbt:FAWyUwEJ0dmIDuAYN_Wg_sC9zo3IIRVR@finch.rmq.cloudamqp.com/qqhlybbt')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=json.dumps(data),
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ))
    print(" [x] Sent %r" % data)
    connection.close()
