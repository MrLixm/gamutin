__all__ = (
    "ColorCursorWidget",
    "ColorCursorWidgetShape",
)

import enum
import logging

from Qt import QtWidgets
from Qt import QtGui

logger = logging.getLogger(__name__)


class ColorCursorWidgetShape(enum.Enum):
    """
    Style of the shape the cursor can take.
    """

    round = 0
    rectangular = 1


class ColorCursorWidget(QtWidgets.QFrame):
    """
    Used with FloatGradientSlider as cursor for the currently selected value.

    This is a simple QFrame supporting styleSheets. You can choose to make it round
    or rectangular with the ``style`` attribute. Default is round.

    The only exception is that you can't use the ``background-color`` and potentially
    ``border-radius`` (if shape == round) as those are set internally.
    """

    shapes = ColorCursorWidgetShape

    def __init__(
        self,
        shape: ColorCursorWidgetShape = None,
        parent: QtWidgets.QWidget = None,
    ):
        super().__init__(parent)
        self._user_stylesheet: str = ""
        self._color = QtGui.QColor(0, 0, 0)
        self.shape = shape or self.shapes.round
        """
        Design of the cursor.
        """

        self.update_stylesheet()

    @property
    def color(self) -> QtGui.QColor:
        return self._color

    @color.setter
    def color(self, color_value: QtGui.QColor):
        self._color = color_value
        self.update_stylesheet()

    @property
    def _internal_stylesheet(self) -> str:
        stylesheet = "QFrame{"
        stylesheet += f"background-color: rgba{str(self.color.toTuple())};"
        if self.shape == self.shapes.round:
            stylesheet += (
                f"border-radius: {min(self.width(), self.height()) / 2 - 1}px;"
            )
        stylesheet += "}"
        return stylesheet

    def update_stylesheet(self):
        stylesheet = self._user_stylesheet + "\n" + self._internal_stylesheet
        super().setStyleSheet(stylesheet)

    # Overrides

    def setStyleSheet(self, stylesheet: str):
        self._user_stylesheet = stylesheet
        self.update_stylesheet()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        super().resizeEvent(event)
        self.update_stylesheet()
