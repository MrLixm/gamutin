import sys

from Qt import QtWidgets

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.exceptions import WidgetUserError
from gamutin.editor.assets.widgets.pathselector import PathSelector
from gamutin.editor.assets.widgets.pathselector import PathType


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QVBoxLayout()
    layout.setSpacing(25)

    window.add_layout(layout)
    lineedit_demo = QtWidgets.QLineEdit()

    def setup_PathSelector(path_selector):
        path_selector.error_signal.connect(
            lambda message: window.show_message(str(message), 3000)
        )
        path_selector.path_changed_signal.connect(
            lambda message: window.show_message(str(message), 3000)
        )

    for path_type in PathType.__all__():
        row_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(row_layout)

        for is_enabled in [True, False]:
            widget = PathSelector()
            widget.set_path_type(path_type)
            widget.setEnabled(is_enabled)
            setup_PathSelector(widget)
            row_layout.addWidget(widget)

            if path_type == PathType.error:
                widget.set_error(WidgetUserError(TypeError, window, "test error"))

    widget = PathSelector()
    widget.set_path_type(PathType.file_exist)
    widget.set_expected_file_extensions([".jpg", ".py"])
    setup_PathSelector(widget)
    layout.addWidget(widget)

    widget = PathSelector()
    widget.set_path_type(PathType.file_exist)
    widget.set_expected_file_extensions([".jpg", ".py"])
    widget.toggle_display_error_message(False)
    setup_PathSelector(widget)
    layout.addWidget(widget)

    layout.addStretch(1)
    layout.addWidget(lineedit_demo)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
