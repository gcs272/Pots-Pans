from potsandpans import geo
from potsandpans.subscription import Subscription
from utility import get_mongodb_connection
import datetime

class Alert:
	def __init__(self, number, body, timestamp):
		self.number = number
		self.body = body
		self.timestamp = datetime.datetime.utcnow().isoformat()
		self.subscription = None
	
	def lookup_subscription(self):
		conn = get_mongodb_connection()
		cursor = conn.potsandpans.subscriptions.find({'number': self.number})
		if cursor.count() <= 0:
			return None
		else:
			record = cursor.next()
			return Subscription(record['number'], None, record['timestamp'], record['latitude'], record['longitude'])

	def handle(self):
		subscription = self.lookup_subscription()
		if subscription is None:
			return render_template('unknown_number.twiml')

		print subscription.latitude
		print subscription.longitude
		
		coords = geo.boundingBox(subscription.latitude, subscription.longitude, 10)
		subscriber_list = Subscription.find_in_area(coords[0], coords[1], coords[2], coords[3])
		for target in subscribers:
			try:
				client = get_twilio_client()
				client.sms.messages.create(to=subscription.number, body="Alert: %s" % (self.body))
			except Exception, e:
				print "Sending failed (%s)" % e
			print "Dispatcher.send(" + str(target.number) + ", " + self.body_text + ")"
			# save message received

	def to_dictionary(self):
		convert = {"number" : self.number,"body" : self.body}

	def save(self):
		pass
