from __future__ import annotations

__all__ = ("ColorDisplayInteractive",)


import logging


from Qt import QtGui

from gamutin.editor.assets.widgets.colorpicker.colordisplay import ColoredRectangle
from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import DEFAULT_COLOR


logger = logging.getLogger(__name__)


class ColorDisplayInteractive(ColoredRectangle):
    """
    A rectangular frame filled with a uniform constant color.

    Designed to be use a large color preview and around RGBAData instances.

    - You can set rounded corner by setting ``border_radius`` attribute.
    """

    def __init__(self):
        super().__init__()
        self._rgbdata = DEFAULT_COLOR

    @property
    def color(self) -> RGBAData:
        return self._rgbdata

    @color.setter
    def color(self, color_value: RGBAData):
        color_int8 = color_value.to_int8(alpha=False)
        self._color = QtGui.QColor(*color_int8)
        self._rgbdata = color_value
        self.setToolTip(str(color_value))
        self.repaint()
