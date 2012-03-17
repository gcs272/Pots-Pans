#!/usr/bin/env python
from pymongo import Connection
from potsandpans.main import app
from twilio.rest import TwilioRestClient

mongodb_connection = None
twilio_client = None

def get_mongodb_connection():
	global mongodb_connection 

	if not mongodb_connection:
		mongodb_connection = Connection(app.config['MONGODB_HOSTNAME'], app.config['MONGODB_PORT'])
	return mongodb_connection

def set_mongodb_connection(connection):
	global mongodb_connection

	mongodb_connection = connection

def get_twilio_instance():
	global twilio_client

	if not twilio_client:
		twilio_client = TwilioRestClient(
