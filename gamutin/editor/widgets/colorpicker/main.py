__all__ = ("ColorPickerWidget",)

import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.widgets.colorpicker.compounds import ColorDisplayWidget
from gamutin.editor.widgets.colorpicker.compounds import ColorEditWidget

logger = logging.getLogger(__name__)


class ColorPickerWidget(QtWidgets.QWidget):
    """
    A widget aimed at selecting a single color value.
    """

    color_changed_signal = QtCore.Signal()
    display_colorspace_changed_signal = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self._updating: bool = False
        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.compound_display = ColorDisplayWidget()
        self.compound_edit = ColorEditWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.compound_display)
        self.layout.addWidget(self.compound_edit)

        # 3. Modify
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.compound_display.setObjectName("CompoundDisplay")
        self.compound_edit.setObjectName("CompoundEdit")

        # 4. Connections
        signal = self.compound_display.color_changed_signal
        signal.connect(self.on_display_color_changed)

        signal = self.compound_display.display_colorspace_changed_signal
        signal.connect(self.on_display_colorspace_changed)

        signal = self.compound_edit.color_changed_signal
        signal.connect(self.on_edited_color_changed)
        return

    def get_color(self):
        """
        Get the color currently displayed, encoded in the workspace colorspace.
        """
        return self.compound_display.get_color()

    def get_display_color(self):
        """
        Get the color currently displayed, encoded in the selected display colorspace.
        """
        return self.compound_display.get_display_color()

    def on_display_color_changed(self):
        if self._updating:
            return

        self._updating = True
        new_color = self.compound_display.get_color()
        self.compound_edit.set_color(new_color)
        self.color_changed_signal.emit()
        self._updating = False

    def on_display_colorspace_changed(self):
        self.display_colorspace_changed_signal.emit()

    def on_edited_color_changed(self):
        if self._updating:
            return

        self._updating = True
        new_color = self.compound_edit.get_color()
        new_color = new_color.as_colorspace(
            self.compound_display.get_workspace_colorspace()
        )
        self.compound_display.set_color(new_color)
        self.color_changed_signal.emit()
        self._updating = False
