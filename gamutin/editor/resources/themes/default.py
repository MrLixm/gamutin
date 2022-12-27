from .base import BaseStyleTheme
from gamutin.editor.resources.stylesheet import ColorQtProperty
from gamutin.editor.resources.stylesheet import LengthQtProperty
from gamutin.editor.resources.stylesheet import LiteralQtProperty


class DefaultStyleTheme(BaseStyleTheme):
    """
    Library of variables to use in StyleSheet.
    """

    @classmethod
    def get_name(cls) -> str:
        return "default"

    # colors
    color_app_primary = ColorQtProperty((201, 229, 119, 255))
    color_text_base = ColorQtProperty((250, 250, 250, 255))
    color_error_red = ColorQtProperty((187, 76, 76, 255))
    color_notification = ColorQtProperty((224, 57, 57, 255))

    # sizes
    size_border_radius_base = LengthQtProperty(4)
    size_min_height_default = LengthQtProperty(20)
    size_padding_default = LengthQtProperty(5)

    # variables: simple search and replace
    # TODO this is not really part of the theme ...
    var_drop_state = LiteralQtProperty("dropState")
    var_error_state = LiteralQtProperty("errorState")
    var_error_text_colored = LiteralQtProperty("errorTextColored")
    var_error_frame = LiteralQtProperty("errorFrame")
