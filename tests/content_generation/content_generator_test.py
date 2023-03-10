import typing

import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.content_summarizer import ContentSummarizer
from slidesgen.content_generation.content_generator import ContentGenerator


class ContentGeneratorTest(unittest.TestCase):

	TOKEN = "3ec663ae-0602-4778-a66f-2da86b670c60"
	# TOKEN = "c070f8ee-cb58-4d57-9b67-dc30c57ce50a"
	FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/1.pdf"
	PAGE_RANGE = (25, 35)
	BATCH_SIZE = 5

	def setUp(self) -> None:
		self.__generator = ContentGenerator(ContentSummarizer(
			ChatSonicClient(
				self.TOKEN
			)
		))

	def test_functionality(self):
		contents = self.__generator.generate(file=self.FILE, start_page=self.PAGE_RANGE[0], end_page=self.PAGE_RANGE[1], batch_size=self.BATCH_SIZE)
		self.assertTrue(isinstance(contents, list))