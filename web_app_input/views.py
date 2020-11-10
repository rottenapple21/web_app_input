from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from . import forms
from django.contrib import messages
import pika
import sys
import json
import os

def welcome(request):
    return render(request, 'welcome.html')

def addlink(request):
    form = forms.AddLinkForm()

    if request.method == 'POST':
        form = forms.AddLinkForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            #produce message

            #url cloudamqp punya Tita
            #url = os.environ.get('CLOUDAMQP_URL', 'amqps://qqhlybbt:FAWyUwEJ0dmIDuAYN_Wg_sC9zo3IIRVR@finch.rmq.cloudamqp.com/qqhlybbt')

            #url cloudamqp punya tim rabbitmq
            url = os.environ.get('CLOUDAMQP_URL', 'amqps://jfslfmrp:BSnicbPhMxYUpuhg-c8IrMGkiUqF9BAQ@jaguar.rmq.cloudamqp.com/jfslfmrp')

            params = pika.URLParameters(url)
            connection = pika.BlockingConnection(params)
            channel = connection.channel()

            channel.queue_declare(queue='task_queue', durable=True)

            channel.basic_publish(exchange='',
                              routing_key='task_queue',
                              body=json.dumps(data), #serialize data to JSON
                              properties=pika.BasicProperties(
                                  delivery_mode = 2, #make message persistent
                              ))
            print(" [x] Sent %r" % data)
            connection.close()

            #form.save() #untuk save form di admin django
            messages.success(request, 'Berhasil Kirim Link!')
            return HttpResponseRedirect(reverse('addlink'))

    return render(request, 'addlink.html', {'form' : form})
