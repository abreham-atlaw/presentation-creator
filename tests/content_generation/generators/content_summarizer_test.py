import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.generators.content_summarizer import ContentSummarizer


class ContentSummarizerTest(unittest.TestCase):

	TOKEN = "c070f8ee-cb58-4d57-9b67-dc30c57ce50a"
	ARTICLE = open("/tests/res/test_data/agile_development.txt").read()

	def setUp(self) -> None:
		self.__content_generator = ContentSummarizer(
			ChatSonicClient(
				self.TOKEN
			)
		)

	def test_functionality(self):
		points = self.__content_generator.summarize(self.ARTICLE)
		self.assertTrue(isinstance(points, list))


