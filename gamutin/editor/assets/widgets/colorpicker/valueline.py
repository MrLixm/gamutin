from __future__ import annotations

__all__ = ("ColorValueLineEdit",)

import logging
from functools import partial

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

from gamutin.editor.utils import copy_to_clipboard
from gamutin.editor.assets.widgets.colorpicker.colorformat import ColorDisplayFormat
from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import DEFAULT_COLOR
from gamutin.editor.assets.widgets.colorpicker.colorformat import BaseColorValidator
from gamutin.editor.assets.widgets.colorpicker.colorformat import VALIDATOR_BY_FORMAT

logger = logging.getLogger(__name__)


class ColorValueLineEdit(QtWidgets.QLineEdit):
    """
    A color tuple as a single row of values that can be displayed under different formats.

    The color is always stored in the same floating point format which allow that simply
     switching between formats doesn't change values. But from the moment the user
     press enter the stored values are boudn to the current format displayed.

    Colorspace information is totally discarded and data is always manipulated "as it is".
    """

    formats = ColorDisplayFormat
    color_changed_signal = QtCore.Signal()

    def __init__(self, currentFormat: ColorDisplayFormat = None):
        super().__init__()

        self._format = currentFormat or ColorDisplayFormat.float
        self._color = DEFAULT_COLOR
        self._validator_by_format = {
            color_format: validator()
            for color_format, validator in VALIDATOR_BY_FORMAT.items()
        }

        self.setToolTip(
            "When you start editing values, until you press Enter or leave the widget, "
            "the value will NOT be considered edited."
        )
        self.setAlignment(QtCore.Qt.AlignRight)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.returnPressed.connect(self.update_values)
        self.editingFinished.connect(self.update_values)
        self.customContextMenuRequested[QtCore.QPoint].connect(
            self.on_context_menu_requested
        )

        self.on_format_changed()

    @property
    def color(self) -> RGBAData:
        """
        Currently stored and displayed color.

        With no colorspace encoding.
        """
        return self._color

    @color.setter
    def color(self, color_value: RGBAData):
        raw_color = color_value.as_colorspace(target_colorspace=None)
        self._color = raw_color
        new_text = self.validator().from_color(self.color)
        self.setText(new_text)
        self.color_changed_signal.emit()

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

        validator = self._validator_by_format.get(self._format)
        if not validator:
            raise ValueError(f"Unsupported format {self._format}")

        self.setValidator(validator)

        # the color stored doesn't change, only the displayed one
        new_text = self.validator().from_color(self.color)
        self.setText(new_text)
        return

    def on_context_menu_requested(self, pointer: QtCore.QPoint):
        """
        Extend the defautl context menu with additional actions, and display it.
        """
        menu = self.createStandardContextMenu()
        menu.addSeparator()

        for color_format in self.formats:
            validator = self._validator_by_format.get(color_format)
            if not validator:
                continue

            formatted_color = validator.from_color(self._color)

            action = QtWidgets.QAction(
                f"Copy to Clipboard as {color_format.value}", self
            )
            action.triggered.connect(partial(copy_to_clipboard, formatted_color))
            menu.addAction(action)

        menu.exec_(QtGui.QCursor.pos())
        return

    def get_color(self) -> RGBAData:
        """
        Get the current color. Does the same as getting the ``color`` attribute.
        """
        return self.color

    def set_color(self, color: RGBAData):
        """
        Set the current color. Does the same as setting the ``color`` attribute.
        """
        self.color = color

    def validator(self) -> BaseColorValidator:
        # override for typehints
        return super().validator()
