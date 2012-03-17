from potsandpans import geo
from utility import get_mongodb_connection

class Alert:
     def __init__(self, sender_number, body_text, timestamp):
          self.sender_number = sender_number
          self.body_text = body_text
          self.timestamp = timestamp
     def parse(self):
          # subsciber_coord = self.db_driver.get_subscriber_coord(self.send_number)
          self.latitude = 0
          self.longitude = 0
     def handle(self):
	  conn = get_mongodb_connection()
          subscriber = conn.potsandpans.subscriber(self.sender_number)
	  coords = geo.boundingBox(subscriber.latitude, subscriber.longitude, 10)
          subscriber_list = conn.potsandpans.subscriber(coords[0], coords[1], coords[2], coords[3])
          for target in subscribers:
                print "Dispatcher.send(" + str(target.number) + ", " + self.body_text + ")"
		# save message received
     def to_dictionary(self):
          convert = {"sender_number" : self.sender_number,
                     "body_text" : self.body_text}
     def save(self):
         pass
