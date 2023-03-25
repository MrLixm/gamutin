__all__ = ("FloatSliderWidget",)

import logging

from Qt import QtWidgets


from gamutin.editor.widgets.colorpicker.sliders.gradientslider import (
    FloatGradientSlider,
)

logger = logging.getLogger(__name__)


class FloatSliderWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # 1. Create
        self.layout = QtWidgets.QHBoxLayout()
        self.slider = FloatGradientSlider()
        self.field_value = QtWidgets.QDoubleSpinBox()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.field_value)
        self.layout.addWidget(self.slider)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.field_value.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )

        # 4. Connections
        self.slider.value_changed_signal.connect(self.on_value_slider_changed)

        return

    def on_value_slider_changed(self):
        value = self.slider.current_value
        self.field_value.setValue(value)
