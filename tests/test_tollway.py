from unittest import TestCase

from decouple import config

from coord.tollway import Tollway


class TollwayTest(TestCase):
	def setUp(self):
		self.tollway_api = Tollway(config('API_KEY'))
		self.latitude = 47.610203
		self.longitude = -122.33677
		self.radius_km = 45
