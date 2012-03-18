#!/usr/bin/env python
from potsandpans.subscription import Subscription
from potsandpans.alert import Alert
import datetime

class Message:
	def __init__(self, number, message):
			self.number = number
			self.message = message
			self.received = datetime.datetime.utcnow().isoformat()

	def get_number(self):
		return self.number

	def is_subscription(self):
		return ('subscribe' in self.message.lower())

	def is_friendrequest(self):
		words = self.message.split(' ')
		if len(words) > 0
			return ('friend+' == words[0].lower())
		else:
			return False

	def is_privatemsg(self)
		words = self.message.split(' ')
		if len(words) > 0:
			return 'shout' == words[0].lower()
		else:
			return False

	def get_subclass(self):
		if self.is_subscription():
			return Subscription(self.number, self.message, self.received)
		elif self.is_friendrequest(self):
			return Friend(self.number, self.message, self.received)
		elif self.is_privatemsg(self):
			return PrivateSMS(self.number, self.message, self.received)
		else:
			return Alert(self.number, self.message, self.received)
	
	def log_received(self, message_id, timestamp):
		conn = get_mongodb_connection()
		message = conn.potsandpans.message
		self.message = message.select(message_id)
		if self.message is not None:
			log = conn.potsandpans.log
			log.insert({"message_id" : message_id,
					"timestamp" : timestamp})
