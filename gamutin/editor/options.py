import enum
import logging

logger = logging.getLogger(__name__)


class MaskOptions(enum.Enum):
    from_alpha = "From Alpha Channel"
    from_file = "From File"
