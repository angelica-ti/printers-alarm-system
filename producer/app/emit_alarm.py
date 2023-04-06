#!/usr/bin/env python
import pika

class Publisher:
    def __init__(self, config = { 'host': 'rabbitmq','port': 5672, 'exchange' : 'topic_logs'}):
        self.config = config
        
    def publish(self, routing_key, message):       
        connection = self.create_connection()
        # Create a new channel with the next available channel number or pass in a 
        # channel number to use 
        channel = connection.channel()
        # Creates an exchange if it does not already exist, and if the exchange exists,
        # verifies that it is of the correct and expected class.
        channel.exchange_declare(exchange=self.config['exchange'], exchange_type='topic')
        #Publishes message to the exchange with the given routing key
        channel.basic_publish(exchange=self.config['exchange'], routing_key=routing_key, body=message)
        print(" [x] Sent message %r for %r" % (message, routing_key))
        connection.close()
        
    def create_connection(self):
        credentials = pika.PlainCredentials('root', 'root')
        param = pika.ConnectionParameters(host=self.config['host'], credentials=credentials,
        port = self.config['port']) 
        return pika.BlockingConnection(param)


