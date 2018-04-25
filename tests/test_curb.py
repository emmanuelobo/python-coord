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
		self.min_latitude = 91368792.66790387
		self.max_latitude = 52984971.22108352
		self.min_longitude = -54565835.98300373
		self.max_longitude = 96118507.92665818

	@vcr.use_cassette('./fixtures/vcr_cassettes/test_curbs_rules_bounding_box.yaml', record_mode='all')
	def test_curbs_rules_bounding_box(self):
		url = f'https://api.coord.co/v1/search/curbs/bybounds/all_rules?min_latitude=44.444&max_latitude=44.444&min_longitude=44.444&max_longitude=44.444&access_key={self.api_key}'
		actualResponse = requests.get(url).json()
		testResponse = self.curbs_api.curbs_rules_bounding_box(
			self.min_latitude, self.max_latitude, self.min_longitude, self.max_longitude)
		self.assertIsInstance(testResponse, dict)
		self.assertDictEqual(actualResponse, testResponse)

	@vcr.use_cassette('./fixtures/vcr_cassettes/test_curbs_rules_bounding_box_at_particular_time.yaml', record_mode='all')
	def test_curbs_rules_bounding_box_at_particular_time(self):
		testResponse = self.curbs_api.curbs_rules_bounding_box_at_particular_time(min_latitude=self.min_latitude, max_latitude=self.max_latitude,
																				  min_longitude=self.min_longitude, max_longitude=self.max_longitude)
		self.assertIsInstance(testResponse, dict)



	@vcr.use_cassette('./fixtures/vcr_cassettes/test_single_curb_rules.yaml')
	def test_single_curb_rules(self):
		pass


	@vcr.use_cassette('./fixtures/vcr_cassettes/test_single_curb_rules_certain_time.yaml')
	def test_single_curb_rules_certain_time(self):
		pass


	@vcr.use_cassette('./fixtures/vcr_cassettes/test_curb_rules_near_location.yaml')
	def test_curb_rules_near_location(self):
		pass


	@vcr.use_cassette('./fixtures/vcr_cassettes/test_curb_rules_at_certain_time_near_location.yaml')
	def test_curb_rules_at_certain_time_near_location(self):
		pass


if __name__ == "__main__":
	unittest.main()
