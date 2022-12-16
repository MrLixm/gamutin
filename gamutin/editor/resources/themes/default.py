from .base import BaseStyleTheme
from gamutin.editor.resources.stylesheet import ColorQtProperty
from gamutin.editor.resources.stylesheet import LengthQtProperty


class DefaultStyleTheme(BaseStyleTheme):
    """
    Library of variables to use in StyleSheet.
    """

    @classmethod
    def get_name(cls) -> str:
        return "default"

    app_primary = ColorQtProperty((201, 229, 119, 255))
    color_text_base = ColorQtProperty((250, 250, 250, 255))
    color_error_red = ColorQtProperty((187, 76, 76, 255))
    size_border_radius_base = LengthQtProperty(4)
