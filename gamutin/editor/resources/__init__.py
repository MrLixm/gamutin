import logging
from pathlib import Path
from typing import Type

from Qt import QtWidgets

from gamutin.editor.resources.stylesheet import StyleSheet
from gamutin.editor.resources.themes import BaseStyleTheme
from gamutin.editor.resources.themes import BlankStyleTheme
from gamutin.editor.resources.themes import DefaultStyleTheme
from gamutin.editor.resources.libraries import BaseResourceLibrary

logger = logging.getLogger(__name__)


class ResourceLibrary(BaseResourceLibrary):
    """
    Collection of disk resources used in the interface for custumization of the look and feel.
    """

    def __init__(self, root: Path):
        super().__init__(root)

        self.root_icon = self.root / "icons"
        self.root_styles = self.root / "styles"

        self.icon_main = self.root_icon / "icon.ico"
        self.icon_file_check_outline = self.root_icon / "file-check-outline.svg"
        self.icon_file_multiple_outline = self.root_icon / "file-multiple-outline.svg"
        self.icon_file_outline = self.root_icon / "file-outline.svg"
        self.icon_folder = self.root_icon / "folder.svg"
        self.icon_folder_check = self.root_icon / "folder-check.svg"
        self.icon_information = self.root_icon / "information.svg"
        self.icon_alert_outline = self.root_icon / "alert-circle-outline.svg"

        self._style_active: StyleSheet = StyleSheet(content="/*empty*/")
        self._theme_active: Type[DefaultStyleTheme] = DefaultStyleTheme

        self.theme_default = DefaultStyleTheme
        self.style_test = StyleSheet.from_path(self.root_styles / "test.qss")

    def register(self):
        """
        Load the resource in the current QApplication instance.
        """

        qapp = QtWidgets.QApplication.instance()
        if not qapp:
            raise RuntimeError("No QApplication instance yet !")

        self._style_active.resolve(self._theme_active)
        self._style_active.validate()
        logger.debug(
            f"[{self.__class__.__name__}][register] Setting stylesheet {self._style_active.content}"
        )
        self._style_active.apply_to(qapp)

        logger.debug(f"[{self.__class__.__name__}][register] Finished on {qapp}")
