__all__ = ("",)

import sys

from Qt import QtWidgets

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.assets.widgets.colorpicker.displaywidget import (
    ColorDisplayAdvancedWidget,
)


TEST_STYLE = """
QWidget{
    background-color: transparent;
    color: #fefefe;
    border: unset;
}
QWidget#testWindow{
    background-color: rgb(25,25,25);
}
QWidget#colorValueRow{
    min-height: 35px;
    background-color: rgb(40,40,40);
}
QTabBar::tab{
    min-width: 40px;
    min-height: 25px;
    background-color: rgb(25,25,25);
}
QTabBar::tab:selected{
    background-color: rgb(40,40,40);
}
QLineEdit#colorValues{
    padding-right: 10px;
}
QWidget#colorspaceDisplay{
    min-height: 30px;
    margin-right: 10px;
}
QWidget#colorspaceDisplay::menu-indicator{
    subcontrol-origin: padding;
    subcontrol-position: right center;
}
"""


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window(350, 300)
    window.set_active_theme(window.themes.default)
    window.layout.setContentsMargins(0, 0, 0, 0)
    window.layout_user.setContentsMargins(0, 0, 0, 0)
    window.setStyleSheet(TEST_STYLE)

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)

    widget = ColorDisplayAdvancedWidget()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
