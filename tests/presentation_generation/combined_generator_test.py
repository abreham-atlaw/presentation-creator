import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.generators import ContentSummarizer, PPTXContentGenerator, PDFContentGenerator
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

	PPTX_FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/in.pptx"

	def setUp(self) -> None:
		self.__pdf_generator = PDFContentGenerator(ContentSummarizer(
				ChatSonicClient(
					self.TOKEN
				)
			))

		self.__pptx_generator = PPTXContentGenerator(max_points=3)

		self.__combined_generator = CombinedGenerator(self.__pptx_generator, template=self.TEMPLATE)

	def test_pdf_generator(self):
		generator = CombinedGenerator(self.__pdf_generator, template=self.TEMPLATE)
		generator.generate_from_file(
			title=self.TITLE,
			file=self.FILE,
			out_path=self.OUT_PATH,
			start_page=self.PAGE_RANGE[0],
			end_page=self.PAGE_RANGE[1],
			batch_size=self.BATCH_SIZE,
		)

	def test_pptx_generator(self):
		generator = CombinedGenerator(self.__pptx_generator, template=self.TEMPLATE)
		generator.generate_from_file(
			title="Test",
			file=self.PPTX_FILE,
			out_path=self.OUT_PATH
		)
