__all__ = ("ColorspaceSelector",)

import logging
from functools import partial

from Qt import QtCore
from Qt import QtWidgets

import gamutin.core.colorspaces
from gamutin.editor.assets.widgets import PushButtonAligned

logger = logging.getLogger(__name__)


class ColorspaceSelector(QtWidgets.QWidget):
    """
    A widget to select a colorspace using a QComboBox

    It's possibel to override its default transfer functions using a QCheckBox.
    """

    colorspace_changed_signal = QtCore.Signal(object)
    """
    Emitted when the colorspace selected in the interface change.
    Emit a :class:`gamutin.core.colorspaces.RgbColorspace` instance.
    """

    def __init__(self, parent=None):
        # type: (QtWidgets.QWidget) -> None
        super().__init__(parent)

        self._current_colorspace: gamutin.core.colorspaces.RgbColorspace = (
            gamutin.core.colorspaces.get_colorspace("sRGB")
        )

        # 1. Create
        self.layout = QtWidgets.QHBoxLayout()
        self.label_legend = QtWidgets.QLabel("ColorSpace")
        self.button_colorspace = PushButtonAligned()
        self.menu_colorspace = QtWidgets.QMenu()
        self.checkbox_force_linear_target = QtWidgets.QCheckBox(
            "Force Linear Transfer-Function"
        )

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.label_legend)
        self.layout.addWidget(self.button_colorspace)
        self.layout.addWidget(self.checkbox_force_linear_target)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.button_colorspace.setMenu(self.menu_colorspace)
        self.button_colorspace.align_text_left()
        self.label_legend.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )

        # 4. Connections
        self.checkbox_force_linear_target.stateChanged.connect(
            self.on_colorspace_changed
        )

        self.update_colorspaces()
        self.set_current_colorspace(self._current_colorspace)

    def align_text_right(self, margin: int = None):
        self.button_colorspace.align_text_right(margin)

    def align_text_left(self, margin: int = None):
        self.button_colorspace.align_text_left(margin)

    def align_text_center(self):
        self.button_colorspace.align_text_center()

    def update_colorspaces(self):
        """
        Add all the currently availabel colorspaces to the menu widget.
        """
        self.menu_colorspace.clear()
        menu_categories = {}
        for colorspace in gamutin.core.colorspaces.get_available_colorspaces():
            colorspace_categories: list[str] = [
                str(colorspace_category.value)
                for colorspace_category in colorspace.categories
            ]
            colorspace_categories.append("All")

            for category in colorspace_categories:
                menu = menu_categories.get(category)
                if not menu:
                    menu = QtWidgets.QMenu(category)
                    menu_categories[category] = menu

                action = QtWidgets.QAction(colorspace.name, self)
                action.setToolTip(colorspace.description)
                action.triggered.connect(
                    partial(self.set_current_colorspace, colorspace)
                )
                menu.addAction(action)

        for menu_category in menu_categories.values():
            self.menu_colorspace.addMenu(menu_category)

    def set_force_linear_visible(self, visible: bool):
        """
        Args:
            visible: True to set visible, False to hide.
        """
        self.checkbox_force_linear_target.setVisible(visible)

    def set_force_linear_enable(self, enable: bool):
        """
        Args:
            enable: True to set enable, False to disable.
        """
        self.checkbox_force_linear_target.setChecked(enable)

    def set_label_visible(self, visible: bool):
        """
        Args:
            visible: True to set visible, False to hide.
        """
        self.label_legend.setVisible(visible)

    def set_label_text(self, text: str):
        """
        Args:
            text: any text to use, keep it short.
        """
        self.label_legend.setText(text)

    def set_current_colorspace(
        self,
        colorspace: gamutin.core.colorspaces.RgbColorspace,
    ):
        """
        Set the given colorspace to be the currently actively selected one in the interface.
        """

        if colorspace.is_linear_copy:
            self.set_force_linear_enable(True)
            colorspace = colorspace.retrieve_linear_source()
        else:
            self.set_force_linear_enable(False)

        self.button_colorspace.setText(colorspace.name)
        self.button_colorspace.setToolTip(colorspace.description)
        self._current_colorspace = colorspace

        self.on_colorspace_changed()

    def get_current_colorspace(self) -> gamutin.core.colorspaces.RgbColorspace:
        """
        Return the colorspace currently selected in the interface.
        As a linear variant if asked as such.
        """
        colorspace_name = self._current_colorspace.name
        force_linear = self.checkbox_force_linear_target.isChecked()
        if force_linear:
            colorspace_name = f"{colorspace_name}:linear"

        colorspace = gamutin.core.colorspaces.get_colorspace(colorspace_name)
        if not colorspace:
            raise ValueError(
                f"Cannot retrieve RgbColorspace from widget with value "
                f"{colorspace_name} and {force_linear=}"
            )
        return colorspace

    def on_colorspace_changed(self, *args):
        """
        Called when the colorspace selected has changed.
        """
        new_colorspace = self.get_current_colorspace()
        self.colorspace_changed_signal.emit(new_colorspace)
        logger.debug(
            f"[{self.__class__.__name__}][on_colorspace_changed] {new_colorspace}"
        )
