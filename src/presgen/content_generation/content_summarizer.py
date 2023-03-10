import typing

from presgen.lib.network.chatsonic import ChatSonicClient


class ContentSummarizer:

	def __init__(self, chatsonic: ChatSonicClient):
		self.__chatsonic = chatsonic

	def summarize(self, text: str) -> typing.List[str]:
		summary = self.__chatsonic.summarize(text)
		points = [f"{point}." for point in summary.split(". ")]

		return points
