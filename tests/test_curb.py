import unittest
from unittest import TestCase

import requests
from decouple import config

from coord import Curb


class CurbsTest(TestCase):
	def setUp(self):
		self.api_key = config('API_KEY')
		self.curbs_api = Curb(self.api_key)

	def test_base_api(self):
		url = f'https://api.coord.co/v1/search/curbs/bybounds/all_rules?min_latitude=44.444&max_latitude=44.444&min_longitude=44.444&max_longitude=44.444&access_key={self.api_key}'
		actualResponse = requests.get(url).json()
		testResponse = self.curbs_api.curbs_rules_bounding_box(44.444, 44.444, 44.444, 44.444)
		print(f'testResponse: {testResponse}')
		print(f'actualResponse: {actualResponse}')
		self.assertIsInstance(testResponse, dict)
		self.assertDictEqual(actualResponse, testResponse)


if __name__ == "__main__":
	unittest.main()
