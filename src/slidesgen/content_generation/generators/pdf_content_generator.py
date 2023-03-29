import typing

from slidesgen.content_generation.generators.content_summarizer import ContentSummarizer
from slidesgen.content_generation.extractors import PDFContentExtractor, FileContentExtractor
from slidesgen.content_generation.data import Content
from .extractor_based_generator import ExtractorBasedGenerator


class PDFContentGenerator(ExtractorBasedGenerator):

	def __init__(self, content_summarizer: ContentSummarizer):
		super().__init__()
		self.__summarizer = content_summarizer

	def _init_extractor(self) -> FileContentExtractor:
		return PDFContentExtractor()

	def _prepare_content(self, contents: typing.List[Content]) -> typing.List[Content]:
		return [
			Content(
				title=content.title,
				body=self.__summarizer.summarize(content.body)
			)
			for content in contents
		]

