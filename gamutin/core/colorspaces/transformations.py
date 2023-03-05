__all__ = (
    "matrix_chromatic_adapation_transform",
    "matrix_colorspace_to_colorspace",
    "colorspace_to_XYZ",
    "colorspace_to_colorspace",
    "exr_chromaticities_to_colorspace",
    "colorspace_to_exr_chromaticities",
)

from typing import Optional

import colour
import numpy

from gamutin.core.colorspaces import RgbColorspace
from gamutin.core.colorspaces import Whitepoint
from gamutin.core.colorspaces import ChromaticAdaptationTransform
from gamutin.core.colorspaces import get_available_colorspaces


# TODO typo in function name
def matrix_chromatic_adapation_transform(
    source_whitepoint: Whitepoint,
    target_whitepoint: Whitepoint,
    transform_name: ChromaticAdaptationTransform,
):
    """
    Return the 3x3 matrix to convert the given illuminant to teh target illuminant
    using the given transform name.

    Args:
        source_whitepoint:
        target_whitepoint:
        transform_name:

    Returns:
        3x3 matrix
    """
    return colour.adaptation.matrix_chromatic_adaptation_VonKries(
        colour.models.xy_to_XYZ(source_whitepoint.coordinates),
        colour.models.xy_to_XYZ(target_whitepoint.coordinates),
        str(transform_name.value),
    )


def matrix_colorspace_to_colorspace(
    source_colorspace: RgbColorspace,
    target_colorspace: RgbColorspace,
    chromatic_adaptation_transform: Optional[ChromaticAdaptationTransform],
) -> numpy.ndarray:
    """
    Compute the matrix :math:`M` converting from given input *RGB*
    colourspace to output *RGB* colourspace using given *chromatic
    adaptation* method.

    Note:
        shameless copy of colour.matrix_RGB_to_RGB()

    Args:
        source_colorspace:
        target_colorspace:
        chromatic_adaptation_transform: for whitepoint conversion

    Returns:
        a 3x3 matrix for the conversion between the 2 given colorspaces.
    """
    if (
        source_colorspace.is_no_op
        or target_colorspace.is_no_op
        or not source_colorspace.gamut
        or not target_colorspace.gamut
    ):
        return numpy.identity(3)

    M = source_colorspace.matrix_to_XYZ

    if (
        chromatic_adaptation_transform is not None
        and source_colorspace.whitepoint
        and target_colorspace.whitepoint
    ):
        M_CAT = matrix_chromatic_adapation_transform(
            source_colorspace.whitepoint,
            target_colorspace.whitepoint,
            chromatic_adaptation_transform,
        )

        M = colour.algebra.matrix_dot(M_CAT, source_colorspace.matrix_to_XYZ)

    M = colour.algebra.matrix_dot(target_colorspace.matrix_from_XYZ, M)

    return M


def colorspace_to_XYZ(
    array: numpy.ndarray,
    source_colorspace: RgbColorspace,
    whitepoint_XYZ: Whitepoint,
    chromatic_adaptation_transform: Optional[ChromaticAdaptationTransform],
) -> numpy.ndarray:
    """
    Convert given *RGB* colourspace array to *CIE XYZ* tristimulus values.
    """
    if source_colorspace.is_no_op or source_colorspace.gamut is None:
        return array.copy()

    RGB = colour.utilities.to_domain_1(array)

    if (
        source_colorspace.transfer_functions is not None
        and source_colorspace.transfer_functions.decoding
    ):
        with colour.utilities.domain_range_scale("ignore"):
            RGB = source_colorspace.transfer_functions.decoding(RGB)

    XYZ = colour.algebra.vector_dot(source_colorspace.matrix_to_XYZ, RGB)

    if chromatic_adaptation_transform is not None and source_colorspace.whitepoint:
        M_CAT = matrix_chromatic_adapation_transform(
            source_colorspace.whitepoint,
            whitepoint_XYZ,
            chromatic_adaptation_transform,
        )
        XYZ = colour.algebra.vector_dot(M_CAT, XYZ)

    return colour.utilities.from_range_1(XYZ)


def colorspace_to_colorspace(
    array: numpy.ndarray,
    source_colorspace: RgbColorspace,
    target_colorspace: RgbColorspace,
    chromatic_adaptation_transform: Optional[ChromaticAdaptationTransform] = None,
):
    """
    Convert given *array* colourspace array from given input *RGB* colourspace
    to output *RGB* colourspace using given *chromatic adaptation* method.

    Note:
        shameless copy of colour.RGB_to_RGB()

    Args:
        array:
        source_colorspace:
        target_colorspace:
        chromatic_adaptation_transform: for whitepoint conversion

    Returns:
        array converted to the given colorspace
    """
    if source_colorspace.is_no_op or target_colorspace.is_no_op:
        return array.copy()
    if source_colorspace == target_colorspace:
        return array.copy()

    RGB = colour.utilities.to_domain_1(array)

    if (
        source_colorspace.transfer_functions is not None
        and source_colorspace.transfer_functions.decoding is not None
    ):
        with colour.utilities.domain_range_scale("ignore"):
            RGB = source_colorspace.transfer_functions.decoding(RGB)

    matrix = matrix_colorspace_to_colorspace(
        source_colorspace,
        target_colorspace,
        chromatic_adaptation_transform,
    )

    RGB = colour.utilities.vector_dot(matrix, RGB)

    if (
        target_colorspace.transfer_functions is not None
        and target_colorspace.transfer_functions.encoding is not None
    ):
        with colour.utilities.domain_range_scale("ignore"):
            RGB = target_colorspace.transfer_functions.encoding(RGB)

    return colour.utilities.from_range_1(RGB)


exr_chromaticities_type = tuple[float, float, float, float, float, float, float, float]
"""
Tuple of values as (R.x, R.y, G.x, G.y, B.x, B.y, whitepoint.x, whitepoint.y) where
``x`` and ``y`` are CIE x,y coordinates.
"""

exr_chromaticities_XYZ: exr_chromaticities_type = (1, 0, 0, 1, 0, 0, 1 / 3, 1 / 3)
"""
References:
   - [1] https://openexr.readthedocs.io/en/latest/TechnicalIntroduction.html#cie-xyz-color
"""


def exr_chromaticities_to_colorspace(
    exr_chromaticities: exr_chromaticities_type,
    ensure_linear_cctf: bool = True,
) -> list[RgbColorspace]:
    """
    Convert OpenEXR ``chromaticities`` attribute to pontential RgbColorspace instances.

    It's possible that multiple matching colorspaces are found as they can only
    differ in transfer-functions, which are not specified in the attribute.

    References:
       - [1] https://openexr.readthedocs.io/en/latest/TechnicalIntroduction.html#rgb-color

    Args:
       exr_chromaticities:
            chromaticities attribute as defined in the OpenEXR spec.
            (R.x, R.y, G.x, G.y, B.x, B.y, whitepoint.x, whitepoint.y)
       ensure_linear_cctf:
            If True make sure the returned colorspace instance use a linear transfer-function
            only if that not already the case.
            If False, the instance might or might not use a linear cctf.
            The OpenEXR spec imply this should be True by default.

    Returns:
        list of RgbColorspace that should match the given chromaticities.
    """
    colorspace_list = []

    # not supported currently
    if exr_chromaticities == exr_chromaticities_XYZ:
        return colorspace_list

    exr_whitepoint = numpy.array(exr_chromaticities[-2:])
    exr_primaries = numpy.array(exr_chromaticities[:-2])
    exr_primaries = exr_primaries.reshape((3, 2))

    for colorspace in get_available_colorspaces():
        if colorspace.whitepoint is None or colorspace.gamut is None:
            continue

        if not numpy.allclose(exr_whitepoint, colorspace.whitepoint.coordinates):
            continue

        if not numpy.allclose(exr_primaries, colorspace.gamut.primaries):
            continue

        if ensure_linear_cctf and not colorspace.transfer_functions.are_linear:
            colorspace_list.append(colorspace.as_linear_copy())
        else:
            colorspace_list.append(colorspace)

    return colorspace_list


def colorspace_to_exr_chromaticities(
    colorspace: RgbColorspace,
) -> Optional[exr_chromaticities_type]:
    """
    Convert the given RgbColorspace to the OpenEXR ``chromaticities`` attribute.

    Structured as ``(R.x, R.y, G.x, G.y, B.x, B.y, whitepoint.x, whitepoint.y)``

    Args:
       colorspace: source colorspace to generate the attribute from

    References:
       - [1] https://openexr.readthedocs.io/en/latest/TechnicalIntroduction.html#rgb-color

    Returns:
        chromaticities attribute as defined in the OpenEXR spec or None if not possible.
    """
    if colorspace.gamut is None or colorspace.whitepoint is None:
        return None

    primaries: list[float] = numpy.concatenate(colorspace.gamut.primaries, -1).tolist()
    whitepoint: list[float] = colorspace.whitepoint.coordinates.tolist()

    return (*primaries, *whitepoint)
