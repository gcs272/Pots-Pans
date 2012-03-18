from potsandpans.alert import Alert
import unittest
import mock

class AlertTest(unittest.TestCase):
    def testConstructor(self):
        alert = Alert('1234567890', 'SUBSCRIBE (0, 0)', 0)
        self.assertEquals(alert.sender_number, '1234567890')
        self.assertEquals(alert.body_text, 'SUBSCRIBE (0, 0)')
        self.assertEquals(alert.timestamp, 0)
    def testParse(self):
        pass
    #def testToDictionary(self):
