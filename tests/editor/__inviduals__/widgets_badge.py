import logging
import sys

from Qt import QtWidgets
from Qt import QtGui

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.widgets.badge import BadgeOverlayWidget

logger = logging.getLogger(__name__)


def show():
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

    _configureLogging(force_debug=True)
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
    show()
