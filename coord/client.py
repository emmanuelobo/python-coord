import requests
from coord.exceptions import InvalidAPIKeyException, InvalidEmailFormatException


class BaseAPI:

	BASE_URL = 'https://api.coord.co/v1'
	INVALID_KEY_MSG = "Forbidden: Coord API calls must include an access_key or an Authorization header"
	BIKE_ENDPOINT = f'{BASE_URL}/bike/'
	USER_ENDPOINT = f'{BASE_URL}/users/'
	CURB_ENDPOINT = f'{BASE_URL}/search/curbs/'
	BLANK = ''

	def __init__(self, secret_key, user=None):
		self.secret_key = 'access_key=' + secret_key

		if user is not None:
			path = f'{self.USER_ENDPOINT}testing/user_and_jwt?{self.secret_key}'
			headers = {'Content-Type': 'application/json'}
			body = {"user": {"email": user}}
			response = requests.post(path, headers=headers, json=body).json()
			if 601 in response.values():
				raise InvalidEmailFormatException()
			else:
				self._jwt_token = response['jwt_token']
				self.email = user
				self.AUTH_HEADER = {'Content-Type': 'application/json', 'Authorization': f'Bearer {self._jwt_token}'}
				self.link_account()

	def check_api_key(self, obj):
		"""
		Checks if the API Key that was entered is valid or not
		:param obj: dict
		"""
		if self.INVALID_KEY_MSG in obj.values():
			raise InvalidAPIKeyException()


	def create_user_session(self, email):
		"""
		Creates a new user session with a new jwt token. If there is already an existing email and jwt token then they are overridden.
		:param email: str
		"""
		path = f'{self.USER_ENDPOINT}testing/user_and_jwt?{self.secret_key}'
		headers = {'Content-Type': 'application/json'}
		body = {"user": {"email": email}}
		response = requests.post(path, headers=headers, json=body).json()
		if 601 in response.values():
			raise InvalidEmailFormatException()
		else:
			self._jwt_token = response['jwt_token']
			self.email = email
			self.link_account()


	def link_account(self):
		path = f'{self.USER_ENDPOINT}testing/user/current/provisioned_systems?{self.secret_key}'
		body = {"system_id": ["CitiBike"]}
		response = requests.put(path, headers=self.AUTH_HEADER, json=body).json()
		return response


