__all__ = ("",)

import abc
import logging
from functools import partial
from typing import Optional

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

logger = logging.getLogger(__name__)


class BadgeMetaclass(type):
    def __init__(mcs, clsname, bases, attrs):
        super().__init__(clsname, bases, attrs)
        mcs.number = 0
        mcs.paint_badge = BadgeMetaclass.paint_badge

    @classmethod
    def paint_badge(mcs, self, event: QtGui.QPaintEvent, *args, **kwargs):

        qpainter = QtGui.QPainter()
        qpainter.begin(self)

        rect = event.rect()
        target_rect = QtCore.QRect(
            rect.left(),
            rect.top(),
            rect.width(),
            rect.height(),
        )

        qpainter.setRenderHints(qpainter.Antialiasing)
        qpainter.setPen(QtGui.QPen(QtCore.Qt.white, 1))
        qpainter.setBrush(QtCore.Qt.red)
        qpainter.drawEllipse(target_rect.center(), 15, 15)
        if self.number > 0:
            qpainter.drawText(target_rect, QtCore.Qt.AlignCenter, str(self.number))

        qpainter.end()


class BadgeMixin(type(QtCore.QObject), BadgeMetaclass):
    pass


class BadgeOverlayWidget(object, metaclass=BadgeMixin):
    pass


def _test_interface():

    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    class TestLabel(QtWidgets.QLabel, metaclass=BadgeMixin):
        def __init__(self):
            super().__init__()
            self.setText("this is some test text")
            print(self.number)

        def paintEvent(self, event: QtGui.QPaintEvent):
            super().paintEvent(event)
            self.paint_badge(self, event)

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QGridLayout()

    widget = TestLabel()
    widget.number = 3
    layout.addWidget(widget)

    widget = TestLabel()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
