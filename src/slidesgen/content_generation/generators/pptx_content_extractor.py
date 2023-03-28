import math
import typing

from slidesgen.content_generation.extractors import FileContentExtractor, PPTXExtractor
from .extractor_based_generator import ExtractorBasedGenerator


class PPTXContentGenerator(ExtractorBasedGenerator):

	def __init__(self, max_points: typing.Optional[int] = None):
		super().__init__()
		self.__max_points = max_points

	def __filter_max_points(self, content: typing.List[str]) -> typing.List[typing.List[str]]:
		return [
			content[i*self.__max_points: (i+1)*self.__max_points]
			for i in range(math.ceil(len(content)/self.__max_points))
		]

	def __prepare_slide_content(self, content: str) -> typing.List[typing.List[str]]:
		points = content.split("\n")
		if self.__max_points is None:
			return [points]
		return self.__filter_max_points(points)

	def _prepare_content(self, content: typing.List[str]) -> typing.List[typing.List[str]]:
		prepared_content = []

		for slide_content in content:
			prepared_content.extend(self.__prepare_slide_content(slide_content))

		return prepared_content

	def _init_extractor(self) -> FileContentExtractor:
		return PPTXExtractor()
