from requests.exceptions import HTTPError, ConnectionError

from lib.utils.logger import default_logger


def network_call(func):

	def wrapper(*args, **kwargs):
		tries = 10  # TODO:
		while tries is None or tries > 0:
			try:
				return func(*args, **kwargs)
			except (HTTPError, ConnectionError) as e:
				default_logger.warning(f"Network Call {func.__name__} Failed.({e})")
				if tries is not None:
					tries -= 1
					default_logger.warning(f"Tries Left {tries}")

		raise HTTPError

	return wrapper
