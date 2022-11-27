"""

"""
from __future__ import annotations

import datetime
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import colour
import OpenImageIO as oiio
import numpy
import xmltodict

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
        if self.colorspace:
            self.image_buf.specmod().attribute("oiio:ColorSpace", self.colorspace.name)
        else:
            self.image_buf.specmod().attribute("oiio:ColorSpace", "scalar")

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


class ImageRepr:
    """
    Serialized representation of the image data for human consumption.
    """

    def __init__(self, image: ImageRead):
        self.image = image

    @property
    def simple_dict(self) -> dict:
        """
        Get a simplified dict representation with only essential information.
        """

        out_dict = {}

        for subimage_index, subimage_data in self.image.get_all_specs().items():

            subimage_index = f"subimage {subimage_index}"
            out_dict[subimage_index] = {}

            for mip_index, level_spec in subimage_data.items():

                mip_index = f"miplevel {mip_index}"
                out_dict[subimage_index][mip_index] = repr_spec_simplified_str(
                    level_spec
                )

        return {str(self.image.path): out_dict}

    @property
    def full_dict(self) -> dict:
        """
        Get a full dict representation with all the information possible.
        """

        out_dict = {}

        for subimage_index, subimage_data in self.image.get_all_specs().items():

            subimage_index = f"subimage {subimage_index}"
            out_dict[subimage_index] = {}

            for mip_index, level_spec in subimage_data.items():

                mip_index = f"miplevel {mip_index}"
                out_dict[subimage_index][mip_index] = repr_spec_full_dict(level_spec)

        return {
            str(self.image.path): {
                "__stats__": repr_stats_simplified_str(self.image.path),
                "content": out_dict,
            },
        }


def convert_bytes(byte_number: int) -> str:
    """
    Automatically convert a bytes number to a more representable unit.

    src: https://stackoverflow.com/a/39988702/13806195
    """
    for unit in ["bytes", "KB", "MB", "GB", "TB"]:
        if byte_number < 1024.0:
            return f"{byte_number:3.1f} {unit}"
        byte_number /= 1024.0


def repr_stats_simplified_str(file_path: Path) -> str:
    """
    Return a simplified string representation of the file stats.
    """
    stat = file_path.stat()
    out_str = ""
    out_str += f"size={convert_bytes(stat.st_size)}, "
    out_str += f"created={datetime.datetime.fromtimestamp(stat.st_ctime)}, "
    out_str += f"modified={datetime.datetime.fromtimestamp(stat.st_mtime)}, "
    return out_str


def repr_spec_simplified_str(image_spec: oiio.ImageSpec) -> str:
    """
    Convert the given image spec to a simplified string representation.
    """
    return f"{image_spec.format} {image_spec.width}x{image_spec.height} - {image_spec.nchannels}:{image_spec.channelnames}"


def repr_spec_full_dict(image_spec: oiio.ImageSpec) -> dict:
    """
    Convert the given image spec to a dictionnary representation.
    """

    def attrib_post_process(path, key, value):
        if key != "attrib":
            return key, value
        return key, f"{value['@type']: >10} {value['@name']} = {value['#text']}"

    return xmltodict.parse(
        image_spec.serialize(format="XML", verbose="detailed"),
        postprocessor=attrib_post_process,
    )
