import unittest
from decouple import config
from coord import Bike, InvalidAPIKeyException


class BikeTests(unittest.TestCase):
	def setUp(self):
		self.bike_api = Bike(config('API_KEY'))

	def test_jwt_token(self):
		bike = Bike(config('API_KEY'), 'manny@gmail.com')
		self.assertIsNotNone(bike)
		self.assertIsNotNone(bike._jwt_token)
		self.assertGreater(len(bike._jwt_token), 0)

	def test_missing_apikey_exception(self):
		bike = Bike('test')
		info = bike.location_info
		try:
			self.assertRaises(InvalidAPIKeyException, info(482, 1))

		except InvalidAPIKeyException:
			pass

	def test_bike_location_search(self):
		response = self.bike_api.location_search(latitude=40.74286877312112, longitude=-73.98918628692627, radius_km=0.5)
		sub = {'id': 'CitiBike-3641'}
		self.assertIsInstance(response, dict)

	def test_bike_location_info(self):
		"""
		bike location information test
		:return:
		"""
		response = self.bike_api.location_info(location_id=482,system_id=1)
		subset = {"type": "Feature"}
		self.assertIsNotNone(response)
		self.assertIsInstance(response, dict)
		# self.assertIn(subset, response)



if __name__ == '__main__':
	unittest.main()