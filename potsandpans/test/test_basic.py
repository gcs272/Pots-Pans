#!/usr/bin/env python
import unittest
import mock

class BasicTest(unittest.TestCase):
	def setUp(self):
		print 'setting up a test'
	
	def testAddition(self):
		self.assertEquals(4, 2 + 2)
	
	def testFailing(self):
		self.assertEquals(5, 2 + 2)
