__all__ = ("BaseColorEditModelWidget",)

import abc
import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.widgets.colorpicker.model import RGBAData

logger = logging.getLogger(__name__)


class BaseColorEditModelWidget(QtWidgets.QWidget):
    color_changed_signal = QtCore.Signal()

    @abc.abstractmethod
    def set_color(self, color: RGBAData):
        """
        Set the color being edited, encoded in the given colorspace (might be None).
        """
        pass

    @abc.abstractmethod
    def get_color(self) -> RGBAData:
        """
        Get the color currently edited, encoded in the workspace colorspace.
        """
        pass
