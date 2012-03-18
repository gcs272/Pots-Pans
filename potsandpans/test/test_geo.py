#!/usr/bin/env python
from potsandpans import geo
import math
import unittest

class GeoTest(unittest.TestCase):
	def test_degree_to_rad(self):
		rad = geo.deg2rad(180)
		self.assertTrue(3.14 < rad < 3.15)

	def test_addition(self):
		lat = 39.959141
		lng = -75.1513957
		rad = geo.boundingBox(lat, lng, 10)
		self.assertTrue(rad[0] < lat)
		self.assertTrue(rad[1] < lng)
		self.assertTrue(rad[2] > lat)
		self.assertTrue(rad[3] > lng)
