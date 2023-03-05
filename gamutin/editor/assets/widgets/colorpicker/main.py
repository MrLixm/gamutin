__all__ = ("ColorPickerWidget",)

import logging

from Qt import QtWidgets

from gamutin.editor.assets.widgets.colorpicker.compound_display import (
    ColorDisplayWidget,
)

logger = logging.getLogger(__name__)


class ColorPickerWidget(QtWidgets.QWidget):
    """
    A widget aimed at selecting a single color value.
    """

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

        return
