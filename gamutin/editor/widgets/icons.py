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
    - When clicked, the icon will emit the ``clicked_signal``
    """

    clicked_signal = QtCore.Signal(object)
    """
    Emitted when the user click on the icon. 
    
    Object emitted is the mouse button a :class:`QtCore.Qt.MouseButton` enum.
    """

    def __init__(self, min_width=20, min_height=20):
        super().__init__()
        self.setObjectName("BaseDisplayIcon")
        self.setMinimumSize(min_width, min_height)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.icon = QtGui.QIcon()
        self.is_active = False
        self._lock_ratio = True
        self.icon_alignment = QtCore.Qt.AlignCenter
        self.icon_margin = 0
        self.scale_on_active = False
        self.scale_on_active_factor = 0.2

    def drawIcon(self, painter: QtGui.QPainter, rect: QtCore.QRect):
        """
        Called by :meth:`paintEvent`
        """

        icon_mode = QtGui.QIcon.Normal
        if not self.isEnabled():
            icon_mode = QtGui.QIcon.Disabled
        if self.is_active and not self.scale_on_active:
            icon_mode = QtGui.QIcon.Active

        dimension = min(rect.width(), rect.height())
        dimension -= self.icon_margin
        if self.scale_on_active and not self.is_active:
            dimension -= int(dimension * self.scale_on_active_factor)

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
        self.is_active = True
        super().enterEvent(event)
        self.update()

    def leaveEvent(self, event: QtCore.QEvent):
        self.is_active = False
        super().enterEvent(event)
        self.update()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.clicked_signal.emit(event.buttons())
        super().mousePressEvent(event)

    def paintEvent(self, event: QtGui.QPaintEvent):
        qpainter = QtGui.QPainter()
        qpainter.begin(self)
        self.drawIcon(qpainter, event.rect())
        qpainter.end()
        super().paintEvent(event)

    def setIcon(self, icon: QtGui.QIcon):
        self.icon = icon

    def enable_scaling_on_active(self, enable: bool, scale_factor: float = None):
        """
        Change the apperance of the icon when it is active by scaling it up.

        Args:
            enable: If True the icon will be rescaled when active.
            scale_factor: [0-1] range. how much of the widget width/height to remove when teh icon is smaller.
        """
        self.scale_on_active = enable
        if scale_factor:
            self.scale_on_active_factor = scale_factor

    def lock_ratio(self, lock: bool):
        """
        Set to True to prevent the icon to become wider when the widget become wider.

        Args:
            lock: True to lock ratio.
        """
        self._lock_ratio = lock

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

    def set_icon_margin(self, margin: int):
        """
        How many pixels to put between the icon and the widget border.
        """
        self.icon_margin = margin
