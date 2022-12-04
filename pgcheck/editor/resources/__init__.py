from pathlib import Path

from .colors import Colors


class ResourceLibrary:
    def __init__(self, root: Path):
        self.root = root
        self.root_icon = self.root / "icons"

        self.icon_main = self.root_icon / "icon.ico"

        self.icon_file_check_outline = self.root_icon / "file-check-outline.svg"
        self.icon_file_multiple_outline = self.root_icon / "file-multiple-outline.svg"
        self.icon_file_outline = self.root_icon / "file-outline.svg"
        self.icon_folder = self.root_icon / "folder.svg"
        self.icon_folder_check = self.root_icon / "folder-check.svg"
        self.icon_information = self.root_icon / "information.svg"
        self.icon_alert_outline = self.root_icon / "alert-circle-outline.svg"

        self.colors = Colors

    def register(self):
        pass
