import typing

import unittest

from lib.network.chatsonic import ChatSonicClient
from content_generation.content_summarizer import ContentSummarizer
from content_generation.content_generator import ContentGenerator


class ContentGeneratorTest(unittest.TestCase):

	TOKEN = "3ec663ae-0602-4778-a66f-2da86b670c60"
	FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/PresentationCreator/res/test_data/1.pdf"
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