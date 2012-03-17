#!/usr/bin/env python
from flask import Flask, redirect, url_for, render_template, request
import json

app = Flask(__name__)
app.config.from_pyfile('/etc/potsandpans/main.cfg')

from potsandpans.message import Message

@app.route('/sms', methods=['POST'])
def sms():
	number = request.form.get('From', None)
	body = request.form.get('Body', None)

	if number and body:
		message = Message(number, body)
		message.get_subclass().handle()	# Handle the subscription or alert
		return json.dumps({'status': 'ok'})
	else:
		return json.dumps({'status': 'error', 'message': 'invalid sms'})
