__all__ = ("PushButtonAligned",)

import logging
from typing import Optional

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

        pin_icon_left, align_text_right
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

        self.is_icon_pinned: bool = False
        self.text_h_alignment: QtCore.Qt.AlignmentFlag = QtCore.Qt.AlignLeft
        self.icon_h_alignment: Optional[QtCore.Qt.AlignmentFlag] = None

        # 1. Create
        self.layout = QtWidgets.QHBoxLayout(self)
        self.label_icon = QtWidgets.QLabel()
        self.label_text = QtWidgets.QLabel(self.text())

        # 2. Add
        self.layout.addStretch(0)
        self.layout.addWidget(self.label_icon)
        self.layout.addWidget(self.label_text)
        self.layout.addStretch(0)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        for label in [self.label_text, self.label_icon]:
            label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.label_text.setObjectName(f"{self.__class__.__name__}:text")
        self.label_icon.setObjectName(f"{self.__class__.__name__}:icon")
        self.label_icon.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        self.setText("")
        self.label_icon.setPixmap(self.icon().pixmap(self.iconSize()))
        self.setIcon(QtGui.QIcon())

        self.set_text_alignment(QtCore.Qt.AlignCenter)

    def setContentsMargins(
        self,
        left: Optional[int],
        top: Optional[int],
        right: Optional[int],
        bottom: Optional[int],
    ):
        """

        Args:
            left: use existing margins if None, else override it
            top: use existing margins if None, else override it
            right: use existing margins if None, else override it
            bottom: use existing margins if None, else override it
        """
        margins = self.getContentsMargins()
        left = left if left is not None else margins[0]
        top = top if top is not None else margins[1]
        right = right if right is not None else margins[2]
        bottom = bottom if bottom is not None else margins[3]
        super().setContentsMargins(left, top, right, bottom)

    def _update_layout(
        self,
        text_v_alignment: QtCore.Qt.AlignmentFlag = None,
    ):
        """
        Call an update on the icon relative to the current text position.
        """
        self.align_icon_left()
        self.layout.removeWidget(self.label_icon)
        self.layout.removeWidget(self.label_text)
        text_v_alignment = text_v_alignment or QtCore.Qt.AlignVCenter

        if self.text_h_alignment == QtCore.Qt.AlignLeft:
            # [i][t][s][s]
            self.layout.insertWidget(0, self.label_text)
            self.layout.insertWidget(0, self.label_icon)

        elif self.text_h_alignment == QtCore.Qt.AlignRight:
            # [s][s][i][t]
            self.layout.insertWidget(-1, self.label_icon)
            self.layout.insertWidget(-1, self.label_text)

        elif self.text_h_alignment == QtCore.Qt.AlignCenter:
            # [s][i][t][s]
            self.layout.insertWidget(1, self.label_text)
            self.layout.insertWidget(1, self.label_icon)

        else:
            raise ValueError(f"Unsupported value for {int(self.text_h_alignment)=}")

        logger.debug(
            f"[{self.__class__.__name__}][_update_layout](text)  {self._repr_layout()}"
        )

        self.label_text.setAlignment(self.text_h_alignment | text_v_alignment)

        if self.icon_h_alignment == QtCore.Qt.AlignLeft:

            if self.is_icon_pinned:
                self.layout.insertWidget(0, self.label_icon)
            else:
                self.align_icon_left()

        elif self.icon_h_alignment == QtCore.Qt.AlignRight:

            if self.is_icon_pinned:
                self.layout.insertWidget(-1, self.label_icon)
            else:
                self.align_icon_right()

        elif self.icon_h_alignment is None:
            pass

        else:
            raise ValueError(f"Unsupported value for {self.icon_h_alignment=}")

        logger.debug(
            f"[{self.__class__.__name__}][_update_layout](icon)    {self._repr_layout()}"
        )
        return

    def _repr_layout(self) -> str:
        """
        Return the layout structure as a string like ``[<>][i][t][<>]``.
        """

        layout_repr = ""
        for child_index in range(self.layout.count()):
            l_item = self.layout.itemAt(child_index)
            if l_item.spacerItem():
                layout_repr += "[<>]"
            else:
                layout_repr += f"[{l_item.widget().objectName().split(':')[-1][0]}]"

        if self.layout.direction() == self.layout.RightToLeft:
            layout_repr = layout_repr[::-1].replace("[", "$").replace("]", "@")
            layout_repr = layout_repr.replace("$", "]").replace("@", "[")
            layout_repr += "(reverted)"

        return layout_repr

    def align_icon_left(self):
        """
        Align icon relative to the text.
        """
        self.layout.setDirection(self.layout.LeftToRight)

    def align_icon_right(self):
        """
        Align icon relative to the text.
        """
        self.layout.setDirection(self.layout.RightToLeft)

    def align_text_left(self, margin=None):

        self.text_h_alignment = QtCore.Qt.AlignLeft
        self._update_layout(QtCore.Qt.AlignVCenter)

        self.setContentsMargins(margin, None, None, None)

    def align_text_right(self, margin=None):

        self.text_h_alignment = QtCore.Qt.AlignRight
        self._update_layout(QtCore.Qt.AlignVCenter)

        self.setContentsMargins(None, None, margin, None)

    def align_text_center(self):

        self.text_h_alignment = QtCore.Qt.AlignCenter
        self._update_layout(QtCore.Qt.AlignVCenter)

    def pin_icon_left(self, margin=None):
        """
        Align icon relative to the PushButton borders.
        """
        self.is_icon_pinned = True
        self.icon_h_alignment = QtCore.Qt.AlignLeft
        self._update_layout()
        self.setContentsMargins(margin, None, None, None)

    def pin_icon_right(self, margin=None):
        """
        Align icon relative to the PushButton borders.
        """
        self.is_icon_pinned = True
        self.icon_h_alignment = QtCore.Qt.AlignRight
        self._update_layout()
        self.setContentsMargins(None, None, margin, None)

    def set_text_alignment(
        self,
        alignment_h: QtCore.Qt.AlignmentFlag,
        alignment_v: Optional[QtCore.Qt.AlignmentFlag] = None,
    ):
        self.text_h_alignment = alignment_h
        self._update_layout(alignment_v)


def _test_interface():
    import sys
    from abc import abstractmethod
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    class TestPushButtonAligned:

        test_name = ""
        expected = ""
        button_text = "This is a test button"

        def __init__(self):
            logger.debug(
                f"[{self.__class__.__name__}][{self.test_name}] expected {self.expected}"
            )
            self.widget = PushButtonAligned(self.get_icon(), self.button_text)
            self.setup()
            logger.debug(f"[{self.__class__.__name__}] Finished.\n")

        @staticmethod
        def get_icon() -> QtGui.QIcon:
            return QtWidgets.QApplication.style().standardIcon(
                QtWidgets.QStyle.SP_ArrowRight
            )

        @abstractmethod
        def setup(self):
            pass

    # PushButtonAligned:basic

    class Test1(TestPushButtonAligned):
        test_name = "default"
        expected = "|    [i]t    |"

        def setup(self):
            pass

    class Test2(TestPushButtonAligned):
        test_name = "pin_icon_left"
        expected = "|[i]    t    |"

        def setup(self):
            self.widget.pin_icon_left()

    class Test3(TestPushButtonAligned):
        test_name = "pin_icon_right"
        expected = "|    t    [i]|"

        def setup(self):
            self.widget.pin_icon_right()

    class Test4(TestPushButtonAligned):
        test_name = "align_text_left"
        expected = "|[i]t        |"

        def setup(self):
            self.widget.align_text_left()

    class Test5(TestPushButtonAligned):
        test_name = "align_text_right"
        expected = "|        [i]t|"

        def setup(self):
            self.widget.align_text_right()

    class Test6(TestPushButtonAligned):
        test_name = "align_icon_left"
        expected = "|    [i]t    |"

        def setup(self):
            self.widget.align_icon_left()

    class Test7(TestPushButtonAligned):
        test_name = "align_icon_right"
        expected = "|    t[i]    |"

        def setup(self):
            self.widget.align_icon_right()

    # PushButtonAligned:advanced

    class Test8(TestPushButtonAligned):
        test_name = "pin_icon_right(15)"
        expected = "|    t    [i] |"

        def setup(self):
            self.widget.pin_icon_right(15)

    class Test9(TestPushButtonAligned):
        test_name = "pin_icon_left(15)"
        expected = "| [i]    t    |"

        def setup(self):
            self.widget.pin_icon_left(15)

    class Test10(TestPushButtonAligned):
        test_name = "pin_icon_right(15), align_text_left"
        expected = "|t       [i] |"

        def setup(self):
            self.widget.pin_icon_right(15)
            self.widget.align_text_left()

    class Test11(TestPushButtonAligned):
        test_name = "pin_icon_right(15), align_text_right"
        expected = "|       t[i] |"

        def setup(self):
            self.widget.pin_icon_right(15)
            self.widget.align_text_right()

    class Test12(TestPushButtonAligned):
        test_name = "pin_icon_left, align_text_left"
        expected = "|[i]t        |"

        def setup(self):
            self.widget.pin_icon_left()
            self.widget.align_text_left()

    class Test13(TestPushButtonAligned):
        test_name = "pin_icon_left, align_text_right"
        expected = "|[i]        t|"

        def setup(self):
            self.widget.pin_icon_left()
            self.widget.align_text_right()

    class Test14(TestPushButtonAligned):
        test_name = "pin_icon_left, text AlignRight|AlignVCenter"
        expected = "|[i]        t|"

        def setup(self):
            self.widget.pin_icon_left()
            self.widget.set_text_alignment(QtCore.Qt.AlignRight, QtCore.Qt.AlignVCenter)

    class Test15(TestPushButtonAligned):
        test_name = "pin_icon_left, align_text_center"
        expected = "|[i]    t    |"

        def setup(self):
            self.widget.pin_icon_left()
            self.widget.align_text_center()

    class Test16(TestPushButtonAligned):
        test_name = "pin_icon_left, align_text_right(15)"
        expected = "|[i]       t |"

        def setup(self):
            self.widget.pin_icon_left()
            self.widget.align_text_right(15)

    class Test17(TestPushButtonAligned):
        test_name = "pin_icon_left(15), align_text_right(15)"
        expected = "| [i]      t |"

        def setup(self):
            self.widget.pin_icon_left(15)
            self.widget.align_text_right(15)

    # succesive call test

    class Test18(TestPushButtonAligned):
        test_name = "pin_icon_left(15)+align_icon_left, align_text_right(15)"
        expected = "|       [i]t |"

        def setup(self):
            self.widget.pin_icon_left(15)
            self.widget.align_text_right(15)
            self.widget.align_icon_left()

    def to_qt_html(source_str: str) -> str:
        source_str = source_str.replace(" ", "&nbsp;")
        source_str = "<code>" + source_str + "</code>"
        return source_str

    layout = QtWidgets.QGridLayout()

    for class_index, test_class in enumerate(TestPushButtonAligned.__subclasses__()):
        test_class_instance = test_class()
        label_id = QtWidgets.QLabel(f"<b>{test_class.__name__}</b>")
        label_title = QtWidgets.QLabel(f"{test_class.test_name}")
        label_expected = QtWidgets.QLabel(to_qt_html(test_class.expected))
        layout.addWidget(label_id, class_index, 0)
        layout.addWidget(label_title, class_index, 1)
        layout.addWidget(test_class_instance.widget, class_index, 2)
        layout.addWidget(label_expected, class_index, 3)

    layout.setSpacing(25)
    layout.setColumnStretch(2, 3)

    window.add_layout(layout)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
