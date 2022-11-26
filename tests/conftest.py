import logging.config

import pytest
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture
def imagepath_wheel_mpart():
    return DATA_DIR / "wheel_mpart.exr"


@pytest.fixture
def imagepath_color_bars_alpha():
    return DATA_DIR / "color_bars_alpha.tif"


@pytest.fixture
def imagepath_wheel_mchannel():
    return DATA_DIR / "wheel_mchannel.exr"


def _configureLogging():
    """
    Configure the python logging module
    """

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "fmt_standard": {
                "format": "{levelname: <7} | {asctime} |[{name: >30}]{message}",
                "style": "{",
            }
        },
        "handlers": {
            "hl_console": {
                "level": "DEBUG",
                "formatter": "fmt_standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            f"": {
                "handlers": ["hl_console"],
                "level": logging.DEBUG,
                "propagate": False,
            },
        },
    }
    # register
    logging.config.dictConfig(logging_config)
    return


_configureLogging()
