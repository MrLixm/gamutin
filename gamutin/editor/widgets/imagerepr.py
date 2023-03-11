__all__ = ("ImageReprWidget",)

import logging
from typing import Optional

from Qt import QtWidgets
from Qt import QtCore

from gamutin.core.io import ImageRead
from gamutin.editor.widgets.dicttreeview import DictTreeModel


logger = logging.getLogger(__name__)


class ImageReprWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # type: (QtWidgets.QWidget) -> None
        super().__init__(parent)

        self._image: Optional[ImageRead] = None
        self.setWindowFlags(QtCore.Qt.Popup)

        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.treeview = QtWidgets.QTreeView()
        self.tree_model = DictTreeModel(headers=["keys", "values"])

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.treeview)
        self.treeview.setModel(self.tree_model)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        # 4. Connections
        return

    def bakeUI(self):
        if not self._image:
            return

        self.tree_model.set_root_data(self._image.as_dict_full())
        self.treeview.expandAll()
        self.treeview.resizeColumnToContents(0)

    def set_image(self, image: ImageRead):
        self._image = image
        self.bakeUI()

    def get_image(self) -> ImageRead:
        return self._image
