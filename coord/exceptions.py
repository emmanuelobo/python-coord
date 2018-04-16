

class InvalidAPIKeyException(Exception):
	"""
	Exception is thrown when the user has not entered a valid API key
	"""

	def __init__(self):
		Exception.__init__(self, "Invalid API key. "
								 "Please ensure that you using a valid API Key. "
								 "You can generate one at https://coord.co/docs/")

