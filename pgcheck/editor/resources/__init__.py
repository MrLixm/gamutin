from pathlib import Path

from .colors import ColorLibrary
from .stylesheet import ColorQtProperty
from .stylesheet import LengthQtProperty
from .stylesheet import StyleSheet
from .stylesheet import StyleTheme


class DefaultStyleTheme(StyleTheme):
    """
    Library of variables to use in StyleSheet.
    """

    @classmethod
    def get_name(cls) -> str:
        return "default"

    color_text_base = ColorQtProperty((250, 250, 250, 255))
    color_error_red = ColorQtProperty((187, 76, 76, 255))
    size_border_radius_base = LengthQtProperty(5)


class ResourceLibrary:
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

        self.colors = ColorLibrary

        self.theme_main = DefaultStyleTheme
        self.style_test = StyleSheet.from_path(self.root_styles / "test.qss")

    def register(self):

        self.style_test.resolve(self.theme_main)
        self.style_test.validate()
