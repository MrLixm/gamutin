from typing import Optional

import colour


_COLORSPACES: dict[str, colour.RGB_Colourspace] = {}


def _load_colorspaces():

    global _COLORSPACES

    colorspace: colour.RGB_Colourspace
    for colorspace_name, colorspace in colour.RGB_COLOURSPACES.items():

        _COLORSPACES[colorspace_name] = colorspace

        if colorspace.cctf_decoding == colour.models.linear_function:
            continue

        variant_colorspace = colorspace.copy()
        variant_colorspace.name = variant_colorspace.name + " Linear"
        variant_colorspace.cctf_decoding = colour.models.linear_function
        variant_colorspace.cctf_encoding = colour.models.linear_function

        _COLORSPACES[variant_colorspace.name] = variant_colorspace


_load_colorspaces()


def get_available_colorspaces() -> list[colour.RGB_Colourspace]:
    return list(_COLORSPACES.values())


def get_available_colorspaces_names() -> list[str]:
    return list(_COLORSPACES.keys())


def get_colorspace(name: str) -> Optional[colour.RGB_Colourspace]:
    return _COLORSPACES.get(name)
