import logging
import logging.config

from pgcheck import c
from pgcheck import cfg
import pgcheck.cli.interface


__all__ = ("start",)

logger = logging.getLogger(f"{pgcheck.__name__}.__main__")


def _configureLogging():
    """
    Configure the python logging module
    """

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "fmt_standard": {
                "format": "{asctime} | {levelname: <7} |[{name: >30}]{message}",
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
            f"{pgcheck.__name__}": {
                "handlers": ["hl_console"],
                "level": cfg.logs_level,
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
    pgcheck.debug()

    # start CLI, that will start the GUI if no argument specified.
    pgcheck.cli.interface.cli()
    return


if __name__ == "__main__":

    _configureLogging()
    start()
