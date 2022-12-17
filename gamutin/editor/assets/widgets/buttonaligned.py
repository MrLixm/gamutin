__all__ = ("PushButtonAligned",)

import logging

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

logger = logging.getLogger(__name__)


class PushButtonAligned(QtWidgets.QPushButton):
    """
    A button on which you can set in which direction the text and its icon is aligned.

    The ``pin_icon...`` methods allow to pin the icon to border of the button, while the
    ``align_icon...`` align it relative to the text.

    Example::

        pin_icon_left, align_text_left
        ————————————————————————
        | [icon] text          |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        pin_icon_left, align_text_left
        ————————————————————————
        | [icon]          text |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        pin_icon_right, align_text_right
        ————————————————————————
        |          text [icon] |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        align_icon_right
        ————————————————————————
        |     text [icon]      |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

    inspired from: https://stackoverflow.com/a/53417349/13806195
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Create
        self.layout = QtWidgets.QHBoxLayout(self)
        self.label_icon = QtWidgets.QLabel()
        self.label_text = QtWidgets.QLabel(self.text())
        self.stretch_l = QtWidgets.QSpacerItem(
            16,
            16,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.stretch_r = QtWidgets.QSpacerItem(
            16,
            16,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding,
        )

        # 2. Add
        self.layout.addWidget(self.label_text)
        self.layout.addWidget(self.label_icon)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        for label in [self.label_text, self.label_icon]:
            label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.label_icon.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        self.setText("")
        self.label_icon.setPixmap(self.icon().pixmap(self.iconSize()))
        self.setIcon(QtGui.QIcon())

        # set default look
        self.align_icon_left()
        self.align_text_center()

    def align_icon_left(self):
        """
        Align icon relative to the text.
        """
        self.layout.setDirection(self.layout.RightToLeft)
        self.layout.removeItem(self.stretch_l)
        self.layout.removeItem(self.stretch_r)
        self.layout.insertItem(0, self.stretch_l)
        self.layout.insertItem(-1, self.stretch_r)

    def align_icon_right(self):
        """
        Align icon relative to the text.
        """
        self.layout.setDirection(self.layout.LeftToRight)
        self.layout.removeItem(self.stretch_l)
        self.layout.removeItem(self.stretch_r)
        self.layout.insertItem(0, self.stretch_l)
        self.layout.insertItem(-1, self.stretch_r)

    def align_text_left(self, margin=0):
        self.label_text.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        left, top, right, bottom = self.getContentsMargins()
        self.setContentsMargins(margin, top, right, bottom)

    def align_text_right(self, margin=0):
        self.label_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        left, top, right, bottom = self.getContentsMargins()
        self.setContentsMargins(left, top, margin, bottom)

    def align_text_center(self):
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)

    def pin_icon_left(self, margin=0):
        """
        Align icon relative to the PushButton borders.
        """
        self.align_icon_left()
        self.layout.removeItem(self.stretch_l)
        self.layout.removeItem(self.stretch_r)

        left, top, right, bottom = self.getContentsMargins()
        self.setContentsMargins(margin, top, right, bottom)

    def pin_icon_right(self, margin=0):
        """
        Align icon relative to the PushButton borders.
        """
        self.align_icon_right()
        self.layout.removeItem(self.stretch_l)
        self.layout.removeItem(self.stretch_r)

        left, top, right, bottom = self.getContentsMargins()
        self.setContentsMargins(left, top, margin, bottom)

    def set_text_alignment(self, alignment: QtCore.Qt.Alignment):
        self.label_text.setAlignment(alignment)


def _test_interface():
    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QGridLayout()
    layout.setSpacing(25)

    window.add_layout(layout)

    widget_list = []
    button_text = "THis is a test button"

    # PushButtonAligned:basic

    icon = QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ArrowRight)
    widget = PushButtonAligned(icon, button_text)
    expected = "|    [i]t    |"
    widget_list.append((widget, "default", expected))

    icon = QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ArrowRight)
    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left()
    expected = "|[i]    t    |"
    widget_list.append((widget, "pin_icon_left", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_right()
    expected = "|    t    [i]|"
    widget_list.append((widget, "pin_icon_right", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.align_text_left()
    expected = "|[i]t        |"
    widget_list.append((widget, "align_text_left", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.align_text_right()
    expected = "|        [i]t|"
    widget_list.append((widget, "align_text_right", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.align_icon_left()
    expected = "|    [i]t    |"
    widget_list.append((widget, "align_icon_left", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.align_icon_right()
    expected = "|    t[i]    |"
    widget_list.append((widget, "align_icon_right", expected))

    # PushButtonAligned:advanced

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_right(15)
    expected = "|    t    [i] |"
    widget_list.append((widget, "pin_icon_right(15)", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left(15)
    expected = "| [i]    t    |"
    widget_list.append((widget, "pin_icon_left(15)", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_right(15)
    widget.set_text_alignment(QtCore.Qt.AlignLeft)
    expected = "|t       [i] |"
    widget_list.append((widget, "pin_icon_right(15), text AlignLeft", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_right(15)
    widget.set_text_alignment(QtCore.Qt.AlignRight)
    expected = "|       t[i] |"
    widget_list.append((widget, "pin_icon_right(15), text AlignRight", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left()
    widget.set_text_alignment(QtCore.Qt.AlignLeft)
    expected = "|[i]t        |"
    widget_list.append((widget, "pin_icon_left, text AlignLeft", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left()
    widget.set_text_alignment(QtCore.Qt.AlignRight)
    expected = "|[i]        t|"
    widget_list.append((widget, "pin_icon_left, text AlignRight", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left()
    widget.set_text_alignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
    expected = "|[i]        t|"
    widget_list.append(
        (widget, "pin_icon_left, text AlignRight|AlignVCenter", expected)
    )

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left()
    widget.set_text_alignment(QtCore.Qt.AlignCenter)
    expected = "|[i]    t    |"
    widget_list.append((widget, "pin_icon_left, text AlignCenter", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left()
    widget.align_text_right(15)
    expected = "|[i]       t |"
    widget_list.append((widget, "pin_icon_left, align_text_right(15)", expected))

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left(15)
    widget.align_text_right(15)
    expected = "| [i]      t |"
    widget_list.append((widget, "pin_icon_left(15), align_text_right(15)", expected))

    # succesive call test

    widget = PushButtonAligned(icon, button_text)
    widget.pin_icon_left(15)
    widget.align_text_right(15)
    widget.align_icon_left()
    expected = "|       [i]t |"
    widget_list.append(
        (widget, "pin_icon_left(15)+align_icon_left, align_text_right(15)", expected)
    )

    def to_qt_html(source_str: str) -> str:
        source_str = source_str.replace(" ", "&nbsp;")
        source_str = "<code>" + source_str + "</code>"
        return source_str

    for widget_index, widget_data in enumerate(widget_list):
        label_title = QtWidgets.QLabel(widget_data[1])
        label_expected = QtWidgets.QLabel(to_qt_html(widget_data[2]))
        layout.addWidget(label_title, widget_index, 0)
        layout.addWidget(widget_data[0], widget_index, 1)
        layout.addWidget(label_expected, widget_index, 2)

    layout.setColumnStretch(1, 3)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
