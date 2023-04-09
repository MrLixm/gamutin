import logging
import sys
from pathlib import Path

from Qt import QtWidgets

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
import gamutin.editor.widgets.colorpicker
from gamutin.editor.widgets.colorpicker.main import ColorPickerWidget

logger = logging.getLogger(__name__)


def get_dev_stylesheet():
    root = Path(gamutin.editor.widgets.colorpicker.__path__[0])
    path = root / "stylesheet.css"
    stylesheet = path.read_text()
    return stylesheet


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()
    window.set_active_theme(window.themes.default)
    window.layout.setContentsMargins(0, 0, 0, 0)
    window.layout_user.setContentsMargins(0, 0, 0, 0)
    window.setStyleSheet(get_dev_stylesheet())

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)

    widget = ColorPickerWidget()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.resize(300, 450)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
