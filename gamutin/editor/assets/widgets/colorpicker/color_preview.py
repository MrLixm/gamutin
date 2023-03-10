from __future__ import annotations

__all__ = (
    "ColoredRectangle",
    "ColorPreviewFullFrame",
    "ColorPreviewLightFrame",
)


import logging


from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore


from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import DEFAULT_COLOR


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


class ColorPreviewFullFrame(ColoredRectangle):
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


class ColorPreviewLightFrame(ColorPreviewFullFrame):
    """
    A rectangular frame filled with a uniform constant color.

    Designed to be used as a small interactive color widget in an ui.

    - You can set rounded corner by setting ``border_radius`` attribute.
    - You can set how much the widget is rescaled when overed with the ``hover_scale`` attribute.
    """

    def __init__(self):
        super().__init__()

        self.hover_scale = 1
        self.animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.setDuration(100)

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
