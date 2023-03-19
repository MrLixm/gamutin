from __future__ import annotations

__all__ = ("ColorExposureGrading",)


import logging
from typing import Optional

from gamutin.core.color import RGBAData


logger = logging.getLogger(__name__)


class ColorExposureGrading:
    """
    Grading filter to manipulate a single color exposure.

    The filter is non-destructive.
    The initial data is retrieved via ``initial_color`` attribute.
    The result of the filter is retrieved via ``current_color`` attribute
    """

    def __init__(self, initial_color: RGBAData):
        self._initial_color = initial_color
        self._initial_array = initial_color.to_array(alpha=False)
        self._exposure_saved: Optional[float] = None
        self.exposure: float = 0.0

    @property
    def initial_color(self) -> RGBAData:
        return self._initial_color

    @initial_color.setter
    def initial_color(self, initial_color_value: RGBAData):
        self._initial_color = initial_color_value
        self._initial_array = initial_color_value.to_array(alpha=False)

    @property
    def current_color(self) -> RGBAData:
        """
        The color with the exposure transform applied.
        """
        new_color = self._initial_array * (2**self.exposure)
        new_color = RGBAData.from_array(
            new_color,
            colorspace=self.initial_color.colorspace,
            alpha=self.initial_color.alpha,
        )
        return new_color

    def save_exposure(self):
        """
        Save the current exposure, so you can restore it later.
        """
        self._exposure_saved = self.exposure

    def restore_saved_exposure(self) -> float:
        """
        Restore the exposure value saved previously.
        """
        if self._exposure_saved is not None:
            self.exposure = self._exposure_saved
        return self._exposure_saved
