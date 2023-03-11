from __future__ import annotations

__all__ = ("BadgeOverlayWidget",)

import logging
from typing import Union

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.editor.cfg import resources

logger = logging.getLogger(__name__)


def paint_badge(widget: Union[BadgeMixin, QtWidgets.QWidget], event: QtGui.QPaintEvent):
    qpainter = QtGui.QPainter()
    qpainter.begin(widget)
    color = widget.badge_color
    if not widget.isEnabled():
        color = QtGui.QColor.fromHsl(color.hue(), 0, color.lightness(), color.alpha())

    source_rect = event.rect()
    target_rect = QtCore.QRectF(
        source_rect.width() - widget.badge_size,
        source_rect.top(),
        widget.badge_size,
        widget.badge_size,
    )

    qpainter.setRenderHints(qpainter.Antialiasing)
    qpainter.setPen(QtGui.QPen(QtCore.Qt.transparent, 1))
    qpainter.setBrush(color)
    # qpainter.drawRect(target_rect)
    qpainter.drawEllipse(
        target_rect.center(),
        widget.badge_size / 2,
        widget.badge_size / 2,
    )

    if widget.badge_number > 0:
        qpainter.setPen(widget.badge_color_text)
        qpainter.setFont(QtGui.QFont("Mono", int((widget.badge_size / 1.3) ** 0.85)))
        qpainter.drawText(
            target_rect,
            QtCore.Qt.AlignCenter,
            str(widget.badge_number),
        )

    qpainter.end()


class BadgeMetaclass(type):
    def __init__(mcs, clsname, bases, attrs):
        super().__init__(clsname, bases, attrs)
        mcs.badge_number: int = 0
        mcs.badge_size: int = 12
        mcs.badge_color: QtGui.QColor = (
            resources.theme_default.color_notification.value.as_qcolor()
        )
        mcs.badge_color_text: QtGui.QColor = (
            resources.theme_default.color_text_base.value.as_qcolor()
        )


class BadgeMixin(type(QtCore.QObject), BadgeMetaclass):
    pass


class BadgeOverlayWidget(object, metaclass=BadgeMixin):
    def __init__(self):
        # for type hints only
        self.badge_number: int = 0
        self.badge_size: int = 12
        self.badge_color: QtGui.QColor = (
            resources.theme_default.color_notification.value.as_qcolor()
        )
        self.badge_color_text: QtGui.QColor = (
            resources.theme_default.color_text_base.value.as_qcolor()
        )

    def paint_badge(self, event: QtGui.QPaintEvent):
        paint_badge(self, event)
