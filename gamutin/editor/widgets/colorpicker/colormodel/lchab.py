__all__ = ("ColorEditLCHabModelWidget",)

import itertools
import logging
from functools import lru_cache
from typing import Any
from typing import Generator

import numpy
from Qt import QtWidgets
from Qt import QtGui

from gamutin.core.colorspaces import sRGB_COLORSPACE
from gamutin.core.colorspaces import RgbColorspace
from gamutin.core.color import LCHabColor
from gamutin.core.color.lchabcolor import generate_hab_gradient
from gamutin.core.color.lchabcolor import generate_chroma_gradient
from gamutin.core.color.lchabcolor import generate_lightness_gradient
from gamutin.editor.widgets.colorpicker.colormodel import BaseColorEditModelWidget
from gamutin.editor.widgets.colorpicker.sliders import FloatSliderWidget

logger = logging.getLogger(__name__)


class LCHabCache:
    """
    Convenient class to generate color from LCHab value with a minimal impact on
    performances.

    The current implementation is still not enough to provide a smooth playback in
    an interface.

    Args:
        samples:
            number of point used to generate the gradient and to sample the range of
            each LCHab channel.
        colorspace:
            colorspace for the LCHab -> display color conversion
    """

    def __init__(self, samples: int, colorspace: RgbColorspace):
        self._samples = samples
        self._colorspace = colorspace
        self._cache: dict[
            tuple[float, float, float], list[tuple[float, QtGui.QColor]]
        ] = {}

        self.l_range = numpy.linspace(0, 100, samples)
        self.c_range = numpy.linspace(0, 100, samples)
        self.h_range = numpy.linspace(0, 360, samples)
        self._range_combinations = list(
            itertools.product(self.l_range, self.c_range, self.h_range)
        )
        logger.debug(
            f"[{self.__class__.__name__}][cache] "
            f"{len(self._range_combinations)} cache combinations possible"
        )

    @lru_cache(maxsize=256)
    def _get_L(self, C, Hab) -> list[tuple[float, QtGui.QColor]]:
        gradient = generate_lightness_gradient(self._samples // 2, hab=Hab, chroma=C)
        v = self.convert_gradient_lchab_to_qcolor(gradient)
        return v

    @lru_cache(maxsize=256)
    def _get_C(self, L, Hab) -> list[tuple[float, QtGui.QColor]]:
        gradient = generate_chroma_gradient(self._samples // 2, hab=Hab, lightness=L)
        return self.convert_gradient_lchab_to_qcolor(gradient)

    @lru_cache(maxsize=256)
    def _get_Hab(self, L, C) -> list[tuple[float, QtGui.QColor]]:
        gradient = generate_hab_gradient(self._samples, lightness=L, chroma=C)
        return self.convert_gradient_lchab_to_qcolor(gradient)

    def get_L(self, C, Hab) -> list[tuple[float, QtGui.QColor]]:
        # Quantization of the args to reduce lru_cache miss
        C = self.c_range[(numpy.abs(self.c_range - C)).argmin()]
        Hab = self.h_range[(numpy.abs(self.h_range - Hab)).argmin()]
        return self._get_L(C, Hab)

    def get_C(self, L, Hab) -> list[tuple[float, QtGui.QColor]]:
        # Quantization of the args to reduce lru_cache miss
        L = self.l_range[(numpy.abs(self.l_range - L)).argmin()]
        Hab = self.h_range[(numpy.abs(self.h_range - Hab)).argmin()]
        return self._get_C(L, Hab)

    def get_Hab(self, L, C) -> list[tuple[float, QtGui.QColor]]:
        # Quantization of the args to reduce lru_cache miss
        L = self.l_range[(numpy.abs(self.l_range - L)).argmin()]
        C = self.c_range[(numpy.abs(self.c_range - C)).argmin()]
        return self._get_Hab(L, C)

    def convert_gradient_lchab_to_qcolor(
        self,
        lchab_gradient: Generator[LCHabColor, Any, Any],
    ) -> list[tuple[float, QtGui.QColor]]:
        color_range = (
            QtGui.QColor(
                *lchab_hab.to_Rgba(colorspace=self._colorspace).to_int8(alpha=False)
            )
            for lchab_hab in lchab_gradient
        )
        color_range = list(color_range)
        color_range = [
            (index / (len(color_range) - 1), color)
            for index, color in enumerate(color_range)
        ]
        return color_range


class ColorEditLCHabModelWidget(BaseColorEditModelWidget):
    """
    Widget that allow to pick a color using 3 horizontal slider editing components
     of the LCHab color model.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # TODO colorspace is hardcoded to sRGB for display
        self.lchab_cache = LCHabCache(samples=80, colorspace=sRGB_COLORSPACE)
        self._updating: bool = False

        # 1. Create
        self.layout = QtWidgets.QGridLayout()
        self.label_h = QtWidgets.QLabel("H")
        self.label_c = QtWidgets.QLabel("C")
        self.label_l = QtWidgets.QLabel("L")
        self.slider_h = FloatSliderWidget()
        self.slider_c = FloatSliderWidget()
        self.slider_l = FloatSliderWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.label_h, 0, 0)
        self.layout.addWidget(self.slider_h, 0, 1)
        self.layout.addWidget(self.label_c, 1, 0)
        self.layout.addWidget(self.slider_c, 1, 1)
        self.layout.addWidget(self.label_l, 2, 0)
        self.layout.addWidget(self.slider_l, 2, 1)

        # 3. Modify
        self.layout.setContentsMargins(*(15,) * 4)
        self.slider_h.maximum = 360
        self.slider_c.maximum = 100
        self.slider_c.value = 80
        self.slider_l.maximum = 100
        self.slider_l.value = 80

        for slider in [self.slider_h, self.slider_c, self.slider_l]:
            slider.setMaximumHeight(35)
            slider.set_cursor_scale(0.85)
            slider.value_changed_signal.connect(self.on_slider_changed)

        self.label_h.setObjectName("LabelH")
        self.label_c.setObjectName("LabelC")
        self.label_l.setObjectName("LabelL")

        # 4. Connections

        self.on_slider_changed()
        return

    def set_color(self, color: LCHabColor):
        """
        Set the color visible in the interface,
        """
        self._updating = True
        self.slider_h.value = color.hue
        self.slider_c.value = color.chroma
        self.slider_l.value = color.lightness
        self._updating = False
        self.color_changed_signal.emit()
        self.update_display_gradients()

    def get_color(self) -> LCHabColor:
        """
        Get the color currently set.
        """
        return LCHabColor(
            hue=self.slider_h.value,
            chroma=self.slider_c.value,
            lightness=self.slider_l.value,
        )

    def on_slider_changed(self):
        self.color_changed_signal.emit()
        self.update_display_gradients()

    def update_display_gradients(self):
        """
        Update the colored gradient displaye din each sliders depending on the
        current LCHab values set.
        """

        if self._updating:
            return
        self._updating = True

        hab = self.slider_h.value
        chroma = self.slider_c.value
        lightness = self.slider_l.value

        color_range = self.lchab_cache.get_Hab(lightness, chroma)
        self.slider_h.set_display_color_range(color_range)

        color_range = self.lchab_cache.get_C(lightness, hab)
        self.slider_c.set_display_color_range(color_range)

        color_range = self.lchab_cache.get_L(chroma, hab)
        self.slider_l.set_display_color_range(color_range)

        self._updating = False
