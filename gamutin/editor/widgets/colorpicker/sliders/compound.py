__all__ = ("FloatSliderWidget",)

import logging

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui


from gamutin.editor.widgets.colorpicker.sliders.gradientslider import (
    FloatGradientSlider,
)
from gamutin.core.mathing import remap
from gamutin.editor.utils import block_signals

logger = logging.getLogger(__name__)


class FloatSliderWidget(QtWidgets.QWidget):
    """
    Widget to select a single float value.

    Made of a combo box displaying the current value and a horizontal slider.

    Styling
    =======

    - The value field is a QDoubleSpinBox than can be retrieved via the name ``FloatValueField``
    - The slider is a QFrame that can be retrieved via the name ``FloatGradientSlider``
    """

    value_changed_signal = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self._minimum: float = 0.0
        self._maximum: float = 1.0
        self._value: float = 0.0
        self._out_of_range_allowed: bool = False
        self._is_updating: bool = False

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
        self.field_value.setMinimumWidth(65)
        self.field_value.setDecimals(4)
        self.slider.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            self.slider.sizePolicy().verticalPolicy(),
        )
        self.field_value.setSingleStep(0.01)
        self.slider.setObjectName("FloatGradientSlider")
        self.field_value.setObjectName("FloatValueField")

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
        self.scaled_value = self.slider.current_value
        self.updated_field()
        self.value_changed_signal.emit()

    def on_value_field_changed(self):
        self.value = self.field_value.value()
        self.update_slider()
        self.value_changed_signal.emit()

    def set_cursor_circle(self, is_circle: bool):
        """
        Set the shape of the cursor to a circle or to rectangle (still editable via stylesheets).

        Args:
            is_circle: True to have the cursor as a circle.
        """
        self.slider.set_cursor_circle(is_circle)

    def set_cursor_scale(self, scale: float):
        """
        Set the scale of the cursor relative to the available height.

        Values above one make the cursor bigger than the slider.

        Args:
            scale: where 1 == full height, > 1 = smaller cursor than slider, ...
        """
        self.slider.set_cursor_scale(scale)

    def set_display_color_range(self, color_range: list[tuple[float, QtGui.QColor]]):
        """
        Set the whole range of color the slider need to display starting from left and
        ending at the right.

        Args:
            color_range: list[tuple(position, color)], where position goes from 0.0 to 1.0
        """
        self.slider.set_display_color_range(color_range=color_range)

    def set_step(self, step: float):
        """
        Change how much value is incremented when asked.

        Args:
            step: usually much smaller than the minumun-maximum range
        """
        if not self._out_of_range_allowed:
            step = min(max(step, self.minimum), self.maximum)
        self.field_value.setSingleStep(step)

    def update_slider(self):
        """
        Update data displayed in the slider.
        """
        if self._is_updating:
            return

        self._is_updating = True

        slider_value = self._value
        slider_value = remap(slider_value, self.minimum, self.maximum, 0.0, 1.0)
        self.slider.current_value = slider_value

        self._is_updating = False

    def updated_field(self):
        """
        Update data displayed in the value field.
        """
        if self._is_updating:
            return

        self._is_updating = True

        field_value = self._value
        self.field_value.setValue(field_value)

        self._is_updating = False
