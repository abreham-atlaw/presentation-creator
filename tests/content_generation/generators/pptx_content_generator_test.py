import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.generators import PPTXContentGenerator


class PPTXContentGeneratorTest(unittest.TestCase):

	FILE = "C:/Users/user/Projects/presentation-creator/presentation-creator/tests/res/test_data/in.pptx"

	def setUp(self) -> None:
		self.__generator = PPTXContentGenerator(max_points=3)

	def test_functionality(self):
		contents = self.__generator.generate(filepath=self.FILE)
		self.assertTrue(isinstance(contents, list))
