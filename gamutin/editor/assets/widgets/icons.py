from Qt import QtWidgets
from Qt import QtGui
from Qt import QtCore


class BaseDisplayIcon(QtWidgets.QLabel):
    """
    A widget made to display an icon with a transparent background.

    Being a QLabel subclass you can still add text that will be draw over it.

    **Warning** : does not support aspect ratio other than 1:1 (square). Works best with SVG.

    - You can add an optional tooltip as usual.
    - When setting the QIcon, its ``Active`` mode will be used if set.
    """

    def __init__(self, min_width=20, min_height=20):
        super().__init__()
        self.setObjectName("BaseDisplayIcon")
        self.setMinimumSize(min_width, min_height)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.icon = QtGui.QIcon()
        self.isActive = False
        self._lock_ratio = True
        self.icon_alignment = QtCore.Qt.AlignCenter

    def drawIcon(self, painter: QtGui.QPainter, rect: QtCore.QRect):
        """
        Called by :meth:`paintEvent`
        """

        icon_mode = QtGui.QIcon.Normal
        if not self.isEnabled():
            icon_mode = QtGui.QIcon.Disabled
        if self.isActive:
            icon_mode = QtGui.QIcon.Active

        dimension = min(rect.width(), rect.height())

        pixmap = self.icon.pixmap(
            QtCore.QSize(
                dimension,
                dimension,
            ),
            icon_mode,
        )

        target_rect: QtCore.QRect = rect.__copy__()
        if self._lock_ratio:
            target_rect.setWidth(dimension)
            target_rect.setHeight(dimension)

        if self.icon_alignment == QtCore.Qt.AlignRight:
            target_rect.moveRight(rect.right())
        elif self.icon_alignment == QtCore.Qt.AlignCenter:
            target_rect.moveCenter(rect.center())
        elif self.icon_alignment == QtCore.Qt.AlignLeft:
            pass

        painter.drawPixmap(target_rect, pixmap)

    def enterEvent(self, event: QtCore.QEvent):
        self.isActive = True
        super().enterEvent(event)
        self.update()

    def leaveEvent(self, event: QtCore.QEvent):
        self.isActive = False
        super().enterEvent(event)
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qpainter = QtGui.QPainter()
        qpainter.begin(self)
        self.drawIcon(qpainter, event.rect())
        qpainter.end()
        super().paintEvent(event)

    def setIcon(self, icon: QtGui.QIcon):
        self.icon = icon

    def set_icon_alignment(self, alignment: QtCore.Qt.AlignmentFlag):
        """
        How to align the icon when text is wider than the icon and lock_ratio = True.
        """

        if alignment not in [
            QtCore.Qt.AlignLeft,
            QtCore.Qt.AlignRight,
            QtCore.Qt.AlignCenter,
        ]:
            raise ValueError("Given alignement is not supported.")

        self.icon_alignment = alignment

    def lock_ratio(self, lock: bool):
        """
        Set to True to prevent the icon to become wider when the widget become wider.

        Args:
            lock: True to lock ratio.
        """
        self._lock_ratio = lock


def _test_interface():

    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window
    from gamutin.editor.cfg import resources

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QGridLayout()

    def get_test_icon_1():
        _icon = QtGui.QIcon(str(resources.icon_file_check_outline))
        _icon.addFile(str(resources.icon_file_outline), QtCore.QSize(), _icon.Active)
        return _icon

    widget = BaseDisplayIcon()
    widget.setIcon(QtGui.QIcon(str(resources.icon_main)))
    layout.addWidget(widget, 0, 0)

    widget = BaseDisplayIcon()
    widget.setIcon(QtGui.QIcon(str(resources.icon_main)))
    widget.setFixedSize(40, 40)
    layout.addWidget(widget, 1, 0)

    widget = BaseDisplayIcon()
    widget.setIcon(QtGui.QIcon(str(resources.icon_alert_outline)))
    layout.addWidget(widget, 0, 1)

    widget = BaseDisplayIcon()
    widget.setIcon(QtGui.QIcon(str(resources.icon_alert_outline)))
    widget.setMinimumSize(40, 40)
    layout.addWidget(widget, 1, 1)

    icon = get_test_icon_1()
    widget = BaseDisplayIcon()
    widget.setIcon(icon)
    layout.addWidget(widget, 2, 0)

    icon = get_test_icon_1()
    widget = BaseDisplayIcon()
    widget.setIcon(icon)
    widget.setText("some text over")
    layout.addWidget(widget, 2, 1)

    icon = get_test_icon_1()
    widget = BaseDisplayIcon()
    widget.setIcon(icon)
    widget.set_icon_alignment(QtCore.Qt.AlignRight)
    widget.setText("some text over")
    layout.addWidget(widget, 2, 2)

    icon = get_test_icon_1()
    widget = BaseDisplayIcon()
    widget.setIcon(icon)
    widget.lock_ratio(False)
    widget.setText("some text over")
    layout.addWidget(widget, 2, 3)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
