from __future__ import annotations

import enum
import sys
import webbrowser
from pathlib import Path
from typing import Optional
from typing import Callable

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from pgcheck.editor.cfg import resources
from pgcheck.core.io import is_path_exists_or_creatable
from pgcheck.editor.compounds.widgets.icons import BaseDisplayIcon


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

    stylesheet = f"""
    QFrame#PathSelector{{
        border: 1px solid rgb(63,63,63);
        border-radius: 10px;
    }}
    QFrame[dropState="true"]{{
        background-color: rgba(255,255,255,0.15);
    }}
    QFrame:disabled#PathSelector{{
        border-color: rgb(50,50,50);
    }}

    *[errorFrame="true"]{{
        border: 1px solid rgba{resources.colors.error_red.value.toTuple()};
    }}
    *[errorState="true"]{{
       color: rgba{resources.colors.error_red.value.toTuple()};
    }}

    """

    error_signal = QtCore.Signal(str)
    """
    Signal emitted when a error happens. Data emmitted is the error message.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._path_type: Optional[PathType] = None
        self._error_message: Optional[str] = None
        self._expected_file_extensions: list[str] = []

        self.setStyleSheet(self.stylesheet)
        self.setObjectName("PathSelector")
        self.setAcceptDrops(True)

        self.cookUI()
        self.bakeUI()

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
            self.error_signal.emit(f"[DropError] {excp}")
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
        self.setProperty("dropState", enable)
        self.setStyleSheet(self.stylesheet)

    @property
    def current_path(self) -> Path:
        """
        Path currently set in the interface.

        Never return None, when no path is specified the current working directory
        is returned instead. (``current_path == Path(".")``)

        When possible an absolute path is returned.
        """
        path = Path(self.lineedit_path.text())
        try:
            return path.resolve().absolute()
        except OSError:
            return path

    @current_path.setter
    def current_path(self, new_path: Path):
        self.lineedit_path.setText(str(new_path))

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QGridLayout()

        self.button_icon = PathInfoIcon()
        self.lineedit_path = QtWidgets.QLineEdit()
        self.button_browse = QtWidgets.QPushButton("Browse")
        self.label_error = QtWidgets.QLabel()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_icon, 0, 0)
        self.layout.addWidget(self.lineedit_path, 0, 1)
        self.layout.addWidget(self.button_browse, 0, 2)
        self.layout.addWidget(self.label_error, 1, 1)

        # 3. Modify
        self.layout.setVerticalSpacing(0)
        self.label_error.setProperty("errorState", True)
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

    def bakeUI(self):

        self.button_icon.set_type(path_type=self._path_type)

        if self._error_message is not None:
            self.button_icon.set_type(path_type=PathType.error)
            self.lineedit_path.setProperty("errorFrame", True)
            self.label_error.setVisible(True)
            self.label_error.setText(self._error_message)
        else:
            self.lineedit_path.setProperty("errorFrame", False)
            self.label_error.setVisible(False)
            self.label_error.setText("")

    def get_error(self) -> Optional[str]:
        """
        Get the current error message if any.

        Returns:
            None if the path is valid else an nicely formatted error message.
        """
        return self._error_message

    def is_path_invalid(self, path: Path) -> Optional[str]:
        """
        Find if the current path set is invalid.

        This doesn't modify the interface to notice it to the user. You must call
        :meth:`set_error` for this.

        Returns:
            The error message if invalid else None if valid.
        """
        error_message = None
        is_valid = self._path_type.get_validate(self._path_type)(path)

        if not is_valid:
            error_message = self._path_type.get_error_message(self._path_type)

        if (
            is_valid
            and "file" in self._path_type.name
            and self._expected_file_extensions
            and path.suffix not in self._expected_file_extensions
        ):
            error_message = f"Invalid extension: '{path.suffix}' not in {self._expected_file_extensions}"

        return error_message

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

    def open_current_path_in_explorer(self):
        """
        Open the current path's directory in the system default file explorer.
        """
        path = self.current_path

        if not path.exists():
            return

        if path.is_file():
            path = path.parent

        webbrowser.open(str(path))
        return

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

    def set_error(self, error_message: Optional[str]):
        """
        Set the widget to the error state with the given reason.

        Args:
            error_message: error message to set in the UI. None to remove the error state.
        """
        if error_message:
            self.error_signal.emit(error_message)

        self._error_message = error_message
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

    def _on_context_menu_requested(self, pointer: QtCore.QPoint):
        def make_current_path_absolute():
            self.current_path = self.current_path

        menu = self.lineedit_path.createStandardContextMenu()

        if self.current_path.exists():

            action1 = QtWidgets.QAction("Open in Explorer")
            action1.triggered.connect(self.open_current_path_in_explorer)

            action2 = QtWidgets.QAction("Make Relative Path Absolute")
            action2.triggered.connect(make_current_path_absolute)

            menu.addSeparator()
            menu.addAction(action1)
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

    from pgcheck.editor.main import getQApp

    app = getQApp()

    layout = QtWidgets.QVBoxLayout()
    layout.setSpacing(25)

    window = QtWidgets.QWidget()
    window.setLayout(layout)
    window.setStyleSheet(
        """
        .QWidget{
            background-color: rgb(150,150,150);
        }
        """
    )

    status_bar = QtWidgets.QStatusBar()
    lineedit_demo = QtWidgets.QLineEdit()

    for path_type in PathType.__all__():

        row_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(row_layout)

        for is_enabled in [True, False]:

            widget = PathSelector()
            widget.set_path_type(path_type)
            widget.setEnabled(is_enabled)
            widget.error_signal.connect(
                lambda message: status_bar.showMessage(message, 2000)
            )
            row_layout.addWidget(widget)

            if path_type == PathType.error:
                widget.set_error("test error")

    widget = PathSelector()
    widget.set_path_type(PathType.file_exist)
    widget.set_expected_file_extensions([".jpg", ".py"])
    widget.error_signal.connect(lambda message: status_bar.showMessage(message, 2000))

    layout.addWidget(widget)
    layout.addStretch(1)
    layout.addWidget(lineedit_demo)
    layout.addWidget(status_bar)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()