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
          # target_subscribers = self.db_driver.get_subscribers(self.coord)
          subscribers = [1, 2, 3, 4] #subscriber_list = DBDriver.GetSubscribers(sms)
          for target in subscribers:
               print "Dispatcher.send(sms, " + str(target) + ")"

     def to_dictionary(self):
          convert = {"sender_number" : self.sender_number,
                     "body_text" : self.body_text,
                     "timestamp" : self.timestamp,
                     "latitude" : self.latitude,
                     "longitude" : self.longitude}
          return convert

     def save(self):
         pass
