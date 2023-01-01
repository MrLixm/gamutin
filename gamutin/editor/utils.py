__all__ = (
    "copy_to_clipboard",
    "block_signals",
)

import logging
from contextlib import contextmanager

from Qt import QtWidgets
from Qt import QtCore

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
