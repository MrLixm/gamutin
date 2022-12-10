import enum
import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.cfg import resources

logger = logging.getLogger(__name__)


def disable_layout_content(layout: QtWidgets.QLayout, disabled: bool):
    """
    Disable all the chidlren widgets recursively in the given layout.
    """
    for child_index in range(layout.count()):
        qt_object = layout.itemAt(child_index).widget()
        if qt_object:
            qt_object.setEnabled(not disabled)
        qt_object = layout.itemAt(child_index).layout()
        if qt_object:
            disable_layout_content(qt_object, disabled)


class TestStyleThemes(enum.Enum):
    """
    Themes availables
    """
    dark = "dark"
    default = "default"


class BlankTestWindow(QtWidgets.QWidget):
    """
    A basic window for testing purposes.
    """

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout_header = QtWidgets.QHBoxLayout()
        self.layout_user = QtWidgets.QVBoxLayout()
        self.status_bar = QtWidgets.QStatusBar()
        self.label_theme = QtWidgets.QLabel("Theme")
        self.combobox_theme = QtWidgets.QComboBox()
        self.checkbox_disabled = QtWidgets.QCheckBox("Disabled")

        self.setLayout(self.layout)
        self.layout.addLayout(self.layout_header)
        self.layout.addLayout(self.layout_user)
        self.layout.addWidget(self.status_bar)
        self.layout_header.addWidget(self.label_theme)
        self.layout_header.addWidget(self.combobox_theme)
        self.layout_header.addWidget(self.checkbox_disabled)
        self.layout_header.addStretch()

        self.layout_header.setContentsMargins(*(15,)*4)
        for style_theme in TestStyleThemes:
            self.combobox_theme.addItem(style_theme.value, style_theme)

        self.combobox_theme.currentIndexChanged.connect(self._on_theme_change)
        self.combobox_theme.currentIndexChanged.emit(-1)
        self.checkbox_disabled.stateChanged.connect(self._on_layout_disabled)
        self.checkbox_disabled.setChecked(False)

    def add_widget(self, widget: QtWidgets.QWidget):
        self.layout_user.addWidget(widget)

    def add_layout(self, layout: QtWidgets.QLayout):
        self.layout_user.addLayout(layout)

    def show_message(self, message: str, timeout: int = 2000):
        self.status_bar.showMessage(message, timeout)

    def _on_theme_change(self, index=None):

        theme_asked: TestStyleThemes = self.combobox_theme.currentData()

        if theme_asked == TestStyleThemes.dark:
            stylesheet = resources.style_test.copy()
            stylesheet.resolve(resources.theme_default)
            stylesheet.apply_to(self)
        else:
            self.setStyleSheet("/*blank*/")
        return

    def _on_layout_disabled(self):
        disable_layout_content(self.layout_user, self.checkbox_disabled.isChecked())


def get_testing_window() -> BlankTestWindow:
    window = BlankTestWindow()
    window.resize(1000, 800)
    return window
