import logging
import sys

from Qt import QtWidgets
from Qt import QtGui

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.widgets.colorpicker.sliders.gradientslider import (
    FloatGradientSlider,
)
from gamutin.editor.widgets.colorpicker.sliders.compound import FloatSliderWidget

logger = logging.getLogger(__name__)


STYLESHEET = (
    "QFrame{"
    "background-color: red;"
    "border-radius: 15px;"
    "border: 2px solid orange;"
    "} "
    "QFrame#FloatValueSliderPosition{"
    "border: 2px solid blue;"
    "background-color: blue;"
    "border-radius: 3px;"
    "} "
    "QLabel{"
    "background-color: transparent;"
    "border: unset;"
    "}"
)


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()
    window.set_active_theme(window.themes.default)
    window.setStyleSheet(STYLESHEET)

    layout = QtWidgets.QVBoxLayout()

    widget = FloatGradientSlider()
    widget.set_display_color_range(
        color_range=[
            (0, QtGui.QColor(0, 0, 150)),
            (0.5, QtGui.QColor(255, 0, 0)),
            (1, QtGui.QColor(0, 255, 0)),
        ]
    )
    layout.addWidget(widget)

    for margins in [
        (-5, -50, -5, -50),
        (-50, -5, -50, -5),
        (-5, -5, -5, -5),
    ]:
        widget = QtWidgets.QLabel(str(margins))
        layout.addWidget(widget)
        widget = FloatGradientSlider()
        widget.set_display_color_range(
            color_range=[
                (0, QtGui.QColor(70, 240, 90)),
                (0.5, QtGui.QColor(230, 100, 150)),
                (1, QtGui.QColor(50, 80, 220)),
            ]
        )
        widget._slider_margins = margins
        layout.addWidget(widget)

    widget = FloatSliderWidget()
    layout.addWidget(widget)

    widget = FloatSliderWidget()
    widget.setStyleSheet("QFrame{border: unset;}")
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
