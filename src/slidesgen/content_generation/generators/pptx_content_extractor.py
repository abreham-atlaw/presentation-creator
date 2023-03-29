import math
import typing

from slidesgen.content_generation.extractors import FileContentExtractor, PPTXExtractor
from slidesgen.content_generation.data import Content
from .extractor_based_generator import ExtractorBasedGenerator


class PPTXContentGenerator(ExtractorBasedGenerator):

	def __init__(self, max_points: typing.Optional[int] = None):
		super().__init__()
		self.__max_points = max_points

	def __filter_max_points(self, body: typing.List[str]) -> typing.List[typing.List[str]]:
		return [
			body[i * self.__max_points: (i + 1) * self.__max_points]
			for i in range(math.ceil(len(body) / self.__max_points))
		]

	def __prepare_slide_body(self, body: typing.List[str]) -> typing.List[typing.List[str]]:
		if self.__max_points is None:
			return [body]
		return self.__filter_max_points(body)

	def _prepare_content(self, contents: typing.List[Content]) -> typing.List[Content]:
		prepared_content = []

		for content in contents:
			prepared_content.extend([
				Content(title=content.title, body=body)
				for body in self.__prepare_slide_body(content.body)
			])

		return prepared_content

	def _init_extractor(self) -> FileContentExtractor:
		return PPTXExtractor()
