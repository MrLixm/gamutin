from pathlib import Path
from typing import Type

from Qt import QtWidgets

from gamutin.editor.resources.stylesheet import StyleSheet
from gamutin.editor.resources.stylesheet import StyleTheme
from gamutin.editor.resources.themes import BlankStyleTheme
from gamutin.editor.resources.themes import DefaultStyleTheme


class ResourceLibrary:
    """
    Collection of disk resources used in the interface for custumization of the look and feel.
    """

    def __init__(self, root: Path):

        self.root = root

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
        self._style_active.apply_to(qapp)

    def set_active_style(self, style: StyleSheet):
        self._style_active = style
        self.register()

    def set_active_theme(self, theme: Type[StyleTheme]):
        self._theme_active = theme
        self.register()

    @property
    def style_active(self) -> StyleSheet:
        """
        The Qt StyleSheet currently being used.

        (might actually not be the real stylesheet set on the QApplication instance !)
        """
        return self._style_active

    @property
    def theme_active(self) -> Type[DefaultStyleTheme]:
        """
        The theme currently being used.
        """
        return self._theme_active
