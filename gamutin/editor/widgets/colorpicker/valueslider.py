__all__ = ("FloatValueDisplaySlider", "FloatValueSlider")

import logging

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

logger = logging.getLogger(__name__)


class ColorCursorWidget(QtWidgets.QFrame):
    """
    Used with FloatValueSlider as cursor for the currently selected value.

    This is a simple rounded QFrame supporting styleSheets. The only exception is that
    you can't use the ``background-color`` and ``border-radius`` as those are set
    internally.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self._user_stylesheet: str = ""
        self._color = QtGui.QColor(0, 80, 0)

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


class FloatValueSlider(QtWidgets.QFrame):
    """
    A slider that allow you to select a float value on the given color range.

    The slider is assumed to work in the 0.0-1.0 range, and it's up to the developer
    to convert this range to the actual range he needs for its use.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self._current_value = 0.0
        self._color_range: [(int, [int])] = [
            (0, [0, 0, 0]),
            (1, [255, 255, 255]),
        ]
        self._user_stylesheet = ""
        # left, top, right, bottom
        self.slider_margins = (-20, -15, -20, -15)
        self.cursor_widget = ColorCursorWidget(self)
        self.cursor_widget.setObjectName("FloatValueSliderPosition")

        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)

    @property
    def _gradient_qss(self) -> str:
        """
        Convert _color_range to a qss gradient property.
        """
        gradient = "qlineargradient( x1:0 y1:0, x2:1 y2:0, "
        for position, color in self._color_range:
            gradient += f"stop:{position} rgb({str(color)[1:][:-1]}) "
        gradient += ")"
        return gradient

    @property
    def current_value(self) -> float:
        return self._current_value

    @current_value.setter
    def current_value(self, current_value_value):
        self._current_value = current_value_value

    @property
    def internal_stylesheet(self) -> str:
        return f"QFrame{{background-color: {self._gradient_qss};}}"

    def set_display_color_range(self, color_range: [(int, [int])]):
        """
        Set the whole range of color the slider need to display starting from left and
        ending at the right.
        """
        self._color_range = color_range
        self.update_stylesheet()

    def update_cursor_widget(self):
        """
        Update the position and the size of the cursor widget for the current state.
        """
        current_rect = self.rect()
        position_rect = current_rect.adjusted(
            self.width() * 0.3,
            0,
            -self.width() * 0.3,
            0,
        )
        self.cursor_widget.setGeometry(position_rect)

    def update_stylesheet(self):
        """
        Set the stylesheet again so the widget is properly displayed.
        """
        stylesheet = self._user_stylesheet + "\n" + self.internal_stylesheet
        super().setStyleSheet(stylesheet)

    # Overrides

    def setStyleSheet(self, stylesheet: str):
        self._user_stylesheet = stylesheet
        self.update_stylesheet()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qstylepainter = QtWidgets.QStylePainter(self)
        qstylepainter.setRenderHint(qstylepainter.Antialiasing, True)

        qstyleoption = QtWidgets.QStyleOption()
        qstyleoption.initFrom(self)

        smaller_rect = self.rect().marginsAdded(QtCore.QMargins(*self.slider_margins))
        qstyleoption.rect = smaller_rect

        qstylepainter.drawPrimitive(QtWidgets.QStyle.PE_Widget, qstyleoption)

        self.update_cursor_widget()
        self.update_stylesheet()


class FloatValueDisplaySlider(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()

        # 2. Add
        self.setLayout(self.layout)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 4. Connections

        self.ui_bake()
        return

    def ui_bake(self):
        """
        Update the state of the interface.
        """
        pass
