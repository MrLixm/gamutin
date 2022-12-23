"""

"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

import colour
import OpenImageIO as oiio
import numpy

logger = logging.getLogger(__name__)


class ImageRead:
    """
    Object to represent an existig image on disk.

    Everything implying reading the file is deffered on the first call.

    Args:
        path: existing path to a file on disk
        colorspace: colorspace the pixel array is encoded in.

    Raises:
        FileNotFoundError: if the given path doesn't exist on disk.
    """

    def __init__(self, path: Path, colorspace: Optional[colour.RGB_Colourspace]):

        self._specs_all: Optional[dict[int, dict[int, oiio.ImageSpec]]] = None

        self.path: Path = path
        self.colorspace: Optional[colour.RGB_Colourspace] = colorspace

        if not self.path.exists():
            raise FileNotFoundError(f"Given path <{path}> doesn't exists on disk.")

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.__key() == other.__key()
        return False

    def __hash__(self) -> int:
        return hash(self.__key())

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(path={self.path}, colorspace={self.colorspace})"
        )

    def __key(self):
        return self.path, self.colorspace

    @property
    def specglobal(self) -> dict[int, dict[int, oiio.ImageSpec]]:
        """
        Get a dict of all ImageSpec for each part of the file, sorted by subimage : miplevel.

        Example::

            {0: {0: <ImageSpec>}, 1: {0: <ImageSpec>}}
        """
        if self._specs_all:
            return self._specs_all

        out_dict = {}
        initial_buf = self.read_as_image_buf()

        for subimg_index in range(initial_buf.nsubimages):

            buf = self.read_as_image_buf(subimage=subimg_index)
            out_dict[subimg_index] = {}

            for mip_index in range(buf.nmiplevels):
                buf = self.read_as_image_buf(subimage=subimg_index, mipmap=mip_index)
                out_dict[subimg_index][mip_index] = buf.spec()

        self._specs_all = out_dict
        return self._specs_all

    @property
    def subimage_number(self) -> int:
        """
        Number of subimage availble in the image.
        """
        return len(self.specglobal.keys())

    def get_spec_at(self, subimage: int, miplevel: int) -> Optional[oiio.ImageSpec]:
        """
        ImageSpec correponding to the image stored at given "levels".
        """
        return self.specglobal.get(subimage, {}).get(miplevel, None)

    def miplevel_number_at(self, subimage_index: int) -> int:
        """
        Number of miplevel availble at given subimage index.
        """
        subimage = self.specglobal.get(subimage_index, {})
        return len(subimage.keys())

    def read_as_array(
        self,
        channels: Optional[tuple] = None,
        subimage: int = 0,
        mipmap: int = 0,
    ) -> numpy.ndarray:
        """
        Read the content of the image as numpy ndarray.

        Args:
            channels: list of name/index of channels to retrieve. ex: ("R", "A")
            subimage: index of the subimage to retrieve. Usually 0.
            mipmap: index of the mipmap to retrieve. Usually 0.

        Returns:
            pixel data as floating point numpy array
        """
        return self.read_as_image_buf(channels, subimage, mipmap).get_pixels(
            oiio.TypeFloat
        )

    def read_as_image_buf(
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
