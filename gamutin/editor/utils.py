__all__ = (
    "copy_to_clipboard",
    "color_interpolate",
    "block_signals",
)

import logging
from contextlib import contextmanager

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

logger = logging.getLogger(__name__)


def copy_to_clipboard(text: str):
    """
    Copy the given text to the application clipboard.

    This will clear the previous clipboard.
    """

    clipboard = QtWidgets.QApplication.clipboard()
    clipboard.clear(mode=clipboard.Clipboard)
    clipboard.setText(text, mode=clipboard.Clipboard)
    return


@contextmanager
def block_signals(qtobject: QtCore.QObject):
    """
    Context/decorator to block any Qt signals emission on the given object.

    Args:
        qtobject: object to block the signal from
    """

    qtobject.blockSignals(True)

    try:
        yield
    finally:
        qtobject.blockSignals(False)


def color_interpolate(color_start: QtGui.QColor, color_end: QtGui.QColor, ratio: float):
    """
    Return the interpolated color between start and end for the given ratio.

    All of this because QGradient does not have a ``colorAt(pos)`` method ...

    Args:
        color_start: any color
        color_end: any color
        ratio: strict 0-1 range

    Returns:
        QColor instance
    """
    r = (1 - ratio) * color_start.redF() + ratio * color_end.redF()
    g = (1 - ratio) * color_start.greenF() + ratio * color_end.greenF()
    b = (1 - ratio) * color_start.blueF() + ratio * color_end.blueF()
    return QtGui.QColor.fromRgbF(r, g, b)
