"""
Config file.
Variable can be modified during runtime.
"""
import logging
from pathlib import Path

from Qt import QtCore

import pgcheck
from .resources import ResourcesManager

__all__ = (
    "__debugthis__",
    "getAppQSettings",
    "resources",
    "validate",
)

logger = logging.getLogger(__name__)

resources: ResourcesManager = ResourcesManager(Path(__file__).parent / "resources")


def getAppQSettings() -> QtCore.QSettings:
    """
    Return an instance of the QSetting class to use for this application. Can be called
    from wherever in the API.
    """
    return QtCore.QSettings(pgcheck.c.org, pgcheck.c.name)


def validate():
    """
    Raise an error is some of the module's attributes have an issue.
    """
    resources.validate()
    return


validate()


def __debugthis__():
    """
    Log all the variables in this module with their current value.
    """
    logger.debug(
        f"""[__debugthis__] {__file__}:
    {resources=}"""
    )


if pgcheck.cfg.debug:
    __debugthis__()
