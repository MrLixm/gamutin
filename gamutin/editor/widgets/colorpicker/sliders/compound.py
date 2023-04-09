__all__ = ("FloatSliderWidget",)

import logging

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui


from gamutin.editor.widgets.colorpicker.sliders.gradientslider import (
    FloatGradientSlider,
)
from gamutin.core.mathing import remap

logger = logging.getLogger(__name__)


class FloatSliderWidget(QtWidgets.QWidget):
    """
    Widget to select a single float value.

    Made of a combo box displaying the current value and a horizontal slider.
    """

    value_changed_signal = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self._minimum: float = 0.0
        self._maximum: float = 1.0
        self._value: float = 0.0
        self._out_of_range_allowed: bool = False

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
        self.field_value.setSingleStep(0.01)

        # 4. Connections
        self.slider.value_changed_signal.connect(self.on_value_slider_changed)
        self.field_value.valueChanged.connect(self.on_value_field_changed)

        self.updated_field()
        self.update_slider()
        return

    @property
    def minimum(self) -> float:
        return self._minimum

    @minimum.setter
    def minimum(self, minimum_value: float):
        self._minimum = minimum_value
        if not self._out_of_range_allowed:
            self.field_value.setMinimum(minimum_value)
        self.updated_field()
        self.update_slider()

    @property
    def maximum(self) -> float:
        return self._maximum

    @maximum.setter
    def maximum(self, maximum_value: float):
        self._maximum = maximum_value
        if not self._out_of_range_allowed:
            self.field_value.setMaximum(maximum_value)
        self.updated_field()
        self.update_slider()

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, new_value: float):
        """
        Args:
            new_value: value already in the [min-max] range set on the widget.
        """
        if not self._out_of_range_allowed:
            new_value = min(max(new_value, self.minimum), self.maximum)

        self._value = new_value
        self.updated_field()
        self.update_slider()

    @property
    def scaled_value(self):
        """
        Value but remapped in the [0-1] range.
        """
        return remap(self.value, self.minimum, self.maximum, 0.0, 1.0)

    @scaled_value.setter
    def scaled_value(self, new_value):
        """
        Remap the given [0-1] value to the internal [min-max] range.

        Args:
            new_value: value in the [0-1] range
        """
        self.value = remap(new_value, 0.0, 1.0, self.minimum, self.maximum)

    def allow_out_of_range(self, allowed: bool):
        """
        If True allows the user to enter values outside the [min-max] range specified.
        """
        self._out_of_range_allowed = allowed
        self.field_value.setMinimum(float("-inf"))
        self.field_value.setMaximum(float("inf"))

    def on_value_slider_changed(self):
        self._value = self.slider.current_value
        self.updated_field()
        self.value_changed_signal.emit()

    def on_value_field_changed(self):
        self._value = self.field_value.value()
        self.update_slider()
        self.value_changed_signal.emit()

    def set_display_color_range(self, color_range: list[tuple[int, QtGui.QColor]]):
        """
        Set the whole range of color the slider need to display starting from left and
        ending at the right.

        Args:
            color_range: list[tuple(position, color)], where position goes from 0.0 to 1.0
        """
        self.slider.set_display_color_range(color_range=color_range)

    def update_slider(self):
        """
        Update data displayed in the slider.
        """
        slider_value = self._value
        if not self._out_of_range_allowed:
            slider_value = remap(slider_value, self.minimum, self.maximum, 0.0, 1.0)
        self.slider.current_value = slider_value

    def updated_field(self):
        """
        Update data displayed in the value field.
        """
        field_value = self._value
        if not self._out_of_range_allowed:
            field_value = remap(field_value, 0.0, 1.0, self.minimum, self.maximum)

        self.field_value.setValue(field_value)
