from __future__ import annotations

__all__ = ("ColorDisplayPreview",)


import logging


from Qt import QtCore
from Qt import QtGui

from gamutin.editor.widgets.colorpicker.colordisplay import ColoredRectangle
from gamutin.editor.widgets.colorpicker.model import RGBAData
from gamutin.editor.widgets.colorpicker.model import DEFAULT_COLOR


logger = logging.getLogger(__name__)


class ColorDisplayPreview(ColoredRectangle):
    """
    A rectangular frame filled with a uniform constant color.

    Designed to be used as a small interactive color widget in an ui.

    - You can set rounded corner by setting ``border_radius`` attribute.
    - You can set how much the widget is rescaled when overed with the ``hover_scale`` attribute.
    """

    def __init__(self):
        super().__init__()

        self._rgbdata: RGBAData = DEFAULT_COLOR
        self.hover_scale = 1
        self.animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.setDuration(100)

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

    def enterEvent(self, event: QtCore.QEvent) -> None:
        initial_rect = self.geometry()
        target_rect = QtCore.QRect(
            0,
            0,
            int(initial_rect.width() * self.hover_scale),
            int(initial_rect.height() * self.hover_scale),
        )
        target_rect.moveCenter(initial_rect.center())

        self.animation.setStartValue(initial_rect)
        self.animation.setEndValue(target_rect)
        self.animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self.animation.start()
        super().leaveEvent(event)
