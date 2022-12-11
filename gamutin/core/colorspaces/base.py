from __future__ import annotations

import dataclasses
from typing import Callable
from typing import Optional

import numpy
import colour

from gamutin.core.utils import simplify
from gamutin.core.colorspaces.categories import ColorspaceCategory


@dataclasses.dataclass
class BaseColorspaceComponent:
    """
    Every colorspace entity or component will be derived from this class.

    Expose 2 attributes :
    - name : a human-readable proper name to identify the object
    - name_simplified: the name but in a more simple syntax for easier typing.
    """

    name: str

    def __post_init__(self):
        self.name_simplified = simplify(self.name)


@dataclasses.dataclass
class Whitepoint(BaseColorspaceComponent):

    coordinates: numpy.ndarray
    """
    CIE xy coordinates as a ndarray(2,)
    """

    def __hash__(self) -> int:
        return (
            hash(self.__class__.__name__)
            + hash(self.name)
            + hash(repr(self.coordinates))
        )

    @classmethod
    def fromColourColorspace(cls, colour_colorspace: colour.RGB_Colourspace):
        return cls(
            colour_colorspace.whitepoint_name,
            colour_colorspace.whitepoint,
        )


@dataclasses.dataclass
class ColorspaceGamut(BaseColorspaceComponent):
    """
    Gamut/Primaries part of a specific colorspace.
    """

    matrix_to_XYZ: numpy.ndarray
    matrix_from_XYZ: numpy.ndarray

    def __hash__(self) -> int:
        return (
            hash(self.__class__.__name__)
            + hash(self.name)
            + hash(repr(self.matrix_to_XYZ))
            + hash(repr(self.matrix_from_XYZ))
        )

    @classmethod
    def fromColourColorspace(cls, colour_colorspace: colour.RGB_Colourspace):
        return cls(
            "Gamut " + colour_colorspace.name,
            colour_colorspace.matrix_RGB_to_XYZ,
            colour_colorspace.matrix_XYZ_to_RGB,
        )


@dataclasses.dataclass
class TransferFunctions(BaseColorspaceComponent):
    """
    Transfer function as decoding and encoding.
    """

    encoding: Optional[Callable]
    decoding: Optional[Callable]

    is_encoding_linear: bool = False
    is_decoding_linear: bool = False

    def __hash__(self) -> int:
        return (
            hash(self.__class__.__name__)
            + hash(self.name)
            + hash(self.encoding)
            + hash(self.decoding)
        )

    def __post_init__(self):
        super().__post_init__()

        if self.encoding is None:
            self.is_encoding_linear = True
        if self.decoding is None:
            self.is_decoding_linear = True

    @property
    def are_linear(self) -> bool:
        return self.is_encoding_linear and self.is_decoding_linear

    @classmethod
    def fromColourColorspace(cls, colour_colorspace: colour.RGB_Colourspace):
        return cls(
            name="CCTF " + colour_colorspace.name,
            encoding=colour_colorspace.cctf_encoding,
            decoding=colour_colorspace.cctf_decoding,
            is_encoding_linear=colour_colorspace.cctf_encoding
            == colour.linear_function,
            is_decoding_linear=colour_colorspace.cctf_decoding
            == colour.linear_function,
        )


TRANSFER_FUNCTIONS_LINEAR = TransferFunctions("CCTF Linear", None, None)


@dataclasses.dataclass
class RgbColorspace(BaseColorspaceComponent):

    gamut: Optional[ColorspaceGamut]
    whitepoint: Optional[Whitepoint]
    transfer_functions: Optional[TransferFunctions]

    categories: tuple[ColorspaceCategory]
    """
    To help sort the colorspace in an interface.
    """

    description: str
    """
    A bit more details on what/why for this colorspace.
    """

    def __hash__(self) -> int:
        return (
            hash(self.__class__.__name__)
            + hash(self.name)
            + hash(self.gamut)
            + hash(self.whitepoint)
            + hash(self.transfer_functions)
            + hash(self.categories)
            + hash(self.description)
        )

    @property
    def is_no_op(self) -> bool:
        """
        Return True if the colorspace should not be processed because it
        defines no transform for any component.
        """

        has_gamut = (
            self.gamut
            or self.gamut.matrix_from_XYZ != numpy.identity(3)
            or self.gamut.matrix_to_XYZ != numpy.identity(3)
        )

        has_whitepoint = self.whitepoint is not None

        has_transfer_function = (
            self.transfer_functions
            or self.transfer_functions.decoding
            or self.transfer_functions.encoding
        )

        return not has_gamut and not has_whitepoint and not has_transfer_function

    def copy(self) -> RgbColorspace:
        """
        Return a shallow copy of this instance.
        """
        return dataclasses.replace(self)
