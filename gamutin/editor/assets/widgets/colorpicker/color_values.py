from __future__ import annotations

__all__ = (
    "ColorValueLineEdit",
    "ColorFormatPickerWidget",
)

import enum
import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import DEFAULT_COLOR
from gamutin.editor.assets.widgets.colorpicker.validators import BaseColorValidator
from gamutin.editor.assets.widgets.colorpicker.validators import ColorFloatValidator
from gamutin.editor.assets.widgets.colorpicker.validators import ColorInt8Validator
from gamutin.editor.assets.widgets.colorpicker.validators import ColorHexValidator
from gamutin.editor.assets.widgets.colorpicker.validators import (
    ColorFloatTupleValidator,
)

logger = logging.getLogger(__name__)


class ColorDisplayFormat(enum.Enum):
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


class ColorValueLineEdit(QtWidgets.QLineEdit):
    """
    A color tuple as a single row of values that can be displayed under different formats.

    The color is always stored in the same floating point format which allow that simply
     switching between formats doesn't change values. But from the moment the user
     press enter the stored values are boudn to the current format displayed.
    """

    formats = ColorDisplayFormat
    color_changed_signal = QtCore.Signal()

    def __init__(self, currentFormat: ColorDisplayFormat = None):
        super().__init__()

        self._format = currentFormat or ColorDisplayFormat.float
        self.color = DEFAULT_COLOR

        self.setToolTip(
            "When you start editing values, until you press Enter or leave the widget, "
            "the value will NOT be considered edited."
        )
        self.setAlignment(QtCore.Qt.AlignRight)

        self.returnPressed.connect(self.update_values)
        self.editingFinished.connect(self.update_values)

        self.on_format_changed()

    @property
    def format(self):
        """
        Retrieve in which format the color is displayed.
        """
        return self._format

    @format.setter
    def format(self, format_value: ColorDisplayFormat):
        """
        Change the format in which the color is displayed.
        """
        if self._format == format_value:
            return

        self._format = format_value
        self.on_format_changed()

    def update_values(self):
        """
        Sanitize the user input by using the fix method of the current validator.
        """
        previous_color = self.color
        new_text = self.validator().fix(self.text())
        new_color = self.validator().to_color(new_text)
        self.setText(new_text)
        self.color = new_color
        self.color_changed_signal.emit()
        logger.debug(
            f"[{self.__class__.__name__}][update_values] "
            f"from {previous_color} to {new_color}"
        )
        return

    def on_format_changed(self):
        """
        Update the state of the interface.
        """

        if self._format == self.formats.float:
            self.setValidator(ColorFloatValidator())

        elif self._format == self.formats.tuple:
            self.setValidator(ColorFloatTupleValidator())

        elif self._format == self.formats.int8:
            self.setValidator(ColorInt8Validator())

        elif self._format == self.formats.hexadecimal:
            self.setValidator(ColorHexValidator())

        else:
            raise ValueError(f"Unsupported format {self._format}")

        # the color stored doesn't change, only the displayed one
        new_text = self.validator().from_color(self.color)
        self.setText(new_text)
        return

    def get_color(self) -> RGBAData:
        return self.color

    def validator(self) -> BaseColorValidator:
        # override for typehints
        return super().validator()
