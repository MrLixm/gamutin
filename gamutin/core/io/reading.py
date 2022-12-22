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


@dataclass(frozen=True)
class ImageRead:
    """
    Object to represent an existig image on disk.

    Read is deffered when asked.

    Args:
        path: existing path to a file on disk
        colorspace: colorspace the pixel array is encoded in.
    """

    path: Path
    colorspace: Optional[colour.RGB_Colourspace]

    def get_image_buf(
        self,
        channels: Optional[tuple] = None,
        subimage: int = 0,
        mipmap: int = 0,
    ) -> oiio.ImageBuf:
        """

        Args:
            channels: list of name/index of channels to retrieve. ex: ("R", "A")
            subimage: index of the subimage to retrieve. Usually 0.
            mipmap: index of the mipmap to retrieve. Usually 0.

        Returns:
            ImageBUf instance as specified
        """
        buf = oiio.ImageBuf(str(self.path), subimage, mipmap)
        if channels:
            buf = oiio.ImageBufAlgo.channels(buf, channels)
        return buf

    def get_all_specs(self) -> dict[int, dict[int, oiio.ImageSpec]]:
        """
        Returns:
            dict of all ImageSpec for each part of the file, sorted by subimage > miplevel
        """
        out_dict = {}
        initial_buf = self.get_image_buf()

        for subimg_index in range(initial_buf.nsubimages):

            buf = self.get_image_buf(subimage=subimg_index)
            out_dict[subimg_index] = {}

            for mip_index in range(buf.nmiplevels):
                buf = self.get_image_buf(subimage=subimg_index, mipmap=mip_index)
                out_dict[subimg_index][mip_index] = buf.spec()

        return out_dict

    def read_array(
        self,
        channels: Optional[tuple] = None,
        subimage: int = 0,
        mipmap: int = 0,
    ) -> numpy.ndarray:
        """

        Args:
            channels: list of name/index of channels to retrieve. ex: ("R", "A")
            subimage: index of the subimage to retrieve. Usually 0.
            mipmap: index of the mipmap to retrieve. Usually 0.

        Returns:
            pixel data as floating point numpy array
        """
        return self.get_image_buf(channels, subimage, mipmap).get_pixels(oiio.TypeFloat)
