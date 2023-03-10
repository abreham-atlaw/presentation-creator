import typing

from dataclasses import dataclass


@dataclass
class Template:

	class Layouts:
		TITLE = 0
		TITLE_AND_CONTENT = 1
		SECTION_HEADER = 2
		TWO_CONTENT = 3
		COMPARISON = 4
		TITLE_ONLY = 5
		BLANK = 6
		CONTENT_WITH_CAPTION = 7
		PICTURE_WITH_CAPTION = 8
		END = 9

	path: typing.Optional[str]
	layouts: typing.Optional[typing.List[int]] = None

	def __post_init__(self):
		if self.layouts is None:
			self.layouts = DEFAULT_LAYOUT

	def get_layout(self, type_: int) -> int:
		return self.layouts.index(type_)


DEFAULT_LAYOUT = [
	Template.Layouts.TITLE,
	Template.Layouts.TITLE_AND_CONTENT,
	Template.Layouts.SECTION_HEADER,
	Template.Layouts.TWO_CONTENT,
	Template.Layouts.COMPARISON,
	Template.Layouts.TITLE_ONLY,
	Template.Layouts.BLANK,
	Template.Layouts.CONTENT_WITH_CAPTION,
	Template.Layouts.PICTURE_WITH_CAPTION,
]
