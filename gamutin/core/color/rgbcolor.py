from __future__ import annotations

__all__ = ("RGBAData",)

import dataclasses
import logging
from typing import Literal
from typing import overload
from typing import Optional
from typing import Union

import numpy

from gamutin.core.colorspaces import RgbColorspace
from gamutin.core.colorspaces import sRGB_COLORSPACE
from gamutin.core.colorspaces import colorspace_to_colorspace
from gamutin.core.colorspaces import ChromaticAdaptationTransform
from gamutin.core.color.colordepth import convert8bitToFloat
from gamutin.core.color.colordepth import convertFloatTo8Bit

logger = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class RGBAData:
    """
    Dataclass to represent a color expressed under the R-G-B color model.

    Internal values are stored as floats expressed in the given colorspace.

    TODO research if not better to store numpy array instead of builtin floats. This
        would allow to store full images.

    Args:
        red: [-0-1+] range
        green: [-0-1+] range
        blue: [-0-1+] range
        colorspace: colorspace in which the R,G,B triplet is encoded in.
        alpha: optional alpha values associated with the RGB triplet. [0-1] range.
    """

    red: float
    green: float
    blue: float
    colorspace: Optional[RgbColorspace] = None
    alpha: Optional[float] = None

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}<({self.r}, {self.g}, {self.b}, {self.a})"
            f":{self.colorspace} at {hex(id(self))}>"
        )

    @property
    def r(self) -> float:
        return self.red

    @property
    def g(self) -> float:
        return self.green

    @property
    def b(self) -> float:
        return self.blue

    @property
    def a(self) -> Optional[float]:
        return self.alpha

    @classmethod
    def from_int8(
        cls,
        red: int,
        green: int,
        blue: int,
        alpha: Optional[float] = None,
    ) -> RGBAData:
        """
        Get a RGBColor instance from a 8bit RGB triplet. The triplet is assumed to
        always be encoded in sRGB(EOTF) colorspace.

        Args:
            red: 0-255 range
            green: 0-255 range
            blue: 0-255 range
            alpha: optional alpha values associated with the RGB triplet. [0-1] range.

        Returns:
            RGBColor instance corresponding to the given parameters.
        """
        new_array = convert8bitToFloat(
            numpy.array((red, green, blue), dtype=numpy.core.uint8)
        )
        return cls.from_array(new_array, colorspace=sRGB_COLORSPACE, alpha=alpha)

    @classmethod
    def from_hex(cls, hexadecimal: str, alpha: Optional[float] = None) -> RGBAData:
        """
        Get a RGBColor instance from a hexadecimal color encoding.

        Args:
            hexadecimal: with or without the "#"
            alpha: optional alpha values associated with the RGB triplet. [0-1] range.

        Returns:
            RGBColor instance corresponding to the given parameters.
        """

        hexadecimal = hexadecimal.lstrip("#")
        # SRC: https://stackoverflow.com/a/29643643/13806195
        r, g, b = tuple(int(hexadecimal[i : i + 2], 16) for i in (0, 2, 4))
        return cls.from_int8(r, g, b, alpha)

    @classmethod
    def from_array(
        cls,
        array: numpy.ndarray,
        colorspace: RgbColorspace,
        alpha: Optional[float] = None,
    ) -> RGBAData:
        """

        Args:
            array:
                R,G,B triplet with an optional 4th alpha component.
                [r,g,b] or [r,g,b,a].
                RGB channels are expressed in floats.
            colorspace: colorspace in which the R,G,B triplet is encoded in.
            alpha: optional alpha values associated with the RGB triplet. [0-1] range.

        Returns:
            RGBColor instance corresponding to the given parameters.
        """

        if array.shape[0] == 4 and alpha is None:
            alpha = array[3]

        return cls(array[0], array[1], array[2], colorspace=colorspace, alpha=alpha)

    def copy(self) -> RGBAData:
        """
        Returns:
            return a new instance copy of this one
        """
        return dataclasses.replace(self)

    def to_array(self, alpha: Union[bool, float] = True) -> numpy.ndarray:
        """
        Args:
            alpha:
                - If True, return the internal alpha value if not none at the end of the array. (size 4 or 3)
                - If False, always return a ndarray of size 3
                - If a float, return an array with the value passed (size 4)

        Returns:
            array(3,) == [r,g,b] or array(4,) == [r,g,b,a]
        """
        return numpy.array(self.to_float(alpha=alpha))

    @overload
    def to_float(self, alpha: float = ...) -> tuple[float, float, float, float]:
        ...

    @overload
    def to_float(self, alpha: Literal[False] = ...) -> tuple[float, float, float]:
        ...

    @overload
    def to_float(
        self,
        alpha: Literal[True] = ...,
    ) -> Union[tuple[float, float, float], tuple[float, float, float, float]]:
        ...

    def to_float(
        self,
        alpha: Union[bool, float] = True,
    ) -> Union[tuple[float, float, float], tuple[float, float, float, float]]:
        """
        Args:
            alpha:
                - If True, return the internal alpha value if not none at the end of the tuple. (len 4 or 3)
                - If False, always return a tuple of len 3
                - If a float, return a tuple with the value passed (len 4)

        Returns:
            (r,g,b) or (r,g,b,a) where component is a float
        """
        if alpha is False:
            return self.red, self.green, self.blue

        if alpha is True and self.alpha is not None:
            return self.red, self.green, self.blue, self.alpha

        return self.red, self.green, self.blue, alpha

    def to_hex(self) -> str:
        """
        Get a hexadecimal representation of the current color.

        Returns:
            hexadecimal color with the "#". Letters in lowercase.
        """
        r, g, b = self.to_int8(alpha=False)
        # SRC: https://stackoverflow.com/a/3380754/13806195
        return "#{0:02x}{1:02x}{2:02x}".format(r, g, b)

    def to_int8(
        self,
        alpha: Union[bool, float] = True,
    ) -> Union[tuple[int, int, int], tuple[int, int, int, float]]:
        """
        Return an RGB(A) triplet encoded with 8bit values. [0-255]

        Args:
            alpha:
                - If True, return the internal alpha value if not none at the end of the tuple. (len 4 or 3)
                - If False, always return a tuple of len 3
                - If a float, return a tuple with the value passed (len 4)

        Returns:
            (r,g,b) or (r,g,b,a)
        """
        as_srgb = self.as_colorspace(sRGB_COLORSPACE)
        as_bits = convertFloatTo8Bit(as_srgb.to_array(alpha=False))
        red = as_bits[0].item()
        green = as_bits[1].item()
        blue = as_bits[2].item()

        if alpha is False:
            return red, green, blue

        if alpha is True and self.alpha is not None:
            return red, green, blue, self.alpha

        return red, green, blue, alpha

    def as_colorspace(
        self,
        target_colorspace: Optional[RgbColorspace],
        cat: Union[ChromaticAdaptationTransform, bool] = True,
    ) -> RGBAData:
        """
        Get a copy of this instance converted in the given colorspace.

        Args:
            target_colorspace:
                new colorspace to encode the color in. If None no transformation is performed.
            cat: chromatic adaptation transform to use. True to use default.

        Returns:
            new RGBColor instance encoded in the given colorspace
        """
        if self.colorspace is None or target_colorspace is None:
            return dataclasses.replace(self, colorspace=target_colorspace)

        if cat is True:
            cat = ChromaticAdaptationTransform.default
        elif cat is False:
            cat = None

        new_array = colorspace_to_colorspace(
            array=self.to_array(alpha=False),
            source_colorspace=self.colorspace,
            target_colorspace=target_colorspace,
            chromatic_adaptation_transform=cat,
        )

        return self.__class__.from_array(new_array, target_colorspace, self.alpha)
