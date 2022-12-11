import numpy
from numpy.testing import assert_array_equal

from gamutin.core import gamut
from gamutin.core import colorspaces


def test_pointer_gamut():

    array_source = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [0.233, -0.1, 0.15]],
        ]
    )
    array_mask = numpy.array(
        [
            [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]],
        ]
    )
    colorspace = colorspaces.get_colorspace("sRGB:linear")

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspaces.POINTER_GAMUT_COLORSPACE,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.invalid_replace,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[1.0, 0.0, 0.0], [0.5, 0.1, 0.3]],
            [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert_array_equal(array_expected, array_result)

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspaces.POINTER_GAMUT_COLORSPACE,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.over,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert_array_equal(array_expected, array_result)

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspaces.POINTER_GAMUT_COLORSPACE,
        invalid_color=(0.99, 0.0, 0.0),
        valid_color=(0.0, 0.66, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.over,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[0.99, 0.0, 0.0], [0.0, 0.66, 0.0]],
            [[0.99, 0.0, 0.0], [0.99, 0.0, 0.0]],
        ]
    )
    assert_array_equal(array_expected, array_result)

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspaces.POINTER_GAMUT_COLORSPACE,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.over,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=array_mask,
    )
    array_expected = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert_array_equal(array_expected, array_result)

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspaces.POINTER_GAMUT_COLORSPACE,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.add,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=array_mask,
    )
    array_expected = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [1.233, -0.1, 0.15]],
        ]
    )
    assert_array_equal(array_expected, array_result)


def test_transform_out_of_gamut_values():

    test_data_list = [
        # defined as: array, input_colorspace, ref_colorspace, is_invalid
        (numpy.array([1.0, 1.0, 0.0]), "itu-r-bt.2020:linear", "sRGB", True),
        (numpy.array([1.0, 1.0, 0.0]), "itu-r-bt.2020:linear", "sRGB:linear", True),
        (numpy.array([0.0, 1.0, 0.0]), "itu-r-bt.2020:linear", "sRGB", True),
        (numpy.array([0.0, 0.0, 1.0]), "itu-r-bt.2020:linear", "sRGB", True),
        (numpy.array([0.0, 0.0, 1.0]), "sRGB:linear", "itu-r-bt.2020:linear", False),
        (numpy.array([0.0, 0.0, 1.0]), "sRGB:linear", "itu-r-bt.2020", False),
    ]

    for test_data in test_data_list:

        colorspace = colorspaces.get_colorspace(test_data[1])
        reference_colorspace = colorspaces.get_colorspace(test_data[2])

        array_result = gamut.transform_out_of_gamut_values(
            input_array=test_data[0],
            input_colorspace=colorspace,
            reference_colorspace=reference_colorspace,
            invalid_color=(0.987, 0.0, 0.0),
            valid_color=(0.033, 0.033, 0.033),
            tolerance_amount=0.0,
            blend_mode=gamut.CompositeBlendModes.over,
            chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
            mask=None,
        )
        if test_data[3]:
            array_expected = numpy.array([0.987, 0.0, 0.0])
        else:
            array_expected = numpy.array((0.033, 0.033, 0.033))

        assert_array_equal(array_expected, array_result)


def test_null_colorspace():

    array_source = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [0.233, -0.1, 0.15]],
        ]
    )
    colorspace = colorspaces.get_colorspace("passthrough")
    assert colorspace

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspaces.POINTER_GAMUT_COLORSPACE,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.invalid_replace,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
            [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert_array_equal(array_expected, array_result)

    array_result = gamut.transform_out_of_gamut_values(
        input_array=array_source,
        input_colorspace=colorspace,
        reference_colorspace=colorspace,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=gamut.CompositeBlendModes.invalid_replace,
        chromatic_adaptation_transform=colorspaces.ChromaticAdaptationTransform.default,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert_array_equal(array_expected, array_result)
    assert array_source is not array_result
