import enum
from typing import Optional

import colour
import numpy

from .blending import blend_arrays
from .blending import BlendModes


class CompositeBlendModes(enum.Enum):

    over = "over"
    invalid_replace = "invalid_replace"
    add = "add"
    multiply = "multiply"

    @classmethod
    def __all__(cls):
        return [item for item in cls]


def transform_out_of_pg_values(
    input_array: numpy.ndarray,
    input_colorspace: colour.RGB_Colourspace,
    invalid_color: tuple[float, float, float],
    valid_color: Optional[tuple[float, float, float]],
    tolerance_amount: float,
    blend_mode: CompositeBlendModes,
) -> numpy.ndarray:
    """

    Args:
        input_array:
        input_colorspace: colorspace encoding of input_array
        invalid_color: color to use for out of pointer's gamut values
        valid_color: color to use for inside of pointer's gamut values. If none just keep the orignal values.
        tolerance_amount: higher means less chance of being flag as invalid
        blend_mode: blending operation to use for invalid/valid values

    Returns:
        input_array values modified using invalid_color and valid_color
    """

    intermediate_array = input_colorspace.cctf_decoding(input_array)
    intermediate_array = colour.RGB_to_XYZ(
        intermediate_array,
        input_colorspace.whitepoint,
        colour.models.CCS_ILLUMINANT_POINTER_GAMUT,
        input_colorspace.matrix_RGB_to_XYZ,
    )
    result_array = colour.is_within_pointer_gamut(intermediate_array, tolerance_amount)
    result_array = result_array.astype(numpy.int_)

    output_array = input_array.copy()

    output_array[result_array != 1] = invalid_color  # Out of PG
    if valid_color is not None and blend_mode != CompositeBlendModes.invalid_replace:
        output_array[result_array == 1] = valid_color  # In PG:

    if blend_mode == CompositeBlendModes.invalid_replace:
        pass  # already good !

    elif blend_mode == CompositeBlendModes.over:
        pass  # already good !

    elif blend_mode == CompositeBlendModes.add:
        output_array = blend_arrays(
            array_b=input_array,
            array_a=output_array,
            blend_mode=BlendModes.add,
        )

    elif blend_mode == CompositeBlendModes.multiply:
        output_array = blend_arrays(
            array_b=input_array,
            array_a=output_array,
            blend_mode=BlendModes.multiply,
        )

    else:
        raise ValueError(
            f"Unsupported blend mode {blend_mode}. "
            f"Expected one of {CompositeBlendModes.__all__()}"
        )

    return output_array
