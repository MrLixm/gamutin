import numpy
from numpy import array_equal

from pgcheck.core import pointergamut
from pgcheck.core import colorspaces


def test_main():

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
    colorspace = colorspaces.get_colorspace("sRGB Linear")

    array_result = pointergamut.transform_out_of_pg_values(
        input_array=array_source,
        input_colorspace=colorspace,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=pointergamut.CompositeBlendModes.invalid_replace,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[1.0, 0.0, 0.0], [0.5, 0.1, 0.3]],
            [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert array_equal(array_expected, array_result)

    array_result = pointergamut.transform_out_of_pg_values(
        input_array=array_source,
        input_colorspace=colorspace,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=pointergamut.CompositeBlendModes.over,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert array_equal(array_expected, array_result)

    array_result = pointergamut.transform_out_of_pg_values(
        input_array=array_source,
        input_colorspace=colorspace,
        invalid_color=(0.99, 0.0, 0.0),
        valid_color=(0.0, 0.66, 0.0),
        tolerance_amount=0.0,
        blend_mode=pointergamut.CompositeBlendModes.over,
        mask=None,
    )
    array_expected = numpy.array(
        [
            [[0.99, 0.0, 0.0], [0.0, 0.66, 0.0]],
            [[0.99, 0.0, 0.0], [0.99, 0.0, 0.0]],
        ]
    )
    assert array_equal(array_expected, array_result)

    array_result = pointergamut.transform_out_of_pg_values(
        input_array=array_source,
        input_colorspace=colorspace,
        invalid_color=(1.0, 0.0, 0.0),
        valid_color=(0.0, 0.0, 0.0),
        tolerance_amount=0.0,
        blend_mode=pointergamut.CompositeBlendModes.over,
        mask=array_mask,
    )
    array_expected = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert array_equal(array_expected, array_result)
