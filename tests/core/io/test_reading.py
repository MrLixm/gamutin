from pathlib import Path

import OpenImageIO as oiio

from gamutin.core import io
from gamutin.core import colorspaces


def test_read_multipart(imagepath_wheel_mpart):
    image = io.ImageRead(
        path=imagepath_wheel_mpart,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )

    buf = image.read_as_image_buf()
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == ("R", "G", "B", "A")

    buf = image.read_as_image_buf(channels=("R", "A"))
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == ("R", "A")

    buf = image.read_as_image_buf(subimage=1)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == (
        "checkerboard.red",
        "checkerboard.green",
        "checkerboard.blue",
    )

    buf = image.read_as_image_buf(subimage=2)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == (
        "layer1.red",
        "layer1.green",
        "layer1.blue",
        "layer1.alpha",
    )

    buf = image.read_as_image_buf(subimage=3)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == ("noisy.y",)


def test_read_channels(imagepath_wheel_mchannel):
    image = io.ImageRead(
        path=imagepath_wheel_mchannel,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )
    buf = image.read_as_image_buf()
    spec: oiio.ImageSpec = buf.spec()
    assert len(spec.channelnames) == 15

    channels = ("layer1.red", "noisy.y", "A")
    buf = image.read_as_image_buf(channels=channels)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == channels


def test_class_frozen(imagepath_wheel_mchannel):
    image1 = io.ImageRead(
        path=imagepath_wheel_mchannel,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )
    image2 = io.ImageRead(
        path=imagepath_wheel_mchannel,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )
    assert image1 == image2
    test_set = set([image1, image2])
    assert len(test_set) == 1


def test_specs_all(imagepath_wheel_mchannel):
    image1 = io.ImageRead(
        path=imagepath_wheel_mchannel,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )
    specs = image1.specglobal
    assert len(specs) == 1
    assert isinstance(specs[0][0], oiio.ImageSpec)
    # test caching
    specs_again = image1.specglobal
    assert specs is specs_again


def test_timing(imagepath_wheel_mchannel):
    import time

    image1 = io.ImageRead(
        path=imagepath_wheel_mchannel,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )
    start_time_ref = time.time()
    image1.read_as_image_buf()
    end_time_ref = time.time() - start_time_ref

    start_time_test = time.time()
    for iteration in range(1000):
        image1.read_as_image_buf()
    end_time_test = time.time() - start_time_test

    print(end_time_ref, end_time_test)


def test_guess_colorspace(imagepath_color_bars_alpha, imagepath_wheel_mchannel):
    file_colorspace = io.guess_colorspace(imagepath_color_bars_alpha)
    assert file_colorspace is colorspaces.sRGB_COLORSPACE

    file_colorspace = io.guess_colorspace(imagepath_wheel_mchannel)
    assert file_colorspace is colorspaces.sRGB_LINEAR_COLORSPACE

    # tif image does not exists on disk so can't guess
    file_colorspace = io.guess_colorspace(Path(r"imageDontExists_01.tif"))
    assert file_colorspace is None

    file_colorspace = io.guess_colorspace(Path(r"imageDontExists_01.jpg"))
    assert file_colorspace is colorspaces.sRGB_COLORSPACE

    return


def test_find_colorspace(imagepath_spacoween, imagepath_wheel_mchannel):
    ap0_colorspace = colorspaces.get_colorspace("ACES2065-1")
    assert ap0_colorspace

    ap1_colorspace = colorspaces.get_colorspace("ACEScg")
    assert ap1_colorspace

    # test chromaticities attribute
    file_colorspace = io.find_colorspace(imagepath_spacoween)
    assert file_colorspace == ap0_colorspace

    file_colorspace = io.find_colorspace(imagepath_wheel_mchannel)
    assert file_colorspace is None

    file_colorspace = io.find_colorspace(Path("imageDoesntExist_test.exr"))
    assert file_colorspace is None

    file_colorspace = io.find_colorspace(Path("imageDoesntExist_sRGB.jpg"))
    assert file_colorspace == colorspaces.sRGB_COLORSPACE

    file_colorspace = io.find_colorspace(
        Path("imageDoesntExist_sRGB_test_ap0.1001.jpg")
    )
    assert file_colorspace == ap0_colorspace

    file_colorspace = io.find_colorspace(
        Path("test/ACEScg/imageDoesntExist_whatever-base.1001.jpg").resolve()
    )
    assert file_colorspace == ap1_colorspace

    return
