"""
Config file.
Variable can be modified during runtime.
"""
import logging
import sys

from . import c

__all__ = (
    "__debugthis__",
    "logs_level",
)

logger = logging.getLogger(__name__)


def _debug() -> bool:

    if len(sys.argv) > 1 and sys.argv[1] == "--debug":
        return True

    if int(c.Env.get(c.Env.debug, False)):
        return True

    return False


debug: bool = _debug()
"""
True to switch to debug mode. This usually display/log additional informations and 
disable some problematic features.
"""


def _logs_level() -> int:

    if len(sys.argv) > 1 and sys.argv[1] == "--debug":
        return logging.DEBUG

    env = c.Env.get(c.Env.logs_debug)
    if env is not None and bool(int(env)):
        return logging.DEBUG

    return logging.INFO


logs_level: int = _logs_level()


def __debugthis__():
    """
    Log all the variables in this module with their current value.
    """

    logger.debug(
        f"""[__debugthis__] {__file__}:
    {debug=}
    {logging.getLevelName(logs_level)=}"""
    )
