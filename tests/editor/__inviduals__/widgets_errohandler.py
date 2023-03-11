import logging
import sys
import random
from functools import partial

from Qt import QtWidgets

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.widgets.errorhandler import ErrorHandlerWidget
from gamutin.editor.widgets.errorhandler import ErrorHandlerTreeWidget
from gamutin.editor.exceptions import WidgetUserError


logger = logging.getLogger(__name__)


def show():
    _configureLogging(force_debug=True)
    app = getQApp()

    all_errors_created: list[WidgetUserError] = []

    window = get_testing_window()

    layout = QtWidgets.QVBoxLayout()
    widget1 = ErrorHandlerWidget()
    widget2 = ErrorHandlerTreeWidget()
    button1 = QtWidgets.QPushButton("Add Error 1")
    button2 = QtWidgets.QPushButton("Add Error 2")
    button3 = QtWidgets.QPushButton("Delete Last Error")
    button4 = QtWidgets.QPushButton("Update Widgets")

    window.add_layout(layout)
    layout.setSpacing(25)
    layout.addWidget(widget1)
    layout.addWidget(widget2)
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addWidget(button4)

    def create_error(source_widget):
        error = WidgetUserError(
            RuntimeError,
            source_widget,
            f"A test error {random.random()}",
            "And this shoudl be the detailed message which is much more long usually.",
        )
        widget1.add_error(error)
        widget2.add_error(error)
        all_errors_created.append(error)

    def delete_last_error():
        last_error = all_errors_created[-1]
        last_error.delete()
        window.show_message(f"Deleted {repr(last_error)}")

    def update_widgets():
        widget1.update_errors()
        widget2.update_errors()

    button1.clicked.connect(partial(create_error, button1))
    button2.clicked.connect(partial(create_error, button2))
    button3.clicked.connect(delete_last_error)
    button4.clicked.connect(update_widgets)

    layout2 = QtWidgets.QVBoxLayout()
    error_1 = WidgetUserError(
        ValueError,
        layout2,
        f"An other test error with {random.random()} number.",
        "And this shoudl be the detailed message which is much more long usually.",
    )

    widget = ErrorHandlerWidget()
    widget.toggle_visibility_of(text_visible=False)
    widget.add_error(error_1)
    layout2.addWidget(widget)

    widget = ErrorHandlerWidget()
    widget.toggle_visibility_of(icon_visible=False)
    widget.add_error(error_1)
    layout2.addWidget(widget)

    layout.addLayout(layout2)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
