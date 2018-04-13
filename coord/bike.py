from coord.client import BaseAPI
import requests


class Bike(BaseAPI):
	def location_search(self, latitude, longitude, radius_km, system_ids=None):
		"""
		Get a list of locations given the input parameters.
		Specify a search area by radius around a latitude and longitude, as well as any filter for specific systems.
		Each location will be a GeoJSON Feature, and aggregated into a GeoJSON FeatureCollection.
		:param latitude:
		:param longitude:
		:param radius_km:
		:param system_ids:
		:return:
		"""

		url = f'{self.BASE_URL}{self.endpoint["bike"]}location?latitude={latitude}&longitude={longitude}&radius_km={radius_km}&{self.secret_key}'
		response = requests.get(url)
		return response.json()

	def location_information(self):
		pass

	def rental_quote_information(self):
		pass

	def system_information(self):
		pass

	def get_pass_instances(self):
		pass

	def get_or_create_session(self):
		pass

	def get_single_session(self):
		pass
