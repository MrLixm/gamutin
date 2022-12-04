from pathlib import Path


class ResourceLibrary:
    def __init__(self, root: Path):
        self.root = root
        self.root_icon = self.root / "icons"

        self.icon_main = self.root_icon / "icon.ico"

    def register(self):
        pass
