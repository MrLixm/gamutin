import logging
import logging.config

from gamutin import c
from gamutin import cfg
import gamutin.cli.interface


__all__ = ("start",)

logger = logging.getLogger(f"{gamutin.__name__}.__main__")


def _configureLogging(force_debug: bool = False):
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
            f"{gamutin.__name__}": {
                "handlers": ["hl_console"],
                "level": logging.DEBUG if force_debug else cfg.logs_level,
                "propagate": False,
            },
            "__main__": {
                "handlers": ["hl_console"],
                "level": logging.DEBUG,
                "propagate": False,
            },
            f"{gamutin.__name__}.editor": {
                "handlers": ["hl_console"],
                "level": logging.DEBUG if force_debug else logging.INFO,
                "propagate": False,
            },
        },
    }
    # register
    logging.config.dictConfig(logging_config)
    return


def start():
    """
    Start the application.
    """
    logger.info(f"[start] Started {c.name} v{c.__version__} ; frozen={c.is_frozen}")
    gamutin.debug()

    # start CLI, that will start the GUI if no argument specified.
    gamutin.cli.interface.cli()
    return


if __name__ == "__main__":
    _configureLogging()
    start()
