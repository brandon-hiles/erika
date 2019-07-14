__version__ = 0.2
__author__ = "Brandon Hiles"

import unittest
import requests
import os

from src.api.data_mining.reuters import Reuters

class ReutersTestCases(unittest.TestCase):

	@classmethod
	def setUp(self):
		self.website = 'https://www.reuters.com/article/us-usa-trump-russia-scenarios/what-happens-if-mueller-finds-trump-fingerprints-in-russia-conspiracy-idUSKCN1QE2GL'
		self.reuters = Reuters(host='localhost', port=27017)

	def test_extractText(self):
		data = requests.get(self.website).content
		actual_data = self.reuters._extract_text(website=data)
		expected_data = open(os.getcwd() + '/tests/api/data_mining/text/reuters.txt', 'r').read()
		self.assertEqual(expected_data, actual_data)

	@classmethod
	def tearDown(self):
		pass