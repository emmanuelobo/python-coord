
class BaseAPI:

	BASE_URL = 'https://api.coord.co/v1'
	endpoint = {'bike': '/bike/'}

	def __init__(self, secret_key):
		self.secret_key = 'access_key=' + secret_key


class Bike(BaseAPI):
	def location_search(self):
		pass

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
