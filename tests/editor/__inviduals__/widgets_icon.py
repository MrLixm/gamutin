import sys

from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore

from gamutin.__main__ import _configureLogging
from gamutin.editor.main import getQApp
from gamutin.editor.testing import get_testing_window
from gamutin.editor.cfg import resources
from gamutin.editor.assets.widgets.icons import BaseDisplayIcon


def show():
    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QGridLayout()

    def get_instance() -> BaseDisplayIcon:
        _widget = BaseDisplayIcon()
        _widget.setStyleSheet("color: red;")
        return _widget

    def get_test_icon_1():
        _icon = QtGui.QIcon(str(resources.icon_file_check_outline))
        _icon.addFile(str(resources.icon_file_outline), QtCore.QSize(), _icon.Active)
        return _icon

    row = 0

    widget = get_instance()
    widget.setIcon(QtGui.QIcon(str(resources.icon_main)))
    layout.addWidget(widget, row, 0)

    widget = get_instance()
    widget.setIcon(QtGui.QIcon(str(resources.icon_alert_outline)))
    layout.addWidget(widget, row, 1)

    row += 1

    widget = get_instance()
    widget.setIcon(QtGui.QIcon(str(resources.icon_main)))
    widget.setFixedSize(40, 40)
    layout.addWidget(widget, row, 0)

    widget = get_instance()
    widget.setIcon(QtGui.QIcon(str(resources.icon_alert_outline)))
    widget.setMinimumSize(40, 40)
    layout.addWidget(widget, row, 1)

    icon = get_test_icon_1()
    widget = get_instance()
    widget.setIcon(icon)
    layout.addWidget(widget, row, 2)

    row += 1

    icon = get_test_icon_1()
    widget = get_instance()
    widget.setIcon(icon)
    widget.setText("some text over")
    layout.addWidget(widget, row, 0)

    icon = get_test_icon_1()
    widget = get_instance()
    widget.setIcon(icon)
    widget.set_icon_alignment(QtCore.Qt.AlignRight)
    widget.setText("some text over")
    layout.addWidget(widget, row, 1)

    row += 1

    icon = get_test_icon_1()
    widget = get_instance()
    widget.setIcon(icon)
    widget.lock_ratio(False)
    widget.setText("some text over")
    layout.addWidget(widget, row, 2)

    row += 1

    icon = get_test_icon_1()
    widget = get_instance()
    widget.setIcon(icon)
    widget.lock_ratio(True)
    widget.setText("some text over")
    widget.setMargin(25)
    widget.set_icon_margin(15)
    layout.addWidget(widget, row, 0)

    row += 1

    widget = QtWidgets.QLabel("some text over QLabel")
    widget.setMargin(25)
    layout.addWidget(widget, row, 0)

    row += 1

    for size_index, size in enumerate((8, 16, 32, 64, 128)):
        icon = get_test_icon_1()
        widget = get_instance()
        widget.setFixedSize(size, size)
        widget.setIcon(icon)
        widget.enable_scaling_on_active(False)
        layout.addWidget(widget, row + 1, size_index)

        icon = get_test_icon_1()
        widget = get_instance()
        widget.setFixedSize(size, size)
        widget.setIcon(icon)
        widget.enable_scaling_on_active(True)
        layout.addWidget(widget, row + 2, size_index)

        icon = get_test_icon_1()
        widget = get_instance()
        widget.setFixedSize(size, size)
        widget.setIcon(icon)
        widget.enable_scaling_on_active(True, 0.1)
        layout.addWidget(widget, row + 3, size_index)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    show()
