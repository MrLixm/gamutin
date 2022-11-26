__all__ = ("ResourcesManager",)

import json
import logging
import os
from pathlib import Path

from Qt import QtWidgets
from Qt import QtGui

from pgcheck.core.exceptions import raisePathExists


logger = logging.getLogger(__name__)


class ResourcesManager:
    def __init__(self, root: Path):

        self.root = root
        """
        Path to the resources/ dir that contains all the resources such as icon, fonts, ...
        """

        self.icons = Icons(self)
        self.fonts = Fonts(self)

    def __repr__(self) -> str:
        return json.dumps(self.__asdict__(), indent=4, default=str)

    def __asdict__(self) -> dict:
        d = self.__dict__.copy()
        for k, v in d.items():
            if hasattr(v, "__asdict__"):
                d[k] = v.__asdict__()
        return d

    def register(self):
        """
        Make all the resources availble in the application by laoding them to Qt.

        A QApplciation instance have to ba available.
        """
        logger.debug(f"[{self.__class__.__name__}][register] Started.")
        assert (
            QtWidgets.QApplication.instance()
        ), "Called register() but no QApplication existing yet."

        self.fonts.register()
        return

    def validate(self):
        """
        Raise an error is some of this instance, its attribute or anything else have
        an issue.
        """
        raisePathExists(self.root)
        self.icons.validate()
        self.fonts.validate()


class Icons:
    def __init__(self, parent: ResourcesManager):
        root = parent.root / "icons"
        self.main = root / "icon.ico"

    def __asdict__(self) -> dict:
        return self.__dict__.copy()

    def validate(self):
        """
        Raise an error is some of this instance, its attribute or anything else have
        an issue.
        """
        raisePathExists(self.main)


class Fonts:
    def __init__(self, parent: ResourcesManager):
        root = parent.root / "fonts"
        self.roboto = BaseFontFamily(directory=root / "Roboto")

    def __asdict__(self) -> dict:
        d = self.__dict__.copy()
        for k, v in d.items():
            if hasattr(v, "__asdict__"):
                d[k] = v.__asdict__()
        return d

    def register(self):
        """
        Load the fonts in the current application.
        """
        self.roboto.register()
        return

    def listAvailable(self) -> dict[str, list[int]]:
        out = dict()
        for fontfamilyname, fontfamily in vars(
            self
        ).items():  # type: str, BaseFontFamily
            out[fontfamily.name] = fontfamily.listAvailable()
        return out

    def validate(self):
        """
        Raise an error is some of this instance, its attribute or anything else have
        an issue.
        """
        # raisePathExists(self.main)


class BaseFont:
    """
    Represents a single font file path.
    """

    def __init__(self, path: Path):
        self.path: Path = path
        # not yet loaded in the app
        self.identifier: int = None

    def register(self):
        """
        Load the fonts in the current application.
        """
        self.identifier = QtGui.QFontDatabase.addApplicationFont(str(self.path))
        logger.debug(f"[Fonts][register] {self.identifier: >3}={self.path.name}")
        return


class BaseFontFamily:
    def __init__(self, directory: Path) -> None:
        self.directory: Path = directory
        self.name: str = directory.stem
        self.fonts: list[BaseFont] = list()

    def __asdict__(self) -> dict:
        return {"directory": self.directory, "fonts": [f.path.name for f in self.fonts]}

    def listAvailable(self) -> list[int]:
        return [basefont.identifier for basefont in self.fonts]

    def register(self):
        """
        Load the fonts in the current application.
        """
        logger.debug(
            f"[BaseFontFamily][register] Started registering <{self.directory}>"
        )

        for font_file_name in os.listdir(self.directory):  # type: str

            font_path = self.directory / font_file_name
            if font_path.suffix not in [".ttf", ".otf"]:
                continue

            font = BaseFont(font_path)
            font.register()
            self.fonts.append(font)
            continue

        return
