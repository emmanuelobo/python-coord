import requests

from coord.client import BaseAPI


class Curb(BaseAPI):
	"""
	The curb search API is a read-only service to describe what you can do on a curb.
	A curb is defined as one side of one roadway, so every street has at least two curbs (those with medians could have four, say).
	To see the curb search API in action and examine example requests and responses, check out our curb explorer tool, which is built entirely on this API!Curbs' geometries are positioned along the edge of the roadway, meaning that curbs meet at the corners of intersections.
	Curbs will never cross over each other. In general, curbs start and end at intersections, though behavior at 'T' intersections, alleys, pedestrian paths, and other crossings will vary by city.
	Every segment of a curb has, at any given time, a primary use and permitted uses.
	The primary use is what the regulator has defined as the desired use of the curb at that time.
	The permitted uses comprise everything that is allowed, including the primary use if any.
	We distinguish these so that we can tell apart areas signed, say, "PASSENGER LOADING ZONE" from those signed "NO STANDING" (which may also allow passenger pick-up and drop-off).
	"""

	def __init__(self, *args):
		super(Curb, self).__init__(*args)

	def curbs_rules_bounding_box(self, min_latitude, max_latitude, min_longitude, max_longitude,
								 temp_rules_window_start=None, temp_rules_window_end=None, primary_use=None,
								 permitted_use=None, vehicle_type=None):
		"""
		Find the rules for all curbs within a bounding box

		:param min_latitude: float
		:param max_latitude: float
		:param min_longitude: float
		:param max_longitude: float
		:param temp_rules_window_start: str
		:param temp_rules_window_end: str
		:param primary_use: str
		:param permitted_use: str
		:param vehicle_type: str
		:return: dict
		"""
		path = (
			f'{self.CURB_ENDPOINT}bybounds/all_rules?'
			f'min_latitude={min_latitude}'
			f'&max_latitude={max_latitude}'
			f'&min_longitude={min_longitude}'
			f'&max_longitude={max_longitude}'
			+ (f'&temp_rules_window_start={temp_rules_window_start}' if temp_rules_window_start is not None else '')
			+ (f'&temp_rules_window_end={temp_rules_window_end}' if temp_rules_window_end is not None else '')
			+ (f'&primary_use={primary_use}' if primary_use is not None else '')
			+ (f'&permitted_use={permitted_use}' if permitted_use is not None else '')
			+ (f'&vehicle_type={vehicle_type}' if vehicle_type is not None else '')
		)
		response = requests.get(path).json()

		return response


	def curbs_rules_bounding_box_at_particular_time(self, min_latitude, max_latitude, min_longitude, max_longitude, time=None,
								 primary_use=None, permitted_use=None, vehicle_type=None, duration_h=None):
		"""
		Find the rules for all curbs within a bounding box at a particular time.

		:param min_latitude:
		:param max_latitude:
		:param min_longitude:
		:param max_longitude:
		:param time:
		:param primary_use:
		:param permitted_use:
		:param vehicle_type:
		:param duration_h:
		:return:
		"""


	def single_curb_rules(self, id, temp_rules_window_start=None, temp_rules_window_end=None):
		"""
		Find the rules on a single curb.

		:param id:
		:param temp_rules_window_start:
		:param temp_rules_window_end:
		:return:
		"""


	def single_curb_rules_certain_time(self, id, time=None):
		"""
		Find the rules on a single curb at a certain time.

		:param id:
		:param time:
		:return:
		"""


	def curb_rules_near_location(self, latitude=None, longitude=None, radius_km=None, temp_rules_window_start=None, temp_rules_window_end=None,
									primary_use=None, permitted_use=None, vehicle_type=None):
		"""
		Find all of the curbs within a given radius of a particular point,
		and return all of their rules across all times of day, days of the week, times of year, etc.

		:param latitude:
		:param longitude:
		:param radius_km:
		:param temp_rules_window_start:
		:param temp_rules_window_end:
		:param primary_use:
		:param permitted_use:
		:param vehicle_type:
		:return:
		"""


	def curb_rules_at_certain_time_near_location(self, latitude=None, longitude=None, radius_km=None, time=None, primary_use=None,
												 vehicle_type=None, duration_h=None):
		"""
		Find the rules for a given curb at a given time and on a given day.
		You can also use this to find all of the places that it is possible to perform a given action (for instance, find all the loading zones, or everywhere with two-hour parking).

		:param latitude:
		:param longitude:
		:param radius_km:
		:param time:
		:param primary_use:
		:param vehicle_type:
		:param duration_h:
		:return:
		"""
