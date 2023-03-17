from __future__ import annotations

__all__ = ("ExposureGradingInfoWidget",)

import logging

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from gamutin import editor
from gamutin.editor.widgets.icons import BaseDisplayIcon


logger = logging.getLogger(__name__)


class ExposureGradingInfoWidget(QtWidgets.QFrame):
    """
    A horizontal widget to display an exposure value,with an option to be reset.

    You use the ``exposure`` property to change the display exposure. And then call
    :meth:`update_exposure` to refresh the UI.
    """

    icon_path = editor.cfg.resources.get_icon("sun.svg")
    reset_exposure_signal = QtCore.Signal()
    """
    Signal emitted when the user ask to reset the exposure to default.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self._exposure: float = 0.0

        # 1. Create
        self.layout = QtWidgets.QHBoxLayout()
        self.icon = BaseDisplayIcon()
        self.label = QtWidgets.QLabel()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.icon)
        self.layout.addWidget(self.label)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.icon.icon = QtGui.QIcon(str(self.icon_path))
        self.icon.enable_scaling_on_active(True, 0.1)
        self.icon.setToolTip("Reset Exposure")
        self.icon.setFixedSize(15, 15)

        # 4. Connections
        self.icon.clicked_signal.connect(self.on_exposure_reset)

        self.update_exposure()
        return

    @property
    def exposure(self):
        return self._exposure

    @exposure.setter
    def exposure(self, exposure_value):
        self._exposure = exposure_value
        self.update_exposure()

    def on_exposure_reset(self, mouse_button: QtCore.Qt.MouseButtons):
        """
        Callback when the user ask to reset the exposure.
        """
        if mouse_button != QtCore.Qt.LeftButton:
            return
        self.reset_exposure_signal.emit()
        logger.debug(f"[{self.__class__.__name__}][on_exposure_reset] emitted.")

    def update_exposure(self):
        """
        Update the interface according to the exposure value.
        """
        self.label.setText(f"{self._exposure:+.2f}")
