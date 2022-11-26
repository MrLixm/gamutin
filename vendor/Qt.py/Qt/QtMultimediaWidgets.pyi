# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtMultimediaWidgets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtMultimediaWidgets
import PySide2

try:
    import typing
except ImportError:
    from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual,
    Missing,
    Invalid,
    Default,
    Instance,
)

class Object(object):
    pass

import shiboken2 as Shiboken

Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtMultimedia
import PySide2.QtMultimediaWidgets

class QCameraViewfinder(PySide2.QtMultimediaWidgets.QVideoWidget):
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...): ...
    def mediaObject(self) -> PySide2.QtMultimedia.QMediaObject: ...
    def setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool: ...

class QGraphicsVideoItem(
    PySide2.QtWidgets.QGraphicsObject, PySide2.QtMultimedia.QMediaBindableInterface
):
    def __init__(
        self, parent: typing.Optional[PySide2.QtWidgets.QGraphicsItem] = ...
    ): ...
    def aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode: ...
    def boundingRect(self) -> PySide2.QtCore.QRectF: ...
    def itemChange(
        self,
        change: PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange,
        value: typing.Any,
    ) -> typing.Any: ...
    def mediaObject(self) -> PySide2.QtMultimedia.QMediaObject: ...
    def nativeSize(self) -> PySide2.QtCore.QSizeF: ...
    def offset(self) -> PySide2.QtCore.QPointF: ...
    def paint(
        self,
        painter: PySide2.QtGui.QPainter,
        option: PySide2.QtWidgets.QStyleOptionGraphicsItem,
        widget: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ): ...
    def setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode): ...
    def setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool: ...
    def setOffset(self, offset: PySide2.QtCore.QPointF): ...
    def setSize(self, size: PySide2.QtCore.QSizeF): ...
    def size(self) -> PySide2.QtCore.QSizeF: ...
    def timerEvent(self, event: PySide2.QtCore.QTimerEvent): ...
    def videoSurface(self) -> PySide2.QtMultimedia.QAbstractVideoSurface: ...

class QVideoWidget(
    PySide2.QtWidgets.QWidget, PySide2.QtMultimedia.QMediaBindableInterface
):
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...): ...
    def aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode: ...
    def brightness(self) -> int: ...
    def contrast(self) -> int: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def hideEvent(self, event: PySide2.QtGui.QHideEvent): ...
    def hue(self) -> int: ...
    def mediaObject(self) -> PySide2.QtMultimedia.QMediaObject: ...
    def moveEvent(self, event: PySide2.QtGui.QMoveEvent): ...
    def nativeEvent(
        self, eventType: PySide2.QtCore.QByteArray, message: int
    ) -> typing.Tuple: ...
    def paintEvent(self, event: PySide2.QtGui.QPaintEvent): ...
    def resizeEvent(self, event: PySide2.QtGui.QResizeEvent): ...
    def saturation(self) -> int: ...
    def setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode): ...
    def setBrightness(self, brightness: int): ...
    def setContrast(self, contrast: int): ...
    def setFullScreen(self, fullScreen: bool): ...
    def setHue(self, hue: int): ...
    def setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool: ...
    def setSaturation(self, saturation: int): ...
    def showEvent(self, event: PySide2.QtGui.QShowEvent): ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def videoSurface(self) -> PySide2.QtMultimedia.QAbstractVideoSurface: ...

class QVideoWidgetControl(PySide2.QtMultimedia.QMediaControl):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def aspectRatioMode(self) -> PySide2.QtCore.Qt.AspectRatioMode: ...
    def brightness(self) -> int: ...
    def contrast(self) -> int: ...
    def hue(self) -> int: ...
    def isFullScreen(self) -> bool: ...
    def saturation(self) -> int: ...
    def setAspectRatioMode(self, mode: PySide2.QtCore.Qt.AspectRatioMode): ...
    def setBrightness(self, brightness: int): ...
    def setContrast(self, contrast: int): ...
    def setFullScreen(self, fullScreen: bool): ...
    def setHue(self, hue: int): ...
    def setSaturation(self, saturation: int): ...
    def videoWidget(self) -> PySide2.QtWidgets.QWidget: ...

# eof
