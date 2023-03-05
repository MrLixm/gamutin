from __future__ import annotations

__all__ = ("ColorPreviewFrame",)


import logging


from Qt import QtWidgets
from Qt import QtGui


from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import DEFAULT_COLOR


logger = logging.getLogger(__name__)


class ColorPreviewFrame(QtWidgets.QFrame):
    """
    A frame filled with a uniform constant color.
    """

    def __init__(self):
        super().__init__()
        self._color = DEFAULT_COLOR
        self.color = DEFAULT_COLOR

    @property
    def color(self) -> RGBAData:
        return self._color

    @color.setter
    def color(self, color_value: RGBAData):
        self._color = color_value
        self.setToolTip(str(color_value))
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qpainter = QtGui.QPainter()
        qpainter.setRenderHint(qpainter.Antialiasing)
        qpainter.begin(self)
        qpainter.fillRect(self.rect(), self._get_qcolor())
        qpainter.end()

    def _get_qcolor(self) -> QtGui.QColor:
        color_int8 = self.color.to_int8(alpha=False)
        return QtGui.QColor(*color_int8)
