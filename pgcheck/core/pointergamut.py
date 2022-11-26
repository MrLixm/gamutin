from typing import Optional

import colour
import numpy


def transform_out_of_pg_values(
    input_array: numpy.ndarray,
    input_colorspace: colour.RGB_Colourspace,
    invalid_color: tuple[float, float, float],
    valid_color: Optional[tuple[float, float, float]],
    tolerance_amount: float,
) -> numpy.ndarray:
    """

    Args:
        input_array:
        input_colorspace: colorspace encoding of input_array
        invalid_color: color to use for out of pointer's gamut values
        valid_color: color to use for inside of pointer's gamut values. If none just keep the orignal values.
        tolerance_amount: higher means less chance of being flag as invalid

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

    # Out of PG
    input_array[result_array != 1] = invalid_color
    # In PG:
    if valid_color is not None:
        input_array[result_array == 1] = valid_color

    return input_array
