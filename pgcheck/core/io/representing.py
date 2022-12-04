"""

"""
from __future__ import annotations

import datetime
import logging
from pathlib import Path

import OpenImageIO as oiio
import xmltodict

from .reading import ImageRead

logger = logging.getLogger(__name__)


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