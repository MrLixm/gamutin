from typing import Optional

from Qt import QtWidgets
from Qt import QtCore

import gamutin.core.utils

__all__ = (
    "ContextWidget",
    "DependencyViewerTreeWidget",
)


class DependencyViewerTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        self.setColumnCount(2)
        self.setAlternatingRowColors(False)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setUniformRowHeights(True)
        self.setRootIsDecorated(False)
        self.setItemsExpandable(False)
        # select only one row at a time
        self.setSelectionMode(self.SingleSelection)
        # select only rows
        self.setSelectionBehavior(self.SelectRows)
        # remove dotted border on columns
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setHeaderLabels(("Name", "Version"))
        header = self.header()
        header.setSectionResizeMode(0, header.ResizeToContents)

    def bakeUI(self):
        self.clear()
        dependencies = gamutin.core.utils.getCurrentDependencies()
        for dependency in dependencies:
            self.addDependency(dependency[0], dependency[1])
        self.sortByColumn(0, QtCore.Qt.AscendingOrder)
        return

    def addDependency(self, name: str, version: str) -> QtWidgets.QTreeWidgetItem:
        twi = QtWidgets.QTreeWidgetItem(self)
        twi.setText(0, name)
        twi.setText(1, version)
        return twi


class ContextWidget(QtWidgets.QFrame):
    name = "ContextWidget"
    style = f"""
    QFrame#{name} {{
        border: 1px solid palette(mid);
        border-radius: 4px;
        background-color: palette(midlight);
    }}
    QLabel {{
        color: palette(mid);
        font-family: monospace;
    }}
    """

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(parent)
        self.setObjectName(self.name)
        self._context: Optional[str] = None
        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.lyt = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()

        # 2. Add
        self.setLayout(self.lyt)
        self.lyt.addWidget(self.label)

        # 3. Modify
        self.setStyleSheet(self.style)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        # 4. Connections
        return

    def bakeUI(self):
        self._context = gamutin.core.utils.getSysContext()
        self.label.setText(f"<pre>{self._context}</pre>")

    def getContext(self) -> Optional[str]:
        """
        Get the string representing the context currently being displayed.
        """
        return self._context
