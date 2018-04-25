import unittest
from unittest import TestCase

import vcr
from decouple import config

from coord.tollway import Tollway


class TollwayTest(TestCase):
	def setUp(self):
		self.tollway_api = Tollway(config('API_KEY'))
		self.latitude = 47.610203
		self.longitude = -122.33677
		self.radius_km = 45
		self.route = {
			"departure_time": "2017-07-28T17:39:43.611Z",
			"steps": [
				{
					"encoded_polyline": "iywaHjemiVCDEFEHMP",
					"road_name": "Lake Washington Blvd E"
				},
				{
					"encoded_polyline": "gzwaHtfmiVCAWLYFUAs@S{@a@e@e@}@kAo@cAWi@g@eBm@gCcA{C]q@u@kAm@_Ag@q@s@gAg@aAUcAGgAA_CA_@JyDRiI`Bql@p@kHtB{Rv@oHfAcNvI}eAvOkkBbEwZlAoIp@{Et@cKhAmN",
					"road_name": "WA-520 E"
				},
				{
					"encoded_polyline": "s|vaHnm`iVXwAh@aFPwBD{@H{ABg@@e@?Q?QAWAQ@IBQBIDKHKj@ONKLAN?^AF?",
					"road_name": "84th Ave NE"
				}
			],
			"vehicle": {
				"axles": 2
			}
		}

	@vcr.use_cassette('./fixtures/vcr_cassettes/test_tolls_on_route.yaml', record_mode='all')
	def test_tolls_on_route(self):
		testResponse = self.tollway_api.tolls_on_route(self.route)
		self.assertIsInstance(testResponse, list)

	@vcr.use_cassette('./fixtures/vcr_cassettes/test_tolls_in_area.yaml', record_mode='all')
	def test_tolls_in_area(self):
		testResponse = self.tollway_api.tolls_in_area(latitude=self.latitude, longitude=self.longitude,
													  radius_km=self.radius_km)
		self.assertIsInstance(testResponse, list)


if __name__ == "__main__":
	unittest.main()
