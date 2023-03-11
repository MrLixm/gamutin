from __future__ import annotations

__all__ = ("ColorDisplayPreview",)


import logging


from Qt import QtCore

from gamutin.editor.widgets.colorpicker.colordisplay import ColorDisplayInteractive


logger = logging.getLogger(__name__)


class ColorDisplayPreview(ColorDisplayInteractive):
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
