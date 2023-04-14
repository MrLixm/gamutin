import time
import numpy
from numpy.testing import assert_array_equal

from gamutin.core.colorspaces import get_colorspace
from gamutin.core.color import LCHabColor
from gamutin.core.color import RGBAData

COLORSPACE_A = get_colorspace("sRGB")
assert COLORSPACE_A
COLORSPACE_B = get_colorspace("ACES2065-1")
assert COLORSPACE_B
COLORSPACE_C = get_colorspace("DCI-P3")
WHITEPOINT_A = COLORSPACE_A.whitepoint
assert WHITEPOINT_A
WHITEPOINT_B = COLORSPACE_B.whitepoint
assert WHITEPOINT_B


COLOR_DATASET = {
    0: {
        "LCHab": (150.3, 30.2, 10.005),
    },
    1: {
        "LCHab": (0, 0, 0),
    },
    2: {
        "LCHab": (360, 100, 100),
    },
    3: {
        "LCHab": (365, 22.3, 100),
    },
    4: {
        "LCHab": (-0.5, 0.456, 50),
    },
}


def test_LCHabColor_init():
    # none should raise error
    LCHabColor(0.1, 0.5, 0.2, 0.6)
    LCHabColor(-0.1, 0.5, 1.2, -0.5)
    LCHabColor(-0.1, 0.5, 1.2, None)
    LCHabColor(*(-0.1, 0.5, 1.2), None)
    LCHabColor(-0.1, 0.5, 1.2)


def test_LCHabColor_prop():
    colorValue = (0.12, 1.896, 0.3)

    color = LCHabColor(*colorValue)

    assert colorValue[0] == color.L
    assert colorValue[1] == color.C
    assert colorValue[2] == color.Hab
    assert None is color.alpha
    assert None is color.a

    colorValue = COLOR_DATASET[3]["LCHab"]

    color = LCHabColor(*colorValue, 0.33)

    assert colorValue[0] == color.L
    assert colorValue[1] == color.C
    assert colorValue[2] == color.Hab
    assert 0.33 == color.alpha
    assert 0.33 == color.a


def test_LCHabColor_classMethod_array():
    array = numpy.array(COLOR_DATASET[3]["LCHab"])
    color = LCHabColor.from_array(array)
    assert array[0] == color.L
    assert array[1] == color.C
    assert array[2] == color.Hab
    assert None is color.alpha
    assert None is color.a

    array = numpy.array(COLOR_DATASET[3]["LCHab"])
    array = numpy.append(array, 0.2)
    color = LCHabColor.from_array(array)
    assert array[0] == color.L
    assert array[1] == color.C
    assert array[2] == color.Hab
    assert 0.2 == color.alpha
    assert 0.2 == color.a


def test_LCHabColor_to_array():
    array = numpy.array(COLOR_DATASET[3]["LCHab"], dtype=numpy.float32)
    color = LCHabColor.from_array(array)
    result = color.to_array(alpha=False)
    assert_array_equal(result, array)

    array = numpy.array(COLOR_DATASET[3]["LCHab"])
    expected = numpy.append(array, 0.36).astype(numpy.float32)
    color = LCHabColor.from_array(array)
    result = color.to_array(alpha=0.36)
    assert_array_equal(result, expected)

    array = numpy.array(COLOR_DATASET[3]["LCHab"], dtype=numpy.float32)
    array = numpy.append(array, 0.2).astype(numpy.float32)
    color = LCHabColor.from_array(array)
    result = color.to_array()
    assert_array_equal(result, array)


def test_LCHabColor_to_tuple():
    for color_dataset in COLOR_DATASET.values():
        color_float = color_dataset["LCHab"]
        expected = (*color_float, 0.44)

        color = LCHabColor(*color_float, 0.44)
        assert color.to_float() == expected


def test_LCHabColor_eq():
    colorA = LCHabColor(0.356, 0.12, -0.1, 0.33)
    colorB = LCHabColor(0.356, 0.12, -0.1, None)
    colorC = LCHabColor(0.356, 0.12, -0.1, 0.33)

    assert colorA == colorC
    assert colorB != colorC
    assert colorA != colorB


def test_LCHabColor_copy():
    for index, dataset in COLOR_DATASET.items():
        source = dataset["LCHab"]
        color = LCHabColor(*source, 0.44)
        color_copy = color.copy()
        assert color == color_copy
        assert color is not color_copy


def test_to_Rgba():
    # TODO improve with proper values testing
    colorA = LCHabColor(0.356, 0.12, -0.1, 0.33)
    rgba = colorA.to_Rgba(COLORSPACE_B)
    assert isinstance(rgba, RGBAData)

    run_times = []
    for index in range(20):
        start_time = time.time()
        colorA = LCHabColor(0.356, 0.12, -0.1, 0.33)
        colorA.to_Rgba(COLORSPACE_B)
        run_times.append(time.time() - start_time)

    average_time = sum(run_times) / len(run_times)
    print(f"conversion to_Rgba average in {average_time}s")
