from __future__ import annotations

import enum
import logging
import sys
import webbrowser
from pathlib import Path
from typing import Optional
from typing import Callable

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.core.io import is_path_exists_or_creatable
from gamutin.editor.cfg import resources
from gamutin.editor.exceptions import WidgetUserError
from gamutin.editor.assets.widgets.icons import BaseDisplayIcon
from gamutin.editor.assets.widgets.errorhandler import ErrorHandlerWidget


logger = logging.getLogger(__name__)


class PathType(enum.Enum):
    """
    Different types of path expected.

    A path can only correspond to one of this type at a time.
    """

    file_exist = {
        "description": "A path to a single file existing on disk.",
        "error_message": "Given path is not an existing file on disk.",
        "icon_path": resources.icon_file_check_outline,
        "validate": lambda path: path.exists() and path.is_file(),
        "qtmode": QtWidgets.QFileDialog.ExistingFile,
    }
    file = {
        "description": "A path to a single file that might or might not exist.",
        "error_message": "Given file path might already exists OR not be a valid path that can be created.",
        "icon_path": resources.icon_file_outline,
        "validate": lambda path: is_path_exists_or_creatable(path) and path.suffix,
        "qtmode": QtWidgets.QFileDialog.AnyFile,
    }
    directory_exists = {
        "description": "A path to a single directory existing on disk.",
        "error_message": "Given path is not an existing directory on disk.",
        "icon_path": resources.icon_folder_check,
        "validate": lambda path: path.exists() and path.is_dir(),
        "qtmode": QtWidgets.QFileDialog.Directory,
    }
    directory = {
        "description": "A path to a single directory that might or might not exist.",
        "error_message": "Given directory path might already exists OR not be a valid path that can be created.",
        "icon_path": resources.icon_folder,
        "validate": lambda path: is_path_exists_or_creatable(path) and not path.suffix,
        "qtmode": QtWidgets.QFileDialog.Directory,
    }
    error = {
        "description": "A invalid path.",
        "error_message": "Invalid path.",
        "icon_path": resources.icon_alert_outline,
        "validate": lambda path: False,
        "qtmode": None,
    }

    @classmethod
    def __all__(cls):
        return [item for item in cls]

    @classmethod
    def get_description(cls, path_type: PathType) -> str:
        return path_type.value["description"]

    @classmethod
    def get_error_message(cls, path_type: PathType) -> str:
        return path_type.value["error_message"]

    @classmethod
    def get_icon_path(cls, path_type: PathType) -> Path:
        return path_type.value["icon_path"]

    @classmethod
    def get_validate(cls, path_type: PathType) -> Callable[[Path], bool]:
        return path_type.value["validate"]

    @classmethod
    def get_qtmode(
        cls, path_type: PathType
    ) -> Optional[QtWidgets.QFileDialog.FileMode]:
        return path_type.value["qtmode"]


class PathSelector(QtWidgets.QFrame):
    """
    A widget made for the user to input a path.

    Various options to handle different types of paths are offered.

    The path set can be retrieved via :prop:`current_path`.

    If the path is invalid an error message can be retrieved via :meth:`get_error`
    """

    error_signal = QtCore.Signal(object)
    """
    Signal emitted when an error is produced OR disappear. 

    Data Type emmitted is a :class:`WidgetUserError` instance when an error is produced.
    Data Type emmitted is a :obj:`None` if the previous error has been cleared.
    """

    path_changed_signal = QtCore.Signal(object)
    """
    Signal emitted when the path is changed. 

    Not emitted when a error is produced.
    Data Type emmitted is a :class:`Path` instance.
    """

    class Properties:
        """
        Qt properties that can be used in the stylesheet for advanced styling.
        """

        dropState = str(resources.theme_default.var_drop_state.value)
        errorState = str(resources.theme_default.var_error_state.value)
        errorFrame = str(resources.theme_default.var_error_frame.value)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._path_type: Optional[PathType] = None
        self._error: Optional[WidgetUserError] = None
        self._display_error_message: bool = True
        self._expected_file_extensions: list[str] = []

        self.setObjectName("PathSelector")
        self.setAcceptDrops(True)

        self.cookUI()
        self.bakeUI()

    @property
    def current_path(self) -> Optional[Path]:
        """
        Path currently set in the interface.

        When possible an absolute resolved path is returned.
        """
        path_input = self.lineedit_path.text()
        if not path_input:
            return None

        path = Path(path_input)
        try:
            return path.resolve().absolute()
        except OSError:
            return path

    @current_path.setter
    def current_path(self, new_path: Optional[Path]):
        new_path = new_path or ""
        self.lineedit_path.setText(str(new_path))

    def bakeUI(self):

        if self._error and self._error.is_deleted:
            self._error = None

        self.button_icon.set_type(path_type=self._path_type)

        self.label_error.setVisible(
            self._error is not None and self._display_error_message
        )
        self.label_error.update_errors()

        if self._error is not None:
            self.button_icon.set_type(path_type=PathType.error)
            self.lineedit_path.setProperty(self.Properties.errorFrame, True)
            self.label_error.add_error(self._error)
        else:
            self.lineedit_path.setProperty(self.Properties.errorFrame, False)

    def browse_path(self):
        """
        Open a file dialog to browse a path.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setWindowTitle(self._path_type.get_description(self._path_type))
        if file_mode := self._path_type.get_qtmode(self._path_type):
            file_dialog.setFileMode(file_mode)
        if self._expected_file_extensions:
            supported_extensions = " *".join(self._expected_file_extensions)
            file_dialog.setNameFilter(f"Supported (*{supported_extensions});; Any (*)")
        if self.current_path:
            start_path = self.current_path
            if start_path.is_file():
                start_path = start_path.parent
            file_dialog.setDirectory(str(start_path))

        if file_dialog.exec_() != file_dialog.Accepted:
            return

        user_selection = file_dialog.selectedFiles()
        file_path = user_selection[0]
        self.current_path = Path(file_path)

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QGridLayout()

        self.button_icon = PathInfoIcon()
        self.lineedit_path = QtWidgets.QLineEdit()
        self.button_browse = QtWidgets.QPushButton("Browse")
        self.label_error = ErrorHandlerWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_icon, 0, 0)
        self.layout.addWidget(self.lineedit_path, 0, 1)
        self.layout.addWidget(self.button_browse, 0, 2)
        self.layout.addWidget(self.label_error, 1, 1)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setVerticalSpacing(0)
        self.label_error.toggle_visibility_of(icon_visible=False)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lineedit_path.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # 4. Connections
        self.lineedit_path.textChanged.connect(self.on_path_changed)
        self.button_browse.clicked.connect(self.browse_path)
        self.customContextMenuRequested[QtCore.QPoint].connect(
            self._on_context_menu_requested
        )
        self.lineedit_path.customContextMenuRequested[QtCore.QPoint].connect(
            self._on_context_menu_requested
        )
        return

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        """
        User starting a drag&drop, producing a "drag".
        """

        try:

            self.process_drop_event(event=event)
            self.set_drop_style(True)
            event.setDropAction(QtCore.Qt.LinkAction)
            event.accept()

        except InterruptedError as excp:
            logger.error(f"[{self.__class__.__name__}][dragEnterEvent] {excp}")
            event.setDropAction(QtCore.Qt.IgnoreAction)
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent):
        """
        User released the drag&drop, producing a "drop".
        """
        self.current_path = self.process_drop_event(event=event)
        self.set_drop_style(False)

    def dragLeaveEvent(self, event: QtGui.QDragLeaveEvent):
        """
        User aborted drag&drop.
        """
        self.set_drop_style(False)

    def get_error(self) -> Optional[WidgetUserError]:
        """
        Get the current error object if any.

        Returns:
            None if the path is valid else a error instance with a nicely formatted error message.
        """
        return self._error

    def is_path_invalid(self, path: Optional[Path]) -> Optional[WidgetUserError]:
        """
        Find if the current path set is invalid.

        This doesn't modify the interface to notice it to the user. You must call
        :meth:`set_error` for this.

        Returns:
            An error instance if invalid else None if valid.
        """
        if path is None:
            return WidgetUserError(ValueError, self, "No path specified.")

        error = None

        is_valid = self._path_type.get_validate(self._path_type)(path)
        if not is_valid:
            error = WidgetUserError(
                "PathInvalid",
                self,
                message=self._path_type.get_error_message(self._path_type),
            )

        if (
            is_valid
            and "file" in self._path_type.name
            and self._expected_file_extensions
            and path.suffix not in self._expected_file_extensions
        ):
            error = WidgetUserError(
                "PathExtensionInvalid",
                self,
                message=f"Invalid extension: '{path.suffix}' not in {self._expected_file_extensions}",
            )

        return error

    def on_path_changed(self):
        """
        Callback called when the path is edited by the user.
        """

        current_text = self.lineedit_path.text()
        # On Windows the default option to copy file path wrap it with quotes,
        # so it's convenient to remove them.
        if (
            sys.platform in ["win32", "cygwin"]
            and current_text.startswith('"')
            and current_text.endswith('"')
        ):
            new_text = current_text.rstrip('"')
            new_text = new_text.lstrip('"')
            self.lineedit_path.setText(new_text)

        path_error = self.is_path_invalid(self.current_path)
        self.set_error(path_error)
        if not path_error and self.current_path:
            self.path_changed_signal.emit(self.current_path)

    def open_current_path_in_explorer(self):
        """
        Open the current path's directory in the system default file explorer.
        """
        path = self.current_path

        if not path or not path.exists():
            return

        if path.is_file():
            path = path.parent

        webbrowser.open(str(path))
        return

    def process_drop_event(self, event: QtGui.QDropEvent) -> Path:
        """

        Args:
            event: drop event with the data to use

        Returns:
            data from the drop properly converted for use. Currently, a Path.

        Raises:
            InterruptedError: if the data from the drop is invalid
        """
        if not event.mimeData() or not event.mimeData().hasUrls():
            raise InterruptedError("No or invalid mimeData type (expected URLs).")

        mime_urls = event.mimeData().urls()
        if len(mime_urls) != 1:
            raise InterruptedError("Only one URL expected, not multiple.")

        mime_urls: QtCore.QUrl = mime_urls[0]
        mime_path = Path(mime_urls.toLocalFile())

        path_error = self.is_path_invalid(mime_path)
        if path_error:
            raise InterruptedError(f"Path {mime_path} is invalid: {path_error}")

        return mime_path

    def set_drop_style(self, enable: bool):
        """
        Style the widget to make it looks like it accepts drag&drop or not.
        """
        self.setProperty(self.Properties.dropState, enable)
        self.style().polish(self)

    def set_error(self, error: Optional[WidgetUserError]):
        """
        Set the widget to the error state with the given reason.

        Args:
            error: error message to set in the UI. None to remove the error state.
        """
        if self._error:
            self._error.delete()

        if error:

            self.error_signal.emit(error)
            self._error = error

        else:

            self.error_signal.emit(None)
            self._error = None

        self.bakeUI()

    def set_path_type(self, path_type: Optional[PathType]):
        """
        Update the interface to expect a path only of the given type.
        """
        self._path_type = path_type
        self.bakeUI()

    def set_expected_file_extensions(self, file_extensions: list[str]):
        """
        Only used if the expected path type is one of a file but can always be called.

        Args:
            file_extensions:
                list of file extensions WITH the dot delimiter. ex: [".jpg", ".txt"]
        """
        self._expected_file_extensions = file_extensions

    def toggle_display_error_message(self, display_errors: bool):
        """
        Change if the widget should display an error message when something wrong happens.

        The error signals are still emitted.
        """
        self._display_error_message = display_errors
        self.bakeUI()

    def _on_context_menu_requested(self, pointer: QtCore.QPoint):
        def make_current_path_absolute():
            self.current_path = self.current_path

        menu = self.lineedit_path.createStandardContextMenu()
        menu.addSeparator()

        if self.current_path and self.current_path.exists():
            action1 = QtWidgets.QAction("Open in Explorer")
            action1.triggered.connect(self.open_current_path_in_explorer)
            menu.addAction(action1)

        action2 = QtWidgets.QAction("Make Relative Path Absolute")
        action2.triggered.connect(make_current_path_absolute)

        menu.addAction(action2)

        menu.exec_(QtGui.QCursor.pos())
        return


class PathInfoIcon(BaseDisplayIcon):
    """
    A single icon that can change depending on the current type assigned.

    Should give information about the path to input.
    """

    def __init__(self):
        super().__init__()
        self.set_type()

    def set_type(self, path_type: Optional[PathType] = None):
        """
        Args:
            path_type:
                change the icon to correspond to this type. Passing None will use
                the default icon which is an "information" one.
        """
        tooltip = ""
        if path_type:
            file_path = path_type.get_icon_path(path_type)
            tooltip += f"<p>{path_type.get_description(path_type)}</p>"
        else:
            file_path = resources.icon_information

        tooltip += "<p>Relative path supported (relative to the latest set working directory).</p>"
        self.setToolTip(tooltip)
        self.setIcon(QtGui.QIcon(str(file_path)))


def _test_interface():
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
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
    _test_interface()
