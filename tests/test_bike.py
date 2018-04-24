import unittest

import vcr
from decouple import config
from coord import Bike, InvalidAPIKeyException
from coord.exceptions import InvalidEmailFormatException


class BikeTests(unittest.TestCase):
	def setUp(self):
		self.bike_api = Bike(config('API_KEY'), 'manny@gmail.com')
		self.longitude_mock = -73.98918628692627
		self.latitude_mock = 40.74286877312112
		self.radius_km_mock = 0.5
		self.location_id_mock = 482
		self.system_id_mock = 1

	def test_jwt_token(self):
		bike = Bike(config('API_KEY'), 'manny@gmail.com')
		self.assertIsNotNone(bike)
		self.assertIsNotNone(bike._jwt_token)
		self.assertGreater(len(bike._jwt_token), 0)

	def test_invalid_email_format_exception(self):
		try:
			self.assertRaises(Bike(config('API_KEY'), 'test'))
		except InvalidEmailFormatException:
			pass

	@vcr.use_cassette('fixtures/vcr_cassettes/test_missing_apikey_exception.yaml')
	def test_missing_apikey_exception(self):
		bike = Bike('test')
		info = bike.location_info
		try:
			self.assertRaises(InvalidAPIKeyException, info(self.location_id_mock, self.system_id_mock))
		except InvalidAPIKeyException:
			pass

	@vcr.use_cassette('fixtures/vcr_cassettes/test_bike_location_search.yaml')
	def test_bike_location_search(self):
		response = self.bike_api.location_search(latitude=self.latitude_mock, longitude=self.longitude_mock,
												 radius_km=self.radius_km_mock)
		self.assertIsInstance(response, dict)
		self.assertIn('features', response)
		self.assertGreater(len(response['features']), 0)
		for feature in response['features']:
			print(feature['properties'], feature['geometry'], feature['type'])

	@vcr.use_cassette('fixtures/vcr_cassettes/test_bike_location_info.yaml')
	def test_bike_location_info(self):
		"""
		bike location information test
		:return:
		"""
		response = self.bike_api.location_info(location_id=self.location_id_mock, system_id=self.system_id_mock)
		self.assertIsNotNone(response)
		self.assertIsInstance(response, dict)

	@vcr.use_cassette('fixtures/vcr_cassettes/test_pass_instance.yaml')
	def test_pass_instance(self):
		response = self.bike_api.pass_instances()
		self.assertIsInstance(response, list)

	@vcr.use_cassette('fixtures/vcr_cassettes/test_active_pass_instances.yaml')
	def test_active_pass_instances(self):
		response = self.bike_api.pass_instances(active=True)
		self.assertIsInstance(response, list)

	@vcr.use_cassette('fixtures/vcr_cassettes/test_inactive_pass_instances.yaml')
	def test_inactive_pass_instances(self):
		response = self.bike_api.pass_instances(active=False)
		self.assertIsInstance(response, list)


if __name__ == '__main__':
	unittest.main()
