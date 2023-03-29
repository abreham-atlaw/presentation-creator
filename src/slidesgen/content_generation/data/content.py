import typing

from dataclasses import dataclass


@dataclass
class Content:

	title: typing.Optional[str]
	body: typing.List[str]

	# TODO: ADD IMAGE...
