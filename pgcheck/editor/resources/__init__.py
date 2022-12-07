from pathlib import Path

from .colors import ColorLibrary
from .stylesheet import StyleSheet
from .stylesheet import StyleTheme


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

        self.theme_main = StyleTheme()
        self.style_test = StyleSheet.from_path(self.root_styles / "test.qss")

    def register(self):

        self.style_test.resolve(self.theme_main)
        self.style_test.validate()
