import unittest

from slidesgen.lib.network.chatsonic import ChatSonicClient
from slidesgen.content_generation.generators import PPTXContentGenerator


class PPTXContentGeneratorTest(unittest.TestCase):

	FILE = "../../res/test_data/out.pptx"

	def setUp(self) -> None:
		self.__generator = PPTXContentGenerator()

	def test_functionality(self):
		contents = self.__generator.generate(filepath=self.FILE)
		self.assertTrue(isinstance(contents, list))
