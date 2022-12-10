import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.assets.widgets import pathselector

logger = logging.getLogger(__name__)


class GamutinMainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # type: (QtWidgets.QWidget) -> None
        super().__init__(parent)
        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.layout = QtWidgets.QVBoxLayout()
        self.label_source = QtWidgets.QLabel("Source")
        self.label_target = QtWidgets.QLabel("Target")
        self.label_options = QtWidgets.QLabel("Processing Options")
        self.button_launch = QtWidgets.QPushButton("Launch Processing")

        self.layout_source = QtWidgets.QGridLayout()
        self.widget_path_source = pathselector.PathSelector()
        self.label_colorspace_source = QtWidgets.QLabel("Source Colorspace")
        self.combobox_colorspace_source = QtWidgets.QComboBox()
        self.checkbox_alpha_mask_source = QtWidgets.QCheckBox("Use Alpha as Mask")

        self.layout_options = QtWidgets.QGridLayout()
        self.label_colorspace_reference = QtWidgets.QLabel("Reference Colorspace")
        self.label_blend_mode = QtWidgets.QLabel("Blend Mode")
        self.label_tolerance = QtWidgets.QLabel("Tolerance")
        self.label_invalid = QtWidgets.QLabel("Invalid Color")
        self.label_valid = QtWidgets.QLabel("Valid Color")
        self.combobox_colorspace_reference = QtWidgets.QComboBox()
        self.combobox_blend_mode = QtWidgets.QComboBox()
        self.slider_tolerance = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.color_invalid = QtWidgets.QPushButton()
        self.color_valid = QtWidgets.QPushButton()

        self.layout_target = QtWidgets.QGridLayout()
        self.checkbox_preview_only = QtWidgets.QCheckBox("Preview Only")
        self.widget_path_target = pathselector.PathSelector()
        self.label_colorspace_target = QtWidgets.QLabel("Target Colorspace")
        self.combobox_colorspace_target = QtWidgets.QComboBox()

        # 2. Add
        self.setLayout(self.layout)
        self.layout.addWidget(self.label_source)
        self.layout.addLayout(self.layout_source)
        self.layout.addWidget(self.label_options)
        self.layout.addLayout(self.layout_options)
        self.layout.addWidget(self.label_target)
        self.layout.addLayout(self.layout_target)
        self.layout.addWidget(self.button_launch)
        self.layout.addStretch()

        self.layout_source.addWidget(self.widget_path_source, 0, 0, 1, -1)
        self.layout_source.addWidget(self.label_colorspace_source, 1, 0)
        self.layout_source.addWidget(self.combobox_colorspace_source, 1, 1)
        self.layout_source.addWidget(self.checkbox_alpha_mask_source, 1, 2)

        self.layout_target.addWidget(self.checkbox_preview_only, 0, 0)
        self.layout_target.addWidget(self.widget_path_target, 1, 0, 1, -1)
        self.layout_target.addWidget(self.label_colorspace_target, 2, 0)
        self.layout_target.addWidget(self.combobox_colorspace_target, 2, 1)

        self.layout_options.addWidget(self.label_colorspace_reference, 0, 0)
        self.layout_options.addWidget(self.label_blend_mode, 1, 0)
        self.layout_options.addWidget(self.label_tolerance, 2, 0)
        self.layout_options.addWidget(self.label_invalid, 3, 0)
        self.layout_options.addWidget(self.label_valid, 4, 0)
        self.layout_options.addWidget(self.combobox_colorspace_reference, 0, 1)
        self.layout_options.addWidget(self.combobox_blend_mode, 1, 1)
        self.layout_options.addWidget(self.slider_tolerance, 2, 1)
        self.layout_options.addWidget(self.color_invalid, 3, 1)
        self.layout_options.addWidget(self.color_valid, 4, 1)

        # 3. Modify
        self.widget_path_source.set_path_type(pathselector.PathType.file_exist)
        self.widget_path_target.set_path_type(pathselector.PathType.file)
        self.checkbox_alpha_mask_source.setToolTip(
            "Use the alpha channel to specify which pixel need to be processed."
        )
        self.checkbox_preview_only.setToolTip(
            "Do not generate a result image on disk. "
            "Instead just preview the result in this application. "
            "<i>(A temporary image will still need to be generated)</i>"
        )
        self.label_colorspace_source.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        self.label_colorspace_target.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        self.layout.setContentsMargins(*(15,) * 4)
        self.layout_source.setContentsMargins(*(25,) * 4)
        self.layout_options.setContentsMargins(*(25,) * 4)
        self.layout_target.setContentsMargins(*(25,) * 4)
        # 4. Connections
        return

    def bakeUI(self):
        pass
