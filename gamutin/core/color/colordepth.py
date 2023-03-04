__all__ = (
    "convert8bitToFloat",
    "convertFloatTo8Bit",
)

import logging

import numpy

logger = logging.getLogger(__name__)


def convert8bitToFloat(source: numpy.ndarray):
    """
    Convert a 8bit RGB color to floating point encoding.

    Args:
        source: arbitrary length array of integers

    Returns:
        new array of the same length as float encoding
    """
    return numpy.asarray(source / 255, dtype=numpy.core.float64)


def convertFloatTo8Bit(source: numpy.ndarray):
    """
    Convert a floating point array of color values to 8bit integer encoding.

    Args:
        source: arbitrary length array of floats

    Returns:
       new  array of the same length as 8bit encoding
    """
    return numpy.asarray(
        numpy.around(numpy.clip(source, 0, 1) * 255),
        dtype=numpy.core.uint8,
    )
