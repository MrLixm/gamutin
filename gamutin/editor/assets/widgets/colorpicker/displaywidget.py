from __future__ import annotations

__all__ = ("ColorDisplayAdvancedWidget",)

import enum
import logging
from functools import partial

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.editor.assets.widgets.colorspaceselector import ColorspaceSelector
from gamutin.editor.assets.widgets.colorpicker.datamodel import RGBAData
from gamutin.editor.assets.widgets.colorpicker.datamodel import DEFAULT_COLOR
from gamutin.editor.assets.widgets.colorpicker.datamodel import sRGB_LINEAR_COLORSPACE
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


class ColorPreviewFrame(QtWidgets.QFrame):
    """
    A frame filled with a uniform constant color.
    """

    def __init__(self):
        super().__init__()
        self._color = DEFAULT_COLOR
        self.color = DEFAULT_COLOR

    @property
    def color(self) -> RGBAData:
        return self._color

    @color.setter
    def color(self, color_value: RGBAData):
        self._color = color_value
        self.setToolTip(str(color_value))
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qpainter = QtGui.QPainter()
        qpainter.setRenderHint(qpainter.Antialiasing)
        qpainter.begin(self)
        qpainter.fillRect(self.rect(), self._get_qcolor())
        qpainter.end()

    def _get_qcolor(self) -> QtGui.QColor:
        # TODO to8bit convert to sRGB auto, remove it !
        color_int8 = self.color.to_int8(alpha=False)
        return QtGui.QColor(*color_int8)


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
        self.layout_bottom = QtWidgets.QVBoxLayout()
        self.widget_bottom = QtWidgets.QWidget()

        self.selector_colorspace_display = ColorspaceSelector()
        self.frame_preview_color = ColorPreviewFrame()
        self.lineedit_color = ColorValueLineEdit()
        self.widget_format_pickers = ColorDisplayFormatPickerWidget()
        self.splitter_preview = QtWidgets.QSplitter()

        # 2. Add
        self.setLayout(self.layout)
        self.widget_bottom.setLayout(self.layout_bottom)
        self.layout.addWidget(self.selector_colorspace_display)
        self.layout.addWidget(self.splitter_preview)
        self.splitter_preview.addWidget(self.frame_preview_color)
        self.splitter_preview.addWidget(self.widget_bottom)
        self.layout_bottom.addWidget(self.lineedit_color)
        self.layout_bottom.addWidget(self.widget_format_pickers)
        self.layout_bottom.addStretch(0)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout_bottom.setContentsMargins(0, 0, 0, 0)
        self.splitter_preview.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_preview.setChildrenCollapsible(False)
        self.splitter_preview.setHandleWidth(15)
        self.frame_preview_color.setMinimumHeight(15)
        self.selector_colorspace_display.set_label_visible(False)
        self.selector_colorspace_display.align_text_right(25)
        # TODO see if re-enable needed
        self.selector_colorspace_display.set_force_linear_visible(False)
        # 4. Connections
        self.widget_format_pickers.format_changed_signal.connect(
            self.on_color_format_changed
        )
        self.lineedit_color.color_changed_signal.connect(self.on_lineedit_color_changed)
        self.selector_colorspace_display.colorspace_changed_signal.connect(
            self.on_display_colorspace_changed
        )
        self.ui_bake()
        return

    def ui_bake(self):
        pass

    def set_color(self, color: RGBAData):
        pass

    def get_color(self) -> RGBAData:
        current_color = self.lineedit_color.color
        workspace_colorspace = sRGB_LINEAR_COLORSPACE
        current_color = current_color.as_colorspace(workspace_colorspace)
        return current_color

    def on_color_format_changed(self, format_value: str):
        """
        Callback called when the user ask to display the color in another format.
        """
        color_format = self.widget_format_pickers.formats(format_value)
        self.lineedit_color.format = color_format
        logger.debug(
            f"[{self.__class__.__name__}][on_color_format_changed] changed to {color_format}"
        )

    def on_lineedit_color_changed(self):
        """
        Callback when the lineedit widget change value.
        """
        new_color = self.get_color()
        display_colorspace = self.selector_colorspace_display.get_current_colorspace()

        new_color = new_color.as_colorspace(display_colorspace)
        self.frame_preview_color.color = new_color

        logger.debug(
            f"[{self.__class__.__name__}][on_lineedit_color_changed]newcolor={new_color}"
        )
        return

    def on_display_colorspace_changed(self):
        """
        Callback when the display colorspace change.
        """
        current_color = self.get_color()
        display_colorspace = self.selector_colorspace_display.get_current_colorspace()

        new_color = current_color.as_colorspace(display_colorspace)
        self.frame_preview_color.color = new_color

        logger.debug(
            f"[{self.__class__.__name__}][on_display_colorspace_changed]newcolor={new_color}"
        )
        return
