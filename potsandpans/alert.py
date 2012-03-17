from potsandpans import geo

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
          # subscriber = self.db_driver.get_subscriber(self.sender_number)
	  coords = geo.boundingBox(subscriber.latitude, subscriber.longitude, 10)
          #subscriber_list = DBDriver.GetSubscribers_inBox(sms)
          for target in subscribers:
                print "Dispatcher.send(" + str(target.number) + ", " + self.body_text + ")"
		# save message received
     def to_dictionary(self):
          convert = {"sender_number" : self.sender_number,
                     "body_text" : self.body_text}
     def save(self):
         pass
