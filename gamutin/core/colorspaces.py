from typing import Optional

import colour
import numpy.linalg

from .utils import simplify


_COLORSPACES: dict[str, colour.RGB_Colourspace] = {}

_COLORSPACE_POINTER_GAMUT_NAME = "Pointer's Gamut"


def _add_colorspace(name: str, colorspace: colour.RGB_Colourspace):

    global _COLORSPACES

    _COLORSPACES[name] = colorspace
    _COLORSPACES[simplify(name)] = colorspace


def _load_colorspaces():

    colorspace: colour.RGB_Colourspace
    for colorspace_name, colorspace in colour.RGB_COLOURSPACES.items():

        _add_colorspace(colorspace_name, colorspace)

    # Add "fake" Pointer's Gamut colorspace
    colorspace = colour.RGB_Colourspace(
        name=_COLORSPACE_POINTER_GAMUT_NAME,
        primaries=numpy.array([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]]),
        whitepoint=colour.models.CCS_ILLUMINANT_POINTER_GAMUT,
        whitepoint_name=_COLORSPACE_POINTER_GAMUT_NAME,
        matrix_RGB_to_XYZ=None,
        matrix_XYZ_to_RGB=None,
        cctf_encoding=colour.linear_function,
        cctf_decoding=colour.linear_function,
        use_derived_matrix_XYZ_to_RGB=True,
        use_derived_matrix_RGB_to_XYZ=True,
    )
    _add_colorspace(colorspace.name, colorspace)


_load_colorspaces()


""" ====================================================================================

PUBLIC

"""


def get_available_colorspaces() -> list[colour.RGB_Colourspace]:
    return list(_COLORSPACES.values())


def get_available_colorspaces_names() -> list[str]:
    return list(_COLORSPACES.keys())


def get_available_colorspaces_names_aliases() -> list[tuple[str]]:
    """
    Get all the colorspaces available as tuple of the different alias
    corresponding to a same colorspace.

    Example::

        [("ProPhoto RGB", "prophoto-rgb", "prophoto"), ...]

    Returns:
        list of colorspaces names available as a tuple of aliases
    """

    buffer_dict = {}

    for colorspace_name, colorspace in _COLORSPACES.items():

        identifier = hash(colorspace)

        if buffer_dict.get(identifier):
            buffer_dict[identifier].append(colorspace_name)
        else:
            buffer_dict[identifier] = [colorspace_name]

    return [tuple(name_tuple) for name_tuple in buffer_dict.values()]


def get_colorspace(name: Optional[str]) -> Optional[colour.RGB_Colourspace]:
    """
    Retrieve the colour colorspace instance corresponding to the given name.

    Args:
        name: literal name of the colourspace or one of its available alias

    Returns:
        colour colorspace instance
    """
    if not name:
        return None

    linear_asked = name.endswith(":linear")
    name = name.rstrip(":linear")

    colorspace = _COLORSPACES.get(name)

    if linear_asked:
        colorspace = colorspace.copy()
        colorspace.name = colorspace.name + " Linear"
        colorspace.cctf_decoding = colour.models.linear_function
        colorspace.cctf_encoding = colour.models.linear_function

    return colorspace


POINTER_GAMUT_COLORSPACE = get_colorspace(_COLORSPACE_POINTER_GAMUT_NAME)
assert POINTER_GAMUT_COLORSPACE
