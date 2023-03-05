__all__ = ("",)

import sys

from Qt import QtWidgets

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.assets.widgets.colorpicker.displaywidget import (
    ColorDisplayAdvancedWidget,
)


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()
    window.resize(350, 200)
    window.layout.setContentsMargins(0, 0, 0, 0)
    window.layout_user.setContentsMargins(0, 0, 0, 0)

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)

    widget = ColorDisplayAdvancedWidget()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
