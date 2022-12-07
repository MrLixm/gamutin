import enum

from Qt import QtGui


class ColorLibrary(enum.Enum):

    error_red = QtGui.QColor(187, 76, 76)

    @classmethod
    def __all__(cls):
        return [item for item in cls]
