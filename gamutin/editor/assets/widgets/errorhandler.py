from __future__ import annotations

__all__ = (
    "ErrorHandlerTreeWidget",
    "ErrorHandlerWidget",
    "ErrorIcon",
    "ErrorTreeWidgetItem",
)

import json
import logging
from typing import Optional

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from gamutin.editor.cfg import resources
from gamutin.editor.utils import copy_to_clipboard
from gamutin.editor.exceptions import WidgetUserError
from gamutin.editor.assets.widgets.icons import BaseDisplayIcon
from gamutin.editor.assets.widgets.badge import BadgeOverlayWidget

logger = logging.getLogger(__name__)


class ErrorIcon(BaseDisplayIcon, BadgeOverlayWidget):
    """
    A simple transparent icon to represent an issue.

    A rounded outlined  circle with an exaclamation mark inside.
    """

    def __init__(self, error_handler: Optional[ErrorHandlerWidget] = None):
        super().__init__()
        self.setIcon(QtGui.QIcon(str(resources.icon_alert_outline)))
        self.enable_scaling_on_active(True, 0.15)
        self.setMargin(8)
        self.error_handler: Optional[ErrorHandlerWidget] = error_handler
        self.badge_size = 12

    def refresh(self):

        if self.error_handler:
            self.badge_number = len(self.error_handler.errors)
        else:
            self.badge_number = None

        self.setToolTip(self.error_handler.current_error_message)
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent):
        super().paintEvent(event)
        if self.error_handler:
            self.paint_badge(event)


class ErrorTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    """
    TreeWidget Item representation of a :class:`WidgetUserError` instance.
    """

    columns = ["Name", "Message", "Source"]

    def __init__(self, error: WidgetUserError, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.error = error

        self.setText(0, self.error.name)
        self.setText(1, self.error.message)
        self.setText(2, str(self.error.widget))


class ErrorHandlerTreeWidget(QtWidgets.QTreeWidget):
    """
    TreeWidget to hold and display multiples :class:`WidgetUserError`
    """

    def __init__(self, parent: QtWidgets.QWidget = None):

        super().__init__(parent)

        self.setColumnCount(len(ErrorTreeWidgetItem.columns))
        self.setRootIsDecorated(False)
        self.setAlternatingRowColors(False)
        self.setUniformRowHeights(True)
        self.setSortingEnabled(True)
        self.setItemsExpandable(False)
        # select only one row at a time
        self.setSelectionMode(self.MultiSelection)
        # select only rows
        self.setSelectionBehavior(self.SelectRows)
        # remove dotted border on columns
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        self.setHeaderLabels(ErrorTreeWidgetItem.columns)
        header = self.header()
        # The user can resize the section
        header.setSectionResizeMode(header.Interactive)
        header.setSectionResizeMode(0, header.ResizeToContents)
        header.setSectionResizeMode(2, header.Stretch)
        header.setSortIndicator(0, QtCore.Qt.AscendingOrder)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested[QtCore.QPoint].connect(self.show_context_menu)

    def add_error(self, error: WidgetUserError) -> ErrorTreeWidgetItem:

        error_item = ErrorTreeWidgetItem(error, self)
        self.update_errors()  # take the opportunity to refresh
        return error_item

    def copy_selection_as_json(self):

        out_dict = {}
        selected_items: list[ErrorTreeWidgetItem] = self.selectedItems()

        for item_index, item in enumerate(selected_items):
            out_dict[item_index] = item.error.as_dict()

        copy_to_clipboard(json.dumps(out_dict, indent=4, default=str, sort_keys=True))

    def get_all_items(self) -> list[ErrorTreeWidgetItem]:
        """
        Get all the qt items stored in the tree widget.

        References:
            [1] https://stackoverflow.com/questions/8961449/pyqt-qtreewidget-iterating
        """

        item_list = list()
        root = self.invisibleRootItem()
        child_count = root.childCount()
        # iterate through the direct child of the invisible_root_item
        for index in range(child_count):
            qitem_child = root.child(index)
            item_list.append(qitem_child)

        return item_list

    def show_context_menu(self, *args):

        menu = QtWidgets.QMenu()
        selected_items: list[ErrorTreeWidgetItem] = self.selectedItems()

        if selected_items:
            action_copy = QtWidgets.QAction("Copy Selected Errors As Json")
            action_copy.triggered.connect(self.copy_selection_as_json())
            menu.addAction(action_copy)

        menu.exec_(QtGui.QCursor.pos())
        return

    def update_errors(self):
        """
        Parse all the erros holded and remove the one that were marked as deleted.
        """

        for error_item in self.get_all_items():

            if error_item.error.is_deleted:
                self.invisibleRootItem().removeChild(error_item)


class ErrorHandlerWidget(QtWidgets.QWidget):
    """
    A horizontal widget to stock and manage errors.

    The widget only display the last error but offer options to display all the errors.
    """

    def __init__(self, parent=None):
        # type: (QtWidgets.QWidget) -> None
        super().__init__(parent)

        self._errors: list[WidgetUserError] = []
        self.setObjectName("ErrorHandlerWidget")

        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QHBoxLayout()
        self.icon_error = ErrorIcon(error_handler=self)
        self.label_time = QtWidgets.QLabel()
        self.label_error = QtWidgets.QLabel()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.icon_error)
        self.layout.addWidget(self.label_time)
        self.layout.addWidget(self.label_error)
        self.layout.addStretch(0)

        # 3. Modify
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        for label in [self.label_error, self.label_time]:
            label.setProperty(
                str(resources.theme_default.var_error_text_colored.value), True
            )
        # 4. Connections
        self.customContextMenuRequested[QtCore.QPoint].connect(self.show_context_menu)
        return

    def bakeUI(self):

        self.setVisible(False)
        self.label_error.setText("")
        self.label_time.setText("")
        if not self._errors:
            return

        last_error = self._errors[-1]

        self.setVisible(True)
        self.icon_error.refresh()
        self.label_time.setText(last_error.time_clock())
        self.label_error.setText(f"{last_error.name}: {last_error.message}")

    @property
    def errors(self) -> list[WidgetUserError]:
        """
        Get all the *active* errors this widget is holding.
        """
        self.filter_errors()
        return self._errors

    @property
    def current_error_message(self) -> str:
        return f"{self.label_time.text()} {self.label_error.text()}"

    def add_error(self, error: WidgetUserError):
        self.update_errors()
        self._errors.append(error)
        self.bakeUI()

    def copy_current_error(self):
        """
        Copy error message currently being displayed to application clipboard.
        """
        copy_to_clipboard(self.current_error_message)

    def filter_errors(self):
        """
        Remove all the errors that have been deleted.

        Use :meth:`update_errors` to also refresh the ui.
        """

        def should_keep_error(error: WidgetUserError):
            return not error.is_deleted

        self._errors = list(filter(should_keep_error, self._errors))
        return

    def show_context_menu(self, *args):

        menu = QtWidgets.QMenu()

        action_copy = QtWidgets.QAction("Copy Error")
        action_copy.triggered.connect(self.copy_current_error)

        action_show_all = QtWidgets.QAction("Show All Errors")
        action_show_all.triggered.connect(self.show_all_error_widget)

        menu.addAction(action_copy)
        menu.addAction(action_show_all)

        menu.exec_(QtGui.QCursor.pos())
        return

    def show_all_error_widget(self):
        """
        Show a TreeWidget with all the error for better parsing.
        """

        window = QtWidgets.QMainWindow(self)
        window.setWindowTitle("Error Handler")
        widget = ErrorHandlerTreeWidget(parent=QtWidgets.QApplication.activeWindow())
        for error in self.errors:
            widget.add_error(error=error)
        window.setCentralWidget(widget)
        window.setContentsMargins(*(15,) * 4)
        window.show()

    def update_errors(self):
        """
        Remove all the errors that have been deleted and refresh the interface.
        """
        self.filter_errors()
        self.bakeUI()


def _test_interface():

    import sys
    import random
    from functools import partial
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
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

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
