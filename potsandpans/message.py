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

	def is_subscription():
		return ('SUBSCRIBE' in self.message or 'subscribe' in self.message)

	def get_subclass():
		if self.if_subscription():
			return Subscription(self.number, self.message, self.timestamp)
		else:
			return Alert(self.number, self.message, self.timestamp)
