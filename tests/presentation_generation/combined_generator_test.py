import typing

import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.content_summarizer import ContentSummarizer
from slidesgen.content_generation.content_generator import ContentGenerator
from slidesgen.presentation_generation.combined_generator import CombinedGenerator
from slidesgen.presentation_generation.data import Template


class CombinedGeneratorTest(unittest.TestCase):

	TITLE = "Information Technology"
	TOKEN = "3ec663ae-0602-4778-a66f-2da86b670c60"
	# TOKEN = "c070f8ee-cb58-4d57-9b67-dc30c57ce50a"
	FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/1.pdf"
	PAGE_RANGE = (25, 35)
	BATCH_SIZE = 5
	OUT_PATH = "C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/out.pptx"
	TEMPLATE = Template(
		path="C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/TechTemplate.pptx",
		layouts=[
			Template.Layouts.TITLE,
			Template.Layouts.TITLE_AND_CONTENT,
			Template.Layouts.SECTION_HEADER,
			Template.Layouts.END
		]
	)

	def setUp(self) -> None:
		self.__generator = CombinedGenerator(
			ContentGenerator(ContentSummarizer(
				ChatSonicClient(
					self.TOKEN
				)
			)),
			template=self.TEMPLATE,)

	def test_functionality(self):
		self.__generator.generate_from_file(
			title=self.TITLE,
			file=self.FILE,
			out_path=self.OUT_PATH,
			start_page=self.PAGE_RANGE[0],
			end_page=self.PAGE_RANGE[1],
			batch_size=self.BATCH_SIZE,
		)
