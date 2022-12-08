from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Type, Any, Optional

from Qt import QtWidgets

from .properties import BaseQtProperty
from .theme import StyleTheme

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class StyleSheetVariable:

    name: str
    """
    Name of the variable, never empty.
    """

    overrides: dict[str, Any]
    """
    Overrides specified if any.
    """

    original_str: str
    """
    The full string as declared in the original stylesheet
    """


def parse_variables(stylesheet_content: str) -> list[StyleSheetVariable]:
    """
    From the given stylesheet string, return all the variable that can be found inside.

    A variable is declared exactly as::

        "{variable_name}"

    It is possible to specify *overrides* using a colon (they can be nested)::

        "{variable_name:override1=value1:override2=value2}"

    Args:
        stylesheet_content: qss looking string

    Returns:
        list of StyleSheetVariable instances, can have duplicates (same name, but not same overrides)
    """

    out_variable_list = []

    pattern = re.compile(r'"\{(\w+)(:[^}]+)*}"')
    variable_match_list = list(pattern.finditer(stylesheet_content))

    for variable_match in variable_match_list:

        override_str = variable_match.group(2)
        if override_str:

            override_pattern = re.compile(r"(\w+)=([^:]+)")
            override_match_list = list(override_pattern.finditer(override_str))

            overrides = {
                override_match.group(1): override_match.group(2)
                for override_match in override_match_list
            }
        else:
            overrides = {}

        variable = StyleSheetVariable(
            name=variable_match.group(1),
            overrides=overrides,
            original_str=variable_match.group(),
        )

        out_variable_list.append(variable)
        continue

    return out_variable_list


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
        """
        Read the content of the given file, assumed to be a qss file with potential variables.
        """
        content = path.read_text("utf-8")
        return cls(content)

    def apply_to(self, widget: QtWidgets.QWidget):
        """
        Apply this stylesheet to the given widget.
        """
        widget.setStyleSheet(self.content)

    def copy(self) -> StyleSheet:
        """
        Return an exact copy of this instance.
        """
        stylesheet_copy = StyleSheet(content=self.content)
        stylesheet_copy._original_content = self._original_content
        return stylesheet_copy

    def get_variables(self) -> dict[str, list[StyleSheetVariable]]:
        """
        Find and return all the variables in the stylesheet.

        A stylesheet with variables cannot be used yet with Qt.

        Returns:
            dict[variable_name, list[variable, ...]] : a same variable can be used
             multiple time through the stylesheet, hence the list.
        """

        variable_list = parse_variables(self.content)

        out_dict = {}
        for variable in variable_list:

            existing_value: Optional[list] = out_dict.get(variable.name)

            if existing_value is None:
                out_dict[variable.name] = [variable]
            else:
                existing_value.append(variable)

        return out_dict

    def reset(self):
        """
        Reset the stylesheet to its intial content given at instance time.

        The StyleSheet might have to be resolved again to replace variables.
        """
        self.content = self._original_content

    def resolve(self, theme: Type[StyleTheme]):
        """
        Resolve all variables in the stylesheet using the given theme.

        Args:
            theme:
        """
        variable_found_dict = self.get_variables()

        for theme_variable in theme.__all__():

            logger.debug(
                f"[{self.__class__.__name__}][resolve] started processing {theme_variable}"
            )
            stylesheet_variable_list: list[StyleSheetVariable]
            stylesheet_variable_list = variable_found_dict.get(theme_variable.name)
            if not stylesheet_variable_list:
                continue

            for stylesheet_variable in stylesheet_variable_list:

                property_value: BaseQtProperty = theme_variable.value
                property_value.apply_overrides(**stylesheet_variable.overrides)

                source_str = stylesheet_variable.original_str
                target_str = property_value.to_qss()

                self.content = self.content.replace(source_str, target_str)

                logger.debug(
                    f"[{self.__class__.__name__}][resolve] replaced {source_str} with {target_str}"
                )
                continue

            continue

    def validate(self):
        """
        Raise an exception if the data stored is not as expected.
        """

        found_variables = self.get_variables()
        if found_variables:
            raise ValueError(
                f"The current stylesheet has variables that are not replaced yet: "
                f"{list(found_variables.keys())}"
            )
