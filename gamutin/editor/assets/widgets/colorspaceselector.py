__all__ = ("ColorspaceSelector",)

import logging

from Qt import QtCore
from Qt import QtWidgets

import gamutin.core.colorspaces

logger = logging.getLogger(__name__)


class ColorspaceSelector(QtWidgets.QWidget):
    """
    A widget to select a colorspace using a QComboBox

    It's possibel to override its default transfer functions using a QCheckBox.
    """

    def __init__(self, parent=None):
        # type: (QtWidgets.QWidget) -> None
        super().__init__(parent)
        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QHBoxLayout()
        self.combobox_colorspace = QtWidgets.QComboBox()
        self.checkbox_force_linear_target = QtWidgets.QCheckBox(
            "Force Linear Transfer-Function"
        )

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.combobox_colorspace)
        self.layout.addWidget(self.checkbox_force_linear_target)

        # 3. Modify
        self.layout.setContentsMargins(*(0,) * 4)
        # 4. Connections
        return

    def bakeUI(self):

        self.combobox_colorspace.clear()

        for colorspace in gamutin.core.colorspaces.get_available_colorspaces():

            self.combobox_colorspace.addItem(colorspace.name, colorspace)
            self.combobox_colorspace.model().sort(0, QtCore.Qt.AscendingOrder)

    def set_force_linear_visible(self, visible: bool):
        """
        Args:
            visible: True to set visible, False to hide.
        """
        self.checkbox_force_linear_target.setVisible(visible)

    def set_force_linear_enable(self, enable: bool):
        """
        Args:
            enable: True to set enable, False to disable.
        """
        self.checkbox_force_linear_target.setChecked(enable)

    def get_current_colorspace(self) -> gamutin.core.colorspaces.RgbColorspace:
        """
        Return the colorspace currently selected in the interface.
        As a linear variant if asked as such.
        """
        colorspace_name = self.combobox_colorspace.currentText()
        force_linear = self.checkbox_force_linear_target.isChecked()
        if force_linear:
            colorspace_name = f"{colorspace_name}:linear"

        colorspace = gamutin.core.colorspaces.get_colorspace(colorspace_name)
        if not colorspace:
            raise ValueError(
                f"Cannot retrieve RgbColorspace from widget with value "
                f"{colorspace_name} and {force_linear=}"
            )
        return colorspace
