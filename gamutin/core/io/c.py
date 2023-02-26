"""
Constants
"""
from typing import Sequence

SUPPORTED_FILE_FORMATS: dict[str, list[str]] = {
    "bmp": ["bmp", "dib"],
    "cineon": ["cin"],
    "dds": ["dds"],
    "dpx": ["dpx"],
    "fits": ["fits"],
    "gif": ["gif"],
    "hdr": ["hdr", "rgbe"],
    "ico": ["ico"],
    "iff": ["iff", "z"],
    "jpeg": ["jpg", "jpe", "jpeg", "jif", "jfif", "jfi"],
    "jpeg2000": ["jp2", "j2k", "j2c"],
    "null": ["null", "nul"],
    "openexr": ["exr", "sxr", "mxr"],
    "png": ["png"],
    "pnm": ["ppm", "pgm", "pbm", "pnm", "pfm"],
    "psd": ["psd", "pdd", "psb"],
    "ptex": ["ptex", "ptx"],
    "rla": ["rla"],
    "sgi": ["sgi", "rgb", "rgba", "bw", "int", "inta"],
    "socket": ["socket"],
    "softimage": ["pic"],
    "tiff": ["tif", "tiff", "tx", "env", "sm", "vsm"],
    "targa": ["tga", "tpic"],
    "term": ["term"],
    "zfile": ["zfile"],
}
"""
Dictionnary of supported file formats ordered as {"format name": ["list of corresponding extensions"]}

Generated from OIIO :

>>> import OpenImageIO as oiio
>>> dict(
>>>     [
>>>         (extension.split(":")[0], extension.split(":")[1].split(","))
>>>         for extension in oiio.get_string_attribute("extension_list").split(";")
>>>     ]
>>> )
"""

SUPPORTED_FILE_EXTENSIONS = [
    "." + extension
    for extension_list in SUPPORTED_FILE_FORMATS.values()
    for extension in extension_list
]
"""
List of all file extensions supported. With the dot delimiter.
"""


def get_extensions_for_supported_formats(format_names: Sequence[str]) -> list[str]:
    """
    Get a flat list of file formats extensions corresponding to the given file format names.

    Args:
        format_names:
            list of formats names as defined in :var:`SUPPORTED_FILE_FORMATS`.
            Do NOT raise error if the format is not supported.

    Returns:
        list of extensions with the dot delimiter
    """

    extensions = []

    for format_name in format_names:
        format_extensions = SUPPORTED_FILE_FORMATS.get(format_name, [])
        extensions.extend(format_extensions)

    return ["." + extension for extension in extensions]
