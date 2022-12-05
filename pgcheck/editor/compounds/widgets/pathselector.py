from __future__ import annotations

import enum
from pathlib import Path
from typing import Optional
from typing import Callable

from Qt import QtWidgets
from Qt import QtGui

from pgcheck.editor.cfg import resources
from pgcheck.core.io import is_path_exists_or_creatable
from pgcheck.editor.compounds.widgets.icons import BaseDisplayIcon


class PathType(enum.Enum):
    """
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
    A widget made for the user to give a path.

    Various options to handle different type of paths are offered.

    # TODO RMB menu to open path in explorer
    """

    stylesheet = f"""
    QFrame#PathSelector{{
        border: 1px solid rgb(63,63,63);
        border-radius: 10px;
    }}
    *[errorFrame="true"]{{
        border: 1px solid rgba{resources.colors.error_red.toTuple()};
    }}
    *[errorState="true"]{{
       color: rgba{resources.colors.error_red.toTuple()};
    }}

    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._path_type: Optional[PathType] = None
        self._error_message: Optional[str] = None
        self._expected_file_extensions: list[str] = []

        self.setStyleSheet(self.stylesheet)
        self.setObjectName("PathSelector")

        self.cookUI()
        self.bakeUI()

    @property
    def current_path(self) -> Path:
        return Path(self.lineedit_path.text())

    @current_path.setter
    def current_path(self, new_path: Path):
        self.lineedit_path.setText(str(new_path))

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.layout_top = QtWidgets.QHBoxLayout()
        self.layout_bottom = QtWidgets.QHBoxLayout()

        self.button_icon = InfoIcon()
        self.lineedit_path = QtWidgets.QLineEdit()
        self.button_browse = QtWidgets.QPushButton("Browse")
        self.label_error = QtWidgets.QLabel()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addLayout(self.layout_top)
        self.layout.addLayout(self.layout_bottom)
        self.layout_top.addWidget(self.button_icon)
        self.layout_top.addWidget(self.lineedit_path)
        self.layout_top.addWidget(self.button_browse)
        self.layout_bottom.addWidget(self.label_error)

        # 3. Modify
        self.label_error.setProperty("errorState", True)
        # 4. Connections
        self.lineedit_path.textChanged.connect(self.on_path_changed)
        self.button_browse.clicked.connect(self.browse_path)
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
        """
        return self._error_message

    def is_current_path_invalid(self) -> Optional[str]:
        """

        Returns:
            The error message if invalid else None if valid.
        """
        error_message = None
        is_valid = self._path_type.get_validate(self._path_type)(self.current_path)

        if not is_valid:
            error_message = self._path_type.get_error_message(self._path_type)

        if (
            is_valid
            and "file" in self._path_type.name
            and self._expected_file_extensions
            and self.current_path.suffix not in self._expected_file_extensions
        ):
            error_message = f"Invalid extension: '{self.current_path.suffix}' not in {self._expected_file_extensions}"

        return error_message

    def on_path_changed(self):
        """
        Callback called when the path is edited by the user.
        """
        path_error = self.is_current_path_invalid()
        self.set_error(path_error)

    def browse_path(self):
        """
        Open a file dialog to browse a path.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setWindowTitle(self._path_type.get_description(self._path_type))
        if file_mode := self._path_type.get_qtmode(self._path_type):
            file_dialog.setFileMode(file_mode)

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
        self._error_message = error_message
        self.bakeUI()

    def set_path_type(self, path_type: Optional[PathType]):
        self._path_type = path_type
        self.bakeUI()

    def set_expected_file_extensions(self, file_extensions: list[str]):
        """
        Args:
            file_extensions:
                list of file extensions with the dot delimiter. ex: [".jpg", ".txt"]
        """
        self._expected_file_extensions = file_extensions


class InfoIcon(BaseDisplayIcon):
    """
    A single icon that can change depending on the current type assigned.
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
        if path_type:
            file_path = path_type.get_icon_path(path_type)
            self.setToolTip(path_type.get_description(path_type))
        else:
            file_path = resources.icon_information

        self.setIcon(QtGui.QIcon(str(file_path)))


if __name__ == "__main__":

    import sys
    from pgcheck.editor.main import getQApp

    _app = getQApp()

    _layout = QtWidgets.QVBoxLayout()
    _window = QtWidgets.QWidget()
    _window.setLayout(_layout)
    _window.setStyleSheet(
        """
        .QWidget{
            background-color: rgb(150,150,150);
        }
        """
    )

    for _path_type in PathType.__all__():

        _widget = PathSelector()
        _widget.set_path_type(_path_type)
        _layout.addWidget(_widget)

        if _path_type == PathType.error:
            _widget.set_error("test error")

    _widget = PathSelector()
    _widget.set_path_type(PathType.file_exist)
    _widget.set_expected_file_extensions([".jpg", ".py"])
    _layout.addWidget(_widget)

    _window.show()

    sys.exit(_app.exec_())
