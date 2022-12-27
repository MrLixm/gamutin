from __future__ import annotations

import copy
import enum
import logging
from abc import ABC, abstractmethod
from typing import Any, TypeVar

from Qt import QtGui

logger = logging.getLogger(__name__)


P = TypeVar("P")


class BaseQtProperty(ABC):
    """
    Represent a value in a Qt StyleSheet whose type is as defined in
    https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-property-types.
    """

    def __init__(self, value: Any):
        self.value = value

    def __str__(self) -> str:
        return self.to_qss()

    @abstractmethod
    def to_qss(self) -> str:
        """
        Converted the internally stored python object to a qss comaptible value.
        """
        pass

    @abstractmethod
    def apply_overrides(self, **kwargs) -> None:
        """
        Changed the internally stored data with the given overrides.

        Args:
            **kwargs:
        """
        pass

    @abstractmethod
    def validate(self) -> None:
        """
        Raise an exception if the internal value stored are not in the expected state.
        """
        pass

    def copy(self: P) -> P:
        return copy.deepcopy(self)


class LiteralQtProperty(BaseQtProperty):
    """
    Where the value doesn't need any processing and can just be used as is in a stylesheet.

    Most of the time for strings looking like enums.
    """

    def to_qss(self) -> str:
        return f"{self.value}"

    def apply_overrides(self, **kwargs) -> None:
        pass

    def validate(self):
        pass


class LengthQtProperty(BaseQtProperty):
    """
    A number value with an associated unit. For now hardcoded to px.

    https://doc.qt.io/qt-5/stylesheet-reference.html#length
    """

    class LengthUnits(enum.Enum):
        px = "px"
        pt = "pt"
        em = "em"
        ex = "ex"

    def to_qss(self) -> str:
        return f"{self.value}px"

    def apply_overrides(self, **kwargs) -> None:

        scale_override = kwargs.get("scale")
        if isinstance(scale_override, str):
            scale_override = float(scale_override)

        if scale_override is not None:
            self.value = self.value * scale_override

        self.validate()
        return

    def validate(self):
        if not isinstance(self.value, (float, int)):
            raise TypeError(
                f"{self.__class__.__name__} internal value error : "
                f"Expected (float, int) got <{type(self.value)} {self.value}>"
            )


class ColorQtProperty(BaseQtProperty):
    """
    A color in the stylesheet under the RGBA model.

    https://doc.qt.io/qt-5/stylesheet-reference.html#color

    Args:
        value: tuple of (r,g,b,a) as integer in 0-255 range.
    """

    def __init__(self, value: tuple[int, int, int, int]):
        super().__init__(value=value)
        self.validate()

    @classmethod
    def from_qcolor(cls, qcolor: QtGui.QColor) -> ColorQtProperty:
        """
        Args:
            qcolor: any kind of QColor (color model doesn't matter)

        Returns:
            class instance
        """
        qcolor = qcolor.toRgb()
        return cls(value=qcolor.toTuple())

    def as_qcolor(self) -> QtGui.QColor:
        return QtGui.QColor(*self.value)

    def to_qss(self) -> str:
        return f"rgba{self.value}"

    def apply_overrides(self, **kwargs) -> None:

        alpha_override = kwargs.get("alpha")
        if isinstance(alpha_override, str):
            alpha_override = float(alpha_override)
        if isinstance(alpha_override, float):
            alpha_override = int(alpha_override * 255)

        if alpha_override is not None:
            self.value = (self.value[0], self.value[1], self.value[2], alpha_override)

        self.validate()
        return

    def validate(self):

        if (
            not isinstance(self.value, tuple)
            or not len(self.value) == 4
            or not all([isinstance(v, int) for v in self.value])
        ):
            raise TypeError(
                f"{self.__class__.__name__} internal value error : "
                f"Expected tuple[int, int, int, int] got <{type(self.value)} {self.value}>"
            )
