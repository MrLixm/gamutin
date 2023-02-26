import logging

from Qt import QtWidgets
from Qt import QtCore

from gamutin.editor.options import SUPPORTED_FILE_EXTENSIONS
from gamutin.editor.options import MaskOptions
from gamutin.editor.options import CompositeBlendModes
from gamutin.editor.assets.widgets import pathselector
from gamutin.editor.assets.widgets.colorspaceselector import ColorspaceSelector
from gamutin.editor.assets.widgets.imageselector import ImageSelectorWidget

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
        self.widget_image_source = ImageSelectorWidget()
        self.widget_path_mask_source = pathselector.PathSelector()
        self.label_mask_source = QtWidgets.QLabel("Mask")
        self.combobox_mask_source = QtWidgets.QComboBox()

        self.layout_options = QtWidgets.QGridLayout()
        self.label_colorspace_reference = QtWidgets.QLabel("Reference Gamut")
        self.label_blend_mode = QtWidgets.QLabel("Blend Mode")
        self.label_tolerance = QtWidgets.QLabel("Tolerance")
        self.label_invalid = QtWidgets.QLabel("Invalid Color")
        self.label_valid = QtWidgets.QLabel("Valid Color")
        self.combobox_colorspace_reference = ColorspaceSelector()
        self.combobox_blend_mode = QtWidgets.QComboBox()
        self.slider_tolerance = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.color_invalid = QtWidgets.QPushButton()
        self.color_valid = QtWidgets.QPushButton()

        self.layout_target = QtWidgets.QGridLayout()
        self.checkbox_preview_only = QtWidgets.QCheckBox("Preview Only")
        self.widget_path_target = pathselector.PathSelector()
        self.combobox_colorspace_target = ColorspaceSelector()

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

        self.layout_source.addWidget(self.widget_image_source, 0, 0, 1, -1)
        self.layout_source.addWidget(self.label_mask_source, 1, 0)
        self.layout_source.addWidget(self.combobox_mask_source, 1, 1)
        self.layout_source.addWidget(self.widget_path_mask_source, 2, 0, 1, -1)

        self.layout_target.addWidget(self.checkbox_preview_only, 0, 0)
        self.layout_target.addWidget(self.widget_path_target, 1, 0, 1, -1)
        self.layout_target.addWidget(self.combobox_colorspace_target, 2, 0)

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
        self.widget_image_source.set_expected_file_extensions(SUPPORTED_FILE_EXTENSIONS)
        self.widget_path_target.set_path_type(pathselector.PathType.file)
        self.widget_path_mask_source.set_path_type(pathselector.PathType.file_exist)
        self.checkbox_preview_only.setToolTip(
            "Do not generate a result image on disk. "
            "Instead just preview the result in this application. "
            "<i>(A temporary image will still need to be generated)</i>"
        )
        self.label_mask_source.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed,
        )
        self.layout.setContentsMargins(*(15,) * 4)
        self.layout_source.setContentsMargins(*(25,) * 4)
        self.layout_source.setVerticalSpacing(15)
        self.layout_options.setContentsMargins(*(25,) * 4)
        self.layout_target.setContentsMargins(*(25,) * 4)
        self.combobox_colorspace_reference.set_force_linear_visible(False)
        self.combobox_colorspace_reference.set_force_linear_enable(False)
        self.combobox_colorspace_target.set_label_text("Target Colorspace")
        # 4. Connections
        self.button_launch.clicked.connect(self.start_processing)
        self.combobox_mask_source.currentIndexChanged.connect(self.on_mask_changed)
        self.checkbox_preview_only.stateChanged.connect(self.on_preview_only_toggled)
        return

    def bakeUI(self):
        for combobox in [
            self.combobox_colorspace_reference,
            self.combobox_colorspace_target,
        ]:
            combobox.bakeUI()

        for composite_blend_mode in CompositeBlendModes:
            self.combobox_blend_mode.addItem(
                composite_blend_mode.name,
                composite_blend_mode,
            )

        for mask_option in MaskOptions:
            self.combobox_mask_source.addItem(str(mask_option.value), mask_option)

    def start_processing(self):
        """
        Called by the user to start processing the options to produce the result.
        """
        pass

    def on_mask_changed(self, *args):
        mask_value: MaskOptions = self.combobox_mask_source.currentData()
        self.widget_path_mask_source.setVisible(True)

        if mask_value == MaskOptions.from_alpha:
            self.widget_path_mask_source.setEnabled(False)
        elif mask_value == MaskOptions.none:
            self.widget_path_mask_source.setVisible(False)
        else:
            self.widget_path_mask_source.setEnabled(True)

    def on_preview_only_toggled(self, *args):
        preview_only: bool = self.checkbox_preview_only.isChecked()
        self.widget_path_target.setEnabled(not preview_only)
