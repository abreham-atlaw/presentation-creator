import typing

import fitz

from slidesgen.lib.utils.logger import default_logger
from slidesgen.content_generation.data import Content
from .file_content_extractor import FileContentExtractor


class PDFContentExtractor(FileContentExtractor):

	def __init__(self, paragraph_delimiter="\n"*4):
		self.__paragraph_delimiter = paragraph_delimiter

	def __choose_block(self, blocks: typing.Tuple) -> str:
		return max(blocks, key=lambda b: len(b[4]))[4]

	def __process_page(self, page: fitz.fitz.Page) -> typing.List[str]:
		content = self.__choose_block(page.get_text_blocks())
		paragraphs = content.split(self.__paragraph_delimiter)
		return paragraphs

	def __batch_paragraphs(self, paragraphs: typing.List[str], batch_size: int) -> typing.List[str]:
		batched = []
		for i in range(0, len(paragraphs), batch_size):
			batched.append(self.__paragraph_delimiter.join(paragraphs[i: i+batch_size]))
		return batched

	def extract(self, file: str, start_page=0, end_page=None, batch_size=1):
		document = fitz.open(file)
		if end_page is None:
			end_page = len(document)

		paragraphs = []

		for i in range(start_page, end_page+1):
			default_logger.info(f"Processing page{i}")
			paragraphs.extend(self.__process_page(document[i]))

		if batch_size != 1:
			paragraphs = self.__batch_paragraphs(paragraphs, batch_size)

		return [
			Content(None, [paragraph])
			for paragraph in paragraphs
		]
