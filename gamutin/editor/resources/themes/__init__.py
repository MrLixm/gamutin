from gamutin.editor.resources.stylesheet import StyleTheme
from gamutin.editor.resources.stylesheet import ColorQtProperty
from gamutin.editor.resources.stylesheet import LengthQtProperty


class DefaultStyleTheme(StyleTheme):
    """
    Library of variables to use in StyleSheet.
    """

    @classmethod
    def get_name(cls) -> str:
        return "default"

    color_text_base = ColorQtProperty((250, 250, 250, 255))
    color_error_red = ColorQtProperty((187, 76, 76, 255))
    size_border_radius_base = LengthQtProperty(4)
