import typing

import unittest

from presentation_generation.presentation_generator import PresentationGenerator


class PresentationGeneratorTest(unittest.TestCase):
	
	CONTENTS = [['Information communication technology has been used for more than a century.', 'Information has been a vital aspect of national and international political power since before Sun Tzu in the sixth century.', 'In the last 30 years the diffusion of information has increased in pace.', 'The first turning point in the information revolution of military affairs came during the first Gulf War..'], ['Most security studies works addressing cyberspace fall somewhere between ambivalence and alarmist.', 'Any policy- maker attempting to make a decision regarding the use of offensive cyber weapon systems would find that there is a lack of debate on how this new category of weapons can generate political benefits.', 'The cyber domain is of critical importance to the functioning of the national security of modern states..'], ['Politics is a zone of bargaining designed to influence others to change their policy positions to fit more closely with one’s own policy platforms.', 'In any given situation there are tools available to individuals to manipulate conditions to their advantage.', 'International politics is not immune to attempts by states to influence the policy positions of one another..']]
	OUT_PATH = "C:/Users/user/Projects/presentation-creator/presentation-creator/PresentationCreator/res/test_data/out.pptx"

	def setUp(self) -> None:
		self.__generator = PresentationGenerator()

	def test_functionality(self):
		self.__generator.generate(self.CONTENTS, self.OUT_PATH)
