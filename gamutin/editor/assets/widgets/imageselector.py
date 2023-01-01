__all__ = ("ImageSelectorWidget",)

import ast
import logging
from typing import Optional

from Qt import QtWidgets
from Qt import QtCore

from gamutin.core.io import ImageRead
from gamutin.editor.utils import block_signals
from gamutin.editor.assets.widgets import pathselector
from gamutin.editor.assets.widgets.colorspaceselector import ColorspaceSelector
from gamutin.editor.assets.widgets.imagerepr import ImageReprWidget
from gamutin.editor.assets.widgets.errorhandler import ErrorHandlerWidget


logger = logging.getLogger(__name__)


class ImageSelectorWidget(QtWidgets.QFrame):
    """
    An "Uber" widget to select an image file and configure how it must be read.

    You can edit :
    - image path
    - image colorspace
    - image subimage and mip level
    - image channels to read
    """

    image_changed_signal = QtCore.Signal(object)
    """
    Emit :class:`ImageRead` or None
    """

    error_signal = QtCore.Signal(object)
    """
    Signal emitted when an error is produced OR disappear. 

    Data Type emmitted is a :class:`WidgetUserError` instance when an error is produced.
    Data Type emmitted is a :obj:`None` if the previous error has been cleared.
    """

    def __init__(self, parent=None):
        # type: (QtWidgets.QWidget) -> None
        super().__init__(parent)

        self.setObjectName("ImageSelector")

        self.cookUI()
        self.bakeUI()

    def cookUI(self):

        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.layout_colorspace = QtWidgets.QHBoxLayout()
        self.layout_image_options = QtWidgets.QHBoxLayout()
        self.widget_path = pathselector.PathSelector()
        self.widget_colorspace_source = ColorspaceSelector()
        self.spinbox_subimage = QtWidgets.QSpinBox()
        self.spinbox_miplevel = QtWidgets.QSpinBox()
        self.combobox_channel = QtWidgets.QComboBox()
        self.label_subimage = QtWidgets.QLabel("Sub Image")
        self.label_miplevel = QtWidgets.QLabel("Mip Level")
        self.label_channel = QtWidgets.QLabel("Channel")
        self.button_colorspace_detect = QtWidgets.QPushButton("Auto-Detect")
        self.button_info = QtWidgets.QPushButton("Info")
        self.error_handler = ErrorHandlerWidget()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addLayout(self.layout_colorspace)
        self.layout.addWidget(self.widget_path)
        self.layout.addLayout(self.layout_image_options)
        self.layout.addWidget(self.error_handler)
        self.layout_colorspace.addStretch(0)
        self.layout_colorspace.addWidget(self.widget_colorspace_source)
        self.layout_colorspace.addWidget(self.button_colorspace_detect)
        self.layout_image_options.addStretch(0)
        self.layout_image_options.addWidget(self.label_subimage)
        self.layout_image_options.addWidget(self.spinbox_subimage)
        self.layout_image_options.addWidget(self.label_miplevel)
        self.layout_image_options.addWidget(self.spinbox_miplevel)
        self.layout_image_options.addWidget(self.label_channel)
        self.layout_image_options.addWidget(self.combobox_channel)
        self.layout_image_options.addWidget(self.button_info)

        # 3. Modify
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout_image_options.setContentsMargins(0, 0, 0, 0)
        self.widget_path.set_path_type(pathselector.PathType.file_exist)
        for label in [self.label_subimage, self.label_miplevel, self.label_channel]:
            label.setSizePolicy(
                QtWidgets.QSizePolicy.Fixed,
                QtWidgets.QSizePolicy.Fixed,
            )
        tooltip = (
            "Which channel from the current subimage/miplevel to keep and in which order."
            "This is specified as a python tuble object where each item is a channel name."
            "(evaluated using <code>ast.literal_eval</code>)"
            'Example: <code>("R", "G", "B", "A")</code>'
        )
        self.label_channel.setToolTip(tooltip)
        self.combobox_channel.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred,
        )
        self.combobox_channel.setEditable(True)
        self.combobox_channel.setToolTip(tooltip)
        self.spinbox_subimage.setMinimum(0)
        self.spinbox_miplevel.setMinimum(0)

        # 4. Connections
        self.widget_colorspace_source.colorspace_changed_signal.connect(
            self.on_image_changed
        )
        self.widget_path.path_changed_signal.connect(self.on_image_changed)
        self.widget_path.error_signal.connect(self.error_handler.add_error)
        self.spinbox_subimage.valueChanged.connect(self.on_image_changed)
        self.spinbox_miplevel.valueChanged.connect(self.on_image_changed)
        self.combobox_channel.currentIndexChanged.connect(self.on_image_changed)
        self.combobox_channel.currentTextChanged.connect(self.on_image_changed)
        self.button_info.clicked.connect(self.show_image_repr)
        return

    def bakeUI(self):

        with block_signals(self):

            current_image = self.current_image
            new_image_spec = None

            if current_image:

                self.spinbox_subimage.setMaximum(current_image.subimage_number - 1)
                self.spinbox_miplevel.setMaximum(
                    current_image.miplevel_number_at(self.subimage) - 1
                )

            for spinbox_widget in [self.spinbox_subimage, self.spinbox_miplevel]:
                if spinbox_widget.value() == -1 and spinbox_widget.maximum() >= 0:
                    spinbox_widget.setValue(0)

            if current_image:
                new_image_spec = current_image.get_spec_at(self.subimage, self.miplevel)

            self.combobox_channel.clear()

            if new_image_spec:

                self.combobox_channel.addItem(repr(new_image_spec.channelnames))

                if not self.combobox_channel.currentText():
                    self.combobox_channel.setCurrentIndex(0)

        return

    def blockSignals(self, block: bool):
        super().blockSignals(block)
        self.widget_colorspace_source.blockSignals(block)
        self.widget_path.blockSignals(block)
        self.widget_path.blockSignals(block)
        self.spinbox_subimage.blockSignals(block)
        self.spinbox_miplevel.blockSignals(block)
        self.combobox_channel.blockSignals(block)
        self.combobox_channel.blockSignals(block)
        self.button_info.blockSignals(block)

    @property
    def current_image(self) -> Optional[ImageRead]:
        """
        Get an ImageRead instance for the current path specified with the given options.
        """
        if not self.widget_path.current_path:
            return None

        return ImageRead(
            path=self.widget_path.current_path,
            colorspace=self.widget_colorspace_source.get_current_colorspace(),
        )

    @property
    def subimage(self) -> int:
        return self.spinbox_subimage.value()

    @property
    def miplevel(self) -> int:
        return self.spinbox_miplevel.value()

    @property
    def channels(self) -> Optional[tuple[str]]:

        if (
            not self.combobox_channel.currentText()
            or not self.combobox_channel.isVisible()
        ):
            return None

        channels = ast.literal_eval(self.combobox_channel.currentText())
        return channels

    def detect_image_colorspace(self):

        if not self.current_image:
            return
        # TODO
        return

    def on_image_changed(self, *args):
        """
        Called when any parameters defining the image has changed.
        """
        new_image = self.current_image

        self.image_changed_signal.emit(new_image)
        self.bakeUI()

        logger.debug(f"[{self.__class__.__name__}][on_image_changed] {new_image}")

    def set_expected_file_extensions(self, file_extensions: list[str]):
        """
        Only used if the expected path type is one of a file but can always be called.

        Args:
            file_extensions:
                list of file extensions WITH the dot delimiter. ex: [".jpg", ".txt"]
        """
        self.widget_path.set_expected_file_extensions(file_extensions)

    def show_image_repr(self):

        window = QtWidgets.QMainWindow(self)
        window.setWindowTitle("Image Info")
        image_repr_widget = ImageReprWidget(QtWidgets.QApplication.activeWindow())
        image_repr_widget.set_image(self.current_image)
        window.setCentralWidget(image_repr_widget)
        window.setContentsMargins(*(15,) * 4)
        window.show()

    def toggle_channel_selection(self, enable: bool):
        """
        Change if the user can select channels from the image or not.
        This hide the widget if not.

        Args:
            enable: True to make it visible and False to hide it.
        """
        self.label_channel.setVisible(enable)
        self.combobox_channel.setVisible(enable)
        if not enable:
            self.combobox_channel.setEditText("")


def _test_interface():

    import sys
    from gamutin.__main__ import _configureLogging
    from gamutin.editor.main import getQApp
    from gamutin.editor.testing import get_testing_window

    _configureLogging()
    app = getQApp()

    window = get_testing_window()

    layout = QtWidgets.QVBoxLayout()
    layout.setSpacing(25)

    window.add_layout(layout)

    widget = ImageSelectorWidget()
    layout.addWidget(widget)
    widget = ImageSelectorWidget()
    widget.toggle_channel_selection(False)
    layout.addWidget(widget)
    widget = ImageSelectorWidget()
    widget.toggle_channel_selection(False)
    widget.set_expected_file_extensions([".jpg", ".exr"])
    layout.addWidget(widget)

    layout.addStretch(1)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    _test_interface()
