__all__ = (
    "CompositeBlendModes",
    "MaskOptions",
    "SUPPORTED_FILE_EXTENSIONS",
)

import enum
import logging

import gamutin.core.io
from gamutin.core.gamut import CompositeBlendModes

logger = logging.getLogger(__name__)


SUPPORTED_FILE_EXTENSIONS = gamutin.core.io.SUPPORTED_FILE_EXTENSIONS


class MaskOptions(enum.Enum):
    none = "None"
    from_alpha = "From Alpha Channel"
    from_file = "From File"
