__all__ = ("WidgetUserError",)

import datetime
import logging
from typing import Union, Type

from Qt import QtWidgets

logger = logging.getLogger(__name__)


class WidgetUserError(Exception):
    """
    For exception that happens on editor widgets cause of the user interaction.

    Args:
        name: a short name to identify the error. No need to be unique.
        widget: the Qt widget the error was produced from
        message: a short message that brieflyd escribe the error
        details: a detailed message of any length to explain the error
    """

    def __init__(
        self,
        name: Union[str, Type[Exception]],
        widget: QtWidgets.QWidget,
        message: str,
        details: str = None,
    ):
        super().__init__(message)

        if not isinstance(name, str):
            name = name.__name__

        self.time = datetime.datetime.now()
        self.name = name
        self.message = message
        self.details = details
        self.widget = widget
        self.is_deleted = False

    def __str__(self):
        msg = f"{self.name}: {self.widget.__class__}>>>{self.message}"
        if self.details:
            msg += f":\n{self.details}"
        return msg

    def as_dict(self) -> dict[str, str]:
        return {
            "time": str(self.time),
            "name": self.name,
            "message": self.message,
            "details": self.details,
            "widget": repr(self.widget),
        }

    def delete(self):
        """
        Mark the error as deleted. This mean it has been resolved.
        """
        self.is_deleted = True

    def time_clock(self) -> str:
        """
        Time at which the error occured as hours:min:second.microseconds
        """
        error_time = self.time.strftime("%H:%M:%S")
        return f"{error_time}.{self.time.microsecond}"
