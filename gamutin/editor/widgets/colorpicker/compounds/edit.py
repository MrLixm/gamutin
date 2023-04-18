__all__ = ("ColorEditWidget",)

import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.core.color import LCHabColor
from gamutin.editor.widgets.colorpicker.model import RGBAData
from gamutin.editor.widgets.colorpicker.model import DEFAULT_COLOR
from gamutin.editor.widgets.colorpicker.model import PASSTHROUGH_COLORSPACE
from gamutin.editor.widgets.colorpicker.colormodel import ColorEditRgbModelWidget
from gamutin.editor.widgets.colorpicker.colormodel import ColorEditLCHabModelWidget


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
        self.tab_lchab = ColorEditLCHabModelWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.tabwidget)
        self.tabwidget.addTab(self.tab_rgb, "RGB")
        self.tabwidget.addTab(self.tab_lchab, "HCL")

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.tabwidget.setTabPosition(self.tabwidget.South)
        self.tab_rgb.setObjectName("ColorEditRgbModelWidget")

        # 4. Connections
        self.tab_rgb.color_changed_signal.connect(self.on_tab_rgb_changed)
        return

    def set_color(self, color: RGBAData):
        """
        Set the color being edited, encoded in the given colorspace (might be None).
        """
        self._color = color
        self.tab_rgb.set_color(color)
        self.tab_lchab.set_color(LCHabColor.from_Rgba(color))
        self.color_changed_signal.emit()

    def get_color(self) -> RGBAData:
        """
        Get the color currently edited, encoded in the workspace colorspace.
        """
        return self._color

    def on_tab_rgb_changed(self):
        self._color = self.tab_rgb.get_color()
        self.color_changed_signal.emit()

    def on_tab_lchab_changed(self):
        lchab_color = self.tab_lchab.get_color()
        lchab_color.to_Rgba()
        self.color_changed_signal.emit()
