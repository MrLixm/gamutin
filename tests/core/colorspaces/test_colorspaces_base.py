import colour
import numpy

from gamutin.core import colorspaces


def test_Whitepoint():

    # valid for now, see in the future
    whitepoint = colorspaces.Whitepoint("blank", coordinates=[])

    whitepoint_coord = colour.colorimetry.CCS_ILLUMINANTS[
        "CIE 1931 2 Degree Standard Observer"
    ]["D65"]
    whitepoint = colorspaces.Whitepoint("test d65", coordinates=whitepoint_coord)

    colorspace = colour.RGB_COLOURSPACES["sRGB"]

    whitepoint_srgb = colorspaces.Whitepoint.from_colour_colorspace(colorspace)
    assert numpy.array_equal(whitepoint_srgb.coordinates, whitepoint.coordinates)
    assert whitepoint_srgb.name == "D65"

    whitepoint_list = [
        colorspaces.Whitepoint("test d65", coordinates=whitepoint_coord),
        colorspaces.Whitepoint("test d65", coordinates=whitepoint_coord),
        colorspaces.Whitepoint("test d65", coordinates=whitepoint_coord * 2),
        colorspaces.Whitepoint("test d60", coordinates=whitepoint_coord),
    ]
    assert len(set(whitepoint_list)) == 3


def test_TransferFunctions():

    # valid for now, see in the future
    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        "",
        "",
    )

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=lambda array: array**2,
        decoding=lambda array: array**1 / 2,
    )
    assert transfer_functions.are_linear is False
    assert transfer_functions.is_encoding_linear is False
    assert transfer_functions.is_decoding_linear is False

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=lambda array: array**2,
        decoding=None,
    )
    assert transfer_functions.are_linear is False
    assert transfer_functions.is_encoding_linear is False
    assert transfer_functions.is_decoding_linear is True

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=None,
        decoding=None,
    )
    assert transfer_functions.are_linear is True
    assert transfer_functions.is_encoding_linear is True
    assert transfer_functions.is_decoding_linear is True

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=lambda array: array * 1,
        decoding=None,
        is_encoding_linear=True,
    )
    assert transfer_functions.are_linear is True
    assert transfer_functions.is_encoding_linear is True
    assert transfer_functions.is_decoding_linear is True

    transfer_functions_list = [
        colorspaces.TransferFunctions(
            "CCTF test",
            encoding=lambda array: array**2,
            decoding=lambda array: array**1 / 2,
        ),
        colorspaces.TransferFunctions(
            "CCTF test",
            encoding=lambda array: array**2,
            decoding=lambda array: array**1 / 2,
        ),
    ]
    assert len(set(transfer_functions_list)) == 2

    def temp_decoding_1(array):
        return array**2

    def temp_encoding_1(array):
        return array**1 / 2

    transfer_functions_list = [
        colorspaces.TransferFunctions(
            "CCTF test",
            encoding=temp_encoding_1,
            decoding=temp_decoding_1,
        ),
        colorspaces.TransferFunctions(
            "CCTF test",
            encoding=temp_encoding_1,
            decoding=temp_decoding_1,
        ),
    ]
    assert len(set(transfer_functions_list)) == 1

    transfer_functions_list = [
        colorspaces.TransferFunctions(
            "CCTF test",
            encoding=temp_encoding_1,
            decoding=temp_decoding_1,
            is_encoding_linear=True,
        ),
        colorspaces.TransferFunctions(
            "CCTF test",
            encoding=temp_encoding_1,
            decoding=temp_decoding_1,
        ),
    ]
    assert len(set(transfer_functions_list)) == 2


def test_RgbColorspace_fromColour():

    colour_colorspace: colour.RGB_Colourspace = colour.RGB_COLOURSPACES["sRGB"]

    colorspace = colorspaces.RgbColorspace.from_colour_colorspace(
        colour_colorspace,
        categories=(colorspaces.ColorspaceCategory.common,),
    )

    assert colorspace.name == "sRGB"
    assert colorspace.categories == (colorspaces.ColorspaceCategory.common,)
    assert colorspace.description == colour_colorspace.__doc__
    numpy.testing.assert_array_equal(
        colorspace.gamut.matrix_to_XYZ,
        colour_colorspace.matrix_RGB_to_XYZ,
    )
    numpy.testing.assert_array_equal(
        colorspace.gamut.matrix_from_XYZ,
        colour_colorspace.matrix_XYZ_to_RGB,
    )
    assert colorspace.gamut.matrix_from_XYZ is not colour_colorspace.matrix_XYZ_to_RGB

    numpy.testing.assert_array_equal(
        colorspace.whitepoint.coordinates,
        colour_colorspace.whitepoint,
    )
    assert colorspace.whitepoint.coordinates is not colour_colorspace.whitepoint

    colorspace = colorspaces.RgbColorspace.from_colour_colorspace(
        colour_colorspace,
        categories=tuple(),
        description="test description",
    )
    assert colorspace.description == "test description"


def test_RgbColorspace():

    try:
        colorspace = colorspaces.RgbColorspace("test fail")
    except TypeError:
        pass
    else:
        raise AssertionError("Exception not raised.")

    colorspace = colorspaces.RgbColorspace("test null", None, None, None, tuple(), "")
    assert colorspace.is_no_op is True

    # some test data

    def temp_decoding_1(array):
        return array**2

    def temp_encoding_1(array):
        return array**1 / 2

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=temp_encoding_1,
        decoding=temp_decoding_1,
    )

    gamut_identity = colorspaces.ColorspaceGamut(
        "identity gamut",
        numpy.identity(3),
        numpy.identity(3),
    )

    gamut_1 = colorspaces.ColorspaceGamut(
        "gamut 1",
        numpy.identity(3) + 0.3,
        numpy.identity(3) + 0.3,
    )

    whitepoint = colorspaces.Whitepoint(
        "test illuminant",
        numpy.array([1 / 3, 1 / 3, 1 / 3]),
    )

    colorspace = colorspaces.RgbColorspace("test null", None, None, None, tuple(), "")
    assert colorspace.is_no_op is True

    colorspace = colorspaces.RgbColorspace(
        "test null",
        gamut=gamut_identity,
        whitepoint=None,
        transfer_functions=None,
        categories=tuple(),
        description="",
    )
    assert colorspace.is_no_op is True

    colorspace = colorspaces.RgbColorspace(
        "test null",
        gamut=gamut_1,
        whitepoint=None,
        transfer_functions=None,
        categories=tuple(),
        description="",
    )
    assert colorspace.is_no_op is False

    colorspace = colorspaces.RgbColorspace(
        "test null",
        gamut=None,
        whitepoint=whitepoint,
        transfer_functions=None,
        categories=tuple(),
        description="",
    )
    assert colorspace.is_no_op is False

    colorspace = colorspaces.RgbColorspace(
        "test null",
        gamut=None,
        whitepoint=None,
        transfer_functions=transfer_functions,
        categories=tuple(),
        description="",
    )
    assert colorspace.is_no_op is False


def test_RgbColorspace_copy():
    def temp_decoding_1(array):
        return array**2

    def temp_encoding_1(array):
        return array**1 / 2

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=temp_encoding_1,
        decoding=temp_decoding_1,
    )

    gamut_1 = colorspaces.ColorspaceGamut(
        "gamut 1",
        numpy.identity(3) + 0.3,
        numpy.identity(3) + 0.3,
    )

    whitepoint = colorspaces.Whitepoint(
        "test illuminant",
        numpy.array([1 / 3, 1 / 3, 1 / 3]),
    )

    colorspace = colorspaces.RgbColorspace(
        "test null",
        gamut=gamut_1,
        whitepoint=whitepoint,
        transfer_functions=transfer_functions,
        categories=tuple(),
        description="",
    )

    colorspace_copy = colorspace.copy()
    assert colorspace_copy is not colorspace
    assert colorspace == colorspace_copy
    assert colorspace.gamut.matrix_from_XYZ is not colorspace_copy.gamut.matrix_from_XYZ
    assert (
        colorspace.whitepoint.coordinates is not colorspace_copy.whitepoint.coordinates
    )
    numpy.testing.assert_array_equal(
        colorspace.whitepoint.coordinates, colorspace_copy.whitepoint.coordinates
    )
    assert (
        colorspace.transfer_functions.decoding
        is colorspace_copy.transfer_functions.decoding
    )
    assert (
        colorspace.transfer_functions.encoding
        is colorspace_copy.transfer_functions.encoding
    )


def test_RgbColorspace_hashing():
    def temp_decoding_1(array):
        return array**2

    def temp_encoding_1(array):
        return array**1 / 2

    transfer_functions = colorspaces.TransferFunctions(
        "CCTF test",
        encoding=temp_encoding_1,
        decoding=temp_decoding_1,
    )

    gamut_1 = colorspaces.ColorspaceGamut(
        "gamut 1",
        numpy.identity(3) + 0.3,
        numpy.identity(3) + 0.3,
    )

    whitepoint = colorspaces.Whitepoint(
        "test illuminant",
        numpy.array([1 / 3, 1 / 3, 1 / 3]),
    )

    colorspace_list = [
        colorspaces.RgbColorspace(
            "test A",
            gamut=gamut_1,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            categories=tuple(),
            description="",
        ),
        colorspaces.RgbColorspace(
            "test A",
            gamut=gamut_1,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            categories=tuple(),
            description="",
        ),
    ]
    assert len(set(colorspace_list)) == 1

    colorspace_list = [
        colorspaces.RgbColorspace(
            "test A",
            gamut=gamut_1,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            categories=tuple(),
            description="",
        ),
        colorspaces.RgbColorspace(
            "test B",
            gamut=gamut_1,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            categories=tuple(),
            description="",
        ),
    ]
    assert len(set(colorspace_list)) == 2

    colorspace_list = [
        colorspaces.RgbColorspace(
            "test A",
            gamut=gamut_1,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            categories=tuple(),
            description="",
        ),
        colorspaces.RgbColorspace(
            "test A",
            gamut=gamut_1,
            whitepoint=whitepoint,
            transfer_functions=transfer_functions,
            categories=tuple(),
            description="test",
        ),
    ]
    assert len(set(colorspace_list)) == 2
