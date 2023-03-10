from __future__ import annotations

__all__ = (
    "ColorDisplayFormat",
    "ColorFormatPickerWidget",
)

import enum
import logging


from Qt import QtWidgets
from Qt import QtCore


logger = logging.getLogger(__name__)


class ColorDisplayFormat(enum.Enum):
    """
    List formats available to represent a color encoding.

    All are assumed to be for the RGB color model.
    """

    float = "0.0"
    tuple = "(0.0,)"
    int8 = "255"
    hexadecimal = "#hex"


class ColorFormatPickerWidget(QtWidgets.QWidget):
    """
    A row of buttons that allow to change in which format a color is displayed.

    Diagram::

        [              (btn)(btn)...]
    """

    format_changed_signal = QtCore.Signal(str)
    """
    Emit the name of the format that has been clicked by the user.
    """

    formats = ColorDisplayFormat

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        # 1. Create
        self.layout = QtWidgets.QHBoxLayout()
        self.tabbar = QtWidgets.QTabBar()
        # 2. Add
        self.setLayout(self.layout)
        self.layout.addStretch(0)
        self.layout.addWidget(self.tabbar)
        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Procedural widget configuration
        for color_format in self.formats:
            tab_index = self.tabbar.addTab(color_format.value)
            self.tabbar.setTabData(tab_index, color_format)

        # 4. Connections
        self.tabbar.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, new_index):
        """
        Callback called when the current format selected change.
        """
        current_tab_index = self.tabbar.currentIndex()
        current_format = self.tabbar.tabData(current_tab_index)
        if not current_format:
            return
        self.format_changed_signal.emit(current_format.value)
