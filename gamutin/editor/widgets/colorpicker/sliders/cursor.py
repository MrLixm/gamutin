__all__ = ("ColorCursorWidget",)

import logging

from Qt import QtWidgets
from Qt import QtGui

logger = logging.getLogger(__name__)


class ColorCursorWidget(QtWidgets.QFrame):
    """
    Used with FloatGradientSlider as cursor for the currently selected value.

    This is a simple rounded QFrame supporting styleSheets. The only exception is that
    you can't use the ``background-color`` and ``border-radius`` as those are set
    internally.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self._user_stylesheet: str = ""
        self._color = QtGui.QColor(0, 0, 0)

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
        return f"""
        QFrame{{
            background-color: rgba{str(self.color.toTuple())};
            /* set the widget to a circle as much as possible */
            border-radius: {min(self.width(), self.height()) / 2 - 1}px;
        }}
        """

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
