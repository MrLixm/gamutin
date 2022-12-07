import enum
import logging
from typing import Optional

import colour
import numpy

from .blending import blend_arrays
from .blending import BlendModes
from .colorspaces import POINTER_GAMUT_COLORSPACE

logger = logging.getLogger(__name__)


class CompositeBlendModes(enum.Enum):

    invalid_replace = (0, BlendModes.over)
    over = (1, BlendModes.over)
    add = (2, BlendModes.add)
    multiply = (3, BlendModes.multiply)

    @classmethod
    def __all__(cls):
        return [item for item in cls]


def transform_out_of_gamut_values(
    input_array: numpy.ndarray,
    input_colorspace: colour.RGB_Colourspace,
    reference_colorspace: colour.RGB_Colourspace,
    invalid_color: tuple[float, float, float],
    valid_color: Optional[tuple[float, float, float]],
    tolerance_amount: float,
    blend_mode: CompositeBlendModes,
    mask: Optional[numpy.ndarray] = None,
) -> numpy.ndarray:
    """

    Args:
        input_array:
        input_colorspace: colorspace encoding of input_array
        invalid_color: color to use for out of pointer's gamut values
        reference_colorspace: colorspace to use the gamut as limit for comparing the input_array
        valid_color: color to use for inside of pointer's gamut values. If none just keep the original values.
        tolerance_amount: higher means less chance of being flag as invalid
        blend_mode: blending operation to use for invalid/valid values
        mask: array of similar shape as input_array. Determine where the transfor is applied.

    Returns:
        input_array values modified using given parameters
    """

    if reference_colorspace == POINTER_GAMUT_COLORSPACE:

        intermediate_array = colour.RGB_to_XYZ(
            input_array,
            input_colorspace.whitepoint,
            reference_colorspace.whitepoint,
            input_colorspace.matrix_RGB_to_XYZ,
            chromatic_adaptation_transform="Bradford",
            cctf_decoding=input_colorspace.cctf_decoding,
        )
        logger.debug(
            "[transform_out_of_gamut_values] calling is_within_pointer_gamut ..."
        )
        result_array = colour.is_within_pointer_gamut(
            intermediate_array, tolerance_amount
        )

    else:

        result_array = colour.RGB_to_RGB(
            input_array,
            input_colourspace=input_colorspace,
            output_colourspace=reference_colorspace,
            chromatic_adaptation_transform="Bradford",  # TODO move to constant
            apply_cctf_decoding=True,
        )

        # out of gamut values = False
        result_array = numpy.where(
            result_array < 0,
            False,
            True,
        )
        result_array = numpy.all(result_array, axis=-1)

    result_array = result_array.astype(numpy.int_)

    output_array = input_array.copy()
    output_array[result_array != 1] = invalid_color  # Out of gamut
    if valid_color is not None and blend_mode != CompositeBlendModes.invalid_replace:
        output_array[result_array == 1] = valid_color  # In gamut

    blend_mode = blend_mode.value[-1]
    logger.debug(f"[transform_out_of_pg_values] applying blend mode {blend_mode} ...")

    output_array = blend_arrays(
        array_b=input_array,
        array_a=output_array,
        blend_mode=blend_mode,
        mask=mask,
    )
    return output_array
