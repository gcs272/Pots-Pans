#!/usr/bin/env python
from potsandpans import geo
import math
import unittest

class GeoTest(unittest.TestCase):
	def test_degree_to_rad(self):
		rad = geo.deg2rad(180)
		self.assertTrue(3.14 < rad < 3.15)
