import typing
from abc import abstractmethod, ABC


class ContentGenerator(ABC):

	@abstractmethod
	def generate(self, *args, **kwargs) -> typing.List[typing.List[str]]:
		pass
