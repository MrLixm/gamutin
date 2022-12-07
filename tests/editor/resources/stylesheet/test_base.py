from gamutin.editor.resources.stylesheet import base


def test_parse_variables_simple():

    stylesheet = """
    QWidget{
        color: "{text_white:alpha=0.5}";
        border-radius: "{border_radius_main}";
        font-size: "{font_size_main:scale=0.5:unit=px}";
    }
    """

    result = base.parse_variables(stylesheet)
    assert len(result) == 3

    expected = [
        base.StyleSheetVariable(
            name="text_white",
            overrides={"alpha": "0.5"},
            original_str='"{text_white:alpha=0.5}"',
        ),
        base.StyleSheetVariable(
            name="border_radius_main",
            overrides={},
            original_str='"{border_radius_main}"',
        ),
        base.StyleSheetVariable(
            name="font_size_main",
            overrides={"scale": "0.5", "unit": "px"},
            original_str='"{font_size_main:scale=0.5:unit=px}"',
        ),
    ]
    assert result == expected
    return


def test_parse_variables_duplicated():

    stylesheet = """
    QWidget{
        color: "{text_white:alpha=0.5}";
        border-radius: "{border_radius_main}";
        font-size: "{font_size_main:scale=0.5:unit=px}";
    }
    QPushButton{
         border-radius: "{border_radius_main}";
         border: 2px solid red;
    }
    """

    result = base.parse_variables(stylesheet)
    assert len(result) == 4

    expected = [
        base.StyleSheetVariable(
            name="text_white",
            overrides={"alpha": "0.5"},
            original_str='"{text_white:alpha=0.5}"',
        ),
        base.StyleSheetVariable(
            name="border_radius_main",
            overrides={},
            original_str='"{border_radius_main}"',
        ),
        base.StyleSheetVariable(
            name="font_size_main",
            overrides={"scale": "0.5", "unit": "px"},
            original_str='"{font_size_main:scale=0.5:unit=px}"',
        ),
        base.StyleSheetVariable(
            name="border_radius_main",
            overrides={},
            original_str='"{border_radius_main}"',
        ),
    ]
    assert result == expected
    return
