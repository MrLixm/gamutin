import logging
import sys

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window

from gamutin.editor.widgets.colorpicker.sliders.compound import FloatSliderWidget

logger = logging.getLogger(__name__)


STYLESHEET = (
    # no selector intentional
    "QFrame{"
    "   background-color: red;"
    "   border-radius: 15px;"
    "   border: 2px solid orange;"
    "} "
    "QFrame#FloatGradientSliderCursor{"
    "   border: 2px solid magenta;"
    "   background-color: blue;"
    "   border-radius: 3px;"
    "} "
    "QFrame#FloatGradientSliderCursor:disabled{"
    "   border-color: grey;"
    "} "
    "QLabel{"
    "   background-color: transparent;"
    "   border: unset;"
    "} "
)

# dark blue red green gradient
COLOR_RANGE_A = [
    (0, QtGui.QColor(0, 0, 150)),
    (0.5, QtGui.QColor(255, 0, 0)),
    (1, QtGui.QColor(0, 255, 0)),
]

# light green pink blue gradient
COLOR_RANGE_B = [
    (0, QtGui.QColor(70, 240, 90)),
    (0.5, QtGui.QColor(230, 100, 150)),
    (1, QtGui.QColor(50, 80, 220)),
]


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()
    window.set_active_theme(window.themes.default)
    window.setStyleSheet(STYLESHEET)
    # remove stretch
    item = window.layout.itemAt(len(window.layout.children()))
    window.layout.removeItem(item)

    layout = QtWidgets.QVBoxLayout()

    layout.addWidget(QtWidgets.QLabel("<h1>FloatSliderWidget</h1>"))

    layout.addWidget(QtWidgets.QLabel("[-10,10] range"))
    widget = FloatSliderWidget()
    widget.set_display_color_range(color_range=COLOR_RANGE_B)
    widget.minimum = -10
    widget.maximum = 10
    layout.addWidget(widget)

    layout.addWidget(QtWidgets.QLabel("default"))
    widget = FloatSliderWidget()
    layout.addWidget(widget)

    layout.addWidget(QtWidgets.QLabel("regular, no stylesheet"))
    widget = FloatSliderWidget()
    widget.setStyleSheet("QFrame{border: unset;}")
    layout.addWidget(widget)

    layout.addWidget(QtWidgets.QLabel("max 25, css min-height"))
    widget = FloatSliderWidget()
    widget.setStyleSheet("QFrame{border: unset; min-height: 35px;}")
    widget.maximum = 25
    layout.addWidget(widget)

    layout.addWidget(QtWidgets.QLabel("allow_out_of_range"))
    widget = FloatSliderWidget()
    widget.allow_out_of_range(True)
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()