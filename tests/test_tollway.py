from unittest import TestCase

from decouple import config

from coord.tollway import Tollway


class TollwayTest(TestCase):
	def setUp(self):
		self.tollway_api = Tollway(config('API_KEY'))