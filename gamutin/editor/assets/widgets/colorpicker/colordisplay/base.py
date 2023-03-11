from __future__ import annotations

__all__ = ("ColoredRectangle",)


import logging


from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

logger = logging.getLogger(__name__)


class ColoredRectangle(QtWidgets.QFrame):
    """
    A rectangular frame filled with a uniform constant color.

    You can set rounded corner to the frame by setting the ``border_radius`` attribute.
    """

    def __init__(self):
        super().__init__()
        self._color = QtGui.QColor(0, 0, 0)
        self._border_radius = 0

        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        # avoid getting a widget with no size at all
        self.setMinimumSize(15, 5)

    @property
    def border_radius(self):
        return self._border_radius

    @border_radius.setter
    def border_radius(self, border_radius_value: int):
        self._border_radius = border_radius_value
        self.repaint()

    @property
    def color(self) -> QtGui.QColor:
        return self._color

    @color.setter
    def color(self, color_value: QtGui.QColor):
        self._color = color_value
        self.setToolTip(str(color_value.getRgbF()))
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qpainter = QtGui.QPainter()
        qpainter.begin(self)
        qpainter.setRenderHint(qpainter.Antialiasing, True)

        qpainter_path = QtGui.QPainterPath()
        qpainter_path.addRoundedRect(
            self.rect(),
            self.border_radius,
            self.border_radius,
        )

        qpainter.setClipPath(qpainter_path)
        qpainter.setPen(QtCore.Qt.NoPen)
        qpainter.fillPath(qpainter_path, QtGui.QBrush(self._color))
        qpainter.drawPath(qpainter_path)
        qpainter.end()
