from __future__ import annotations

__all__ = ("ColorDisplayAdvancedWidget",)

import enum
import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.assets.widgets.colorspaceselector import ColorspaceSelector
from gamutin.editor.assets.widgets.colorpicker.color_preview import ColorPreviewFrame
from gamutin.editor.assets.widgets.colorpicker.color_values import ColorValueLineEdit
from gamutin.editor.assets.widgets.colorpicker.color_values import (
    ColorFormatPickerWidget,
)
from gamutin.editor.assets.widgets.colorpicker.model import RGBAData
from gamutin.editor.assets.widgets.colorpicker.model import sRGB_LINEAR_COLORSPACE


logger = logging.getLogger(__name__)


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
        self.widget_format_pickers = ColorFormatPickerWidget()
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
