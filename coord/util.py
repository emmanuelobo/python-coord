from coord.exceptions import InvalidAPIKeyException


class Utility:

	@staticmethod
	def check_api_key(obj):
		invalid_key_msg = "Forbidden: Coord API calls must include an access_key or an Authorization header"
		if invalid_key_msg in obj.values():
			raise InvalidAPIKeyException()
