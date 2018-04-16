import requests
from coord.client import BaseAPI


class Bike(BaseAPI):
	"""
	The Bike Share API is a comprehensive API that allows both getting information about bike share systems,
	including available bikes and prices, as well as actually booking bikes from those systems.
	"""

	def __init__(self, *args):
		super(Bike, self).__init__(*args)
		self.BIKE_PATH = f'{self.BASE_URL}{self.BIKE_ENDPOINT}'
	
	def location_search(self, latitude, longitude, radius_km, system_ids=None):
		"""
		Get a list of locations given the input parameters.
		Specify a search area by radius around a latitude and longitude, as well as any filter for specific systems.
		Each location will be a GeoJSON Feature, and aggregated into a GeoJSON FeatureCollection.

		:param latitude: float
		:param longitude: float
		:param radius_km: float
		:param system_ids: array
		:return: dict
		"""

		path = f'{self.BIKE_PATH}location?latitude={latitude}&longitude={longitude}&radius_km={radius_km}&{self.secret_key}'
		response = requests.get(path).json()
		self.check_api_key(response)

		return response

	def location_info(self, location_id, system_id):
		"""
		A bike location may be a single bike station (which can have multiple docked bikes) or a single dockless bike itself.
		All working docks are returned, but only free and rentable dockless bikes are returned.

		:param location_id: int
		:param system_id: int
		:return: dict
		"""
		path = f'{self.BIKE_PATH}location/{system_id}&{location_id}?{self.secret_key}'
		response = requests.get(path).json()
		self.check_api_key(response)

		return response

	def rental_quote_info(self, system_ids=None):
		"""
		Provide quotes for renting a bike, via different types of passes that you can buy.
		Quotes can be obtained for all systems or for specific systems.
		Quotes may be associated with specific regions within a system.
		Please keep in mind that both the quotes and usage fees associated with the quotes are estimates.

		:param system_ids: array
		:return: dict
		"""

		path = f'{self.BIKE_PATH}quote?{self.secret_key}'
		response = requests.get(path).json()
		self.check_api_key(response)

		return response

	def system_info(self, system_id):
		"""
		Bike systems are individual bike share systems, often per-region.Information is returned as a GeoJSON Feature.
		The geometry of the GeoJSON Feature is a MultiPolygon that defines the system's operational area.
		All bike systems have an operational area, in which bikes may be found and parked.
		For systems that require bikes be docked, this area is somewhat arbitrary, as bikes are only found at stations.
		In this case, the operational area is roughly the city or jurisdiction that the system covers.
		For semi-dockless and dockless systems that allow bikes to be parked anywhere, the operational area is very important and strictly defined. Often there are extra fees for parking outside of the operational area (also known as a "catchment area"), and almost all bikes should be within the area.Areas are returned as a GeoJSON MultiPolygon since areas may be discontiguous or have holes.

		:param system_id: int
		:return: dict
		"""

		path = f'{self.BIKE_PATH}system/{system_id}/{self.secret_key}'
		response = requests.get(path).json()
		self.check_api_key(response)

		return response

	def pass_instances(self, active=None):
		"""
		This method requires an authenticated user.
		See authentication section at https://coord.co/docs/bike for details of how to authenticate.
		Return all of a user's pass instances by default.
		Use the active parameter to filter by active/inactive passes.
		This endpoint can be used before renting a bike to see if the user already has any active pass and can be used to show a log of current and prior pass purchases.

		:param active: boolean
		:return: list
		"""
		if active is None:
			path = f'{self.BIKE_PATH}user/current/pass_instance?{self.secret_key}'
			response = requests.get(path, headers=self.AUTH_HEADER)
		elif active:
			path = f'{self.BIKE_PATH}user/current/pass_instance?active=true&{self.secret_key}'
			response = requests.get(path,  headers=self.AUTH_HEADER)
		elif not active:
			path = f'{self.BIKE_PATH}user/current/pass_instance?active=false&{self.secret_key}'
			response = requests.get(path, headers=self.AUTH_HEADER)

		return response

	def get_or_create_sessions(self):
		"""
		This method requires an authenticated user.
		See authentication section at https://coord.co/docs/bike for details of how to authenticate.
		See above for details of how to authenticate. Return all of a user's sessions by default.
		Use the active parameter to filter by active/inactive sessions.

		:return: list
		"""
		path = f'{self.BIKE_PATH}user/current/session?{self.secret_key}'
		response = requests.get(path).json()
		self.check_api_key(response)

		return response

	def single_session(self, session_id):
		"""
		Returns the requested bike session.

		:return: list
		"""

		path = f'{self.BIKE_PATH}session/{session_id}?{self.secret_key}'
		response = requests.get(path).json()[0]
		self.check_api_key(response)

		return response
