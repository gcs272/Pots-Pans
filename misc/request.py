#!/usr/bin/env python
import requests
import sys

if len(sys.argv) <= 2:
	print 'Usage: python request.py <event> <message>'
	sys.exit(-1)

if sys.argv[1] == 'subscribe':
	print 'subscribing'
	resp = requests.post('http://localhost:5000/sms', data={
		'From': '555-555-1212',
		'Body': sys.argv[2]
	})
else:
	print 'alerting'
	resp = requests.post('http://localhost:5000/sms', data={
		'From': '555-555-1212',
		'Body': sys.argv[2]
	})
print resp.content
