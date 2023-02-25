__all__ = (
    "ChromaticAdaptationTransform",
    "get_available_colorspaces",
    "get_available_colorspaces_names",
    "get_available_colorspaces_names_aliases",
    "get_colorspace",
    "POINTER_GAMUT_COLORSPACE",
    "sRGB_COLORSPACE",
    "sRGB_LINEAR_COLORSPACE",
)

import enum
import importlib
import logging
from typing import Optional

import colour

from gamutin.core.colorspaces.base import RgbColorspace
from gamutin.core.colorspaces.base import ColorspaceGamut
from gamutin.core.colorspaces.base import Whitepoint
from gamutin.core.colorspaces.base import TransferFunctions
from gamutin.core.colorspaces.base import TRANSFER_FUNCTIONS_LINEAR
from gamutin.core.colorspaces.categories import ColorspaceCategory

logger = logging.getLogger(__name__)

_COLORSPACES: dict[str, RgbColorspace] = {}
"""
Data dict of all the colorspaces available in the package. The key represent an identifier
to access the corresponding colorspace.

You can have multiple keys poiting to the same colorspace instance. 
This allow to created "alias" identifiers.

TODO determine if the dict is sorted
"""

# Names of special colorspace that must be handled differently
_COLORSPACE_POINTER_GAMUT_NAME = "Pointer's Gamut"


def _add_colorspace(colorspace: RgbColorspace, additional_aliases: list[str] = None):
    """
    Register the given colorspace in the package.

    Args:
        colorspace: colorspace class instance
        additional_aliases: optional list of str that can return the colorspace when queried.
    """

    global _COLORSPACES
    additional_aliases = additional_aliases or []

    _COLORSPACES[colorspace.name] = colorspace
    _COLORSPACES[colorspace.name_simplified] = colorspace

    for alias in additional_aliases:
        _COLORSPACES[alias] = colorspace

    return


def _load_colour_colorspaces():
    colour_colorspace_config = {
        "RGB_COLOURSPACE_ACES2065_1": {
            "category": [ColorspaceCategory.aces],
            "aliases": ["aces", "ap0"],
        },
        "RGB_COLOURSPACE_ACESCC": {
            "category": [ColorspaceCategory.aces],
        },
        "RGB_COLOURSPACE_ACESCCT": {
            "category": [ColorspaceCategory.aces],
        },
        "RGB_COLOURSPACE_ACESPROXY": {
            "category": [ColorspaceCategory.aces],
        },
        "RGB_COLOURSPACE_ACESCG": {
            "category": [ColorspaceCategory.aces, ColorspaceCategory.working_space],
            "aliases": ["ap1"],
        },
        "RGB_COLOURSPACE_ADOBE_RGB1998": {
            "category": [ColorspaceCategory.common],
        },
        "RGB_COLOURSPACE_ADOBE_WIDE_GAMUT_RGB": {
            "category": [ColorspaceCategory.working_space],
        },
        "RGB_COLOURSPACE_ALEXA_WIDE_GAMUT": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_APPLE_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_BEST_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_BETA_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_BLACKMAGIC_WIDE_GAMUT": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_BT470_525": {
            "category": [],
        },
        "RGB_COLOURSPACE_BT470_625": {
            "category": [],
        },
        "RGB_COLOURSPACE_BT709": {
            "category": [ColorspaceCategory.common],
            "aliases": ["rec709", "bt709"],
        },
        "RGB_COLOURSPACE_BT2020": {
            "category": [ColorspaceCategory.working_space],
            "aliases": ["rec2020", "bt2020"],
        },
        "RGB_COLOURSPACE_CIE_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_CINEMA_GAMUT": {
            "category": [],
        },
        "RGB_COLOURSPACE_COLOR_MATCH_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_DAVINCI_WIDE_GAMUT": {
            "category": [ColorspaceCategory.working_space],
        },
        "RGB_COLOURSPACE_DCDM_XYZ": {
            "category": [],
        },
        "RGB_COLOURSPACE_DCI_P3": {
            "category": [ColorspaceCategory.p3],
        },
        "RGB_COLOURSPACE_DCI_P3_P": {
            "category": [ColorspaceCategory.p3],
        },
        "RGB_COLOURSPACE_DISPLAY_P3": {
            "category": [ColorspaceCategory.p3],
        },
        "RGB_COLOURSPACE_DJI_D_GAMUT": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_DON_RGB_4": {
            "category": [],
        },
        "RGB_COLOURSPACE_ECI_RGB_V2": {
            "category": [],
        },
        "RGB_COLOURSPACE_EKTA_SPACE_PS_5": {
            "category": [],
        },
        "RGB_COLOURSPACE_FILMLIGHT_E_GAMUT": {
            "category": [ColorspaceCategory.working_space],
        },
        "RGB_COLOURSPACE_PROTUNE_NATIVE": {
            "category": [],
        },
        "RGB_COLOURSPACE_MAX_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_N_GAMUT": {
            "category": [],
        },
        "RGB_COLOURSPACE_P3_D65": {
            "category": [ColorspaceCategory.p3],
        },
        "RGB_COLOURSPACE_PAL_SECAM": {
            "category": [],
        },
        "RGB_COLOURSPACE_RED_COLOR": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_RED_COLOR_2": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_RED_COLOR_3": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_RED_COLOR_4": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_DRAGON_COLOR": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_DRAGON_COLOR_2": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_RED_WIDE_GAMUT_RGB": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_ROMM_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_RIMM_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_ERIMM_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_PROPHOTO_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_RUSSELL_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_SHARP_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_SMPTE_240M": {
            "category": [],
        },
        "RGB_COLOURSPACE_SMPTE_C": {
            "category": [],
        },
        "RGB_COLOURSPACE_NTSC1953": {
            "category": [],
        },
        "RGB_COLOURSPACE_NTSC1987": {
            "category": [],
        },
        "RGB_COLOURSPACE_S_GAMUT": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_S_GAMUT3": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_S_GAMUT3_CINE": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_VENICE_S_GAMUT3": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_VENICE_S_GAMUT3_CINE": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_sRGB": {
            "category": [ColorspaceCategory.working_space, ColorspaceCategory.common],
        },
        "RGB_COLOURSPACE_V_GAMUT": {
            "category": [ColorspaceCategory.camera],
        },
        "RGB_COLOURSPACE_XTREME_RGB": {
            "category": [],
        },
        "RGB_COLOURSPACE_F_GAMUT": {
            "category": [ColorspaceCategory.camera],
        },
    }

    colour_dataset = importlib.import_module("colour.models.rgb.datasets")

    for colorspace_name, colorspace_data in colour_colorspace_config.items():
        try:
            colour_colorspace: colour.RGB_Colourspace = getattr(
                colour_dataset, colorspace_name
            )
        except ImportError as excp:
            logger.error(
                f"[_load_colour_colorspaces] Colour colorspace <{colorspace_name} was not imported: {excp}>"
            )
            continue

        colorspace = RgbColorspace.from_colour_colorspace(
            colour_colorspace,
            categories=tuple(colorspace_data.get("category", [])),
        )

        aliases = colorspace_data.get("aliases", [])
        _add_colorspace(colorspace, additional_aliases=aliases)

    return


def _load_colorspaces():
    _load_colour_colorspaces()

    colorspace = RgbColorspace(
        name="Passthrough",
        gamut=None,
        whitepoint=None,
        transfer_functions=None,
        description="A 'null' colorspace that does nothing.",
        categories=(ColorspaceCategory.common,),
    )
    _add_colorspace(colorspace, additional_aliases=["raw", "null"])

    whitepoint = Whitepoint(
        f"{_COLORSPACE_POINTER_GAMUT_NAME} Whitepoint",
        coordinates=colour.models.CCS_ILLUMINANT_POINTER_GAMUT,
    )
    colorspace = RgbColorspace(
        name=_COLORSPACE_POINTER_GAMUT_NAME,
        gamut=None,
        whitepoint=whitepoint,
        transfer_functions=None,
        description=(
            "The Pointer’s gamut is (an approximation of) the gamut of real surface "
            "colors as can be seen by the human eye, based on the research by "
            "Michael R. Pointer (1980). What this means is that every color that can "
            "be reflected by the surface of an object of any material is inside the "
            "Pointer’s gamut.\n Pointer’s gamut is defined for diffuse reflection "
            "(matte surface). "
            "Specular reflection objects can reflect colors that are outside the Pointer’s gamut. \n"
            "Also not technically a colorspace."
        ),
        categories=tuple(),
    )
    _add_colorspace(colorspace)


_load_colorspaces()

""" ====================================================================================

PUBLIC

"""


class ChromaticAdaptationTransform(enum.Enum):
    bianco_2010 = "Bianco 2010"
    bianco_pc_2010 = "Bianco PC 2010"
    bradford = "Bradford"
    CAT02_Brill = "CAT02 Brill 2008"
    CAT02 = "CAT02"
    CAT16 = "CAT16"
    CMCCAT2000 = "CMCCAT2000"
    CMCCAT97 = "CMCCAT97"
    fairchild = "Fairchild"
    sharp = "Sharp"
    von_kries = "Von Kries"
    XYZ_scaling = "XYZ Scaling"
    default = "Bradford"


def get_available_colorspaces() -> list[RgbColorspace]:
    """
    List of RgbColorspace with no duplicates and sorted alphabetically by name.
    """

    def get_colorspace_name(colorspace: RgbColorspace):
        return colorspace.name

    return sorted(
        list(set(_COLORSPACES.values())),
        key=get_colorspace_name,
    )


def get_available_colorspaces_names() -> list[str]:
    """
    List of colorspace indentifier that correspond to a colorspace.
    No duplicates and sorted alphabetically by name.
    """
    return sorted(list(set(_COLORSPACES.keys())))


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


def get_colorspace(name: Optional[str]) -> Optional[RgbColorspace]:
    """
    Retrieve the colour colorspace instance corresponding to the given name.

    You can ask a linear variant of the colorspace by suffixing the name with ``:linear``

    Args:
        name: literal name of the colourspace or one of its available alias

    Returns:
        colorspace instance or None if not found.
    """
    if not name:
        return None

    linear_asked = name.endswith(":linear")
    name = name.rstrip(":linear")

    colorspace = _COLORSPACES.get(name)
    if not colorspace:
        return None

    if linear_asked:
        colorspace = colorspace.get_linear_copy()

    return colorspace


POINTER_GAMUT_COLORSPACE = get_colorspace(_COLORSPACE_POINTER_GAMUT_NAME)
assert POINTER_GAMUT_COLORSPACE

sRGB_COLORSPACE = get_colorspace("sRGB")
assert sRGB_COLORSPACE
sRGB_LINEAR_COLORSPACE = get_colorspace("sRGB:linear")
assert sRGB_LINEAR_COLORSPACE
