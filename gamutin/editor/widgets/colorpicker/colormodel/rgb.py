__all__ = ("ColorEditRgbModelWidget",)

import logging

from Qt import QtWidgets
from Qt import QtGui

from gamutin.core.color import RGBAData
from gamutin.editor.widgets.colorpicker.colormodel import BaseColorEditModelWidget
from gamutin.editor.widgets.colorpicker.sliders import FloatSliderWidget
from gamutin.editor.widgets.colorspaceselector import ColorspaceSelector

logger = logging.getLogger(__name__)


class ColorEditRgbModelWidget(BaseColorEditModelWidget):
    """
    Widget that allow to pick a color using 3 horizontal slider.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # 1. Create
        self.layout = QtWidgets.QGridLayout()
        self.label_r = QtWidgets.QLabel("R")
        self.label_g = QtWidgets.QLabel("G")
        self.label_b = QtWidgets.QLabel("B")
        self.slider_r = FloatSliderWidget()
        self.slider_g = FloatSliderWidget()
        self.slider_b = FloatSliderWidget()
        self.colorspace_selector = ColorspaceSelector()
        self.checkbox_colorspace = QtWidgets.QCheckBox()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.label_r, 0, 0)
        self.layout.addWidget(self.slider_r, 0, 1)
        self.layout.addWidget(self.label_g, 1, 0)
        self.layout.addWidget(self.slider_g, 1, 1)
        self.layout.addWidget(self.label_b, 2, 0)
        self.layout.addWidget(self.slider_b, 2, 1)
        self.layout.addWidget(self.checkbox_colorspace, 3, 0)
        self.layout.addWidget(self.colorspace_selector, 3, 1, 1, -1)

        # 3. Modify
        self.layout.setContentsMargins(*(15,) * 4)
        self.slider_r.set_display_color_range(
            [
                (0, QtGui.QColor(0, 0, 0)),
                (1, QtGui.QColor(255, 0, 0)),
            ]
        )
        self.slider_g.set_display_color_range(
            [
                (0, QtGui.QColor(0, 0, 0)),
                (1, QtGui.QColor(0, 255, 0)),
            ]
        )
        self.slider_b.set_display_color_range(
            [
                (0, QtGui.QColor(0, 0, 0)),
                (1, QtGui.QColor(0, 0, 255)),
            ]
        )

        for slider in [self.slider_r, self.slider_g, self.slider_b]:
            slider.setMaximumHeight(35)
            slider.set_cursor_scale(0.85)
            slider.allow_out_of_range(True)
            slider.value_changed_signal.connect(self.color_changed_signal.emit)

        self.colorspace_selector.setObjectName("ColorspaceSelector")
        self.label_r.setObjectName("LabelR")
        self.label_g.setObjectName("LabelG")
        self.label_b.setObjectName("LabelB")
        self.checkbox_colorspace.setToolTip("Disable to not specify any colorspace.")

        # 4. Connections
        self.checkbox_colorspace.stateChanged.connect(self.on_checkbox_changed)
        self.colorspace_selector.colorspace_changed_signal.connect(
            self.on_colorspace_changed
        )

        self.on_checkbox_changed()
        return

    def set_color(self, color: RGBAData):
        """
        Set teh color visible in the interface,
        """
        self.slider_r.value = color.r
        self.slider_g.value = color.g
        self.slider_b.value = color.b
        self.color_changed_signal.emit()

    def get_color(self) -> RGBAData:
        """
        Get the color currently set.
        """
        return RGBAData(
            self.slider_r.value,
            self.slider_g.value,
            self.slider_b.value,
            colorspace=self.get_colorspace(),
        )

    def get_colorspace(self):
        """
        Get the current colorspace in which the RGB value are supposed to be expressed.
        """
        if self.checkbox_colorspace.isChecked():
            return self.colorspace_selector.get_current_colorspace()
        return None

    def on_colorspace_changed(self, new_colorspace):
        logger.debug(
            f"[{self.__class__.__name__}][on_colorspace_changed] {new_colorspace=}"
        )
        self.color_changed_signal.emit()

    def on_checkbox_changed(self):
        is_checked = self.checkbox_colorspace.isChecked()
        logger.debug(
            f"[{self.__class__.__name__}][on_colorspace_changed] {is_checked=}"
        )
        self.colorspace_selector.setEnabled(is_checked)
        self.color_changed_signal.emit()
