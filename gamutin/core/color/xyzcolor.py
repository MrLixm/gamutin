from __future__ import annotations

__all__ = ("XYZColor",)

import dataclasses
import logging
from typing import Literal
from typing import overload
from typing import Optional
from typing import Union

import colour
import numpy

from gamutin.core.color import RGBAData
from gamutin.core.colorspaces import RgbColorspace
from gamutin.core.colorspaces import Whitepoint
from gamutin.core.colorspaces import ChromaticAdaptationTransform


logger = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class XYZColor:
    """
    Dataclass to represent a color expressed under the CIE XYZ color model.

    Internal values are stored as floats.

    TODO research if not better to store numpy array instead of builtin floats. This
        would allow to store full images.

    Args:
        X: [-0-1+] range
        Y: [-0-1+] range
        Z: [-0-1+] range
        whitepoint: illuminant
        alpha: optional alpha values associated with the XYZ triplet. [0-1] range.

    References:
        - [1] https://en.wikipedia.org/wiki/CIE_1931_color_space
    """

    X: float
    Y: float
    Z: float
    whitepoint: Whitepoint
    alpha: Optional[float] = None

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}<(X={self.X}, Y={self.Y}, Z={self.Z}, {self.a})"
            f"at {hex(id(self))}>"
        )

    @property
    def a(self) -> Optional[float]:
        return self.alpha

    @classmethod
    def from_array(
        cls,
        array: numpy.ndarray,
        whitepoint: Whitepoint,
        alpha: Optional[float] = None,
    ) -> XYZColor:
        """

        Args:
            array:
                X,Y,Z triplet with an optional 4th alpha component.
                [X,Y,Z] or [X,Y,Z,a].
                XYZ channels are expressed in floats.
            whitepoint: illuminant
            alpha: optional alpha values associated with the XYZ triplet. [0-1] range.

        Returns:
            XYZColor instance corresponding to the given parameters.
        """

        if array.shape[0] == 4 and alpha is None:
            alpha = array[3]

        return cls(array[0], array[1], array[2], whitepoint=whitepoint, alpha=alpha)

    @classmethod
    def from_Rgba(cls, rgba: RGBAData):
        array = rgba.to_array(alpha=False)

        converted = colour.RGB_to_XYZ(
            array,
            illuminant_RGB=rgba.colorspace.whitepoint.coordinates,
            illuminant_XYZ=rgba.colorspace.whitepoint.coordinates,
            matrix_RGB_to_XYZ=rgba.colorspace.matrix_to_XYZ,
            chromatic_adaptation_transform=ChromaticAdaptationTransform.default.value,
            cctf_decoding=rgba.colorspace.transfer_functions.decoding,
        )
        return cls.from_array(
            array=converted,
            whitepoint=rgba.colorspace.whitepoint,
            alpha=rgba.alpha,
        )

    def copy(self) -> XYZColor:
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
            array(3,) == [X,Y,Z] or array(4,) == [X,Y,Z,a]
        """
        return numpy.array(self.to_float(alpha=alpha), dtype=numpy.core.float32)

    def to_Rgba(self, colorspace: RgbColorspace) -> RGBAData:
        array = self.to_array(alpha=False)
        converted = colour.XYZ_to_RGB(
            array,
            illuminant_XYZ=self.whitepoint.coordinates,
            illuminant_RGB=colorspace.whitepoint.coordinates,
            matrix_XYZ_to_RGB=colorspace.matrix_from_XYZ,
            chromatic_adaptation_transform=ChromaticAdaptationTransform.default.value,
            cctf_encoding=colorspace.transfer_functions.encoding,
        )
        return RGBAData.from_array(converted, colorspace=colorspace, alpha=self.alpha)

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
            (X,Y,Z) or (X,Y,Z,a) where components are floats
        """
        if alpha is False:
            return self.X, self.Y, self.Z

        if alpha is True and self.alpha is not None:
            return self.X, self.Y, self.Z, self.alpha

        return self.X, self.Y, self.Z, alpha
