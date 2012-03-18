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
		return self.message.lower().startswith('subscribe')

	def is_friendrequest(self):
		return self.message.lower().startswith('friend')

	def is_privatemsg(self):
		return self.message.lower().startswith('shout')

	def get_subclass(self):
		if self.is_subscription():
			return Subscription(self.number, self.message, self.received)
		elif self.is_friendrequest():
			return Friend(self.number, self.message, self.received)
		elif self.is_privatemsg():
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
