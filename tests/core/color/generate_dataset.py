__all__ = ("",)

import logging

import OpenImageIO as oiio
import numpy

logger = logging.getLogger(__name__)


def float_to_uint8(source):
    image_spec = oiio.ImageSpec(1, 1, 3, oiio.FLOAT)
    image_buf = oiio.ImageBuf(image_spec)
    image = numpy.array([[source]], dtype=numpy.float32)
    image_buf.set_pixels(oiio.ROI.All, image)

    return image_buf.get_pixels(format=oiio.UINT8)


def uint8_to_float(source):
    image_spec = oiio.ImageSpec(1, 1, 3, oiio.UINT8)
    image_buf = oiio.ImageBuf(image_spec)
    image = numpy.array([[source]], dtype=numpy.uint8)
    image_buf.set_pixels(oiio.ROI.All, image)

    return image_buf.get_pixels(format=oiio.FLOAT)


def print_dataset():
    SOURCE_DATASET_FLOAT = [
        [0.0, 0.0, 0.0],
        [1.0, 1.0, 1.0],
        [1.1, 0.5, 0.3],
        [-0.322, 0.1, 0.9999],
        [1.0, -0.000001, 1 / 3],
    ]

    SOURCE_DATASET_UINT8 = [
        [255, 255, 255],
        [0, 0, 0],
        [255, 126, 0],
        [0, 1, 0],
        [128, 127, 126],
    ]

    indent = " " * 4

    print(f'{{\n{indent}"float_to_uint8": [')
    for source in SOURCE_DATASET_FLOAT:
        result = float_to_uint8(source)

        result_str = numpy.array2string(result[0][0], separator=",")
        print(f'{indent*2}{{"source":{source}, "expected": {result_str}}},')
    print("    ],")

    print(f'{indent}"uint8_to_float": [')
    for source in SOURCE_DATASET_UINT8:
        result = uint8_to_float(source)

        result_str = numpy.array2string(result[0][0], separator=",")
        print(f'{indent*2}{{"source":{source}, "expected": {result_str}}},')
    print("    ],")
    print("}")


if __name__ == "__main__":
    print_dataset()
