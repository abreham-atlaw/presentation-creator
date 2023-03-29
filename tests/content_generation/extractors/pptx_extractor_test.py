import unittest

from slidesgen.content_generation.extractors import PPTXExtractor


class PPTExtractorTest(unittest.TestCase):

	FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/in.pptx"
	PAGE_RANGE = (25, 100)
	BATCH_SIZE = 5

	def setUp(self) -> None:
		self.__extractor = PPTXExtractor()

	def test_functionality(self):
		paragraphs = self.__extractor.extract(file_path=self.FILE)
		self.assertTrue(isinstance(paragraphs, list))
