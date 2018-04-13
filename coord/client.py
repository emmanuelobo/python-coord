import requests


class BaseAPI:

	BASE_URL = 'https://api.coord.co/v1'
	endpoint = {'bike': '/bike/'}

	def __init__(self, secret_key):
		self.secret_key = 'access_key=' + secret_key


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

		url = f'https://api.coord.co/v1/bike/location?latitude={latitude}&longitude={longitude}&radius_km={radius_km}&{self.secret_key}'
		response = requests.get(url)
		return response.content

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
