import enum
from abc import abstractmethod


class BaseStyleTheme(enum.Enum):
    """
    Library of variables to use in StyleSheets.

    This is an abstract class that must be subclassed.
    """

    @classmethod
    def __all__(cls):
        return [item for item in cls]

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Pretty name of the theme.

        Can be displayed in an interface.
        """
        pass


class BlankStyleTheme(BaseStyleTheme):
    @classmethod
    def get_name(cls) -> str:
        return "blank"
