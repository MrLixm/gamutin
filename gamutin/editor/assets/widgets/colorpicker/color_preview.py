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
    A rectangular frame filled with a uniform constant color.

    You can set rounded corner by setting ``border_radius`` attribute.
    """

    def __init__(self):
        super().__init__()
        self._color = DEFAULT_COLOR
        self.color = DEFAULT_COLOR
        self._border_radius = 0
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )

    @property
    def border_radius(self):
        return self._border_radius

    @border_radius.setter
    def border_radius(self, border_radius_value: int):
        self._border_radius = border_radius_value
        self.repaint()

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
        qpainter.begin(self)
        qpainter.setRenderHint(qpainter.Antialiasing, True)

        qpainter_path = QtGui.QPainterPath()
        qpainter_path.addRoundedRect(
            self.rect(), self.border_radius, self.border_radius
        )

        qpainter.setClipPath(qpainter_path)
        qpainter.setPen(QtCore.Qt.NoPen)
        qpainter.fillPath(qpainter_path, QtGui.QBrush(self._get_qcolor()))
        qpainter.drawPath(qpainter_path)
        qpainter.end()

    def _get_qcolor(self) -> QtGui.QColor:
        color_int8 = self.color.to_int8(alpha=False)
        return QtGui.QColor(*color_int8)
