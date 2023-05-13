"""
Bridge between core and editor.
"""
from __future__ import annotations

__all__ = (
    "ColorExposureGrading",
    "DEFAULT_COLOR",
    "GuiColorManagementControler",
    "PASSTHROUGH_COLORSPACE",
    "RGBAData",
    "RgbColorspace",
    "sRGB_COLORSPACE",
    "sRGB_LINEAR_COLORSPACE",
)

import logging

from Qt import QtGui
from Qt import QtCore

from gamutin.core.color import RGBAData
from gamutin.core.color import XYZColor
from gamutin.core.color import LCHabColor
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


class GuiColorManagementControler:
    """
    Create a controller that can be propagated through the interface to centralize
    active color-management configuration.

    Widgets usually defined a input colorspace, which is converted to the working
    colorspace, which might then be converted to the display colorspace, if displaying
    it is needed.
    """

    display_colorspace_changed_signal = QtCore.Signal()
    working_colorspace_changed_signal = QtCore.Signal()

    def __init__(self):
        self._display_colorspace: RgbColorspace = sRGB_COLORSPACE
        self._working_colorspace: RgbColorspace = sRGB_LINEAR_COLORSPACE

    @property
    def display_colorspace(self) -> RgbColorspace:
        return self._display_colorspace

    @display_colorspace.setter
    def display_colorspace(self, new_display_colorspace: RgbColorspace):
        self._display_colorspace = new_display_colorspace
        self.display_colorspace_changed_signal.emit()

    @property
    def working_colorspace(self) -> RgbColorspace:
        return self._working_colorspace

    @working_colorspace.setter
    def working_colorspace(self, new_working_colorspace: RgbColorspace):
        self._working_colorspace = new_working_colorspace
        self.working_colorspace_changed_signal.emit()
