__version__ = 0.3
__author__ = "Brandon Hiles"

import unittest

from tests.api.data_mining.test_SiteAvailability import SiteAvailabilityTestCases
from tests.api.data_mining.test_parser import ParserTestCases
from tests.api.data_mining.test_reuters import ReutersTestCases

# Run Unit Tests

def site_availability_suite():
    suite = unittest.TestSuite()
    suite.addTest(SiteAvailabilityTestCases('test_checkReutersSiteAvailability'))
    suite.addTest(SiteAvailabilityTestCases('test_checkWSJSiteAvailability'))
    return suite

def parser_suite():
    suite = unittest.TestSuite()
    suite.addTest(ParserTestCases('test_grabSiteMapUrls'))
    suite.addTest(ParserTestCases('test_parseSiteMapUrls'))
    suite.addTest(ParserTestCases('test_grabElements'))
    return suite

def reuter_suite():
    suite = unittest.TestSuite()
    suite.addTest(ReutersTestCases('test_extractText'))
    return suite
