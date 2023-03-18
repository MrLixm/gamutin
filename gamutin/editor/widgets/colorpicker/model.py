"""
Bridge between core and editor.
"""
from __future__ import annotations

__all__ = (
    "ColorExposureGrading",
    "DEFAULT_COLOR",
    "PASSTHROUGH_COLORSPACE",
    "RGBAData",
    "RgbColorspace",
    "sRGB_COLORSPACE",
    "sRGB_LINEAR_COLORSPACE",
)

import logging

from gamutin.core.color import RGBAData
from gamutin.core.colorspaces import PASSTHROUGH_COLORSPACE
from gamutin.core.colorspaces import RgbColorspace
from gamutin.core.colorspaces import sRGB_LINEAR_COLORSPACE
from gamutin.core.colorspaces import sRGB_COLORSPACE
from gamutin.core.grading import ColorExposureGrading

logger = logging.getLogger(__name__)


DEFAULT_COLOR = RGBAData(0, 0, 0, colorspace=None, alpha=None)
"""
A color value to use as default when None has been set by the user yet.
"""
