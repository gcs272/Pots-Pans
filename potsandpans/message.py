#!/usr/bin/env python
import datetime

class Message:
	def __init__(self, number, message):
			self.number = number
			self.message = message
			self.received = datetime.datetime.utcnow().isoformat()
