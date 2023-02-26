from __future__ import annotations

__all__ = (
    "BaseColorspaceComponent",
    "Whitepoint",
    "ColorspaceGamut",
    "TransferFunctions",
    "TRANSFER_FUNCTIONS_LINEAR",
    "RgbColorspace",
)

import copy
import dataclasses
from abc import abstractmethod
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

    @abstractmethod
    def _tuplerepr(self) -> tuple:
        """
        The class represented as a tuple object. Used for hashing.
        """
        pass

    def __str__(self):
        return f"{self.__class__.__name__}<{self.name} at {hex(id(self))}>"

    def __hash__(self):
        return hash(self._tuplerepr())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._tuplerepr() == other._tuplerepr()
        return NotImplemented


@dataclasses.dataclass(eq=False)
class Whitepoint(BaseColorspaceComponent):
    coordinates: numpy.ndarray
    """
    CIE xy coordinates as a ndarray(2,)
    """

    def _tuplerepr(self):
        return (
            self.__class__.__name__,
            self.name,
            repr(self.coordinates),
        )

    @classmethod
    def from_colour_colorspace(cls, colour_colorspace: colour.RGB_Colourspace):
        return cls(
            colour_colorspace.whitepoint_name,
            colour_colorspace.whitepoint.copy(),
        )


@dataclasses.dataclass(eq=False)
class ColorspaceGamut(BaseColorspaceComponent):
    """
    Gamut/Primaries part of a specific colorspace.
    """

    primaries: numpy.ndarray

    def _tuplerepr(self):
        return (
            self.__class__.__name__,
            self.name,
            repr(self.primaries),
        )

    @classmethod
    def from_colour_colorspace(cls, colour_colorspace: colour.RGB_Colourspace):
        return cls(
            "Gamut " + colour_colorspace.name,
            colour_colorspace.primaries,
        )


@dataclasses.dataclass(eq=False)
class TransferFunctions(BaseColorspaceComponent):
    """
    Transfer functions as decoding and encoding.

    A transfer function might or might not be linear and need to be specified if so.
    """

    encoding: Optional[Callable]
    decoding: Optional[Callable]

    is_encoding_linear: bool = False
    is_decoding_linear: bool = False

    def _tuplerepr(self):
        return (
            self.__class__.__name__,
            self.name,
            self.encoding,
            self.decoding,
            self.is_encoding_linear,
            self.is_decoding_linear,
        )

    def __post_init__(self):
        super().__post_init__()

        if self.encoding is None:
            self.is_encoding_linear = True
        if self.decoding is None:
            self.is_decoding_linear = True

    @property
    def are_linear(self) -> bool:
        """
        Return True if the encoding and decoding are linear transfer-functions.
        """
        return self.is_encoding_linear and self.is_decoding_linear

    @classmethod
    def from_colour_colorspace(cls, colour_colorspace: colour.RGB_Colourspace):
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


@dataclasses.dataclass(eq=False)
class RgbColorspace(BaseColorspaceComponent):
    """
    Top level entity specifying how a colorspace is defined.

    By color-science standard, every colorspace define :
    - gamut
    - whitepoint
    - transfer functions

    To perform colorspace conversion a 3x3 matrix from and to CIE XYZ is required,
    which can be derived automatically from the gamut and whitepoint if not specified.

    """

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

    matrix_to_XYZ: numpy.ndarray = None
    matrix_from_XYZ: numpy.ndarray = None

    def __post_init__(self):
        super().__post_init__()

        if (
            self.matrix_to_XYZ is None
            and self.matrix_from_XYZ is None
            and self.gamut
            and self.whitepoint
        ):
            self.matrix_to_XYZ: numpy.ndarray = colour.normalised_primary_matrix(
                primaries=self.gamut.primaries,
                whitepoint=self.whitepoint.coordinates,
            )
            self.matrix_from_XYZ: numpy.ndarray = numpy.linalg.inv(self.matrix_to_XYZ)

    def _tuplerepr(self) -> tuple:
        return (
            self.__class__.__name__,
            self.name,
            self.gamut,
            self.whitepoint,
            self.transfer_functions,
            self.categories,
            self.description,
        )

    @property
    def is_no_op(self) -> bool:
        """
        Return True if the colorspace should not be processed because it
        defines no transform for any component.
        """

        has_gamut = (
            self.gamut is not None
            or (
                self.matrix_from_XYZ is not None
                and not numpy.array_equal(self.matrix_from_XYZ, numpy.identity(3))
            )
            or (
                self.matrix_to_XYZ is not None
                and not numpy.array_equal(self.matrix_to_XYZ, numpy.identity(3))
            )
        )

        has_whitepoint = self.whitepoint is not None

        has_transfer_function = self.transfer_functions is not None and (
            self.transfer_functions.decoding or self.transfer_functions.encoding
        )

        return not has_gamut and not has_whitepoint and not has_transfer_function

    def copy(self) -> RgbColorspace:
        """
        Return a shallow copy of this instance.
        """
        return copy.deepcopy(self)

    def get_linear_copy(self) -> RgbColorspace:
        """
        Return a copy of this colorspace but with linear transfer-functions set.
        """
        colorspace = self.copy()
        colorspace.name = colorspace.name + " Linear"
        colorspace.transfer_functions = TRANSFER_FUNCTIONS_LINEAR
        return colorspace

    @classmethod
    def from_colour_colorspace(
        cls,
        colour_colorspace: colour.RGB_Colourspace,
        categories: tuple[ColorspaceCategory],
        description: Optional[str] = None,
    ):
        gamut = ColorspaceGamut.from_colour_colorspace(colour_colorspace)
        whitepoint = Whitepoint.from_colour_colorspace(colour_colorspace)
        transfer_functions = TransferFunctions.from_colour_colorspace(colour_colorspace)

        return cls(
            name=colour_colorspace.name,
            gamut=gamut,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            description=description or colour_colorspace.__doc__,
            categories=categories,
            matrix_from_XYZ=colour_colorspace.matrix_XYZ_to_RGB.copy(),
            matrix_to_XYZ=colour_colorspace.matrix_RGB_to_XYZ.copy(),
        )
