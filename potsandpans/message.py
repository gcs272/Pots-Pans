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

	def get_subclass(self):
		if self.is_subscription():
			return Subscription(self.number, self.message, self.received)
		else:
			return Alert(self.number, self.message, self.received)
