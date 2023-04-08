import logging
import sys

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.widgets.colorpicker.sliders.compound import FloatSliderWidget

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
    app = getQApp()
    window = get_testing_window()
    # remove stretch
    item = window.layout.itemAt(len(window.layout.children()))
    window.layout.removeItem(item)

    layout = QtWidgets.QVBoxLayout()

    layout.addWidget(QtWidgets.QLabel("<h1><code>set_cursor_scale()</code></h1>"))
    slider_src = FloatSliderWidget()
    slider_src.set_display_color_range(color_range=COLOR_RANGE_B)
    slider_src.setMinimumHeight(25)
    FloatSliderWidget()

    cursor_scale_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
    cursor_scale_slider.setMinimum(-100)
    cursor_scale_slider.setMaximum(100)

    text_editor = QtWidgets.QTextEdit()
    text_editor.setMaximumHeight(120)
    text_editor.setTabStopDistance(
        QtGui.QFontMetricsF(text_editor.font()).horizontalAdvance(" ") * 4
    )
    text_editor.setText(
        "QFrame{\n"
        "    border-radius: 0px;"
        "    qproperty-cursor_circle: 0;"
        "\n}\n\n"
        "QFrame#FloatGradientSliderCursor{\n"
        "    max-width: 10px"
        "\n}"
    )

    def set_cursor_scale(new_value: int):
        scale = (new_value + 100) / 100
        slider_src.slider.set_cursor_scale(scale)
        cursor_scale_slider.setToolTip(str(scale))

    def set_stylesheet():
        text = text_editor.toPlainText()
        slider_src.setStyleSheet(text)

    cursor_scale_slider.valueChanged.connect(set_cursor_scale)
    text_editor.textChanged.connect(set_stylesheet)
    set_stylesheet()

    layout.addWidget(cursor_scale_slider)
    layout.addWidget(text_editor)
    layout.addWidget(slider_src)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
