from typing import Optional

import colour

from .utils import simplify


_COLORSPACES: dict[str, colour.RGB_Colourspace] = {}


def _add_colorspace(name: str, colorspace: colour.RGB_Colourspace):

    global _COLORSPACES

    _COLORSPACES[name] = colorspace
    _COLORSPACES[simplify(name)] = colorspace


def _load_colorspaces():

    colorspace: colour.RGB_Colourspace
    for colorspace_name, colorspace in colour.RGB_COLOURSPACES.items():

        _add_colorspace(colorspace_name, colorspace)


_load_colorspaces()


def get_available_colorspaces() -> list[colour.RGB_Colourspace]:
    return list(_COLORSPACES.values())


def get_available_colorspaces_names() -> list[str]:
    return list(_COLORSPACES.keys())


def get_available_colorspaces_names_aliases() -> list[tuple[str]]:
    """
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


def get_colorspace(name: str) -> Optional[colour.RGB_Colourspace]:

    linear_asked = name.endswith(":linear")
    name = name.rstrip(":linear")

    colorspace = _COLORSPACES.get(name)

    if linear_asked:
        colorspace = colorspace.copy()
        colorspace.name = colorspace.name + " Linear"
        colorspace.cctf_decoding = colour.models.linear_function
        colorspace.cctf_encoding = colour.models.linear_function

    return colorspace
