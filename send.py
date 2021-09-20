#!/usr/bin/env python
import pika
import psutil


f = open("Send_folder/big_image.jpg", 'rb')
i = f.read()

''')
The first thing we need to do is to establish a connection
with RabbitMQ server.
'''

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

'''
Next, before sending we need to make sure the recipient queue exists.
If we send a message to non-existing location, RabbitMQ will just
drop the message.
Let's create a hello queue to which the message will be delivered
'''
channel.queue_declare(queue='hello')

'''
This exchange is special ‒ it allows us to specify exactly to
which queue the message should go.
The queue name needs to be specified in the routing_key parameter
'''
channel.basic_publish(exchange='', routing_key='hello', body=i)

print(" [x] Sent 'Hello World!'")


'''
Before exiting the program we need to make sure the network
buffers were flushed and our message was actually delivered to RabbitMQ.
We can do it by gently closing the connection.
'''
connection.close()
