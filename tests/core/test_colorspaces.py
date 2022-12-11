from colour.models import linear_function

from gamutin.core import colorspaces


def test_get_colorspace():

    result_a = colorspaces.get_colorspace("srgb")
    result_b = colorspaces.get_colorspace("sRGB")
    assert result_a
    assert result_b
    assert result_a is result_b

    result_a = colorspaces.get_colorspace("Adobe RGB (1998)")
    result_b = colorspaces.get_colorspace("adobe-rgb-1998")
    assert result_a
    assert result_b
    assert result_a is result_b

    result_a = colorspaces.get_colorspace("DCI-P3+")
    result_b = colorspaces.get_colorspace("dci-p3+")
    assert result_a
    assert result_b
    assert result_a is result_b

    return


def test_get_colorspace_linear():

    result = colorspaces.get_colorspace("srgb")
    assert result.transfer_functions != colorspaces.TRANSFER_FUNCTIONS_LINEAR

    result = colorspaces.get_colorspace("srgb:linear")
    assert result.transfer_functions == colorspaces.TRANSFER_FUNCTIONS_LINEAR

    result = colorspaces.get_colorspace("DCI-P3+")
    assert result.transfer_functions != colorspaces.TRANSFER_FUNCTIONS_LINEAR

    result = colorspaces.get_colorspace("DCI-P3+:linear")
    assert result.transfer_functions == colorspaces.TRANSFER_FUNCTIONS_LINEAR
