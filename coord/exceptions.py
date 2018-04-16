

class InvalidAPIKeyException(Exception):
	"""
	Exception is thrown when the user has not entered a valid API key
	"""

	def __init__(self):
		Exception.__init__(self, "Invalid API key. "
								 "Please ensure that you using a valid API Key. "
								 "You can generate one at https://coord.co/docs/")


class InvalidEmailFormatException(Exception):
	"""
	Exception is thrown when the user enters an email address in an invalid format.
	"""
	def __init__(self):
		Exception.__init__(self, "Improper E-mail Format. "
								 "Please ensure that you enter a valid email address in the correct format.")
