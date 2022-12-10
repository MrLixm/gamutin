import logging
from abc import abstractmethod, ABC
from pathlib import Path
from typing import Type

from gamutin.editor.resources.stylesheet import StyleSheet
from gamutin.editor.resources.themes import BaseStyleTheme
from gamutin.editor.resources.themes import BlankStyleTheme

logger = logging.getLogger(__name__)


class BaseResourceLibrary(ABC):
    """
    Collection of disk resources used in the interface for customization of the look and feel.
    """

    def __init__(self, root: Path):

        self.root = root

        self._style_active: StyleSheet = StyleSheet(content="/*empty*/")
        self._theme_active: Type[BaseStyleTheme] = BlankStyleTheme

    @abstractmethod
    def register(self):
        """
        Load the resource in the current QApplication instance.
        """
        pass

    def set_active_style(self, style: StyleSheet):
        self._style_active = style
        self.register()

    def set_active_theme(self, theme: Type[BaseStyleTheme]):
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
    def theme_active(self) -> Type[BaseStyleTheme]:
        """
        The theme currently being used.
        """
        return self._theme_active
