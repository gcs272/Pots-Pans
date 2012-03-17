#!/usr/bin/env python
from potsandpans.message import Message
import unittest
import mock

class MessageTest(unittest.TestCase):
	def testConstructor(self):
		message = Message('123456', 'hello world')
		self.assertEquals('123456', message.get_number())
