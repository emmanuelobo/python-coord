import unittest
from unittest import TestCase

import requests
import vcr
from decouple import config

from coord import Curb


class CurbsTest(TestCase):
	def setUp(self):
		self.api_key = config('API_KEY')
		self.curbs_api = Curb(self.api_key)
		self.min_latitude_mock = 44.44
		self.max_latitude_mock = 44.44
		self.min_longitude_mock = 44.44
		self.max_longitude_mock = 44.44

	@vcr.use_cassette('./fixtures/vcr_cassettes/test_curbs_rules_bounding_box.yaml', record_mode='all')
	def test_curbs_rules_bounding_box(self):
		url = f'https://api.coord.co/v1/search/curbs/bybounds/all_rules?min_latitude=44.444&max_latitude=44.444&min_longitude=44.444&max_longitude=44.444&access_key={self.api_key}'
		actualResponse = requests.get(url).json()
		testResponse = self.curbs_api.curbs_rules_bounding_box(self.min_latitude_mock, self.max_latitude_mock, self.min_longitude_mock, self.max_longitude_mock)
		self.assertIsInstance(testResponse, dict)
		self.assertDictEqual(actualResponse, testResponse)
		


if __name__ == "__main__":
	unittest.main()
