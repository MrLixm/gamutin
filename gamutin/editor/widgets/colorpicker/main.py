__all__ = ("ColorPickerWidget",)

import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.widgets.colorpicker.compounds import (
    ColorDisplayWidget,
)

logger = logging.getLogger(__name__)


class ColorPickerWidget(QtWidgets.QWidget):
    """
    A widget aimed at selecting a single color value.
    """

    color_changed_signal = QtCore.Signal()
    display_colorspace_changed_signal = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.compound_display = ColorDisplayWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.compound_display)

        # 3. Modify
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 4. Connections
        self.compound_display.color_changed_signal.connect(self.on_color_changed)
        self.compound_display.display_colorspace_changed_signal.connect(
            self.on_display_colorspace_changed
        )
        return

    def get_color(self):
        """
        Get the color currently displayed, encoded in the workspace colorspace.
        """
        return self.compound_display.get_color()

    def get_display_color(self):
        """
        Get the color currently displayed, encoded in the selected display colorspace.
        """
        return self.compound_display.get_display_color()

    def on_color_changed(self):
        self.color_changed_signal.emit()

    def on_display_colorspace_changed(self):
        self.display_colorspace_changed_signal.emit()
