import typing
from abc import ABC, abstractmethod


class FileContentExtractor(ABC):

	@abstractmethod
	def extract(self, file_path: str, *args, **kwargs) -> typing.List[str]:
		pass
