from coord.client import BaseAPI
import requests


class Bike(BaseAPI):

	def __init__(self, *args):
		super(Bike, self).__init__(*args)
		self.BIKE_PATH = f'{self.BASE_URL}{self.endpoint["bike"]}'
	
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

		path = f'{self.BIKE_PATH}location?latitude={latitude}&longitude={longitude}&radius_km={radius_km}&{self.secret_key}'
		response = requests.get(path)
		return response.json()

	def location_info(self, location_id, system_id):
		"""
		A bike location may be a single bike station (which can have multiple docked bikes) or a single dockless bike itself.
		All working docks are returned, but only free and rentable dockless bikes are returned.
		:param location_id: int
		:param system_id: int
		:return: dict
		"""
		path = f'{self.BIKE_PATH}location?{system_id}&{location_id}'
		response = requests.get(path)
		return response.json()

	def rental_quote_info(self):
		pass

	def system_info(self):
		pass

	def pass_instances(self):
		pass

	def get_or_create_session(self):
		pass

	def single_session(self):
		pass
