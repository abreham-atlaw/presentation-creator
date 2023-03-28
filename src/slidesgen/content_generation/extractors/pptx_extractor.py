import typing

import pptx
from pptx.presentation import Presentation
from pptx.slide import Slide
from pptx.shapes.placeholder import SlidePlaceholder
from .file_content_extractor import FileContentExtractor


class PPTXExtractor(FileContentExtractor):

	@staticmethod
	def __extract_slide(slide: Slide) -> str:
		return max(([
			shape.text
			for shape in slide.shapes
			if isinstance(shape, SlidePlaceholder)
		]), key=lambda text: len(text))

	def extract(self, file_path: str, *args, **kwargs) -> typing.List[str]:
		presentation: Presentation = pptx.Presentation(file_path)
		return [
			self.__extract_slide(slide)
			for slide in presentation.slides
		]