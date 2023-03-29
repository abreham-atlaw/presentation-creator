import typing
from abc import abstractmethod, ABC

from slidesgen.content_generation.data import Content

class ContentGenerator(ABC):

	@abstractmethod
	def generate(self, *args, **kwargs) -> typing.List[Content]:
		pass
