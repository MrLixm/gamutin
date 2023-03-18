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
        self._exposure_grading_active: bool = False
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
        self.update_exposure()
        self.cancel_exposure_grading()

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
            self.update_exposure()
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
        self.widget_exposure.exposure = exposure_grading_value.exposure

    def apply_exposure_grading(self):
        """
        Get out of exposure edit but bake it into the active color.
        """
        if self._exposure_grading:
            self._set_color(self._exposure_grading.current_color)
            self._exposure_grading = None

        self.widget_exposure.setVisible(False)
        self.widget_apply.setVisible(False)
        self.color_edited_signal.emit()

    def start_exposure_grading(self):
        """
        Called when the user start to edit the exposure value.
        """
        if not self._exposure_grading:
            self._exposure_grading = ColorExposureGrading(self._rgbdata)

        self._exposure_grading.save_exposure()
        self.widget_exposure.exposure = self._exposure_grading.exposure
        self.widget_exposure.setVisible(True)
        self.widget_apply.setVisible(True)

    def set_exposure(self, exposure: float):
        """
        Set the exposure value currently displayed in the UI.
        """
        new_exposure = self._exposure_grading.exposure + exposure
        self._exposure_grading.exposure = new_exposure
        self.widget_exposure.exposure = new_exposure
        self.update_exposure()
        self.repaint()

    def restore_exposure_grading(self):
        """
        Called when the user cancel the current interactive edit of the exposure but
        we stay with an active exposure edit.
        """
        if self._exposure_grading:
            self._exposure_grading.restore_saved_exposure()

        self.widget_exposure.update_exposure()

    def cancel_exposure_grading(self):
        """
        Remove any exposure edit and roll back to the initial color before it was started.
        """
        if self._exposure_grading:
            self._set_color(self._exposure_grading.initial_color)
            self._exposure_grading = None

        self.widget_exposure.setVisible(False)
        self.widget_apply.setVisible(False)

    def update_exposure(self):
        """
        Update all the interface elelemt susing the exposure effect.
        """
        if not self._exposure_grading_active:
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

    def _set_color(self, color_value: RGBAData):
        """
        Set the currently displayed color.
        """
        self._rgbdata = color_value
        color_int8 = color_value.to_int8(alpha=False)
        self._color = QtGui.QColor(*color_int8)
        self.setToolTip(str(color_value))

    def paintEvent(self, event: QtGui.QPaintEvent):
        """
        Request to repaint all or part of a widget.
        """
        if not self._exposure_grading:
            return super().paintEvent(event)

        self._set_color(self._exposure_grading.current_color)
        super().paintEvent(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        A key was pressed while the widget was in focus.
        """
        if event.key() == QtCore.Qt.Key_Escape:
            self._exposure_grading_active = False
            self._previous_mouse_pos = None
            self.restore_exposure_grading()
            self.update_exposure()
            self.repaint()

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

        self._exposure_grading_active = True
        self.setFocus()
        self.start_exposure_grading()

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
        self.set_exposure(exposure)
        self._previous_mouse_pos = event.pos()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Mouse click was released.
        """
        if not event.button() == QtCore.Qt.LeftButton:
            return

        self._exposure_grading_active = False
        self._previous_mouse_pos = None
        self.clearFocus()
        self.update_exposure()
        self.repaint()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Widget is changing dimensiions.
        """
        super().resizeEvent(event)
        self.update_exposure()
