"""
SOURCE: https://github.com/fre-sch/dict-treemodel-qt5
"""
from __future__ import annotations

__all__ = ("DictTreeModel", "TreeNode")

from typing import Any
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import TypeVar

from Qt import QtCore
from Qt import QtWidgets


AdapterType = TypeVar("AdapterType")


def is_char_sequence(value) -> bool:
    """
    In most instances testing for Sequence or Iterable, these string types are undesirable.
    """
    return isinstance(value, (bytes, bytearray, str))


def is_sequence(value) -> bool:
    """
    Is value a sequence (and also not a string type).
    """
    return isinstance(value, Sequence) and not is_char_sequence(value)


def is_iterable(value) -> bool:
    """
    Is value an iterable (and also not a string or mapping type).
    """
    return (
        isinstance(value, Iterable)
        and not is_char_sequence(value)
        and not isinstance(value, Mapping)
    )


class TreeNode:
    """
    TreeNode adapts Python data types to QTreeModel.

    QTreeView expects child nodes in the tree to 'know' about their parents.
    Basic Python data types (dicts, lists, strings, etc) don't have references
    to their parents. TreeNode wraps plain data types to keep a reference to
    the parent.

    QTreeView also expects child nodes to be indexed per parent, or tree level.
    While this could be done with `list.index(item)` for lists, it's more
    complex for mapping types, and it's also inefficient.
    So TreeNode also stores the index per parent.

    The consequence is TreeNode isn't a dynamic adapter, ie. changes in the
    underlying data are not automatically reflected in the TreeNodes, the
    TreeModel and finally not immediately visible in the TreeView. To view
    changes, the tree must be rebuilt.

    Provide adapter callables to convert Python types to TreeNode. Comes with
    adapters for Iterable and Mapping. See ref:`TreeNode.adapter` for more.
    """

    class Unacceptable(Exception):
        """
        TreeNode adapters must raise this exception for types they don't handle.
        """

        pass

    adapters = []

    def __init__(self, key: Any, value: Any, parent: TreeNode = None, row: int = 0):

        self.key = key
        self.value = self.adapt(self, value)
        self.parent = parent
        self.row = row

    @property
    def has_children(self) -> bool:
        return is_sequence(self.value)

    def __len__(self) -> int:

        if self.has_children:
            return len(self.value)

        return 1

    def __getitem__(self, index) -> Optional[Any]:

        if self.has_children:
            return self.value[index]

    def data(self, column: int):

        if column == 0:
            return self.key
        elif column == 1:
            return self.value

    @classmethod
    def adapt(cls, parent: TreeNode, value: Any):

        for adapter in cls.adapters:
            try:
                return adapter(cls, parent, value)
            except cls.Unacceptable:
                continue

        return value

    @classmethod
    def adapter(cls, function: AdapterType) -> AdapterType:
        """
        Decorator to add value-to-TreeNode adapters.
        Adapters must return a list of TreeNode, or must raise
        ``TreeNode.Unacceptable`` for types they don't adapt.

        Adapters have a signature of::

            def adapter(
                cls: Type[TreeNode],
                parent: TreeNode,
                value: Any
            ) -> Sequence[TreeNode]:
                pass

        Example adapter for Iterable (builtin)::

            @TreeNode.adapter
            def iterable_adapter(cls, parent, value):
                if not is_iterable(value):
                    raise cls.Unacceptable()
                return [cls(i, value, parent, i)
                        for i, value in enumerate(value)]

        Example adapter for Mapping (builtin)::

            @TreeNode.adapter
            def mapping_adapter(cls, parent, value):
                if not isinstance(value, Mapping):
                    raise cls.Unacceptable()
                return [cls(key, value, parent, i)
                        for i, (key, value) in enumerate(value.items())]
        """
        cls.adapters.append(function)
        return function


@TreeNode.adapter
def iterable_adapter(cls, parent, value):
    """
    TreeNode adapter for Iterable (excluding Mappings and string types).
    """
    if not is_iterable(value):
        raise cls.Unacceptable()
    return [cls(i, item_value, parent, i) for i, item_value in enumerate(value)]


@TreeNode.adapter
def mapping_adapter(cls, parent, value):
    """
    TreeNode adapter for Mapping.
    """
    if not isinstance(value, Mapping):
        raise cls.Unacceptable()
    return [
        cls(item_key, item_value, parent, i)
        for i, (item_key, item_value) in enumerate(value.items())
    ]


class DictTreeModel(QtCore.QAbstractItemModel):
    """
    TreeModel used to represent a python dict object.

    Args:
        data: dict object to represent
        headers: list of name to use in the headers to caracterize data column/rows
        parent_widget:
    """

    def __init__(
        self,
        data: dict = None,
        headers: Sequence[str] = None,
        parent_widget: QtWidgets.QWidget = None,
    ):

        super().__init__(parent_widget)

        self.headers = headers or ("Key", "Value")
        self.set_root_data(data or {})

    def set_root_data(self, data: dict):
        self.root = TreeNode("__root__", data, None)
        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(
            self.createIndex(0, 0),
            self.createIndex(self.rowCount(), self.columnCount()),
        )
        self.layoutChanged.emit()

    def check_for_root(self, parent: Optional[QtCore.QModelIndex]):
        return (
            self.root
            if not parent or not parent.isValid()
            else parent.internalPointer()
        )

    def columnCount(self, parent: QtCore.QModelIndex = None):
        return len(self.headers)

    def headerData(self, section, orient, role=None):
        if orient == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headers[section]

    def rowCount(self, parent: QtCore.QModelIndex = None) -> int:
        node = self.check_for_root(parent)
        return len(node)

    def index(
        self,
        row: int,
        col: int,
        parent: QtCore.QModelIndex = ...,
    ) -> QtCore.QModelIndex:
        node = self.check_for_root(parent)
        child = node[row]
        return self.createIndex(row, col, child) if child else QtCore.QModelIndex()

    def parent(self, index: QtCore.QModelIndex = ...) -> QtCore.QModelIndex:
        if not index.isValid():
            return QtCore.QModelIndex()
        child = index.internalPointer()
        parent = child.parent
        if parent is self.root:
            return QtCore.QModelIndex()
        return self.createIndex(parent.row, 0, parent)

    def hasChildren(self, parent: QtCore.QModelIndex = ...) -> bool:
        node = self.check_for_root(parent)
        return node is not None and node.has_children

    def data(self, index: QtCore.QModelIndex, role=...):
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            node = index.internalPointer()
            return node.data(index.column())


def _test_interface():

    import sys
    from pathlib import Path
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window
    from gamutin.core.io import ImageRead

    _configureLogging()
    app = getQApp()

    initial_data = {
        "students": [
            {
                "id": 1,
                "first_name": "Alex",
                "last_name": "Alligator",
                "courses": [
                    {"id": "CS010", "title": "Computer Sciences Introduction"},
                    {"id": "MTH010", "title": "Math Introduction"},
                ],
            }
        ]
    }

    window = get_testing_window()

    model = DictTreeModel(initial_data)

    layout = QtWidgets.QVBoxLayout()
    layout.setSpacing(25)

    tree_view = QtWidgets.QTreeView()
    tree_view.setModel(model)

    path = Path(r"G:\temp\normal_BaseColor.1001.exr")  # TODO use relative path
    if path.exists():
        data = ImageRead(path, None).as_dict_full()
        model.set_root_data(data)

    tree_view.resizeColumnToContents(0)
    tree_view.expandAll()

    window.add_layout(layout)
    layout.addWidget(tree_view)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
