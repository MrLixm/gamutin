import sys

from Qt import QtWidgets


from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.assets.widgets.imageselector import ImageSelectorWidget


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QVBoxLayout()
    layout.setSpacing(25)

    window.add_layout(layout)

    widget = ImageSelectorWidget()
    layout.addWidget(widget)
    widget = ImageSelectorWidget()
    widget.toggle_channel_selection(False)
    layout.addWidget(widget)
    widget = ImageSelectorWidget()
    widget.toggle_channel_selection(False)
    widget.set_expected_file_extensions([".jpg", ".exr"])
    layout.addWidget(widget)

    layout.addStretch(1)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
