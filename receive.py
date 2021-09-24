#!/usr/bin/env python
import pika, sys, os
import json
import pickle



def callback(ch, method, properties, body):
    decerialized = pickle.loads(body)
    filename = decerialized["name"]
    content =  decerialized["content"]

    filepath = "Receive_folder/" + filename
    f = open(filepath,"wb")
    f.write(content)
    f.close()
    print("File received")

def main():
    credentials = pika.PlainCredentials('the_user', 'The_pass')
    
    parameters = pika.ConnectionParameters('192.168.1.2',5672,'/',credentials)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

