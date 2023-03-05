__all__ = ("ColorspaceSelector",)

import logging
from functools import partial

from Qt import QtCore
from Qt import QtWidgets

import gamutin.core.colorspaces
from gamutin.editor.assets.widgets import PushButtonAligned

logger = logging.getLogger(__name__)


class ColorspaceSelector(PushButtonAligned):
    """
    A widget to select a colorspace using a nested menu.

    Colorspace are ordered in different categories, each represented by a menu.

    It's possibel to override the colorspace default transfer functions using
    the "Force Linear Transfer-Function" action.
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
        self.menu = QtWidgets.QMenu()
        self.action_force_linear = QtWidgets.QAction("Force Linear Transfer-Function")
        # 2. Modify
        self.setMenu(self.menu)
        self.align_text_left()
        self.action_force_linear.setCheckable(True)
        self.action_force_linear.setChecked(False)
        # 3. Connections
        self.action_force_linear.triggered.connect(self.on_colorspace_changed)

        self.update_colorspaces()
        self.set_current_colorspace(self._current_colorspace)

    def update_colorspaces(self):
        """
        Add all the currently available colorspaces to the menu widget.
        """

        # build a dict with all the action to add
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

        # actually build the visible menu
        self.menu.clear()
        self.menu.addAction(self.action_force_linear)

        for menu_category in menu_categories.values():
            self.menu.addMenu(menu_category)

        return

    def set_force_linear_visible(self, visible: bool):
        """
        Args:
            visible: True to set visible, False to hide.
        """
        self.action_force_linear.setVisible(visible)

    def set_force_linear_enable(self, enable: bool):
        """
        Args:
            enable: True to set enable, False to disable.
        """
        self.action_force_linear.setChecked(enable)

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

        self._current_colorspace = colorspace

        self.on_colorspace_changed()

    def get_current_colorspace(self) -> gamutin.core.colorspaces.RgbColorspace:
        """
        Return the colorspace currently selected in the interface.
        As a linear variant if asked as such.
        """
        colorspace_name = self._current_colorspace.name
        colorspace = gamutin.core.colorspaces.get_colorspace(colorspace_name)

        force_linear = self.action_force_linear.isChecked()
        if force_linear:
            colorspace = colorspace.as_linear_copy()

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

        self.setText(new_colorspace.name)
        self.setToolTip(new_colorspace.description)

        self.colorspace_changed_signal.emit(new_colorspace)
        logger.debug(
            f"[{self.__class__.__name__}][on_colorspace_changed] {new_colorspace}"
        )
