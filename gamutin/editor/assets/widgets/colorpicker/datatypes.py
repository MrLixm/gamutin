from __future__ import annotations

__all__ = (
    "ColorFloat",
    "ColorFloatTuple",
    "Color8Bit",
)

import logging
from abc import ABC

logger = logging.getLogger(__name__)


class BaseColorDataType(ABC):
    pass


class ColorFloat(BaseColorDataType):
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


class Color8Bit(BaseColorDataType):
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
