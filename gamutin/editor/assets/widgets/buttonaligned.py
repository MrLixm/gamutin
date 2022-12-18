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
