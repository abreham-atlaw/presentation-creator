import typing

from slidesgen.content_generation.content_generator import ContentGenerator
from slidesgen.presentation_generation.presentation_generator import PresentationGenerator


class CombinedGenerator(PresentationGenerator):

	def __init__(self, content_generator: ContentGenerator, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__content_generator = content_generator

	def generate_from_file(self, title: str, file: str, out_path: str, *args, **kwargs):
		contents = self.__content_generator.generate(file, *args, **kwargs)
		self.generate(title, contents, out_path)
