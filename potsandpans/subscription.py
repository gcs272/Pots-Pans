#!/usr/bin/env python
from utility import get_mongodb_connection

class Subscription():
	def __init__(self, number, body, timestamp):
		self.number = number
		self.body = body 
		self.timestamp = timestamp
		self.parse()

	def parse(self):
		""" Parse an incoming message in the form "SUBSCRIBE -1.932091 1.309280" """
		sub = self.body.split(' ')
		if len(sub) == 3:
			self.latitude = sub[1]
			self.longitude = sub[2]
		else:
			self.latitude = None
			self.longitude = None
			raise Exception("Invalid message")
	
	def handle(self):
		print 'handling subscription'
		self.save()

	def to_dictionary(self):
		return {
			"number" : self.number,
			"timestamp" : self.timestamp,
			"latitude" : self.latitude,
			"longitude" : self.longitude 
		}
	
	def save(self):
		conn = get_mongodb_connection()
		subscriptions = conn.potsandpans.subscriptions
		print 'inserting'
		subscriptions.insert(self.to_dictionary())
		print 'inserted'
