#!/usr/bin/env python
import unittest
import mock

class BasicTest(unittest.TestCase):
	def setUp(self):
		pass

	def testAddition(self):
		self.assertEquals(4, 2 + 2)
