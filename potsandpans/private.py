from flask import render_template
from potsandpans.friend import Friend
from potsandpans.subscription import Subscription
from utility import get_mongodb_connection, get_twilio_instance
import datetime

class PrivateSMS:
	def __init__(self, number, body, timestamp):
		self.number = number
		self.body = body
		self.timestamp = datetime.datetime.utcnow().isoformat()
		
	def lookup_subscription(self):
		conn = get_mongodb_connection()
		cursor = conn.potsandpans.subscriptions.find({'number': self.number})
		if cursor.count() <= 0:
			return None
		else:
			record = cursor.next()
			return Subscription(record['number'], None, record['timestamp'], float(record['latitude']), float(record['longitude']))

	def handle(self):
		subscription = self.lookup_subscription()
		if subscription is None:
			return render_template('unknown_number.twiml')

		friends = Subscription.find_friends(subscription.number)
		listeners = 0
		for target in friends:
			try:
				client = get_twilio_instance()
				client.sms.messages.create(to=target.number, from_='+14155992671', body="%(number)s messaged: %(body)s" % ("number" : self.number, "body" : self.body))
				listeners += 1
			except Exception, e:
				pass

		client = get_twilio_instance()
		client.sms.messages.create(to=subscription.number, from_='+14155992671', body="Your alert was sent to %d friends." % (listeners))

	def to_dictionary(self):
		convert = {"number" : self.number,"body" : self.body}

	def save(self):
		conn = get_mongodb_connection()
                alerts = conn.potsandpans.alerts
		if alert.insert(self.to_dictionary()):
			return render_template('subscription_stored.twiml')
		else:
			return render_template('subscription_failed.twiml')

