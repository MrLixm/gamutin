"""
Config file.
Variable can be modified during runtime.
"""
import logging
from pathlib import Path

from Qt import QtCore

import gamutin
from .resources import ResourceLibrary

__all__ = (
    "__debugthis__",
    "getAppQSettings",
    "resources",
)

logger = logging.getLogger(__name__)

resources: ResourceLibrary = ResourceLibrary(Path(__file__).parent / "resources")


def getAppQSettings() -> QtCore.QSettings:
    """
    Return an instance of the QSetting class to use for this application. Can be called
    from wherever in the API.
    """
    return QtCore.QSettings(gamutin.c.org, gamutin.c.name)


def __debugthis__():
    """
    Log all the variables in this module with their current value.
    """
    logger.debug(
        f"""[__debugthis__] {__file__}:
    {resources=}"""
    )


if gamutin.cfg.debug:
    __debugthis__()
