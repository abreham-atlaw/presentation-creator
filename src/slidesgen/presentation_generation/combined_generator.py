import typing

from slidesgen.content_generation.content_generator import ContentGenerator
from slidesgen.presentation_generation.presentation_generator import PresentationGenerator


class CombinedGenerator(PresentationGenerator):

	def __init__(self, content_generator: ContentGenerator):
		super().__init__()
		self.__content_generator = content_generator

	def generate_from_file(self, file: str, out_path: str, template: str = None, *args, **kwargs):
		contents = self.__content_generator.generate(file, *args, **kwargs)
		self.generate(contents, out_path, template)
