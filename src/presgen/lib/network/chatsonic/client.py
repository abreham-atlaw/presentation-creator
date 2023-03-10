import typing

from presgen.lib.network.rest_interface import NetworkApiClient, Request
from .requests import SummaryRequest


class ChatSonicClient(NetworkApiClient):

	def __init__(self, token: str, *args, **kwargs):
		super().__init__(
			url="https://api.writesonic.com/v2/"
		)
		self.__token = token

	def summarize(self, text: str) -> str:
		return self.execute(
			SummaryRequest(text)
		)

	def __construct_headers(self, headers) -> typing.Dict[str, typing.Any]:
		if headers is None:
			headers = {}
		headers = headers.copy()
		headers["X-API-KEY"] = self.__token

		return headers

	def execute(self, request: Request, headers: typing.Optional[typing.Dict] = None):
		return super().execute(
			request,
			headers=self.__construct_headers(headers)
		)
