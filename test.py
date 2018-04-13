import unittest
import requests
from decouple import config
from coord.client import Bike


class BikeTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_base_url_endpoint(self):
		bike_api = Bike(config('API_KEY'))
		print(bike_api.BASE_URL)


if __name__ == '__main__':
	unittest.main()