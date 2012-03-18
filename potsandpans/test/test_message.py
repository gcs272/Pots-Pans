#!/usr/bin/env python
from potsandpans.message import Message
from potsandpans.subscription import Subscription
from potsandpans.alert import Alert
import unittest
import mock

class MessageTest(unittest.TestCase):
	def testConstructor(self):
		message = Message('123456', 'hello world')
		self.assertEquals('123456', message.get_number())

        def testIsSubscription(self):
                sub_upper_msg = Message('12345', "SUBSCRIBE 0 0")
                self.assertTrue(sub_upper_msg.is_subscription())
                sub_lower_msg = Message('12345', "subscribe 0 0")
                self.assertTrue(sub_lower_msg.is_subscription())
                sub_varied_msg = Message('12345', "sUbScRiBe 0 0")
                self.assertTrue(sub_varied_msg.is_subscription())
                non_sub_msg = Message('12345', "hello world")
                self.assertFalse(non_sub_msg.is_subscription())

        def testGetSubclass(self):
                sub_upper_msg = Message('12345', "SUBSCRIBE 0 0")
                subscription = sub_upper_msg.get_subclass()
                self.assertEqual(subscription.__class__, Subscription)
                self.assertNotEqual(subscription.__class__, Alert)
                non_sub_msg = Message('12345', "hello world")
                alert = non_sub_msg.get_subclass()
                self.assertEqual(alert.__class__, Alert)
                self.assertNotEqual(alert.__class__, Subscription)
