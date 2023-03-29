import typing
from abc import ABC, abstractmethod

from slidesgen.content_generation.data import Content


class FileContentExtractor(ABC):

	@abstractmethod
	def extract(self, file_path: str, *args, **kwargs) -> typing.List[Content]:
		pass
