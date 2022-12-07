import enum
from abc import abstractmethod


class StyleTheme(enum.Enum):
    """
    Library of variables to use in StyleSheet.
    """

    @classmethod
    def __all__(cls):
        return [item for item in cls]

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        pass
