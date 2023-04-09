__all__ = ("FloatGradientSlider",)

import logging

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.core.mathing import remap
from gamutin.editor.utils import color_interpolate

from gamutin.editor.widgets.colorpicker.sliders.cursor import ColorCursorWidget

logger = logging.getLogger(__name__)


class FloatGradientSlider(QtWidgets.QFrame):
    """
    A slider that allow you to select a float value on the given color range.

    The slider is assumed to work in the 0.0-1.0 range, and it's up to the developer
    to convert this range to the actual range he needs for its use. Though it's possible
    that the value internally stored is outside of this range but would then not be
    properly displayed by the slider.

    Styling
    =======

    The widget can be fully styled with stylesheet except for the style of the cursor
    that will stay a circle.

    You can use :

    - ``qproperty-cursor_scale`` float
    - ``qproperty-cursor_circle`` int : 1 for cicle, 0 for rectangular
    - ``QFrame#FloatGradientSliderCursor``

    You can't use :

    - ``background-color``
    - ``QFrame#FloatGradientSliderCursor{border-radius}``
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
        self._cursor_scale = 1.1
        self.cursor_widget = ColorCursorWidget(parent=self)
        self.cursor_widget.setObjectName("FloatGradientSliderCursor")

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

        [0.0-1.0] range but might be outside.
        """
        return self._current_value

    @current_value.setter
    def current_value(self, value: float):
        """
        Args:
            value: value to set the slider to. [0.0-1.0] range but might be outside.
        """
        self._current_value = value
        self.cursor_widget.color = self.current_color
        self.setToolTip(str(value))

    @property
    def current_color(self) -> QtGui.QColor:
        """
        The color from the color_range corresponding to the current value.
        """
        gradient = self._gradient
        stops = gradient.stops()
        color = QtGui.QColor(0, 0, 0)
        current_value = min(max(self.current_value, 0.0), 1.0)

        for stop_index in range(len(stops) - 1):
            current_stop = stops[stop_index]
            next_stop = stops[stop_index + 1]

            ratio = remap(current_value, current_stop[0], next_stop[0], 0.0, 1.0)
            color = color_interpolate(current_stop[1], next_stop[1], ratio)

            if current_value <= next_stop[0]:
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
        margin = self.cursor_widget.height() - self.cursor_widget.height() * max(
            self._cursor_scale, 1.0
        )
        # left, top, right, bottom
        margins = QtCore.QMargins(
            int(margin - (self.cursor_widget.width() / 2)),
            int(margin),
            int(margin - (self.cursor_widget.width() / 2)),
            int(margin),
        )
        # print(f"slider_rect:: {self.rect()=} >> {self.rect().marginsAdded(margins)}")
        return self.rect().marginsAdded(margins)

    @property
    def cursor_pos(self) -> QtCore.QPointF:
        """
        Center position of the cursor relative to the widget rect.
        """
        xpos = min(max(self.current_value, 0.0), 1.0) * self.slider_rect.width()
        # convert from slider space, to widget space
        xpos = remap(
            xpos,
            self.rect().left(),
            self.slider_rect.right(),
            self.slider_rect.left(),
            self.rect().right(),
        )
        return QtCore.QPointF(xpos, self.rect().center().y())

    def get_cursor_scale(self) -> float:
        """
        Get the scale of the cursor relative to the available height.
        """
        return self._cursor_scale

    def set_cursor_scale(self, scale: float):
        """
        Set the scale of the cursor relative to the available height.

        Values above one make the cursor bigger than the slider.

        Args:
            scale: where 1 == full height, > 1 = smaller cursor than slider, ...
        """
        self._cursor_scale = scale

    cursor_scale = QtCore.Property(float, get_cursor_scale, set_cursor_scale)

    def set_cursor_circle(self, is_circle: bool):
        """
        Set the shape of the cursor to a circle or to rectangle (still editable via stylesheets).

        Args:
            is_circle: True to have the cursor as a circle.
        """
        if is_circle:
            self.cursor_widget.shape = self.cursor_widget.shapes.round
        else:
            self.cursor_widget.shape = self.cursor_widget.shapes.rectangular
        self.cursor_widget.update_stylesheet()

    cursor_circle = QtCore.Property(int, fset=set_cursor_circle)

    def set_display_color_range(self, color_range: list[tuple[int, QtGui.QColor]]):
        """
        Set the whole range of color the slider need to display starting from left and
        ending at the right.

        Args:
            color_range: list[tuple(position, color)], where position goes from 0.0 to 1.0
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
        new_rect = QtCore.QRect(current_rect)
        new_rect.setWidth(self.height())
        if self._cursor_scale < 1.0:
            new_rect.setSize(new_rect.size() * self._cursor_scale)

        # offset initial cursor position based on the current width
        # this is to support resizing of the cursor via stylesheets
        cursor_pos = self.cursor_pos
        current_width = self.cursor_widget.width()
        diff_width = (new_rect.width() / 2) - (current_width / 2)
        new_x_pos = cursor_pos.x() + diff_width
        cursor_pos.setX(new_x_pos)

        new_rect.moveCenter(cursor_pos.toPoint())
        self.cursor_widget.setGeometry(new_rect)

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