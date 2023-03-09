import typing

from .content_extractor import ContentExtractor
from .content_summarizer import ContentSummarizer


class ContentGenerator(ContentExtractor):

	def __init__(self, content_summarizer: ContentSummarizer, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__content_summarizer = content_summarizer

	def generate(self,  file: str, start_page=0, end_page=None, batch_size=1) -> typing.List[typing.List[str]]:
		contents = self.extract(file=file, start_page=start_page, end_page=end_page, batch_size=batch_size)

		summarized = []

		for content in contents:
			summarized.append(self.__content_summarizer.summarize(content))

		return summarized
