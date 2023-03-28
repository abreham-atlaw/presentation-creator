import typing
from abc import ABC, abstractmethod

from slidesgen.content_generation.extractors import FileContentExtractor
from .content_generator import ContentGenerator


class ExtractorBasedGenerator(ContentGenerator):

	def __init__(self):
		self.__extractor = self._init_extractor()

	@abstractmethod
	def _init_extractor(self) -> FileContentExtractor:
		pass

	@abstractmethod
	def _prepare_content(self, content: typing.List[str]) -> typing.List[typing.List[str]]:
		pass

	def generate(self, filepath: str, *extraction_args, **extraction_kwargs) -> typing.List[typing.List[str]]:
		content = self.__extractor.extract(filepath, *extraction_args, **extraction_kwargs)
		content = self._prepare_content(content)
		return content




