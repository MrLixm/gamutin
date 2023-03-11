from __future__ import annotations

__all__ = ("ColorDisplayFormat",)

import enum
import logging


logger = logging.getLogger(__name__)


class ColorDisplayFormat(enum.Enum):
    """
    List formats available to represent a color encoding.

    All are assumed to be for the RGB color model.
    """

    float = "0.0"
    tuple = "(0.0,)"
    int8 = "255"
    hexadecimal = "#hex"
