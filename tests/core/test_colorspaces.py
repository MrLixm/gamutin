from pgcheck.core import colorspaces


def test_get_colorspace():

    result_a = colorspaces.get_colorspace("srgb")
    result_b = colorspaces.get_colorspace("sRGB")
    assert result_a
    assert result_b
    assert result_a is result_b

    result_a = colorspaces.get_colorspace("Adobe RGB (1998) Linear")
    result_b = colorspaces.get_colorspace("adobe-rgb-1998-linear")
    assert result_a
    assert result_b
    assert result_a is result_b

    result_a = colorspaces.get_colorspace("DCI-P3+")
    result_b = colorspaces.get_colorspace("dci-p3+")
    assert result_a
    assert result_b
    assert result_a is result_b

    return
