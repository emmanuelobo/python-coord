class BaseAPI:

	BASE_URL = 'https://api.coord.co/v1'
	endpoint = {'bike': '/bike/'}

	def __init__(self, secret_key):
		self.secret_key = 'access_key=' + secret_key
