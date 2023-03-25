import logging
import sys

from Qt import QtWidgets
from Qt import QtGui

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.widgets.colorpicker.valueslider import FloatValueSlider
from gamutin.editor.widgets.colorpicker.valueslider import FloatSliderWidget

logger = logging.getLogger(__name__)


STYLESHEET = (
    "QFrame{"
    "background-color: red;"
    "border-radius: 15px;"
    "border: 2px solid blue;"
    "} "
    "QFrame#FloatValueSliderPosition{"
    "border: 2px solid white;"
    "background-color: blue;"
    "border-radius: 3px;"
    "} "
)


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()
    window.set_active_theme(window.themes.default)
    window.setStyleSheet(STYLESHEET)

    layout = QtWidgets.QVBoxLayout()

    widget = FloatValueSlider()
    widget.set_display_color_range(
        color_range=[
            (0, QtGui.QColor(0, 0, 150)),
            (0.5, QtGui.QColor(255, 0, 0)),
            (1, QtGui.QColor(0, 255, 0)),
        ]
    )
    # widget.setStyleSheet(STYLESHEET)
    layout.addWidget(widget)

    widget = FloatSliderWidget()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
