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


def _test_interface():

    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    class TestLabel(QtWidgets.QLabel, BadgeOverlayWidget):
        def __init__(self):
            super().__init__()
            self.setText("this is some test text")
            self.setSizePolicy(
                QtWidgets.QSizePolicy.Fixed,
                QtWidgets.QSizePolicy.Fixed,
            )
            assert self.badge_number is not None

        def paintEvent(self, event: QtGui.QPaintEvent):
            super().paintEvent(event)
            self.paint_badge(event)

    class TestButton(QtWidgets.QPushButton, BadgeOverlayWidget):
        def __init__(self):
            super().__init__()
            self.setText("this is some test text")
            assert self.badge_number is not None

        def paintEvent(self, event: QtGui.QPaintEvent):
            super().paintEvent(event)
            self.paint_badge(event)

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QGridLayout()

    widget = TestLabel()
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 3
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 3
    widget.setMargin(20)
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 3
    widget.setMargin(20)
    widget.badge_size = 8
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 3
    widget.setMargin(20)
    widget.badge_size = 12
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 3
    widget.setMargin(20)
    widget.badge_size = 24
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 3
    widget.setMargin(20)
    widget.badge_size = 30
    layout.addWidget(widget)

    widget = TestLabel()
    widget.badge_number = 16
    widget.setMargin(20)
    widget.setStyleSheet(
        f"font-family: {QtGui.QFontDatabase().families()[2]}; font-size: 15px;"
    )
    widget.badge_size = 20
    layout.addWidget(widget)

    widget = TestButton()
    widget.badge_number = 3
    layout.addWidget(widget)

    widget = TestButton()
    widget.badge_number = 3
    widget.setStyleSheet("margin: 5px;")
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
