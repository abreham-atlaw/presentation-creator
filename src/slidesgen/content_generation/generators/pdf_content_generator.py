import typing

from slidesgen.content_generation.generators.content_summarizer import ContentSummarizer
from slidesgen.content_generation.extractors import PDFContentExtractor, FileContentExtractor
from .extractor_based_generator import ExtractorBasedGenerator


class PDFContentGenerator(ExtractorBasedGenerator):

	def __init__(self, content_summarizer: ContentSummarizer):
		super().__init__()
		self.__summarizer = content_summarizer

	def _init_extractor(self) -> FileContentExtractor:
		return PDFContentExtractor()

	def _prepare_content(self, content: typing.List[str]) -> typing.List[typing.List[str]]:
		summarized = []

		for con in content:
			summarized.append(self.__summarizer.summarize(con))

		return summarized
