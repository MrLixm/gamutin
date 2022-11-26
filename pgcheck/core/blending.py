import enum
from typing import Optional

import numpy


class BlendModes(enum.Enum):

    over = "over"
    add = "add"
    multiply = "multiply"

    @classmethod
    def __all__(cls):
        return [item for item in cls]


def blend_arrays(
    array_b: numpy.ndarray,
    array_a: numpy.ndarray,
    blend_mode: BlendModes,
    mask: Optional[numpy.ndarray] = None,
):
    """

    Args:
        array_b: bottom layer
        array_a: top layer
        blend_mode: blend operation to use
        mask: amount of array_a to use

    Returns:
        a single array , result of the blending of b and a
    """

    if array_a.shape != array_b.shape:
        raise ValueError(
            f"array_b doesn't have the same shape as array_a : "
            f"{array_a.shape=} != {array_b.shape=}"
        )
    if mask is not None and mask.shape != array_b.shape:
        raise ValueError(
            f"mask doesn't have the same shape as array_b : "
            f"{mask.shape=} != {array_b.shape=}"
        )

    if blend_mode == BlendModes.over:
        if mask is not None:
            return array_b * (1.0 - mask) + array_a * mask
        return array_a

    elif blend_mode == BlendModes.add:
        if mask is not None:
            return array_b + array_a * mask
        return array_b + array_a

    elif blend_mode == BlendModes.multiply:
        if mask is not None:
            return array_b * (array_a * mask)
        return array_b * array_a

    else:
        raise ValueError(
            f"Unsupported blend mode {blend_mode}. Expected one of {BlendModes.__all__()}"
        )
