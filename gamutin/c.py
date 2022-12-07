"""
Constants.
Lowest level module.
"""
from __future__ import annotations

__all__ = ("name", "__version__")

import enum
import json
import logging
import os
import sys
from typing import Any

logger = logging.getLogger(__name__)

__version_major__ = 0
__version_minor__ = 1
__version_patch__ = 0
__version__ = f"{__version_major__}.{__version_minor__}.{__version_patch__}"
if __version_prerelease__ := "":
    __version__ += f"-{__version_prerelease__}"
# ! scroll down for version extends

name = "gamutin"
"""
Package name. Mostly used in the editor.
"""

org = "pyco"
"""
Organisation.
"""

vcs_url = "https://github.com/MrLixm/gamutin"
"""
url of the remote VCS repository for this package.
"""


""" ------------------------------------------------------------------------------------
ENVIRONMENT VARIABLES

All are optionals.
"""

ENVPREFIX = name.upper()


class Env(enum.Enum):

    logs_debug = f"{ENVPREFIX}_LOGS_DEBUG"
    """
    Set logging to debug level
    """

    debug = f"{ENVPREFIX}_DEBUG"
    """
    Enable the debug mode for the application
    """

    platform_fake = f"{ENVPREFIX}_PLATFORM_FAKE"
    """
    string is one of sys.platform. Used to fake a specific plateform during build.
    """

    dependencies_list = f"{ENVPREFIX}_DEPENDENCIES"
    """
    static list of python dependencies coco is using. Used when app is frozen.
    """

    build_id = f"{ENVPREFIX}_BUILD_ID"
    """
    Set during build by pyinstaller.
    """

    @classmethod
    def __all__(cls):
        return [attr for attr in cls]

    @classmethod
    def __asdict__(cls) -> dict[str, str]:
        out = dict()
        for attr in cls.__all__():
            out[str(attr.value)] = cls.get(attr)
        return out

    @classmethod
    def get(cls, key: Env, default: Any = None) -> str | None | Any:
        return os.environ.get(str(key.value), default)


""" ------------------------------------------------------------------------------------
CONTEXT
"""


class Plateform:
    """
    Utility class to improve upon ``sys.platform``
    """

    ENV_FAKE = "PLATFORM_FAKE"
    """
    Name of the environment variable that can be used to "fake" the platform currently
    active. Value must be one of ``sys.platform``.

    It is recommend to override it in the instance and the package's prefix.
    """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"

    @property
    def name(self) -> str:

        if self.is_linux:
            return "linux"
        elif self.is_mac:
            return "mac"
        elif self.is_windows:
            return "windows"
        else:
            raise OSError("Unsupported plateform {}".format(sys.platform))

    @property
    def source(self) -> str:
        return os.environ.get(self.ENV_FAKE) or sys.platform

    @property
    def is_linux(self) -> bool:
        return self.source.startswith("linux")

    @property
    def is_mac(self) -> bool:
        return self.source.startswith("darwin")

    @property
    def is_windows(self) -> bool:
        return self.source in ("win32", "cygwin")


plateform = Plateform()
plateform.ENV_FAKE = Env.platform_fake.value


is_frozen: bool = getattr(sys, "frozen", False)
"""
True if the module is being executed from a frozen pyinstaller executable.
"""


""" ------------------------------------------------------------------------------------
POST-MODIFICATIONS

for stuff that needed other objects to be computed
"""

if __version_build__ := Env.get(Env.build_id):
    __version__ += f"+{__version_build__}"


def __debugthis__():
    """
    Log all the variables in this module with their current value.
    """

    logger.debug(
        f"""[__debugthis__] {__file__}:
    {__version__=}
    {__version_major__=}
    {__version_minor__=}
    {__version_patch__=}
    Env={json.dumps(Env.__asdict__(), indent=4, default=str)}
    {ENVPREFIX=}
    {is_frozen=}
    {name=}
    {org=}
    {plateform=}
    {vcs_url=}"""
    )
