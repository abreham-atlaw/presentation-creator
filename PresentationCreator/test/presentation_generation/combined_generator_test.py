import typing

import unittest

from lib.network.chatsonic import ChatSonicClient
from content_generation.content_summarizer import ContentSummarizer
from content_generation.content_generator import ContentGenerator
from presentation_generation.combined_generator import CombinedGenerator


class CombinedGeneratorTest(unittest.TestCase):

	TOKEN = "3ec663ae-0602-4778-a66f-2da86b670c60"
	FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/PresentationCreator/res/test_data/1.pdf"
	PAGE_RANGE = (25, 35)
	BATCH_SIZE = 5
	OUT_PATH = "C:/Users/user/Projects/presentation-creator/presentation-creator/PresentationCreator/res/test_data/out.pptx"

	def setUp(self) -> None:
		self.__generator = CombinedGenerator(ContentGenerator(ContentSummarizer(
			ChatSonicClient(
				self.TOKEN
			)
		)))

	def test_functionality(self):
		self.__generator.generate_from_file(
			file=self.FILE,
			out_path=self.OUT_PATH,
			start_page=self.PAGE_RANGE[0],
			end_page=self.PAGE_RANGE[1],
			batch_size=self.BATCH_SIZE
		)
