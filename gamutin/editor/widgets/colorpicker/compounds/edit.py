__all__ = ("ColorEditWidget",)

import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.widgets.colorpicker.model import RGBAData
from gamutin.editor.widgets.colorpicker.model import DEFAULT_COLOR
from gamutin.editor.widgets.colorpicker.model import PASSTHROUGH_COLORSPACE
from gamutin.editor.widgets.colorpicker.colormodel import ColorEditRgbModelWidget


logger = logging.getLogger(__name__)


class ColorEditWidget(QtWidgets.QWidget):
    color_changed_signal = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self._color = DEFAULT_COLOR

        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.tabwidget = QtWidgets.QTabWidget()
        self.tab_rgb = ColorEditRgbModelWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.tabwidget)
        self.tabwidget.addTab(self.tab_rgb, "RGB")

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.tabwidget.setTabPosition(self.tabwidget.South)

        # 4. Connections

        return

    def set_color(self, color: RGBAData):
        """
        Set the color being edited, encoded in the given colorspace (might be None).
        """
        self._color = color

    def get_color(self) -> RGBAData:
        """
        Get the color currently edited, encoded in the workspace colorspace.
        """
        return self._color
