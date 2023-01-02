from gamutin.core import colorspaces


def test_exr_chromaticities():

    chromat_bt709 = (0.64, 0.33, 0.3, 0.6, 0.15, 0.06, 0.3127, 0.329)
    chromat_CIE_XYZ = (1, 0, 0, 1, 0, 0, 1 / 3, 1 / 3)
    chromat_random = (0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.5, 0.5)

    colorspace = colorspaces.get_colorspace("sRGB")
    result = colorspaces.colorspace_to_exr_chromaticities(colorspace)
    assert result == chromat_bt709

    colorspace = colorspaces.get_colorspace("raw")
    result = colorspaces.colorspace_to_exr_chromaticities(colorspace)
    assert result is None

    result = colorspaces.exr_chromaticities_to_colorspace(
        chromat_bt709,
        force_linear_cctf=True,
    )
    assert colorspaces.get_colorspace("sRGB").get_linear_copy() in result

    result = colorspaces.exr_chromaticities_to_colorspace(
        chromat_bt709,
        force_linear_cctf=False,
    )
    assert colorspaces.get_colorspace("sRGB") in result
    assert result == [
        colorspaces.get_colorspace("bt709"),
        colorspaces.get_colorspace("sRGB"),
    ]

    result = colorspaces.exr_chromaticities_to_colorspace(
        chromat_CIE_XYZ,
        force_linear_cctf=False,
    )
    assert result == []

    result = colorspaces.exr_chromaticities_to_colorspace(
        chromat_random,
        force_linear_cctf=False,
    )
    assert result == []

    return
