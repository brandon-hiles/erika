__version__ = 0.1
__author__ = "Brandon Hiles"

import requests
import unittest

class SiteAvailabilityTestCases(unittest.TestCase):

    """
    A simple test suite to make sure that the websites of interest
    are available.

    Test: Send Signal to Server
    Expected Result: HTTP Code of 200
    """

    @classmethod
    def setUp(self):
        self.websites = ['https://www.reuters.com',
        'https://www.wsj.com']

    def test_checkReutersSiteAvailability(self):
        try:
            r = requests.head(self.websites[0])
            status= str(r.status_code)
            self.assertEqual(int(status), 200)
        except requests.ConnectionError:
            return "failed to connect"

    def test_checkWSJSiteAvailability(self):
        try:
            r = requests.head(self.websites[1])
            status= str(r.status_code)
            self.assertEqual(int(status), 200)
        except requests.ConnectionError:
            return "failed to connect"

    @classmethod
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
