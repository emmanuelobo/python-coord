import requests

from coord.client import BaseAPI


class Tollway(BaseAPI):
	"""
	The Tolls API is a read-only service to answer questions about the prices and locations of toll roads.
	Some tolls are charged at single points, so you pay them when you cross a toll gate or pass a toll booth.
	Other tolls are distance-based: the amount that you pay depends on where you enter a toll road and also where you exit.
	Some toll roads charge different prices by time of day, and some are totally dynamic, changing their price depending on demand at a given time.
	Note that while we support distance based tolls that are applied using toll gates or booths, we currently do not support mileage-based user fees that are assessed based on odometer readings.
	"""

	def tolls_on_route(self, route):
		"""
		Get all toll rates corresponding to a single route

		:param route: dict
		:return: dict
		"""

		headers = {'Content-Type': 'application/json'}
		path = f'{self.TOLLWAY_ENDPOINT}route?{self.secret_key}'
		response = requests.post(path, data=route, headers=headers).json()

		return response

	def tolls_in_area(self, latitude, longitude, radius_km):
		"""
		Get all tolls in an area defined by a center location and a radius

		:param latitude: float
		:param longitude: float
		:param radius_km: float
		:return: dict
		"""
		path = f'{self.TOLLWAY_ENDPOINT}toll?latitude={latitude}&longitude={longitude}&radius_km={radius_km}&{self.secret_key}'
		response = requests.get(path).json()

		return response

	def toll_details(self, toll_id):
		"""
		Get the details (e.g. pricing) of a toll specified by toll's ID

		:param toll_id: int
		:return: dict
		"""
		path = f'{self.TOLLWAY_ENDPOINT}toll?id={toll_id}&{self.secret_key}'
		response = requests.get(path).json()

		return response
