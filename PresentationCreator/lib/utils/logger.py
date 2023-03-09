from typing import *

from datetime import datetime
import os


class Logger:

	class Colors:
		PURPLE = '\033[95m'
		OKBLUE = '\033[94m'
		OKCYAN = '\033[96m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	def __init__(self, logging=True, logging_pid=True, logging_console=True, logging_file_path=None):

		self.__logging = logging
		self.__logging_pid = logging_pid
		self.__logging_console = logging_console
		self.__logging_file_path = logging_file_path
		if not self.__logging_console and self.__logging_file_path is None:
			raise ValueError("logging_file_path cannot be null when logging_console is false")

	def print(self, *args, color: Union[str, None] = None, prefix: Union[str, None] = None, **kwargs):
		if not self.__logging:
			return
		if color is None:
			color = Logger.Colors.ENDC
		if prefix is None:
			prefix = ""
		prefix = f"[{datetime.now()}] {prefix}"
		if self.__logging_pid:
			prefix = f"PID:{os.getpid()} {prefix}"
		if not self.__logging_console:
			kwargs["file"] = open(self.__logging_file_path, "a")
		print(color, prefix, *args, Logger.Colors.ENDC, **kwargs)
		if not self.__logging_console:
			kwargs["file"].close()

	def log_function(self, func, args, kwargs, prefix=None):
		self.info(f"Starting {func.__name__} with args={args}, kwargs={kwargs} ...", prefix=prefix)
		return_value = func(*args, **kwargs)
		self.info(f"Done {func.__name__} with args={args}, kwargs={kwargs} => returned {return_value}.", prefix=prefix)
		return return_value

	def logged_method(self, func):

		def wrapper(self, *args, **kwargs):
			args = (self,) + args
			return self.log_function(func, args, kwargs, prefix=f"{self.__class__.__name__}:")
		return wrapper

	def info(self, *args: Any, **kwargs: Any):
		self.print(*args, color=Logger.Colors.OKBLUE, **kwargs)

	def warning(self, *args: Any, **kwargs: Any):
		self.print(*args, Logger.Colors.WARNING, **kwargs)
	
	def error(self, *args: Any, **kwargs: Any):
		self.print(*args, Logger.Colors.FAIL, **kwargs)

	def success(self, *args: Any, **kwargs: Any):
		self.print(*args, Logger.Colors.OKGREEN, **kwargs)


default_logger = Logger()