import unittest
import requests
from decouple import config
from coord.client import Bike


class BikeTests(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_bike_location(self):
		bike_api = Bike(config('API_KEY'))
		response = bike_api.location_search(latitude=40.74286877312112, longitude=-73.98918628692627, radius_km=0.5)
		print(response)


if __name__ == '__main__':
	unittest.main()