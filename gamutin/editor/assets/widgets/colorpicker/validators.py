from __future__ import annotations

__all__ = (
    "BaseColorValidator",
    "ColorFloatValidator",
    "ColorFloatTupleValidator",
    "ColorHexValidator",
    "ColorInt8Validator",
)

import abc
import re

from Qt import QtGui

from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import DEFAULT_COLOR


class BaseColorValidator(QtGui.QValidator):
    @abc.abstractmethod
    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        pass

    @abc.abstractmethod
    def fix(self, user_input: str) -> str:
        pass

    @abc.abstractmethod
    def to_color(self, user_input: str) -> RGBAData:
        pass

    @abc.abstractmethod
    def from_color(self, color: RGBAData) -> str:
        pass


class ColorFloatValidator(BaseColorValidator):
    """
    Validator for a floating point RGB tuple.

    Example of a valid string: ``0.1560 -0.2681 1.5041``
    """

    DECIMALS = 4
    DEFAULT_VALUE = 0.0
    SEPARATOR = " "

    def to_color(self, user_input: str) -> RGBAData:
        """
        Args:
            user_input: example: ``0.253 -0.1 0.005``
        """
        if not user_input:
            return DEFAULT_COLOR

        channels = user_input.split(self.SEPARATOR)
        channels = [float(channel) for channel in channels]
        return RGBAData(*channels)

    def from_color(self, color: RGBAData) -> str:
        return (
            f"{color.r:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{color.g:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{color.b:.{self.DECIMALS}f}"
        )

    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        if re.search("[^\d.\s-]", user_input):
            return self.Invalid

        return self.Acceptable

    def fix(self, user_input: str) -> str:
        """
        Convert the given string into a usable color.
        """
        if not user_input:
            return self.from_color(DEFAULT_COLOR)

        fixed_input = user_input.lstrip(" ")
        fixed_input = fixed_input.rstrip(" ")
        fixed_input = re.sub(r"\s{2,}", "", fixed_input)
        channels = fixed_input.split(" ")
        channel_number = len(channels)

        if channel_number > 3:
            # strip out additional channels
            channels = channels[:3]

        elif channel_number == 1:
            channels *= 3

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

        fixed_input = self.SEPARATOR.join(fixed_channels)
        color = self.to_color(fixed_input)
        return self.from_color(color)


class ColorFloatTupleValidator(ColorFloatValidator):
    """
    Validator for a floating point RGB tuple represented as python tuple.

    Example of a valid string: ``0.1560 -0.2681 1.5041``
    """

    DECIMALS = 4
    DEFAULT_VALUE = 0.0
    SEPARATOR = ", "

    def to_color(self, user_input: str) -> RGBAData:
        """
        Args:
            user_input: example: ``(0.253, -0.1, 0.005)``
        """

        if not user_input:
            return DEFAULT_COLOR

        user_input = user_input.lstrip("(").rstrip(")")
        channels = user_input.split(self.SEPARATOR)
        channels = [float(channel) for channel in channels]
        return RGBAData(*channels)

    def from_color(self, color: RGBAData) -> str:
        return (
            f"({color.r:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{color.g:.{self.DECIMALS}f}{self.SEPARATOR}"
            f"{color.b:.{self.DECIMALS}f})"
        )

    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        simplified_input = user_input.lstrip("(").rstrip(")")

        if re.search("[^\d.\s\-,]", simplified_input):
            return self.Invalid

        return self.Acceptable

    def fix(self, user_input: str) -> str:
        """
        Convert the given string into a usable color.
        """
        if not user_input:
            return self.from_color(DEFAULT_COLOR)

        fixed_str = user_input.lstrip("(").rstrip(")")
        fixed_str = fixed_str.replace(" ", "")
        channels = fixed_str.split(",")
        fixed_str = super().fix(" ".join(channels))
        color = self.to_color(fixed_str)
        return self.from_color(color)


class ColorInt8Validator(BaseColorValidator):
    """
    Validator for a 8bit integers RGB colors.

    Example of a valid string: ``126 0 255``
    """

    DEFAULT_VALUE = 0
    SEPARATOR = " "

    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        if re.search("[^\d\s]", user_input):
            return self.Invalid

        return self.Acceptable

    def to_color(self, user_input: str) -> RGBAData:
        """
        Args:
            user_input: example: ``0.253 -0.1 0.005``
        """
        if not user_input:
            return DEFAULT_COLOR

        channels = user_input.split(self.SEPARATOR)
        channels = [int(channel) for channel in channels]
        return RGBAData.from_int8(*channels)

    def from_color(self, color: RGBAData) -> str:
        color_tuple = color.to_int8(alpha=False)
        return (
            f"{color_tuple[0]}{self.SEPARATOR}"
            f"{color_tuple[1]}{self.SEPARATOR}"
            f"{color_tuple[2]}"
        )

    def fix(self, user_input: str) -> str:
        """
        Convert the given string into a usable color.
        """
        if not user_input:
            return self.from_color(DEFAULT_COLOR)

        fixed_input = user_input.lstrip(" ")
        fixed_input = fixed_input.rstrip(" ")
        fixed_input = re.sub(r"\s{2,}", "", fixed_input)
        channels = fixed_input.split(" ")
        channel_number = len(channels)

        if channel_number > 3:
            # strip out additional channels
            channels = channels[:3]

        elif channel_number == 1:
            channels *= 3

        elif channel_number < 3:
            # add missing channels with default value
            channels += [f"{int(self.DEFAULT_VALUE)}"] * (3 - channel_number)

        fixed_channels = []
        for channel in channels:
            # if a channel is more than 3 number it's usually a typo so just remove it
            fixed_channel = channel[:3]
            fixed_channel_value = int(fixed_channel)
            # clamp to 255
            fixed_channel_value = min(fixed_channel_value, 255)
            fixed_channels.append(str(fixed_channel_value))

        fixed_input = self.SEPARATOR.join(fixed_channels)
        color = self.to_color(fixed_input)
        return self.from_color(color)


class ColorHexValidator(BaseColorValidator):
    """
    Validator for a hexadecimal RGB colors.

    Example of a valid string: ``#78BD68``
    """

    def validate(self, user_input: str, cursor_pos: int) -> QtGui.QValidator.State:
        if not user_input.startswith("#"):
            return self.Invalid

        sanitized_input = user_input.lstrip("#").lower()

        if re.search("[^a-f0-9]", sanitized_input):
            return self.Invalid

        return self.Acceptable

    def to_color(self, user_input: str) -> RGBAData:
        """
        Args:
            user_input: example: ``#78BD68``
        """
        if not user_input:
            return DEFAULT_COLOR

        return RGBAData.from_hex(user_input)

    def from_color(self, color: RGBAData) -> str:
        return color.to_hex()

    def fix(self, user_input: str) -> str:
        """
        Convert the given string into a usable color.
        """
        if not user_input:
            return self.from_color(DEFAULT_COLOR)

        sanitized_user_input = user_input.lstrip("#").lower()
        sanitized_user_input = sanitized_user_input[:6]

        if len(sanitized_user_input) == 2:
            fixed_input = sanitized_user_input * 3
        else:
            fixed_input = sanitized_user_input.ljust(6, "0")

        return f"#{fixed_input}"
