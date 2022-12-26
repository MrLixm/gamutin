__all__ = ("copy_to_clipboard",)

import logging

from Qt import QtWidgets

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
