__all__ = ("FloatSliderWidget", "FloatValueSlider")

import logging

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.core.mathing import remap
from gamutin.editor.utils import color_interpolate

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


class FloatValueSlider(QtWidgets.QFrame):
    """
    A slider that allow you to select a float value on the given color range.

    The slider is assumed to work in the 0.0-1.0 range, and it's up to the developer
    to convert this range to the actual range he needs for its use.
    """

    value_changed_signal = QtCore.Signal()
    """
    Emitted when the user change the current value via the interface.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self._current_value = 0.0
        self._color_range: list[tuple[int, QtGui.QColor]] = [
            (0, QtGui.QColor.fromRgbF(0.0, 0.0, 0.0)),
            (1, QtGui.QColor.fromRgbF(1.0, 1.0, 1.0)),
        ]
        self._user_stylesheet: str = ""
        self._value_editing_active: bool = False
        # left, top, right, bottom
        self.slider_margins = (-20, -15, -20, -15)
        self.cursor_widget = ColorCursorWidget(self)
        self.cursor_widget.setObjectName("FloatValueSliderPosition")

        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)

        self.current_value = 0.0

    @property
    def _gradient_qss(self) -> str:
        """
        Convert _color_range to a qss gradient property.
        """
        gradient = "qlineargradient( x1:0 y1:0, x2:1 y2:0, "
        for position, color in self._color_range:
            gradient += f"stop:{position} rgba{color.toTuple()} "
        gradient += ")"
        return gradient

    @property
    def _gradient(self) -> QtGui.QLinearGradient:
        """
        Convert _color_range to a QLinearGradient instance.
        """
        gradient = QtGui.QLinearGradient()
        for position, color in self._color_range:
            gradient.setColorAt(position, color)
        return gradient

    @property
    def current_value(self) -> float:
        """
        Current value the slider is set to.

        Strict [0.0-1.0] range.
        """
        return self._current_value

    @current_value.setter
    def current_value(self, value: float):
        """
        Args:
            value: value to set the slider to. Strict [0.0-1.0] range.
        """
        self._current_value = value
        self.cursor_widget.color = self.current_color

    @property
    def current_color(self) -> QtGui.QColor:
        """
        The color from the color_range corresponding to the current value.
        """
        gradient = self._gradient
        stops = gradient.stops()
        color = QtGui.QColor(0, 0, 0)

        for stop_index in range(len(stops) - 1):
            current_stop = stops[stop_index]
            next_stop = stops[stop_index + 1]

            if self.current_value <= next_stop[0]:
                ratio = remap(
                    self.current_value, current_stop[0], next_stop[0], 0.0, 1.0
                )
                color = color_interpolate(current_stop[1], next_stop[1], ratio)
                break

        return color

    @property
    def internal_stylesheet(self) -> str:
        return f"QFrame{{background-color: {self._gradient_qss};}}"

    @property
    def slider_rect(self) -> QtCore.QRect:
        """
        Actual area to paint the horizontal slider on (smaller than the whole widget rect)
        """
        margins = QtCore.QMargins(
            int(self.slider_margins[0] - (self.cursor_widget.width() / 2)),
            self.slider_margins[1],
            int(self.slider_margins[2] - (self.cursor_widget.width() / 2)),
            self.slider_margins[3],
        )
        return self.rect().marginsAdded(margins)

    @property
    def cursor_pos(self) -> QtCore.QPointF:
        """
        Center position of the cursor relative to the widget rect.
        """
        xpos = self.current_value * self.slider_rect.width()
        # convert from slider space, to widget space
        xpos = remap(
            xpos,
            self.rect().left(),
            self.slider_rect.right(),
            self.slider_rect.left(),
            self.rect().right(),
        )
        return QtCore.QPointF(xpos, self.rect().center().y())

    def set_display_color_range(self, color_range: list[tuple[int, QtGui.QColor]]):
        """
        Set the whole range of color the slider need to display starting from left and
        ending at the right.
        """
        self._color_range = color_range
        self.update_stylesheet()
        self.cursor_widget.color = self.current_color

    def start_value_editing(self):
        """
        Allow the mouse to change the current value.
        """
        self._value_editing_active = True

    def stop_value_editing(self):
        """
        Block the mouse to change the current value.
        """
        self._value_editing_active = False

    def update_cursor_widget(self):
        """
        Update the position and the size of the cursor widget for the current state.
        """
        current_rect = self.rect()
        new_rect = QtCore.QRectF(current_rect)
        new_rect.setWidth(self.height())
        new_rect.moveCenter(self.cursor_pos)
        self.cursor_widget.setGeometry(new_rect.toRect())

    def update_stylesheet(self):
        """
        Set the stylesheet again so the widget is properly displayed.
        """
        stylesheet = self._user_stylesheet + "\n" + self.internal_stylesheet
        super().setStyleSheet(stylesheet)

    def _set_current_value_from_mouse_event(self, event: QtGui.QMouseEvent):
        """
        Set the currently displaying value depending on the position of the mouseEvent

        Args:
            event: a mouse event
        """
        # convert from widget space, to slider space
        normalised_x_pos = remap(
            event.localPos().x(),
            self.slider_rect.left(),
            self.rect().right(),
            self.rect().left(),
            self.slider_rect.right(),
        )
        normalised_x_pos = normalised_x_pos / self.slider_rect.width()
        # current value can never go outside 0-1 range
        normalised_x_pos = max(min(normalised_x_pos, 1.0), 0.0)
        self.current_value = normalised_x_pos
        self.value_changed_signal.emit()

    # Overrides

    def setStyleSheet(self, stylesheet: str):
        self._user_stylesheet = stylesheet
        self.update_stylesheet()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qstylepainter = QtWidgets.QStylePainter(self)
        qstylepainter.setRenderHint(qstylepainter.Antialiasing, True)

        qstyleoption = QtWidgets.QStyleOption()
        qstyleoption.initFrom(self)
        qstyleoption.rect = self.slider_rect

        qstylepainter.drawPrimitive(QtWidgets.QStyle.PE_Widget, qstyleoption)

        self.update_cursor_widget()
        self.update_stylesheet()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        A key was pressed while the widget was in focus.
        """
        if event.key() == QtCore.Qt.Key_Escape:
            self.stop_value_editing()
            self.clearFocus()

        return super().keyPressEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse was clicked while on the widget.

        We usually want to start the interactive exposure grading, unless the click
        event was from the exposure widget with a "reset" or an "apply" asked.
        """
        if not event.buttons() == QtCore.Qt.LeftButton:
            return super().mousePressEvent(event)

        self.setFocus()
        self.start_value_editing()
        self._set_current_value_from_mouse_event(event=event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse started moving.
        """
        if not self._value_editing_active:
            return

        self._set_current_value_from_mouse_event(event=event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse click was released.
        """
        if not event.button() == QtCore.Qt.LeftButton:
            return

        self.stop_value_editing()
        self.clearFocus()


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
