from __future__ import annotations

__all__ = ("BadgeOverlayWidget",)

import logging

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

logger = logging.getLogger(__name__)


def paint_badge(widget: BadgeMixin, event: QtGui.QPaintEvent):
    qpainter = QtGui.QPainter()
    qpainter.begin(widget)

    rect = event.rect()
    target_rect = QtCore.QRect(
        rect.right() - widget.badge_size - 1,
        rect.top() + widget.badge_size,
        widget.badge_size,
        widget.badge_size,
    )

    qpainter.setRenderHints(qpainter.Antialiasing)
    qpainter.setPen(QtGui.QPen(QtCore.Qt.transparent, 1))
    qpainter.setBrush(QtGui.QColor(250, 40, 40))
    qpainter.drawEllipse(target_rect.center(), widget.badge_size, widget.badge_size)

    if widget.badge_number > 0:
        qpainter.setPen(QtGui.QColor(250, 250, 250))
        qpainter.setFont(QtGui.QFont("Sans", 6))
        qpainter.drawText(target_rect, QtCore.Qt.AlignCenter, str(widget.badge_number))

    qpainter.end()


class BadgeMetaclass(type):
    def __init__(mcs, clsname, bases, attrs):
        super().__init__(clsname, bases, attrs)
        mcs.badge_number = 0
        mcs.badge_size = 6


class BadgeMixin(type(QtCore.QObject), BadgeMetaclass):
    pass


class BadgeOverlayWidget(object, metaclass=BadgeMixin):
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
    widget.badge_size = 16
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
