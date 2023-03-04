"""

"""
from __future__ import annotations

__all__ = (
    "ImageRead",
    "find_colorspace",
    "guess_colorspace",
)

import logging
from pathlib import Path
from typing import Optional, Union

import OpenImageIO as oiio
import numpy

from .c import get_extensions_for_supported_formats
from .representing import repr_spec_full_dict
from .representing import repr_stats_simplified_str
from .representing import repr_spec_simplified_str
from gamutin.core.colorspaces import RgbColorspace
from gamutin.core.colorspaces import get_available_colorspaces_names_aliases
from gamutin.core.colorspaces import get_colorspace
from gamutin.core.colorspaces import exr_chromaticities_to_colorspace
from gamutin.core.colorspaces import sRGB_COLORSPACE
from gamutin.core.colorspaces import sRGB_LINEAR_COLORSPACE
from gamutin.core.utils import split_at_words


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

    def __init__(self, path: Path, colorspace: Optional[RgbColorspace]):
        self._specs_all: Optional[dict[int, dict[int, oiio.ImageSpec]]] = None

        self.path: Path = path
        self.colorspace: Optional[RgbColorspace] = colorspace

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

    def as_dict_simple(self) -> dict[str, dict]:
        """
        Get a simplified dict representation with only essential information.

        This doesn't include any actual pixel data.
        """

        out_dict = {}

        for subimage_index, subimage_data in self.specglobal.items():
            subimage_index = f"subimage {subimage_index}"
            out_dict[subimage_index] = {}

            for mip_index, level_spec in subimage_data.items():
                mip_index = f"miplevel {mip_index}"
                out_dict[subimage_index][mip_index] = repr_spec_simplified_str(
                    level_spec
                )

        return {str(self.path): out_dict}

    def as_dict_full(self) -> dict[str, Union[dict, str]]:
        """
        Get a full dict representation with all the information possible.

        This doesn't include any actual pixel data.
        """

        out_dict = {}

        for subimage_index, subimage_data in self.specglobal.items():
            subimage_index = f"subimage {subimage_index}"
            out_dict[subimage_index] = {}

            for mip_index, level_spec in subimage_data.items():
                mip_index = f"miplevel {mip_index}"
                out_dict[subimage_index][mip_index] = repr_spec_full_dict(level_spec)

        return {
            str(self.path): {
                "__stats__": repr_stats_simplified_str(self.path),
                "content": out_dict,
            },
        }

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

    def reload(self):
        """
        Update any cached data in the case the file on disk has changed.
        """
        self.__init__(path=self.path, colorspace=self.colorspace)


def guess_colorspace(file_path: Path) -> Optional[RgbColorspace]:
    """
    Try to guess the colorspace encoding of the given file.

    This is a highly probable but not 100% accurate result. Better chance to return
    a colorspace than :func:`find_colorspace` function.

    Args:
        file_path: path to a file on disk that may not exist

    Returns:

    """
    if result := find_colorspace(file_path):
        return result

    if file_path.suffix in get_extensions_for_supported_formats(["openexr", "hdr"]):
        return sRGB_LINEAR_COLORSPACE

    elif file_path.suffix in get_extensions_for_supported_formats(
        ["jpeg", "png", "targa", "dds", "bmp"]
    ):
        return sRGB_COLORSPACE

    elif (
        file_path.suffix in get_extensions_for_supported_formats(["tiff"])
        and file_path.exists()
    ):
        file = ImageRead(file_path, None)
        file_spec = file.get_spec_at(0, 0)
        if file_spec.format == oiio.FLOAT:
            return sRGB_LINEAR_COLORSPACE
        else:
            return sRGB_COLORSPACE

    return None


def find_colorspace(file_path: Path) -> Optional[RgbColorspace]:
    """
    Return the colorspace encoding of the given file.

    This is a safe result with NO hypothetic guesses, but as such it might have less
    chance of finding one.

    The find is performed as :

    - check the file path :
        - check for an exact with the full directory name of the file
        - check for the colorspace name in the filename when split at word. The right-most occurence is picked.
    - if .exr
        - get "chromaticities" metadata attribute and derive a colorspace from it

    Args:
        file_path: path to a file on disk that may not exist

    Returns:
        None if no colorspace can be found.
    """

    file_name_split = split_at_words(file_path.stem, split_camel_case=False)

    # list of word to check that they correspond to a colorspace name
    words_list = [file_path.parent.name] + file_name_split

    colorspace = None

    # TODO potential performance improvement here ?
    for word in words_list:
        for colorspaces_aliases in get_available_colorspaces_names_aliases():
            for colorspace_alias in colorspaces_aliases:
                if colorspace_alias == word:
                    colorspace = get_colorspace(colorspace_alias)

    if colorspace:
        logger.debug("[find_colorspace] found from file path.")
        return colorspace

    if not file_path.exists():
        return None

    file = ImageRead(file_path, None)
    file_spec = file.get_spec_at(0, 0)

    if file_spec and file_path.suffix == ".exr":
        exr_chromaticities = file_spec.getattribute("chromaticities")

        if exr_chromaticities:
            assert isinstance(exr_chromaticities, tuple)

            colorspace = exr_chromaticities_to_colorspace(
                exr_chromaticities,
                ensure_linear_cctf=True,
            )
            logger.debug(
                f"[find_colorspace] found from OpenEXR chromaticities attribute: "
                f"{list(map(str, colorspace))}"
            )
            colorspace = colorspace[0]

    # TODO #6 detect icc profiles

    return colorspace
