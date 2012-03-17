from potsandpans.message import Message
from potsandpans.alert import Alert
from potsandpans.subscription import Subscription

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
