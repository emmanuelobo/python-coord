import requests

from coord.exceptions import InvalidAPIKeyException, InvalidEmailFormatException


class BaseAPI:

	BASE_URL = 'https://api.coord.co/v1'
	INVALID_KEY_MSG = "Forbidden: Coord API calls must include an access_key or an Authorization header"
	BIKE_ENDPOINT = '/bike/'
	USER_ENDPOINT = '/users/'
	CURB_ENDPOINT = '/curb/'

	def __init__(self, secret_key, user=None):
		self.secret_key = 'access_key=' + secret_key

		if user is not None:
			path = f'{self.BASE_URL}{self.USER_ENDPOINT}testing/user_and_jwt?{self.secret_key}'
			headers = {'Content-Type': 'application/json'}
			body = {"user": {"email": user}}
			response = requests.post(path, headers=headers, json=body).json()
			if 601 in response.values():
				raise InvalidEmailFormatException()
			else:
				self._jwt_token = response['jwt_token']
				self.email = user

	def check_api_key(self, obj):
		if self.INVALID_KEY_MSG in obj.values():
			raise InvalidAPIKeyException()
