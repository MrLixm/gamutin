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

    @classmethod
    def fromColourColorspace(cls, colour_colorspace: colour.RGB_Colourspace):
        return cls(
            "CCTF " + colour_colorspace.name,
            colour_colorspace.cctf_encoding,
            colour_colorspace.cctf_decoding,
        )


@dataclasses.dataclass
class RgbColorspace:

    gamut: Optional[ColorspaceGamut]
    whitepoint: Optional[Whitepoint]
    transfer_functions: Optional[TransferFunctions]

    categories: list[ColorspaceCategory]
    """
    To help sort the colorspace in an interface.
    """

    description: str
    """
    A bit more details on what/why for this colorspace.
    """

    def is_no_op(self):
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
