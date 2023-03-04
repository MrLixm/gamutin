from __future__ import annotations

__all__ = ("ColorDisplayAdvancedWidget",)

import enum
import logging
from functools import partial

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.assets.widgets.colorspaceselector import ColorspaceSelector
from gamutin.editor.assets.widgets.colorpicker.datatypes import ColorFloat
from gamutin.editor.assets.widgets.colorpicker.datatypes import ColorFloatTuple
from gamutin.editor.assets.widgets.colorpicker.validators import ColorFloatValidator
from gamutin.editor.assets.widgets.colorpicker.validators import (
    ColorFloatTupleValidator,
)


logger = logging.getLogger(__name__)


class ColorDisplayFormat(enum.Enum):
    float = "0.0"
    tuple = "(0.0,)"
    integer = "255"
    hexadecimal = "#hex"


class ColorDisplayFormatPickerWidget(QtWidgets.QWidget):
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
    """

    formats = ColorDisplayFormat

    def __init__(self, currentFormat: ColorDisplayFormat = None):
        super().__init__()
        self._format = currentFormat or ColorDisplayFormat.float
        self.returnPressed.connect(self.apply_validator_fix)
        self.ui_bake()

    def ui_bake(self):
        """
        Update the state of the interface.
        """
        # TODO handle value conversions between formats
        if self._format == self.formats.float:
            self.setValidator(ColorFloatValidator())

        elif self._format == self.formats.tuple:
            self.setValidator(ColorFloatTupleValidator())

        else:
            raise ValueError(f"Unsupported format {self._format}")

        if not self.text():
            self.apply_validator_fix()

        return

    def apply_validator_fix(self):
        """
        Sanitize the user input by using the fix method of the current validator.
        """
        new_color: ColorFloat = self.validator().fix(self.text())
        self.setText(str(new_color))
        return

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
        self.ui_bake()


class ColorDisplayAdvancedWidget(QtWidgets.QWidget):
    """
    A widget aiming at displaying a color with its value under different represenations.

    The widget is not read-only, it's actually possible to edit the color from it.

    Diagram::

        _________________________________
        [           display colorspace ▽]
        ---------------------------------
                  *color preview*
        _________________________________
        (colorspace)      0.00 0.00 0.00
        ---------------------------------
                    [btn][btn][btn][btn]

    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.colorspace_display_widget = ColorspaceSelector()
        self.color_preview_frame = QtWidgets.QFrame()
        self.color_lineedit = ColorValueLineEdit()
        self.color_format_picker = ColorDisplayFormatPickerWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.colorspace_display_widget)
        self.layout.addWidget(self.color_preview_frame)
        self.layout.addWidget(self.color_lineedit)
        self.layout.addWidget(self.color_format_picker)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.color_preview_frame.setMinimumHeight(15)
        self.colorspace_display_widget.set_label_visible(False)
        # TODO see if re-enable needed
        self.colorspace_display_widget.set_force_linear_visible(False)
        # 4. Connections
        self.color_format_picker.format_changed_signal.connect(
            self.on_color_format_changed
        )

        self.ui_bake()
        return

    def ui_bake(self):
        pass

    def set_color(self, color):
        pass

    def get_color(self, color):
        pass

    def on_color_format_changed(self, format_value: str):
        """
        Callback called when the user ask to display the color in another format.
        """
        color_format = self.color_format_picker.formats(format_value)
        self.color_lineedit.format = color_format
        logger.debug(
            f"[{self.__class__.__name__}][on_color_format_changed] changed to {color_format}"
        )


def _test_interface():
    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)

    widget = ColorDisplayAdvancedWidget()
    layout.addWidget(widget)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
