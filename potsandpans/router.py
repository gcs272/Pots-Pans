class Sms:
    # [sender_number, lat, long, timestamp]
     @staticmethod
     def parse_type(body_text):
         if "subscribe" in body_text:
              return Subscription
         else:
              return Alert

class Subscription:
     def __init__(self, sender_number, body_text, timestamp):
          self.sender_number = sender_number
          self.body_text = body_text
          self.timestamp = timestamp
     def parse(self):
          sub = self.body_text.split(' ')
          if len(sub) == 3:
               #self.coord = sub[1], sub[2]
               self.latitude = sub[1]
               self.longitude = sub[0]
          else:
               self.latitude = None
               self.longitude = None
               print "Error: Incorrect number of parameters for subscriptions"
     def handle(self):
          pass
     def to_dictionary(self):
          convert = {"sender_number" : self.sender_number,
                     "timestamp" : self.timestamp,
                     "latitude" : self.latitude,
                     "longitude" : self.longitude}
          return convert
     def save(self):
          pass

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

def quick_test():          
     phone_number = 1234567890
     sub_sms_body = "subscribe 39.959141, -75.1513957"
     alert_sms_body = "Alert relevant parties"
     
     test_sms_list = [sub_sms_body, alert_sms_body]
     
     for sms_body in test_sms_list:
          sms_type = Sms.parse_type(sms_body)
          sms_request = sms_type(phone_number, sms_body, 0)
          sms_request.parse()
          # l1, l2 = sms.coord
          print sms_request.to_dictionary()
          sms_request.handle()
          #sms.store()

quick_test()
