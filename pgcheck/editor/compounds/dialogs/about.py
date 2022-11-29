import math

from Qt import QtWidgets
from Qt import QtCore

import pgcheck
from .context_dialogs import ContextWidget
from .context_dialogs import DependencyViewerTreeWidget

__all__ = ("AboutDialog",)


class AboutDialog(QtWidgets.QDialog):
    """
    Main "About" dialog.
    The user can display this dialog to know more about the current app instance he
    is using.
    """

    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__(parent)
        self.setWindowTitle(f"{self.parent().windowTitle()} - About")
        self.resize(
            math.floor(self.parent().width() / 2),
            math.floor(self.parent().height() / 2),
        )

        self.cookUI()
        return

    def cookUI(self):

        # Create
        self.lyt = QtWidgets.QVBoxLayout()
        self.lbl_app = QtWidgets.QLabel(
            f"<h1>{pgcheck.c.name.title()} - v{pgcheck.c.__version__}</h1>"
        )
        self.ctx_wgt = ContextWidget(self)
        self.lbl_dependencies = QtWidgets.QLabel("Dependencies Used: ")
        self.tw_dependencies = DependencyViewerTreeWidget(self)

        # Assign
        self.setLayout(self.lyt)
        self.lyt.addWidget(self.lbl_app)
        self.lyt.addWidget(self.ctx_wgt)
        self.lyt.addWidget(self.lbl_dependencies)
        self.lyt.addWidget(self.tw_dependencies)

        # Modify
        self.lbl_app.setAlignment(QtCore.Qt.AlignCenter)
        self.tw_dependencies.setMinimumHeight(150)
        return

    def parent(self) -> QtWidgets.QMainWindow:
        # override for type-hints
        return super().parent()
