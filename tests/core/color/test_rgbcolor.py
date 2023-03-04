import numpy
from numpy.testing import assert_allclose
from numpy.testing import assert_array_equal

from gamutin.core.colorspaces import sRGB_COLORSPACE
from gamutin.core.color import RGBData


COLOR_DATASET = {
    0: {
        "float": (0.5, 0.2, 0.3),
        "8bit": (128, 51, 76),
        "floatFrom8": (0.5, 0.2, 0.3),
        "hex": "#80334C",
    },
    1: {
        "float": (1, 0.3, 0.3),
        "8bit": (255, 76, 76),
        "floatFrom8": (1, 0.3, 0.3),
        "hex": "#ff4c4c",
    },
    2: {
        "float": (0.766, -0.1, 0.15),
        "8bit": (195, 0, 38),
        "floatFrom8": (0.766, 0, 0.15),
        "hex": "#C30026",
    },
    3: {
        "float": (2, -0.333, 0),
        "8bit": (255, 0, 0),
        "floatFrom8": (1, 0, 0),
        "hex": "#FF0000",
    },
    4: {
        "float": (0.005, 0.456, 0.9999),
        "8bit": (1, 116, 255),
        "floatFrom8": (0.005, 0.456, 0.9999),
        "hex": "#0174FF",
    },
}


def test_RGBData_init():
    # none should raise error
    color = RGBData(0.1, 0.5, 0.2, sRGB_COLORSPACE, 0.6)
    color = RGBData(-0.1, 0.5, 1.2, sRGB_COLORSPACE, -0.5)
    color = RGBData(-0.1, 0.5, 1.2, sRGB_COLORSPACE, None)
    color = RGBData(*(-0.1, 0.5, 1.2), sRGB_COLORSPACE, None)
    color = RGBData(-0.1, 0.5, 1.2, "this is possible")


def test_RGBData_prop():
    colorValue = (0.12, 1.896, 0.3)

    color = RGBData(*colorValue, sRGB_COLORSPACE)

    assert colorValue[0] == color.red
    assert colorValue[0] == color.r
    assert colorValue[1] == color.green
    assert colorValue[1] == color.g
    assert colorValue[2] == color.blue
    assert colorValue[2] == color.b
    assert None is color.alpha
    assert None is color.a

    colorValue = COLOR_DATASET[3]["float"]

    color = RGBData(*colorValue, sRGB_COLORSPACE, 0.33)

    assert colorValue[0] == color.red
    assert colorValue[0] == color.r
    assert colorValue[1] == color.green
    assert colorValue[1] == color.g
    assert colorValue[2] == color.blue
    assert colorValue[2] == color.b
    assert 0.33 == color.alpha
    assert 0.33 == color.a


def test_RGBData_classMethod_8bit():
    tolerance = 0.002

    for color_dataset in COLOR_DATASET.values():
        color_8bit = color_dataset["8bit"]
        expected = color_dataset["floatFrom8"]

        color = RGBData.from8Bit(*color_8bit, alpha=None)
        assert_allclose(expected[0], color.red, atol=tolerance)
        assert_allclose(expected[0], color.r, atol=tolerance)
        assert_allclose(expected[1], color.green, atol=tolerance)
        assert_allclose(expected[1], color.g, atol=tolerance)
        assert_allclose(expected[2], color.blue, atol=tolerance)
        assert_allclose(expected[2], color.b, atol=tolerance)
        assert None is color.alpha
        assert None is color.a


def test_RGBData_classMethod_hex():
    tolerance = 0.002

    for color_dataset in COLOR_DATASET.values():
        color_floatFrom8 = color_dataset["floatFrom8"]
        color_hex = color_dataset["hex"]

        color = RGBData.fromHex(color_hex, alpha=0.33)
        assert_allclose(color_floatFrom8[0], color.red, atol=tolerance)
        assert_allclose(color_floatFrom8[0], color.r, atol=tolerance)
        assert_allclose(color_floatFrom8[1], color.green, atol=tolerance)
        assert_allclose(color_floatFrom8[1], color.g, atol=tolerance)
        assert_allclose(color_floatFrom8[2], color.blue, atol=tolerance)
        assert_allclose(color_floatFrom8[2], color.b, atol=tolerance)
        assert 0.33 is color.alpha
        assert 0.33 is color.a


def test_RGBData_classMethod_array():
    array = numpy.array(COLOR_DATASET[3]["float"])
    color = RGBData.fromArray(array, sRGB_COLORSPACE)
    assert array[0] == color.red
    assert array[0] == color.r
    assert array[1] == color.green
    assert array[1] == color.g
    assert array[2] == color.blue
    assert array[2] == color.b
    assert None == color.alpha
    assert None == color.a

    array = numpy.array(COLOR_DATASET[3]["float"])
    array = numpy.append(array, 0.2)
    color = RGBData.fromArray(array, sRGB_COLORSPACE)
    assert array[0] == color.red
    assert array[0] == color.r
    assert array[1] == color.green
    assert array[1] == color.g
    assert array[2] == color.blue
    assert array[2] == color.b
    assert 0.2 == color.alpha
    assert 0.2 == color.a


def test_RGBData_toArray():
    array = numpy.array(COLOR_DATASET[3]["float"])
    color = RGBData.fromArray(array, sRGB_COLORSPACE)
    result = color.toArray(alpha=False)
    assert_array_equal(result, array)

    array = numpy.array(COLOR_DATASET[3]["float"])
    expected = numpy.append(array, 0.36)
    color = RGBData.fromArray(array, sRGB_COLORSPACE)
    result = color.toArray(alpha=0.36)
    assert_array_equal(result, expected)

    array = numpy.array(COLOR_DATASET[3]["float"])
    array = numpy.append(array, 0.2)
    color = RGBData.fromArray(array, sRGB_COLORSPACE)
    result = color.toArray()
    assert_array_equal(result, array)


def test_RGBData_toTuple():
    for color_dataset in COLOR_DATASET.values():
        color_float = color_dataset["float"]
        expected = (*color_float, 0.44)

        color = RGBData(*color_float, sRGB_COLORSPACE, 0.44)
        assert color.toTupleFloat() == expected


def test_RGBData_toHex():
    for index, dataset in COLOR_DATASET.items():
        source = dataset["float"]
        expected = dataset["hex"].lower()

        color = RGBData(*source, sRGB_COLORSPACE, 0.44)
        result = color.toHex()
        assert result == expected


def test_RGBData_to8Bit():
    for index, dataset in COLOR_DATASET.items():
        source = dataset["float"]
        expected = dataset["8bit"]

        color = RGBData(*source, sRGB_COLORSPACE, 0.44)
        result = color.to8Bit(alpha=False)
        assert result == expected
        expected = (*expected, 0.44)
        result = color.to8Bit(alpha=True)
        assert result == expected
