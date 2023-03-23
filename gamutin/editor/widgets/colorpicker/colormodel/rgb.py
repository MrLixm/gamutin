__all__ = ("ColorEditRgbModelWidget",)

import logging

from Qt import QtWidgets

from gamutin.core.color import RGBAData
from gamutin.editor.widgets.colorpicker.colormodel import BaseColorEditModelWidget

logger = logging.getLogger(__name__)


class ColorEditRgbModelWidget(BaseColorEditModelWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()

        # 2. Add
        self.setLayout(self.layout)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 4. Connections
        return

    def set_color(self, color: RGBAData):
        pass

    def get_color(self) -> RGBAData:
        pass
