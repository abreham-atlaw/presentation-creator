import unittest

from slidesgen.content_generation.extractors import PDFContentExtractor


class PDFExtractorTest(unittest.TestCase):

	FILE = "/tests/res/test_data/1.pdf"
	PAGE_RANGE = (25, 100)
	BATCH_SIZE = 5

	def setUp(self) -> None:
		self.__extractor = PDFContentExtractor()

	def test_functionality(self):
		paragraphs = self.__extractor.extract(file=self.FILE, start_page=self.PAGE_RANGE[0], end_page=self.PAGE_RANGE[1], batch_size=self.BATCH_SIZE)
		self.assertTrue(isinstance(paragraphs, list))
