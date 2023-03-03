from __future__ import annotations

__all__ = (
    "ColorFloatValidator",
    "ColorFloatTupleValidator",
)

import re

from Qt import QtGui

from gamutin.editor.assets.widgets.colorpicker.datatypes import ColorFloat
from gamutin.editor.assets.widgets.colorpicker.datatypes import ColorFloatTuple


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

        fixed_channels = [float(channel) for channel in fixed_channels]
        return ColorFloat(*fixed_channels)


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
        color = super().fix(" ".join(channels))
        return ColorFloatTuple(color.r, color.g, color.b)
