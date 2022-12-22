import OpenImageIO as oiio

from gamutin.core import io
from gamutin.core import colorspaces


def test_read_multipart(imagepath_wheel_mpart):

    image = io.ImageRead(
        path=imagepath_wheel_mpart,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )

    buf = image.get_image_buf()
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == ("R", "G", "B", "A")

    buf = image.get_image_buf(channels=("R", "A"))
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == ("R", "A")

    buf = image.get_image_buf(subimage=1)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == (
        "checkerboard.red",
        "checkerboard.green",
        "checkerboard.blue",
    )

    buf = image.get_image_buf(subimage=2)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == (
        "layer1.red",
        "layer1.green",
        "layer1.blue",
        "layer1.alpha",
    )

    buf = image.get_image_buf(subimage=3)
    spec: oiio.ImageSpec = buf.spec()
    assert spec.channelnames == ("noisy.y",)


def test_read_channels(imagepath_wheel_mchannel):

    image = io.ImageRead(
        path=imagepath_wheel_mchannel,
        colorspace=colorspaces.get_colorspace("sRGB:linear"),
    )
    buf = image.get_image_buf()
    spec: oiio.ImageSpec = buf.spec()
    assert len(spec.channelnames) == 15

    channels = ("layer1.red", "noisy.y", "A")
    buf = image.get_image_buf(channels=channels)
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
