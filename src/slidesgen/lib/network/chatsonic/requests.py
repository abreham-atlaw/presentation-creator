import typing

import json

from slidesgen.lib.network.rest_interface import Request


class SummaryRequest(Request):

	def __init__(self, text: str):
		super().__init__(
			url="/business/content/summary",
			method=Request.Method.POST,
			get_params={
				"engine": "premium",
				"language": "en"
			},
			post_data=json.dumps({
				"article_text": text
			})
		)

	def _filter_response(self, response):
		return response[0].get("summary")


class ChatRequest(Request):

	def __init__(self, text: str, enable_memory=False):
		super().__init__(
			url="/business/content/chatsonic",
			method=Request.Method.POST,
			get_params={
				"engine": "premium",
			},
			post_data=json.dumps({
				"input_text": text,
				"enable_google_results": False,
				"enable_memory": enable_memory
			})
		)

	def _filter_response(self, response):
		return response.get("message")
