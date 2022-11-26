import numpy
from numpy import array_equal

from pgcheck.core import blending


def test_basic():

    array_b = numpy.array([0.5, 0.1, 0.3])
    array_a = numpy.array([1.0, 0.0, 0.2])

    array_result = blending.blend_arrays(
        array_b=array_b,
        array_a=array_a,
        blend_mode=blending.BlendModes.add,
        mask=None,
    )
    assert array_equal(array_result, numpy.array([1.5, 0.1, 0.5]))

    array_result = blending.blend_arrays(
        array_b=array_b,
        array_a=array_a,
        blend_mode=blending.BlendModes.multiply,
        mask=None,
    )
    assert array_equal(array_result, numpy.array([0.5, 0.0, 0.06]))

    array_result = blending.blend_arrays(
        array_b=array_b,
        array_a=array_a,
        blend_mode=blending.BlendModes.over,
        mask=None,
    )
    assert array_equal(array_result, array_a)


def test_mask():

    array_b = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [0.233, -0.1, 0.15]],
        ]
    )
    array_a = numpy.array(
        [
            [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    array_mask = numpy.array(
        [
            [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]],
        ]
    )

    array_result = blending.blend_arrays(
        array_b=array_b,
        array_a=array_a,
        blend_mode=blending.BlendModes.over,
        mask=array_mask,
    )
    array_result_expected = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
        ]
    )
    assert array_equal(array_result, array_result_expected)

    array_result = blending.blend_arrays(
        array_b=array_b,
        array_a=array_a,
        blend_mode=blending.BlendModes.add,
        mask=array_mask,
    )
    array_result_expected = numpy.array(
        [
            [[0.0, 1.0, 0.0], [0.5, 0.1, 0.3]],
            [[0.0, 0.0, 0.0], [1.233, -0.1, 0.15]],
        ]
    )
    assert array_equal(array_result, array_result_expected)
