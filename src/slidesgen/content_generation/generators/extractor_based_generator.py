import typing
from abc import ABC, abstractmethod

from slidesgen.content_generation.extractors import FileContentExtractor
from slidesgen.content_generation.data import Content
from .content_generator import ContentGenerator


class ExtractorBasedGenerator(ContentGenerator):

	def __init__(self):
		self.__extractor = self._init_extractor()

	@abstractmethod
	def _init_extractor(self) -> FileContentExtractor:
		pass

	@abstractmethod
	def _prepare_content(self, contents: typing.List[Content]) -> typing.List[Content]:
		pass

	def generate(self, filepath: str, *extraction_args, **extraction_kwargs) -> typing.List[Content]:
		contents = self.__extractor.extract(filepath, *extraction_args, **extraction_kwargs)
		contents = self._prepare_content(contents)
		return contents




