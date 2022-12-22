__all__ = (
    "CompositeBlendModes",
    "MaskOptions",
)

import enum
import logging

from gamutin.core.gamut import CompositeBlendModes


logger = logging.getLogger(__name__)


class MaskOptions(enum.Enum):
    none = "None"
    from_alpha = "From Alpha Channel"
    from_file = "From File"
