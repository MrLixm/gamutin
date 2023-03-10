from __future__ import annotations

__all__ = ("ColorThumbnailWidget",)

import logging

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore


from gamutin.editor.assets.widgets.colorpicker.main import ColorPickerWidget
from gamutin.editor.assets.widgets.colorpicker.color_preview import (
    ColorPreviewLightFrame,
)
from gamutin.editor.assets.widgets.colorpicker.color_values import ColorValueLineEdit


logger = logging.getLogger(__name__)


class ColorThumbnailWidget(QtWidgets.QWidget):
    """
    Widget that represent the currently selected color in a simplified way.

    When clicking on it, you can open the color picker to edit the color.

    A rounded rectangular frame filled with a uniform constant color.
    """

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QHBoxLayout()
        self.color_picker = ColorPickerWidget()
        self.color_preview = ColorPreviewLightFrame()
        self.color_values = ColorValueLineEdit()

        self.setLayout(self.layout)
        self.layout.addWidget(self.color_preview)
        self.layout.addWidget(self.color_values)
        self.layout.addStretch(0)

        self.color_preview.setObjectName("colorPreview")
        self.color_preview.border_radius = 4
        self.color_preview.hover_scale = 1.2
        self.color_preview.setMinimumSize(50, 15)
        self.color_preview.mousePressEvent = self.onMousePressEventColorPicker
        self.color_preview.setSizePolicy(
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Minimum,
        )

        self.color_values.setObjectName("colorPreviewValues")
        self.color_values.setReadOnly(True)
        self.color_values.setAlignment(QtCore.Qt.AlignLeft)
        self.color_values.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )

        self.color_picker.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.color_picker.color_changed_signal.connect(self.on_color_changed)
        self.color_picker.display_colorspace_changed_signal.connect(
            self.on_color_changed
        )

    def onMousePressEventColorPicker(self, event: QtGui.QMouseEvent):
        self.color_picker.show()

    def on_color_changed(self):
        display_color = self.color_picker.get_display_color()
        self.color_preview.color = display_color
        color = self.color_picker.get_color()
        self.color_values.color = color