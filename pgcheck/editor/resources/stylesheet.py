from __future__ import annotations

import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)


# TODO use a datclass, enum ?
class StyleTheme:
    """
    Library of variables to use in StyleSheet.
    """

    pass


class StyleSheet:
    """
     Qt StyleSheet system to style interface in a procedural way but extended.

     Stylesheet are stored with "variables" to be replaced. This allows to have the color
     defined at one place and used at multiple place in the stylesheet for example.

     A variable is defined as::

         "{color_name}"

     Where the whole variable will be replaced by its corresponding value.

     It's possible to pass argument along the variable after a color.
    Liek for colors, you can  override the alpha component by specifying a float after a colon::

         "{color_name:0.5}"

     Which in the example above will be replaced with ``rgba(X,X,X,124)``
    """

    def __init__(self, content: str):

        self._original_content = content
        """
        Unedited content of the stylesheet as given initially
        """

        self.content = content
        """
        Content of the stylesheet that can directly be used in ``widget.setStyleSheet()``
        """

    @classmethod
    def from_path(cls, path: Path) -> StyleSheet:
        content = path.read_text("utf-8")
        return cls(content)

    def find_variables(self, token_name) -> list[re.Match]:
        pattern = re.compile(rf'"\{{{token_name}(:[\w.-]+)?}}"')
        return list(pattern.finditer(self.content))

    def resolve(self, theme: StyleTheme):
        """
        Resolve all variables in the stylesheet using the given theme.

        Args:
            theme:
        """
        pass  # TODO

    def validate(self):
        """
        Raise an exception if the data stored is not as expected.
        """

        found_tokens = self.find_variables(r"[^\n]")
        if found_tokens:
            raise ValueError(
                f"The current stylesheet has tokens that are not replaced yet: "
                f"{[match.group() for match in found_tokens]}"
            )
