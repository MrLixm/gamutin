from __future__ import annotations

__all__ = ("ColorDisplayInteractive",)


import logging
from typing import Optional

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from gamutin.editor.widgets.colorpicker.colordisplay import ColoredRectangle
from gamutin.editor.widgets.colorpicker.model import ColorExposureGrading
from gamutin.editor.widgets.colorpicker.model import RGBAData
from gamutin.editor.widgets.colorpicker.model import DEFAULT_COLOR
from gamutin.editor.widgets.colorpicker.grading import ExposureGradingInfoWidget


logger = logging.getLogger(__name__)


class ColorDisplayInteractive(ColoredRectangle):
    """
    A rectangular frame filled with a uniform constant color.

    Designed to be use a large interactive color preview. You can edit the color from
    it, which will emit the ``color_edited_signal`` Signal.
    """

    color_edited_signal = QtCore.Signal()
    """
    Emitted only when the **user** change the displayed color.
    """

    def __init__(self):
        super().__init__()
        self._rgbdata: RGBAData = DEFAULT_COLOR
        self._exposure_grading: Optional[ColorExposureGrading] = None
        self._exposure_grading_interactive: bool = False
        self._exposure_grading_edited: bool = False
        self._previous_mouse_pos: Optional[QtCore.QPoint] = None

        self.layout = QtWidgets.QVBoxLayout()
        self.layout_header = QtWidgets.QHBoxLayout()
        self.label_exposure_interactive = QtWidgets.QLabel(self)
        self.widget_exposure = ExposureGradingInfoWidget()
        self.widget_apply = QtWidgets.QPushButton("Apply")

        self.setLayout(self.layout)
        self.layout.addLayout(self.layout_header)
        self.layout.addStretch(0)
        self.layout_header.addWidget(self.widget_exposure)
        self.layout_header.addWidget(self.widget_apply)
        self.layout_header.addStretch(0)

        self.label_exposure_interactive.setObjectName("exposureLabel")
        self.widget_exposure.setObjectName("effectExposure")
        self.widget_apply.setObjectName("effectApply")

        self.widget_exposure.reset_exposure_signal.connect(self.cancel_exposure_grading)
        self.widget_apply.clicked.connect(self.apply_exposure_grading)

        self.update_interactive_exposure()
        self.update_widget_effect()

    @property
    def color(self) -> RGBAData:
        """
        Get the current color being displayed
        """
        return self._rgbdata

    @color.setter
    def color(self, color_value: RGBAData):
        """
        Set the current color being displayed.
        """
        self._set_color(color_value)
        if self.exposure_grading:
            self.exposure_grading.initial_color = color_value
            self.update_interactive_exposure()
        self.repaint()

    @property
    def exposure_grading(self) -> Optional[ColorExposureGrading]:
        """
        Get the active exposure grading effect that might be None.
        """
        return self._exposure_grading

    @exposure_grading.setter
    def exposure_grading(self, exposure_grading_value: Optional[ColorExposureGrading]):
        """
        Set or clear the active exposure grading effect
        """
        self._exposure_grading = exposure_grading_value
        if exposure_grading_value:
            self.widget_exposure.exposure = exposure_grading_value.exposure
        self.update_widget_effect()

    def _set_color(self, color_value: RGBAData):
        """
        Set the currently displayed color.
        """
        self._rgbdata = color_value
        color_int8 = color_value.to_int8(alpha=False)
        self._color = QtGui.QColor(*color_int8)
        self.setToolTip(str(color_value))
        self.repaint()

    def add_exposure(self, exposure: float):
        """
        Combine the given exposure value to the currently set one.
        """
        new_exposure = self._exposure_grading.exposure + exposure
        self.set_exposure(new_exposure)

    def apply_exposure_grading(self):
        """
        Get out of exposure edit but bake it into the active color.
        """
        if not self.exposure_grading:
            return
        self._set_color(self.exposure_grading.current_color)
        self.exposure_grading = None
        self.color_edited_signal.emit()

    def cancel_exposure_grading(self):
        """
        Remove any exposure edit and roll back to the initial color before it was started.
        """
        if self.exposure_grading:
            self._set_color(self.exposure_grading.initial_color)
            self.exposure_grading = None

    def cancel_interactive_exposure_grading(self):
        """
        Called when the user cancel the current interactive edit of the exposure.

        But we preserve eeh value that has been potentially set before.
        """
        self._previous_mouse_pos = None
        self._exposure_grading_interactive = False
        self.update_interactive_exposure()

        if self.exposure_grading:
            saved_exposure = self.exposure_grading.restore_saved_exposure()
            self.set_exposure(saved_exposure)

    def set_exposure(self, exposure: float):
        """
        Set the exposure value currently displayed in the UI.
        """
        self._exposure_grading.exposure = exposure
        self.widget_exposure.exposure = exposure
        self._exposure_grading_edited = True
        self.update_interactive_exposure()
        self._set_color(self._exposure_grading.current_color)

    def start_interactive_exposure_grading(self):
        """
        Called when the user start to edit the exposure value.
        """
        self._exposure_grading_interactive = True
        if not self.exposure_grading:
            self.exposure_grading = ColorExposureGrading(self._rgbdata)
            self._exposure_grading_edited = False

        self.exposure_grading.save_exposure()
        self.update_interactive_exposure()
        self.update_widget_effect()

    def stop_interactive_exposure_grading(self):
        """
        Called when we leave the current interactive edit of the exposure.
        """
        self._exposure_grading_interactive = False
        self._previous_mouse_pos = None
        self.update_interactive_exposure()

        if not self._exposure_grading_edited:
            self.cancel_exposure_grading()

    def update_interactive_exposure(self):
        """
        Update all the label_exposure_interactive widget using the exposure effect.
        """
        if not self._exposure_grading_interactive:
            self.label_exposure_interactive.setVisible(False)
            return

        self.label_exposure_interactive.setVisible(True)
        self.label_exposure_interactive.setText(
            f"{self._exposure_grading.exposure:+.6}"
        )

        width = self.label_exposure_interactive.sizeHint().width()
        height = self.label_exposure_interactive.sizeHint().height()

        self.label_exposure_interactive.setGeometry(
            int(self.rect().center().x() - (width / 2)),
            int(self.rect().center().y() - (height / 2)),
            width,
            height,
        )

    def update_widget_effect(self):
        """
        Update the top left widgets shwocasing the current exposure effect.
        """
        if self._exposure_grading:
            self.widget_exposure.setVisible(True)
            self.widget_apply.setVisible(True)
        else:
            self.widget_exposure.setVisible(False)
            self.widget_apply.setVisible(False)

    # Overrides

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        A key was pressed while the widget was in focus.
        """
        if event.key() == QtCore.Qt.Key_Escape:
            self.cancel_interactive_exposure_grading()
            self.clearFocus()

        return super().keyPressEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse was clicked while on the widget.

        We usually want to start the interactive exposure grading, unless the click
        event was from the exposure widget with a "reset" or an "apply" asked.
        """
        if (
            self.layout_header.geometry().contains(event.pos())
            or not event.buttons() == QtCore.Qt.LeftButton
        ):
            return super().mousePressEvent(event)

        self.setFocus()
        self.start_interactive_exposure_grading()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse started moving.
        """
        if not self._exposure_grading:
            return

        if not self._previous_mouse_pos:
            self._previous_mouse_pos = event.pos()
            return

        xpos = event.pos().x()
        ypos = event.pos().y()
        axis_horizontal = False

        if xpos != self._previous_mouse_pos.x():
            axis_horizontal = True
        # else means vertical axis

        # only support horizontal for now
        if not axis_horizontal:
            return

        amount_horizontal = xpos - self._previous_mouse_pos.x()

        exposure: float = float(amount_horizontal * 0.01)
        self.add_exposure(exposure)
        self._previous_mouse_pos = event.pos()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse click was released.
        """
        if not event.button() == QtCore.Qt.LeftButton:
            return

        self.stop_interactive_exposure_grading()
        self.clearFocus()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Widget is changing dimensiions.
        """
        super().resizeEvent(event)
        self.update_interactive_exposure()
