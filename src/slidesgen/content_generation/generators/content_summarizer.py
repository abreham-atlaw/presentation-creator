import typing

from slidesgen.lib.network.chatsonic import ChatSonicClient


class ContentSummarizer:

	def __init__(self, chatsonic: ChatSonicClient):
		self.__chatsonic = chatsonic

	def summarize(self, article: str) -> typing.List[str]:
		prepared_text = f"Summarize the following text to be suitable for lecture presentation.\n{article}"

		response: str = self.__chatsonic.chat(prepared_text)
		return [f"{point}." for point in response.split(". ")]

