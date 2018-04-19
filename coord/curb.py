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
		path = f'{self.CURB_ENDPOINT}bybounds/all_rules?min_latitude={min_latitude}&max_latitude={max_longitude}&min_longitude={min_longitude}&max_longitude={max_longitude}' \
			   f'&temp_rules_window_start={temp_rules_window_start}&temp_rules_window_end={temp_rules_window_end}&primary_use=load_passengers&permitted_use={permitted_use}&vehicle_type=all&access_key={self.secret_key}'
		response = requests.get(path).json()

		return response
