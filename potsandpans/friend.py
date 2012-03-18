#!/usr/bin/env python
from flask import render_template
from utility import get_mongodb_connection

class Friend():
	def __init__(self, number, body, timestamp, friendnum):
		self.number = number
		self.body = body 
		self.timestamp = timestamp
		self.friendnum = friendnum

		if friendnum is None and body is not None:
			self.parse()
		else:
			self.friendnum = friendnum

	def parse(self):
		""" Parse an incoming message in the form "Friend +18005551212" """
		sub = self.body.split(' ')
		if len(sub) == 2:
			self.friendnum = sub[1]
		else:
			self.friendnum = None
			raise Exception("Invalid message")
	
	def handle(self):
		return self.save()

	def to_dictionary(self):
		return {
			"number" : self.number,
			"timestamp" : self.timestamp,
			"friendnum" : self.friendnum
		}
	
	def save(self):
		conn = get_mongodb_connection()
		friends = conn.potsandpans.friends
		if friends.insert(self.to_dictionary()):
			return render_template('friend_stored.twiml')
		else:
			return render_template('friend_add_failed.twiml')

	@staticmethod
	def find_friends(number):
		conn = get_mongodb_connection()
		query = {"number": number}
		cursor = conn.potsandpans.friends.find(query)

		friends = []
		for record in cursor:
			friends.append(Friend(record['number'], None, record['timestamp'], record['friendnum']))

		return friends
