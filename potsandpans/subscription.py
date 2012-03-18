#!/usr/bin/env python
from flask import render_template
from utility import get_mongodb_connection

class Subscription():
	def __init__(self, number, body, timestamp, latitude=None, longitude=None):
		self.number = number
		self.body = body 
		self.timestamp = timestamp

		if latitude is None and body is not None:
			self.parse()
		else:
			self.latitude = latitude
			self.longitude = longitude

	def parse(self):
		""" Parse an incoming message in the form "SUBSCRIBE -1.932091 1.309280" """
		sub = self.body.split(' ')
		if len(sub) == 3:
			self.latitude = float(sub[1])
			self.longitude = float(sub[2])
		else:
			self.latitude = None
			self.longitude = None
			raise Exception("Invalid message")
	
	def handle(self):
		return self.save()

	def to_dictionary(self):
		return {
			"number" : self.number,
			"timestamp" : self.timestamp,
			"latitude" : self.latitude,
			"longitude" : self.longitude 
		}
	
	def save(self):
		conn = get_mongodb_connection()
		subscriptions = conn.potsandpans.subscriptions
		if subscriptions.insert(self.to_dictionary()):
			return render_template('subscription_stored.twiml')
		else:
			return render_template('subscription_failed.twiml')

	@staticmethod
	def find_in_area(number, min_lat, min_long, max_lat, max_long):
		
		conn = get_mongodb_connection()
		query = {
			"latitude": {
				"$gt":min_lat, 
				"$lt":max_lat
			}, 
			"longitude": {
				"$gt": min_long, 
				"$lt": max_long
			},
			"number": {
				"$ne": number
			}
		}

		print query

		cursor = conn.potsandpans.subscriptions.find(query)

		print '\n\nfound %d subscriptions\n\n' % (cursor.count())

		subscriptions = []
		for record in cursor:
			subscriptions.append(Subscription(record['number'], None, record['timestamp'], record['latitude'], record['longitude']))

		return subscriptions
