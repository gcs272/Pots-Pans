#!/usr/bin/env python
class Subscription:
	def __init__(self, sender_number, body_text, timestamp):
		self.sender_number = sender_number
		self.body_text = body_text
		self.timestamp = timestamp
	
	def parse(self):
		sub = self.body_text.split(' ')
		if len(sub) == 3:
			self.latitude = sub[1]
			self.longitude = sub[0]
		else:
			self.latitude = None
			self.longitude = None
			print "Error: Incorrect number of parameters for subscriptions"
	
	def handle(self):
		pass

	def to_dictionary(self):
		convert = {"sender_number" : self.sender_number,
			"timestamp" : self.timestamp,
			"latitude" : self.latitude,
			"longitude" : self.longitude}
		return convert
	
	def save(self):
		pass
