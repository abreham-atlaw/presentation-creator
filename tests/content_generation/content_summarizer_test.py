import typing

import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.content_summarizer import ContentSummarizer


class ContentSummarizerTest(unittest.TestCase):

	TOKEN = "3ec663ae-0602-4778-a66f-2da86b670c60"
	ARTICLE = open("C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/agile_development.txt").read()

	def setUp(self) -> None:
		self.__content_generator = ContentSummarizer(
			ChatSonicClient(
				self.TOKEN
			)
		)

	def test_functionality(self):
		points = self.__content_generator.summarize(self.ARTICLE)
		self.assertTrue(isinstance(points, list))


