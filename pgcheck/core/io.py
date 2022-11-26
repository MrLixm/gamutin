"""

"""
from __future__ import annotations
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import colour
import OpenImageIO as oiio
import numpy

logger = logging.getLogger(__name__)


@dataclass
class ImageRead:
    """
    Object to represent an existig image on disk.

    Read is deffered when asked.

    Args:
        path: existing path to a file on disk
        colorspace: colorspace the pixel array is encoded in.
    """

    path: Path
    colorspace: colour.RGB_Colourspace

    def get_image_buf(self, subimage: int = 0, mipmap: int = 0) -> oiio.ImageBuf:
        return oiio.ImageBuf(str(self.path), subimage, mipmap)

    def read_array(self, subimage: int, mipmap: int) -> numpy.ndarray:
        return self.get_image_buf(subimage, mipmap).get_pixels(oiio.TypeFloat)


@dataclass
class ImageWrite:
    """
    Object to represent an image that must be written to disk.

    Args:
        path: existing path to a file on disk
        colorspace: colorspace the pixel array is encoded in.
    """

    path: Path
    colorspace: Optional[colour.RGB_Colourspace]

    def __post_init__(self):
        self.image_buf: oiio.ImageBuf = oiio.ImageBuf()

    def set_pixels(self, array: numpy.ndarray):
        """

        Args:
            array: pixel data, must be float encoded.
        """
        spec = oiio.ImageSpec(
            array.shape[1],
            array.shape[0],
            array.shape[2],
            oiio.TypeFloat,
        )
        self.image_buf: oiio.ImageBuf = oiio.ImageBuf(spec)
        self.image_buf.set_pixels(spec.roi_full, array)
        return

    def write(self):

        self.image_buf.specmod().attribute("compression", "jpg:99")
        self.image_buf.specmod().attribute("oiio:ColorSpace", self.colorspace.name)

        if self.image_buf.has_error:
            raise RuntimeError(
                f"Current ImageBuf {self.image_buf} has errors: {self.image_buf.geterror()}"
            )

        logger.info(f"[{self.__class__.__name__}][write] About to write to {self.path}")
        self.image_buf.write(str(self.path))

        if self.image_buf.has_error:
            raise RuntimeError(
                f"Error writing ImageBuf {self.image_buf}: {self.image_buf.geterror()}"
            )
        return


def img2str(img: numpy.ndarray, single_pixel=True) -> str:
    """
    Pretty print a 2D image to a str.

    Args:
        img: 2D image as numpy array
        single_pixel: if True only print the first pixel at x:0,y:0
    """

    if single_pixel:
        img: numpy.ndarray = img[0][0]

    with numpy.printoptions(
        precision=3,
        suppress=True,
        formatter={"float": "{: 0.5f}".format},
    ):
        return f"{img}"
