from __future__ import annotations

__all__ = ("",)

import ast
import enum
import logging
import re

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui


from gamutin.editor.assets.widgets.colorspaceselector import ColorspaceSelector

logger = logging.getLogger(__name__)


class ColorFloat:
    """
    Represent a floating point RGB triplet that can easily be manipulated for UI integration.

    Defined in range [-0-1+]
    Displayed without any additional character where the channels are just split by a whitespace.
    """

    DECIMALS = 4
    SEPARATOR = " "

    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return (
            f"{self.r:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{self.g:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{self.b:.{self.DECIMALS}f}"
        )

    def as_tuple(self) -> tuple[float, float, float]:
        return self.r, self.g, self.b

    @classmethod
    def from_string(cls, color_str: str) -> ColorFloat:
        """
        Convert the properly formatted color_str string to a ColorFloat instance.

        Example of properly formatted: ``0.1560 -0.2681 1.5041``
        """
        channels = color_str.split(cls.SEPARATOR)
        channels = [float(channel) for channel in channels]
        return cls(*channels)


class ColorFloatTuple(ColorFloat):
    """
    Represent a floating point RGB triplet that can easily be manipulated for UI integration.

    Defined in range [-0-1+]
    Displayed as a python tuple.
    """

    SEPARATOR = ", "

    def __str__(self) -> str:
        return (
            f"({self.r:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{self.g:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{self.b:.{self.DECIMALS}f})"
        )

    @classmethod
    def from_string(cls, color_str: str) -> ColorFloatTuple:
        """
        Convert the properly formatted color_str string to a ColorFloat instance.

        Example of properly formatted: ``(0.1560, -0.2681, 1.5041)``
        """
        channels = ast.literal_eval(color_str)
        return cls(*channels)


class Color8Bit:
    """
    Represent a 8bit integer RGB triplet that can easily be manipulated for UI integration.

    Defined in range [0-255] even if not clamped.
    """

    SEPARATOR = " "

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return f"{self.r}{self.SEPARATOR}{self.g}{self.SEPARATOR}{self.b}"

    def as_tuple(self) -> tuple[int, int, int]:
        return self.r, self.g, self.b

    @classmethod
    def from_string(cls, color_str: str) -> Color8Bit:
        """
        Convert the properly formatted color_str string to a ColorFloat instance.

        Example of properly formatted: ``0.1560 -0.2681 1.5041``
        """
        channels = color_str.split(cls.SEPARATOR)
        channels = [int(channel) for channel in channels]
        return cls(*channels)


class ColorFloatValidator(QtGui.QValidator):
    """
    Validator for a floating point RGB tuple.

    Example of a valid string: ``0.1560 -0.2681 1.5041``
    """

    DECIMALS = 4
    DEFAULT_VALUE = 0.0

    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        if re.search("[^\d.\s-]", user_input):
            return self.Invalid

        return self.Acceptable

    def fix(self, user_input: str) -> ColorFloat:
        """
        Convert the given string into a usable color.
        """
        if not user_input:
            return ColorFloat(*((self.DEFAULT_VALUE,) * 3))

        fixed_str = user_input.lstrip(" ")
        fixed_str = fixed_str.rstrip(" ")
        fixed_str = re.sub(r"\s{2,}", "", fixed_str)
        channels = fixed_str.split(" ")
        channel_number = len(channels)

        if channel_number > 3:
            # strip out additional channels
            channels = channels[:3]

        elif channel_number < 3:
            # add missing channels with default value
            channels += [f"{self.DEFAULT_VALUE:.{self.DECIMALS}f}"] * (
                3 - channel_number
            )

        fixed_channels = []
        for channel in channels:
            minus_char_number = channel.count("-")

            if channel.startswith("-") and minus_char_number == 1:
                fixed_channel = channel

            else:
                fixed_channel = channel.replace("-", "")

                if channel.startswith("-"):
                    fixed_channel = "-" + fixed_channel

            dot_char_number = fixed_channel.count(".")
            if dot_char_number >= 2:
                before, after = fixed_channel.split(".", 1)
                fixed_channel = before + "." + after.replace(".", "")

            fixed_channels.append(fixed_channel)

        fixed_str = ColorFloat.SEPARATOR.join(fixed_channels)
        return ColorFloat.from_string(fixed_str)


class ColorFloatTupleValidator(QtGui.QValidator):
    """
    Validator for a floating point RGB tuple represented as python tuple.

    Example of a valid string: ``0.1560 -0.2681 1.5041``
    """

    DECIMALS = 4
    DEFAULT_VALUE = 0.0

    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        if not user_input.startswith("(") or not user_input.endswith(")"):
            return self.Invalid

        simplified_input = user_input.lstrip("(").rstrip(")")

        if re.search("[^\d.\s\-,]", simplified_input):
            return self.Invalid

        return self.Acceptable

    def fix(self, user_input: str) -> ColorFloatTuple:
        """
        Convert the given string into a usable color.
        """
        if not user_input:
            return ColorFloatTuple(*((self.DEFAULT_VALUE,) * 3))

        fixed_str = user_input.lstrip("(").rstrip(")")
        fixed_str = fixed_str.replace(" ", "")
        channels = fixed_str.split(",")
        channel_number = len(channels)

        if channel_number > 3:
            # strip out additional channels
            channels = channels[:3]

        elif channel_number < 3:
            # add missing channels with default value
            channels += [f"{self.DEFAULT_VALUE:.{self.DECIMALS}f}"] * (
                3 - channel_number
            )

        fixed_channels = []
        for channel in channels:
            minus_char_number = channel.count("-")

            if channel.startswith("-") and minus_char_number == 1:
                fixed_channel = channel

            else:
                fixed_channel = channel.replace("-", "")

                if channel.startswith("-"):
                    fixed_channel = "-" + fixed_channel

            dot_char_number = fixed_channel.count(".")
            if dot_char_number >= 2:
                before, after = fixed_channel.split(".", 1)
                fixed_channel = before + "." + after.replace(".", "")

            fixed_channels.append(fixed_channel)

        fixed_str = ColorFloatTuple.SEPARATOR.join(fixed_channels)
        return ColorFloatTuple.from_string(fixed_str)


class ColorDisplayFormat(enum.Enum):
    float = "0.0"
    tuple = "(0.0,)"
    integer = "255"
    hexadecimal = "#hex"


class ColorValueLineEdit(QtWidgets.QLineEdit):
    """
    A color tuple as a single row of values that can be displayed under different formats.
    """

    formats = ColorDisplayFormat

    def __init__(self, currentFormat: ColorDisplayFormat = None):
        super().__init__()
        self._format = currentFormat or ColorDisplayFormat.float
        self.returnPressed.connect(self.apply_validator_fix)
        self.bakeUI()

    def bakeUI(self):
        if self._format == self.formats.float:
            self.setValidator(ColorFloatValidator())

        elif self._format == self.formats.tuple:
            self.setValidator(ColorFloatTupleValidator())

        else:
            raise ValueError(f"Unsupported format {self._format}")

        if not self.text():
            self.apply_validator_fix()

        return

    def apply_validator_fix(self):
        new_color: ColorFloat = self.validator().fix(self.text())
        self.setText(str(new_color))
        return

    def get_color(self) -> ColorFloat:
        return ColorFloat.from_string(self.text())

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, format_value: ColorDisplayFormat):
        self._format = format_value


class ColorDisplayAdvancedWidget(QtWidgets.QWidget):
    """
    A widget aiming at displaying a color with its value under different represenations.

    The widget is not read-only, it's actually possible to edit the color from it.

    Diagram::

        _________________________________
        [           display colorspace ▽]
        ---------------------------------
                  *color preview*
        _________________________________
        (colorspace)      0.00 0.00 0.00
        ---------------------------------
                    [btn][btn][btn][btn]

    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.colorspace_display_widget = ColorspaceSelector()
        self.color_preview_frame = QtWidgets.QFrame()
        self.color_lineedit = ColorValueLineEdit()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.colorspace_display_widget)
        self.layout.addWidget(self.color_preview_frame)
        self.layout.addWidget(self.color_lineedit)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.color_preview_frame.setMinimumHeight(15)
        self.colorspace_display_widget.set_label_visible(False)
        # TODO see if re-enable needed
        self.colorspace_display_widget.set_force_linear_visible(False)
        # 4. Connections
        return

    def bakeUI(self):
        pass

    def set_color(self, color):
        pass

    def get_color(self, color):
        pass


def _test_interface():
    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)

    widget = ColorDisplayAdvancedWidget()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
