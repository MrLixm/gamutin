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
PySide2.QtCore, except for defaults which are replaced by "...".
"""

# Module PySide2.QtCore
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

class ClassInfo(object):
    def __init__(self, **info: typing.Dict): ...

class MetaFunction(object):
    def __call__(self, *args: typing.Any) -> typing.Any: ...

class MetaSignal(type):
    @staticmethod
    def __instancecheck__(object: object) -> bool: ...

class Property(object):
    def __init__(
        self,
        type: type,
        fget: typing.Optional[typing.Callable] = ...,
        fset: typing.Optional[typing.Callable] = ...,
        freset: typing.Optional[typing.Callable] = ...,
        fdel: typing.Optional[typing.Callable] = ...,
        doc: str = ...,
        notify: typing.Optional[typing.Callable] = ...,
        designable: bool = ...,
        scriptable: bool = ...,
        stored: bool = ...,
        user: bool = ...,
        constant: bool = ...,
        final: bool = ...,
    ): ...
    def getter(self, func: typing.Callable): ...
    def read(self, func: typing.Callable): ...
    def setter(self, func: typing.Callable): ...
    def write(self, func: typing.Callable): ...

class QAbstractAnimation(PySide2.QtCore.QObject):
    Forward: QAbstractAnimation = ...  # 0x0
    KeepWhenStopped: QAbstractAnimation = ...  # 0x0
    Stopped: QAbstractAnimation = ...  # 0x0
    Backward: QAbstractAnimation = ...  # 0x1
    DeleteWhenStopped: QAbstractAnimation = ...  # 0x1
    Paused: QAbstractAnimation = ...  # 0x1
    Running: QAbstractAnimation = ...  # 0x2

    class DeletionPolicy(object):
        KeepWhenStopped: QAbstractAnimation.DeletionPolicy = ...  # 0x0
        DeleteWhenStopped: QAbstractAnimation.DeletionPolicy = ...  # 0x1

    class Direction(object):
        Forward: QAbstractAnimation.Direction = ...  # 0x0
        Backward: QAbstractAnimation.Direction = ...  # 0x1

    class State(object):
        Stopped: QAbstractAnimation.State = ...  # 0x0
        Paused: QAbstractAnimation.State = ...  # 0x1
        Running: QAbstractAnimation.State = ...  # 0x2
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def currentLoop(self) -> int: ...
    def currentLoopTime(self) -> int: ...
    def currentTime(self) -> int: ...
    def direction(self) -> PySide2.QtCore.QAbstractAnimation.Direction: ...
    def duration(self) -> int: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def group(self) -> PySide2.QtCore.QAnimationGroup: ...
    def loopCount(self) -> int: ...
    def pause(self): ...
    def resume(self): ...
    def setCurrentTime(self, msecs: int): ...
    def setDirection(self, direction: PySide2.QtCore.QAbstractAnimation.Direction): ...
    def setLoopCount(self, loopCount: int): ...
    def setPaused(self, arg__1: bool): ...
    def start(self, policy: PySide2.QtCore.QAbstractAnimation.DeletionPolicy = ...): ...
    def state(self) -> PySide2.QtCore.QAbstractAnimation.State: ...
    def stop(self): ...
    def totalDuration(self) -> int: ...
    def updateCurrentTime(self, currentTime: int): ...
    def updateDirection(
        self, direction: PySide2.QtCore.QAbstractAnimation.Direction
    ): ...
    def updateState(
        self,
        newState: PySide2.QtCore.QAbstractAnimation.State,
        oldState: PySide2.QtCore.QAbstractAnimation.State,
    ): ...

class QAbstractEventDispatcher(PySide2.QtCore.QObject):
    class TimerInfo(Shiboken.Object):
        def __init__(self, id: int, i: int, t: PySide2.QtCore.Qt.TimerType): ...

    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def closingDown(self): ...
    def filterNativeEvent(
        self, eventType: PySide2.QtCore.QByteArray, message: int
    ) -> typing.Tuple: ...
    def flush(self): ...
    def hasPendingEvents(self) -> bool: ...
    def installNativeEventFilter(
        self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter
    ): ...
    @staticmethod
    def instance(
        thread: typing.Optional[PySide2.QtCore.QThread] = ...,
    ) -> PySide2.QtCore.QAbstractEventDispatcher: ...
    def interrupt(self): ...
    def processEvents(
        self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags
    ) -> bool: ...
    def registerEventNotifier(
        self, notifier: PySide2.QtCore.QWinEventNotifier
    ) -> bool: ...
    def registerSocketNotifier(self, notifier: PySide2.QtCore.QSocketNotifier): ...
    @typing.overload
    def registerTimer(
        self,
        interval: int,
        timerType: PySide2.QtCore.Qt.TimerType,
        object: PySide2.QtCore.QObject,
    ) -> int: ...
    @typing.overload
    def registerTimer(
        self,
        timerId: int,
        interval: int,
        timerType: PySide2.QtCore.Qt.TimerType,
        object: PySide2.QtCore.QObject,
    ): ...
    def registeredTimers(self, object: PySide2.QtCore.QObject) -> typing.List: ...
    def remainingTime(self, timerId: int) -> int: ...
    def removeNativeEventFilter(
        self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter
    ): ...
    def startingUp(self): ...
    def unregisterEventNotifier(self, notifier: PySide2.QtCore.QWinEventNotifier): ...
    def unregisterSocketNotifier(self, notifier: PySide2.QtCore.QSocketNotifier): ...
    def unregisterTimer(self, timerId: int) -> bool: ...
    def unregisterTimers(self, object: PySide2.QtCore.QObject) -> bool: ...
    def wakeUp(self): ...

class QAbstractItemModel(PySide2.QtCore.QObject):
    NoLayoutChangeHint: QAbstractItemModel = ...  # 0x0
    VerticalSortHint: QAbstractItemModel = ...  # 0x1
    HorizontalSortHint: QAbstractItemModel = ...  # 0x2

    class CheckIndexOption(object):
        NoOption: QAbstractItemModel.CheckIndexOption = ...  # 0x0
        IndexIsValid: QAbstractItemModel.CheckIndexOption = ...  # 0x1
        DoNotUseParent: QAbstractItemModel.CheckIndexOption = ...  # 0x2
        ParentIsInvalid: QAbstractItemModel.CheckIndexOption = ...  # 0x4

    class CheckIndexOptions(object): ...

    class LayoutChangeHint(object):
        NoLayoutChangeHint: QAbstractItemModel.LayoutChangeHint = ...  # 0x0
        VerticalSortHint: QAbstractItemModel.LayoutChangeHint = ...  # 0x1
        HorizontalSortHint: QAbstractItemModel.LayoutChangeHint = ...  # 0x2
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def beginInsertColumns(
        self, parent: PySide2.QtCore.QModelIndex, first: int, last: int
    ): ...
    def beginInsertRows(
        self, parent: PySide2.QtCore.QModelIndex, first: int, last: int
    ): ...
    def beginMoveColumns(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceFirst: int,
        sourceLast: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationColumn: int,
    ) -> bool: ...
    def beginMoveRows(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceFirst: int,
        sourceLast: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationRow: int,
    ) -> bool: ...
    def beginRemoveColumns(
        self, parent: PySide2.QtCore.QModelIndex, first: int, last: int
    ): ...
    def beginRemoveRows(
        self, parent: PySide2.QtCore.QModelIndex, first: int, last: int
    ): ...
    def beginResetModel(self): ...
    def buddy(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def canDropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool: ...
    def changePersistentIndex(
        self, from_: PySide2.QtCore.QModelIndex, to: PySide2.QtCore.QModelIndex
    ): ...
    def changePersistentIndexList(self, from_: typing.List, to: typing.List): ...
    def checkIndex(
        self,
        index: PySide2.QtCore.QModelIndex,
        options: PySide2.QtCore.QAbstractItemModel.CheckIndexOptions = ...,
    ) -> bool: ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    @typing.overload
    def createIndex(
        self, row: int, column: int, id: int = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    @typing.overload
    def createIndex(
        self, row: int, column: int, ptr: object
    ) -> PySide2.QtCore.QModelIndex: ...
    def data(
        self, index: PySide2.QtCore.QModelIndex, role: int = ...
    ) -> typing.Any: ...
    def decodeData(
        self,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
        stream: PySide2.QtCore.QDataStream,
    ) -> bool: ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def encodeData(self, indexes: typing.List, stream: PySide2.QtCore.QDataStream): ...
    def endInsertColumns(self): ...
    def endInsertRows(self): ...
    def endMoveColumns(self): ...
    def endMoveRows(self): ...
    def endRemoveColumns(self): ...
    def endRemoveRows(self): ...
    def endResetModel(self): ...
    def fetchMore(self, parent: PySide2.QtCore.QModelIndex): ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent: PySide2.QtCore.QModelIndex = ...) -> bool: ...
    def hasIndex(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...
    ) -> typing.Any: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    def insertColumn(
        self, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def insertColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def insertRow(self, row: int, parent: PySide2.QtCore.QModelIndex = ...) -> bool: ...
    def insertRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict: ...
    def match(
        self,
        start: PySide2.QtCore.QModelIndex,
        role: int,
        value: typing.Any,
        hits: int = ...,
        flags: PySide2.QtCore.Qt.MatchFlags = ...,
    ) -> typing.List: ...
    def mimeData(self, indexes: typing.List) -> PySide2.QtCore.QMimeData: ...
    def mimeTypes(self) -> typing.List: ...
    def moveColumn(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceColumn: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    def moveColumns(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceColumn: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    def moveRow(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceRow: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    def moveRows(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceRow: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, child: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def persistentIndexList(self) -> typing.List: ...
    def removeColumn(
        self, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def removeColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def removeRow(self, row: int, parent: PySide2.QtCore.QModelIndex = ...) -> bool: ...
    def removeRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def resetInternalData(self): ...
    def revert(self): ...
    def roleNames(self) -> typing.Dict: ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def setData(
        self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...
    ) -> bool: ...
    def setHeaderData(
        self,
        section: int,
        orientation: PySide2.QtCore.Qt.Orientation,
        value: typing.Any,
        role: int = ...,
    ) -> bool: ...
    def setItemData(
        self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict
    ) -> bool: ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = ...): ...
    def span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize: ...
    def submit(self) -> bool: ...
    def supportedDragActions(self) -> PySide2.QtCore.Qt.DropActions: ...
    def supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions: ...

class QAbstractListModel(PySide2.QtCore.QAbstractItemModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex) -> int: ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent: PySide2.QtCore.QModelIndex) -> bool: ...
    def index(
        self, row: int, column: int = ..., parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, child: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...

class QAbstractNativeEventFilter(Shiboken.Object):
    def __init__(self): ...
    def nativeEventFilter(
        self, eventType: PySide2.QtCore.QByteArray, message: int
    ) -> typing.Tuple: ...

class QAbstractProxyModel(PySide2.QtCore.QAbstractItemModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def buddy(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def canDropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool: ...
    def data(
        self, proxyIndex: PySide2.QtCore.QModelIndex, role: int = ...
    ) -> typing.Any: ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def fetchMore(self, parent: PySide2.QtCore.QModelIndex): ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent: PySide2.QtCore.QModelIndex = ...) -> bool: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...
    ) -> typing.Any: ...
    def itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict: ...
    def mapFromSource(
        self, sourceIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mapSelectionFromSource(
        self, selection: PySide2.QtCore.QItemSelection
    ) -> PySide2.QtCore.QItemSelection: ...
    def mapSelectionToSource(
        self, selection: PySide2.QtCore.QItemSelection
    ) -> PySide2.QtCore.QItemSelection: ...
    def mapToSource(
        self, proxyIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mimeData(self, indexes: typing.List) -> PySide2.QtCore.QMimeData: ...
    def mimeTypes(self) -> typing.List: ...
    def resetInternalData(self): ...
    def revert(self): ...
    def setData(
        self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...
    ) -> bool: ...
    def setHeaderData(
        self,
        section: int,
        orientation: PySide2.QtCore.Qt.Orientation,
        value: typing.Any,
        role: int = ...,
    ) -> bool: ...
    def setItemData(
        self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict
    ) -> bool: ...
    def setSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel): ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = ...): ...
    def sourceModel(self) -> PySide2.QtCore.QAbstractItemModel: ...
    def span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize: ...
    def submit(self) -> bool: ...
    def supportedDragActions(self) -> PySide2.QtCore.Qt.DropActions: ...
    def supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions: ...

class QAbstractState(PySide2.QtCore.QObject):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QState] = ...): ...
    def active(self) -> bool: ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def machine(self) -> PySide2.QtCore.QStateMachine: ...
    def onEntry(self, event: PySide2.QtCore.QEvent): ...
    def onExit(self, event: PySide2.QtCore.QEvent): ...
    def parentState(self) -> PySide2.QtCore.QState: ...

class QAbstractTableModel(PySide2.QtCore.QAbstractItemModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent: PySide2.QtCore.QModelIndex) -> bool: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, child: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...

class QAbstractTransition(PySide2.QtCore.QObject):
    ExternalTransition: QAbstractTransition = ...  # 0x0
    InternalTransition: QAbstractTransition = ...  # 0x1

    class TransitionType(object):
        ExternalTransition: QAbstractTransition.TransitionType = ...  # 0x0
        InternalTransition: QAbstractTransition.TransitionType = ...  # 0x1
    def __init__(self, sourceState: typing.Optional[PySide2.QtCore.QState] = ...): ...
    def addAnimation(self, animation: PySide2.QtCore.QAbstractAnimation): ...
    def animations(self) -> typing.List: ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def eventTest(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def machine(self) -> PySide2.QtCore.QStateMachine: ...
    def onTransition(self, event: PySide2.QtCore.QEvent): ...
    def removeAnimation(self, animation: PySide2.QtCore.QAbstractAnimation): ...
    def setTargetState(self, target: PySide2.QtCore.QAbstractState): ...
    def setTargetStates(self, targets: typing.Sequence): ...
    def setTransitionType(
        self, type: PySide2.QtCore.QAbstractTransition.TransitionType
    ): ...
    def sourceState(self) -> PySide2.QtCore.QState: ...
    def targetState(self) -> PySide2.QtCore.QAbstractState: ...
    def targetStates(self) -> typing.List: ...
    def transitionType(self) -> PySide2.QtCore.QAbstractTransition.TransitionType: ...

class QAnimationGroup(PySide2.QtCore.QAbstractAnimation):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def addAnimation(self, animation: PySide2.QtCore.QAbstractAnimation): ...
    def animationAt(self, index: int) -> PySide2.QtCore.QAbstractAnimation: ...
    def animationCount(self) -> int: ...
    def clear(self): ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def indexOfAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> int: ...
    def insertAnimation(
        self, index: int, animation: PySide2.QtCore.QAbstractAnimation
    ): ...
    def removeAnimation(self, animation: PySide2.QtCore.QAbstractAnimation): ...
    def takeAnimation(self, index: int) -> PySide2.QtCore.QAbstractAnimation: ...

class QBasicMutex(Shiboken.Object):
    def __init__(self): ...
    def isRecursive(self) -> bool: ...
    def lock(self): ...
    def tryLock(self) -> bool: ...
    def try_lock(self) -> bool: ...
    def unlock(self): ...

class QBasicTimer(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QBasicTimer): ...
    def isActive(self) -> bool: ...
    @typing.overload
    def start(self, msec: int, obj: PySide2.QtCore.QObject): ...
    @typing.overload
    def start(
        self,
        msec: int,
        timerType: PySide2.QtCore.Qt.TimerType,
        obj: PySide2.QtCore.QObject,
    ): ...
    def stop(self): ...
    def swap(self, other: PySide2.QtCore.QBasicTimer): ...
    def timerId(self) -> int: ...

class QBitArray(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QBitArray): ...
    @typing.overload
    def __init__(self, size: int, val: bool = ...): ...
    def __and__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray: ...
    def __copy__(self): ...
    def __iand__(
        self, arg__1: PySide2.QtCore.QBitArray
    ) -> PySide2.QtCore.QBitArray: ...
    def __invert__(self) -> PySide2.QtCore.QBitArray: ...
    def __ior__(self, arg__1: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray: ...
    def __ixor__(
        self, arg__1: PySide2.QtCore.QBitArray
    ) -> PySide2.QtCore.QBitArray: ...
    def __or__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray: ...
    def __xor__(self, arg__2: PySide2.QtCore.QBitArray) -> PySide2.QtCore.QBitArray: ...
    def at(self, i: int) -> bool: ...
    def bits(self) -> bytes: ...
    def clear(self): ...
    def clearBit(self, i: int): ...
    @typing.overload
    def count(self) -> int: ...
    @typing.overload
    def count(self, on: bool) -> int: ...
    @typing.overload
    def fill(self, val: bool, first: int, last: int): ...
    @typing.overload
    def fill(self, val: bool, size: int = ...) -> bool: ...
    @staticmethod
    def fromBits(data: bytes, len: int) -> PySide2.QtCore.QBitArray: ...
    def isEmpty(self) -> bool: ...
    def isNull(self) -> bool: ...
    def resize(self, size: int): ...
    @typing.overload
    def setBit(self, i: int): ...
    @typing.overload
    def setBit(self, i: int, val: bool): ...
    def size(self) -> int: ...
    def swap(self, other: PySide2.QtCore.QBitArray): ...
    def testBit(self, i: int) -> bool: ...
    def toggleBit(self, i: int) -> bool: ...
    def truncate(self, pos: int): ...

class QBuffer(PySide2.QtCore.QIODevice):
    @typing.overload
    def __init__(
        self,
        buf: PySide2.QtCore.QByteArray,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def atEnd(self) -> bool: ...
    def buffer(self) -> PySide2.QtCore.QByteArray: ...
    def canReadLine(self) -> bool: ...
    def close(self): ...
    def connectNotify(self, arg__1: PySide2.QtCore.QMetaMethod): ...
    def data(self) -> PySide2.QtCore.QByteArray: ...
    def disconnectNotify(self, arg__1: PySide2.QtCore.QMetaMethod): ...
    def open(self, openMode: PySide2.QtCore.QIODevice.OpenMode) -> bool: ...
    def pos(self) -> int: ...
    def readData(self, data: bytes, maxlen: int) -> int: ...
    def seek(self, off: int) -> bool: ...
    def setBuffer(self, a: PySide2.QtCore.QByteArray): ...
    def setData(self, data: PySide2.QtCore.QByteArray): ...
    def size(self) -> int: ...
    def writeData(self, data: bytes, len: int) -> int: ...

class QByteArray(Shiboken.Object):
    Base64Encoding: QByteArray = ...  # 0x0
    IgnoreBase64DecodingErrors: QByteArray = ...  # 0x0
    KeepTrailingEquals: QByteArray = ...  # 0x0
    Base64UrlEncoding: QByteArray = ...  # 0x1
    OmitTrailingEquals: QByteArray = ...  # 0x2
    AbortOnBase64DecodingErrors: QByteArray = ...  # 0x4

    class Base64Option(object):
        Base64Encoding: QByteArray.Base64Option = ...  # 0x0
        IgnoreBase64DecodingErrors: QByteArray.Base64Option = ...  # 0x0
        KeepTrailingEquals: QByteArray.Base64Option = ...  # 0x0
        Base64UrlEncoding: QByteArray.Base64Option = ...  # 0x1
        OmitTrailingEquals: QByteArray.Base64Option = ...  # 0x2
        AbortOnBase64DecodingErrors: QByteArray.Base64Option = ...  # 0x4

    class Base64Options(object): ...

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: bytearray): ...
    @typing.overload
    def __init__(self, arg__1: bytes): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, size: int, c: int): ...
    @typing.overload
    def __add__(self, a2: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def __add__(self, a2: int) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def __add__(self, arg__1: bytearray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def __add__(self, arg__1: bytes): ...
    def __copy__(self): ...
    @typing.overload
    def __iadd__(self, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def __iadd__(self, arg__1: bytearray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def __iadd__(self, c: int) -> PySide2.QtCore.QByteArray: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __str__(self) -> object: ...
    @typing.overload
    def append(self, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def append(self, c: int) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def append(self, count: int, c: int) -> PySide2.QtCore.QByteArray: ...
    def at(self, i: int) -> int: ...
    def back(self) -> int: ...
    def capacity(self) -> int: ...
    def cbegin(self) -> bytes: ...
    def cend(self) -> bytes: ...
    def chop(self, n: int): ...
    def chopped(self, len: int) -> PySide2.QtCore.QByteArray: ...
    def clear(self): ...
    @typing.overload
    def compare(
        self, a: PySide2.QtCore.QByteArray, cs: PySide2.QtCore.Qt.CaseSensitivity = ...
    ) -> int: ...
    @typing.overload
    def compare(self, c: bytes, cs: PySide2.QtCore.Qt.CaseSensitivity = ...) -> int: ...
    @typing.overload
    def contains(self, a: PySide2.QtCore.QByteArray) -> bool: ...
    @typing.overload
    def contains(self, c: int) -> bool: ...
    @typing.overload
    def count(self) -> int: ...
    @typing.overload
    def count(self, a: PySide2.QtCore.QByteArray) -> int: ...
    @typing.overload
    def count(self, c: int) -> int: ...
    def data(self) -> bytes: ...
    @typing.overload
    def endsWith(self, a: PySide2.QtCore.QByteArray) -> bool: ...
    @typing.overload
    def endsWith(self, c: int) -> bool: ...
    def fill(self, c: int, size: int = ...) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def fromBase64(base64: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def fromBase64(
        base64: PySide2.QtCore.QByteArray,
        options: PySide2.QtCore.QByteArray.Base64Options,
    ) -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def fromHex(hexEncoded: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def fromPercentEncoding(
        pctEncoded: PySide2.QtCore.QByteArray, percent: int = ...
    ) -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def fromRawData(arg__1: bytes, size: int) -> PySide2.QtCore.QByteArray: ...
    def front(self) -> int: ...
    def indexOf(self, a: PySide2.QtCore.QByteArray, from_: int = ...) -> int: ...
    @typing.overload
    def insert(
        self, i: int, a: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def insert(self, i: int, count: int, c: int) -> PySide2.QtCore.QByteArray: ...
    def isEmpty(self) -> bool: ...
    def isLower(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isSharedWith(self, other: PySide2.QtCore.QByteArray) -> bool: ...
    def isUpper(self) -> bool: ...
    def lastIndexOf(self, a: PySide2.QtCore.QByteArray, from_: int = ...) -> int: ...
    def left(self, len: int) -> PySide2.QtCore.QByteArray: ...
    def leftJustified(
        self, width: int, fill: int = ..., truncate: bool = ...
    ) -> PySide2.QtCore.QByteArray: ...
    def length(self) -> int: ...
    def mid(self, index: int, len: int = ...) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def number(
        arg__1: float, f: int = ..., prec: int = ...
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def number(arg__1: int, base: int = ...) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def number(arg__1: int, base: int = ...) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def prepend(self, a: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def prepend(self, c: int) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def prepend(self, count: int, c: int) -> PySide2.QtCore.QByteArray: ...
    def remove(self, index: int, len: int) -> PySide2.QtCore.QByteArray: ...
    def repeated(self, times: int) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def replace(
        self, before: PySide2.QtCore.QByteArray, after: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def replace(
        self, before: str, after: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def replace(
        self, before: int, after: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def replace(self, before: int, after: int) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def replace(
        self, index: int, len: int, s: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QByteArray: ...
    def reserve(self, size: int): ...
    def resize(self, size: int): ...
    def right(self, len: int) -> PySide2.QtCore.QByteArray: ...
    def rightJustified(
        self, width: int, fill: int = ..., truncate: bool = ...
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def setNum(
        self, arg__1: float, f: int = ..., prec: int = ...
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def setNum(self, arg__1: int, base: int = ...) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def setNum(self, arg__1: int, base: int = ...) -> PySide2.QtCore.QByteArray: ...
    def setRawData(self, a: bytes, n: int) -> PySide2.QtCore.QByteArray: ...
    def shrink_to_fit(self): ...
    def simplified(self) -> PySide2.QtCore.QByteArray: ...
    def size(self) -> int: ...
    def split(self, sep: int) -> typing.List: ...
    def squeeze(self): ...
    @typing.overload
    def startsWith(self, a: PySide2.QtCore.QByteArray) -> bool: ...
    @typing.overload
    def startsWith(self, c: int) -> bool: ...
    def swap(self, other: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def toBase64(self) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toBase64(
        self, options: PySide2.QtCore.QByteArray.Base64Options
    ) -> PySide2.QtCore.QByteArray: ...
    def toDouble(self) -> typing.Tuple: ...
    def toFloat(self) -> typing.Tuple: ...
    @typing.overload
    def toHex(self) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toHex(self, separator: int) -> PySide2.QtCore.QByteArray: ...
    def toInt(self, base: int = ...) -> typing.Tuple: ...
    def toLong(self, base: int = ...) -> typing.Tuple: ...
    def toLongLong(self, base: int = ...) -> typing.Tuple: ...
    def toLower(self) -> PySide2.QtCore.QByteArray: ...
    def toPercentEncoding(
        self,
        exclude: PySide2.QtCore.QByteArray = ...,
        include: PySide2.QtCore.QByteArray = ...,
        percent: int = ...,
    ) -> PySide2.QtCore.QByteArray: ...
    def toShort(self, base: int = ...) -> typing.Tuple: ...
    def toUInt(self, base: int = ...) -> typing.Tuple: ...
    def toULong(self, base: int = ...) -> typing.Tuple: ...
    def toULongLong(self, base: int = ...) -> typing.Tuple: ...
    def toUShort(self, base: int = ...) -> typing.Tuple: ...
    def toUpper(self) -> PySide2.QtCore.QByteArray: ...
    def trimmed(self) -> PySide2.QtCore.QByteArray: ...
    def truncate(self, pos: int): ...

class QByteArrayMatcher(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QByteArrayMatcher): ...
    @typing.overload
    def __init__(self, pattern: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, pattern: bytes, length: int): ...
    def __copy__(self): ...
    @typing.overload
    def indexIn(self, ba: PySide2.QtCore.QByteArray, from_: int = ...) -> int: ...
    @typing.overload
    def indexIn(self, str: bytes, len: int, from_: int = ...) -> int: ...
    def pattern(self) -> PySide2.QtCore.QByteArray: ...
    def setPattern(self, pattern: PySide2.QtCore.QByteArray): ...

class QCalendar(Shiboken.Object):
    class System(object):
        User: QCalendar.System = ...  # -0x1
        Gregorian: QCalendar.System = ...  # 0x0
        Julian: QCalendar.System = ...  # 0x8
        Milankovic: QCalendar.System = ...  # 0x9
        Jalali: QCalendar.System = ...  # 0xa
        IslamicCivil: QCalendar.System = ...  # 0xb
        Last: QCalendar.System = ...  # 0xb

    class YearMonthDay(Shiboken.Object):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, YearMonthDay: PySide2.QtCore.QCalendar.YearMonthDay): ...
        @typing.overload
        def __init__(self, y: int, m: int = ..., d: int = ...): ...
        def __copy__(self): ...
        def isValid(self) -> bool: ...

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, system: PySide2.QtCore.QCalendar.System): ...
    def __copy__(self): ...
    @staticmethod
    def availableCalendars() -> typing.List: ...
    @typing.overload
    def dateFromParts(
        self, parts: PySide2.QtCore.QCalendar.YearMonthDay
    ) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def dateFromParts(
        self, year: int, month: int, day: int
    ) -> PySide2.QtCore.QDate: ...
    def dayOfWeek(self, date: PySide2.QtCore.QDate) -> int: ...
    def daysInMonth(self, month: int, year: typing.Optional[int] = ...) -> int: ...
    def daysInYear(self, year: int) -> int: ...
    def hasYearZero(self) -> bool: ...
    def isDateValid(self, year: int, month: int, day: int) -> bool: ...
    def isGregorian(self) -> bool: ...
    def isLeapYear(self, year: int) -> bool: ...
    def isLunar(self) -> bool: ...
    def isLuniSolar(self) -> bool: ...
    def isProleptic(self) -> bool: ...
    def isSolar(self) -> bool: ...
    def isValid(self) -> bool: ...
    def maximumDaysInMonth(self) -> int: ...
    def maximumMonthsInYear(self) -> int: ...
    def minimumDaysInMonth(self) -> int: ...
    def monthName(
        self,
        locale: PySide2.QtCore.QLocale,
        month: int,
        year: typing.Optional[int] = ...,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...
    def monthsInYear(self, year: int) -> int: ...
    def name(self) -> str: ...
    def partsFromDate(
        self, date: PySide2.QtCore.QDate
    ) -> PySide2.QtCore.QCalendar.YearMonthDay: ...
    def standaloneMonthName(
        self,
        locale: PySide2.QtCore.QLocale,
        month: int,
        year: typing.Optional[int] = ...,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...
    def standaloneWeekDayName(
        self,
        locale: PySide2.QtCore.QLocale,
        day: int,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...
    def weekDayName(
        self,
        locale: PySide2.QtCore.QLocale,
        day: int,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...

class QCborArray(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QCborArray): ...
    def __add__(self, v: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QCborArray: ...
    def __copy__(self): ...
    def __iadd__(self, v: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QCborArray: ...
    def __lshift__(self, v: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QCborArray: ...
    def append(self, value: PySide2.QtCore.QCborValue): ...
    def at(self, i: int) -> PySide2.QtCore.QCborValue: ...
    def clear(self): ...
    def compare(self, other: PySide2.QtCore.QCborArray) -> int: ...
    def contains(self, value: PySide2.QtCore.QCborValue) -> bool: ...
    def empty(self) -> bool: ...
    def first(self) -> PySide2.QtCore.QCborValue: ...
    @staticmethod
    def fromJsonArray(
        array: PySide2.QtCore.QJsonArray,
    ) -> PySide2.QtCore.QCborArray: ...
    @staticmethod
    def fromStringList(list: typing.Sequence) -> PySide2.QtCore.QCborArray: ...
    @staticmethod
    def fromVariantList(list: typing.Sequence) -> PySide2.QtCore.QCborArray: ...
    def insert(self, i: int, value: PySide2.QtCore.QCborValue): ...
    def isEmpty(self) -> bool: ...
    def last(self) -> PySide2.QtCore.QCborValue: ...
    def pop_back(self): ...
    def pop_front(self): ...
    def prepend(self, value: PySide2.QtCore.QCborValue): ...
    def push_back(self, t: PySide2.QtCore.QCborValue): ...
    def push_front(self, t: PySide2.QtCore.QCborValue): ...
    def removeAt(self, i: int): ...
    def removeFirst(self): ...
    def removeLast(self): ...
    def size(self) -> int: ...
    def swap(self, other: PySide2.QtCore.QCborArray): ...
    def takeAt(self, i: int) -> PySide2.QtCore.QCborValue: ...
    def takeFirst(self) -> PySide2.QtCore.QCborValue: ...
    def takeLast(self) -> PySide2.QtCore.QCborValue: ...
    def toCborValue(self) -> PySide2.QtCore.QCborValue: ...
    def toJsonArray(self) -> PySide2.QtCore.QJsonArray: ...
    def toVariantList(self) -> typing.List: ...

class QCborError(Shiboken.Object):
    NoError: QCborError = ...  # 0x0
    UnknownError: QCborError = ...  # 0x1
    AdvancePastEnd: QCborError = ...  # 0x3
    InputOutputError: QCborError = ...  # 0x4
    GarbageAtEnd: QCborError = ...  # 0x100
    EndOfFile: QCborError = ...  # 0x101
    UnexpectedBreak: QCborError = ...  # 0x102
    UnknownType: QCborError = ...  # 0x103
    IllegalType: QCborError = ...  # 0x104
    IllegalNumber: QCborError = ...  # 0x105
    IllegalSimpleType: QCborError = ...  # 0x106
    InvalidUtf8String: QCborError = ...  # 0x204
    DataTooLarge: QCborError = ...  # 0x400
    NestingTooDeep: QCborError = ...  # 0x401
    UnsupportedType: QCborError = ...  # 0x402

    class Code(object):
        NoError: QCborError.Code = ...  # 0x0
        UnknownError: QCborError.Code = ...  # 0x1
        AdvancePastEnd: QCborError.Code = ...  # 0x3
        InputOutputError: QCborError.Code = ...  # 0x4
        GarbageAtEnd: QCborError.Code = ...  # 0x100
        EndOfFile: QCborError.Code = ...  # 0x101
        UnexpectedBreak: QCborError.Code = ...  # 0x102
        UnknownType: QCborError.Code = ...  # 0x103
        IllegalType: QCborError.Code = ...  # 0x104
        IllegalNumber: QCborError.Code = ...  # 0x105
        IllegalSimpleType: QCborError.Code = ...  # 0x106
        InvalidUtf8String: QCborError.Code = ...  # 0x204
        DataTooLarge: QCborError.Code = ...  # 0x400
        NestingTooDeep: QCborError.Code = ...  # 0x401
        UnsupportedType: QCborError.Code = ...  # 0x402
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QCborError: PySide2.QtCore.QCborError): ...
    def __copy__(self): ...
    def toString(self) -> str: ...

class QCborKnownTags(object):
    DateTimeString: QCborKnownTags = ...  # 0x0
    UnixTime_t: QCborKnownTags = ...  # 0x1
    PositiveBignum: QCborKnownTags = ...  # 0x2
    NegativeBignum: QCborKnownTags = ...  # 0x3
    Decimal: QCborKnownTags = ...  # 0x4
    Bigfloat: QCborKnownTags = ...  # 0x5
    COSE_Encrypt0: QCborKnownTags = ...  # 0x10
    COSE_Mac0: QCborKnownTags = ...  # 0x11
    COSE_Sign1: QCborKnownTags = ...  # 0x12
    ExpectedBase64url: QCborKnownTags = ...  # 0x15
    ExpectedBase64: QCborKnownTags = ...  # 0x16
    ExpectedBase16: QCborKnownTags = ...  # 0x17
    EncodedCbor: QCborKnownTags = ...  # 0x18
    Url: QCborKnownTags = ...  # 0x20
    Base64url: QCborKnownTags = ...  # 0x21
    Base64: QCborKnownTags = ...  # 0x22
    RegularExpression: QCborKnownTags = ...  # 0x23
    MimeMessage: QCborKnownTags = ...  # 0x24
    Uuid: QCborKnownTags = ...  # 0x25
    COSE_Encrypt: QCborKnownTags = ...  # 0x60
    COSE_Mac: QCborKnownTags = ...  # 0x61
    COSE_Sign: QCborKnownTags = ...  # 0x62
    Signature: QCborKnownTags = ...  # 0xd9f7

class QCborMap(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QCborMap): ...
    def __copy__(self): ...
    def clear(self): ...
    def compare(self, other: PySide2.QtCore.QCborMap) -> int: ...
    @typing.overload
    def contains(self, key: PySide2.QtCore.QCborValue) -> bool: ...
    @typing.overload
    def contains(self, key: str) -> bool: ...
    @typing.overload
    def contains(self, key: int) -> bool: ...
    def empty(self) -> bool: ...
    @staticmethod
    def fromJsonObject(o: typing.Dict) -> PySide2.QtCore.QCborMap: ...
    @staticmethod
    def fromVariantHash(hash: typing.Dict) -> PySide2.QtCore.QCborMap: ...
    @staticmethod
    def fromVariantMap(map: typing.Dict) -> PySide2.QtCore.QCborMap: ...
    def isEmpty(self) -> bool: ...
    def keys(self) -> typing.List: ...
    @typing.overload
    def remove(self, key: PySide2.QtCore.QCborValue): ...
    @typing.overload
    def remove(self, key: str): ...
    @typing.overload
    def remove(self, key: int): ...
    def size(self) -> int: ...
    def swap(self, other: PySide2.QtCore.QCborMap): ...
    @typing.overload
    def take(self, key: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    def take(self, key: str) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    def take(self, key: int) -> PySide2.QtCore.QCborValue: ...
    def toCborValue(self) -> PySide2.QtCore.QCborValue: ...
    def toJsonObject(self) -> typing.Dict: ...
    def toVariantHash(self) -> typing.Dict: ...
    def toVariantMap(self) -> typing.Dict: ...
    @typing.overload
    def value(self, key: PySide2.QtCore.QCborValue) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    def value(self, key: str) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    def value(self, key: int) -> PySide2.QtCore.QCborValue: ...

class QCborParserError(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QCborParserError: PySide2.QtCore.QCborParserError): ...
    def __copy__(self): ...
    def errorString(self) -> str: ...

class QCborSimpleType(object):
    False_: QCborSimpleType = ...  # 0x14
    True_: QCborSimpleType = ...  # 0x15
    Null: QCborSimpleType = ...  # 0x16
    Undefined: QCborSimpleType = ...  # 0x17

class QCborStreamReader(Shiboken.Object):
    Error: QCborStreamReader = ...  # -0x1
    EndOfString: QCborStreamReader = ...  # 0x0
    UnsignedInteger: QCborStreamReader = ...  # 0x0
    Ok: QCborStreamReader = ...  # 0x1
    NegativeInteger: QCborStreamReader = ...  # 0x20
    ByteArray: QCborStreamReader = ...  # 0x40
    ByteString: QCborStreamReader = ...  # 0x40
    String: QCborStreamReader = ...  # 0x60
    TextString: QCborStreamReader = ...  # 0x60
    Array: QCborStreamReader = ...  # 0x80
    Map: QCborStreamReader = ...  # 0xa0
    Tag: QCborStreamReader = ...  # 0xc0
    SimpleType: QCborStreamReader = ...  # 0xe0
    Float16: QCborStreamReader = ...  # 0xf9
    HalfFloat: QCborStreamReader = ...  # 0xf9
    Float: QCborStreamReader = ...  # 0xfa
    Double: QCborStreamReader = ...  # 0xfb
    Invalid: QCborStreamReader = ...  # 0xff

    class StringResultCode(object):
        Error: QCborStreamReader.StringResultCode = ...  # -0x1
        EndOfString: QCborStreamReader.StringResultCode = ...  # 0x0
        Ok: QCborStreamReader.StringResultCode = ...  # 0x1

    class Type(object):
        UnsignedInteger: QCborStreamReader.Type = ...  # 0x0
        NegativeInteger: QCborStreamReader.Type = ...  # 0x20
        ByteArray: QCborStreamReader.Type = ...  # 0x40
        ByteString: QCborStreamReader.Type = ...  # 0x40
        String: QCborStreamReader.Type = ...  # 0x60
        TextString: QCborStreamReader.Type = ...  # 0x60
        Array: QCborStreamReader.Type = ...  # 0x80
        Map: QCborStreamReader.Type = ...  # 0xa0
        Tag: QCborStreamReader.Type = ...  # 0xc0
        SimpleType: QCborStreamReader.Type = ...  # 0xe0
        Float16: QCborStreamReader.Type = ...  # 0xf9
        HalfFloat: QCborStreamReader.Type = ...  # 0xf9
        Float: QCborStreamReader.Type = ...  # 0xfa
        Double: QCborStreamReader.Type = ...  # 0xfb
        Invalid: QCborStreamReader.Type = ...  # 0xff
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, data: bytes, len: int): ...
    @typing.overload
    def __init__(self, data: bytearray, len: int): ...
    @typing.overload
    def __init__(self, device: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def addData(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def addData(self, data: bytes, len: int): ...
    @typing.overload
    def addData(self, data: bytearray, len: int): ...
    def clear(self): ...
    def containerDepth(self) -> int: ...
    def currentOffset(self) -> int: ...
    def currentStringChunkSize(self) -> int: ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def enterContainer(self) -> bool: ...
    def hasNext(self) -> bool: ...
    def isArray(self) -> bool: ...
    def isBool(self) -> bool: ...
    def isByteArray(self) -> bool: ...
    def isContainer(self) -> bool: ...
    def isDouble(self) -> bool: ...
    def isFalse(self) -> bool: ...
    def isFloat(self) -> bool: ...
    def isFloat16(self) -> bool: ...
    def isInteger(self) -> bool: ...
    def isInvalid(self) -> bool: ...
    def isLengthKnown(self) -> bool: ...
    def isMap(self) -> bool: ...
    def isNegativeInteger(self) -> bool: ...
    def isNull(self) -> bool: ...
    @typing.overload
    def isSimpleType(self) -> bool: ...
    @typing.overload
    def isSimpleType(self, st: PySide2.QtCore.QCborSimpleType) -> bool: ...
    def isString(self) -> bool: ...
    def isTag(self) -> bool: ...
    def isTrue(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def isUnsignedInteger(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastError(self) -> PySide2.QtCore.QCborError: ...
    def leaveContainer(self) -> bool: ...
    def length(self) -> int: ...
    def next(self, maxRecursion: int = ...) -> bool: ...
    def parentContainerType(self) -> PySide2.QtCore.QCborStreamReader.Type: ...
    def readByteArray(self) -> PySide2.QtCore.QCborStringResultByteArray: ...
    def readString(self) -> PySide2.QtCore.QCborStringResultString: ...
    def reparse(self): ...
    def reset(self): ...
    def setDevice(self, device: PySide2.QtCore.QIODevice): ...
    def toBool(self) -> bool: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInteger(self) -> int: ...
    def toSimpleType(self) -> PySide2.QtCore.QCborSimpleType: ...
    def toUnsignedInteger(self) -> int: ...
    def type(self) -> PySide2.QtCore.QCborStreamReader.Type: ...

class QCborStreamWriter(Shiboken.Object):
    @typing.overload
    def __init__(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, device: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def append(self, b: bool): ...
    @typing.overload
    def append(self, ba: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def append(self, d: float): ...
    @typing.overload
    def append(self, f: float): ...
    @typing.overload
    def append(self, i: int): ...
    @typing.overload
    def append(self, i: int): ...
    @typing.overload
    def append(self, st: PySide2.QtCore.QCborSimpleType): ...
    @typing.overload
    def append(self, str: bytes, size: int = ...): ...
    @typing.overload
    def append(self, tag: PySide2.QtCore.QCborKnownTags): ...
    @typing.overload
    def append(self, u: int): ...
    @typing.overload
    def append(self, u: int): ...
    def appendByteString(self, data: bytes, len: int): ...
    def appendNull(self): ...
    def appendTextString(self, utf8: bytes, len: int): ...
    def appendUndefined(self): ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def endArray(self) -> bool: ...
    def endMap(self) -> bool: ...
    def setDevice(self, device: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def startArray(self): ...
    @typing.overload
    def startArray(self, count: int): ...
    @typing.overload
    def startMap(self): ...
    @typing.overload
    def startMap(self, count: int): ...

class QCborStringResultByteArray(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self, QCborStringResultByteArray: PySide2.QtCore.QCborStringResultByteArray
    ): ...
    def __copy__(self): ...

class QCborStringResultString(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self, QCborStringResultString: PySide2.QtCore.QCborStringResultString
    ): ...
    def __copy__(self): ...

class QCborValue(Shiboken.Object):
    Invalid: QCborValue = ...  # -0x1
    Compact: QCborValue = ...  # 0x0
    Integer: QCborValue = ...  # 0x0
    NoTransformation: QCborValue = ...  # 0x0
    LineWrapped: QCborValue = ...  # 0x1
    SortKeysInMaps: QCborValue = ...  # 0x1
    ExtendedFormat: QCborValue = ...  # 0x2
    UseFloat: QCborValue = ...  # 0x2
    UseFloat16: QCborValue = ...  # 0x6
    UseIntegers: QCborValue = ...  # 0x8
    ByteArray: QCborValue = ...  # 0x40
    String: QCborValue = ...  # 0x60
    Array: QCborValue = ...  # 0x80
    Map: QCborValue = ...  # 0xa0
    Tag: QCborValue = ...  # 0xc0
    SimpleType: QCborValue = ...  # 0x100
    False_: QCborValue = ...  # 0x114
    True_: QCborValue = ...  # 0x115
    Null: QCborValue = ...  # 0x116
    Undefined: QCborValue = ...  # 0x117
    Double: QCborValue = ...  # 0x202
    DateTime: QCborValue = ...  # 0x10000
    Url: QCborValue = ...  # 0x10020
    RegularExpression: QCborValue = ...  # 0x10023
    Uuid: QCborValue = ...  # 0x10025

    class DiagnosticNotationOption(object):
        Compact: QCborValue.DiagnosticNotationOption = ...  # 0x0
        LineWrapped: QCborValue.DiagnosticNotationOption = ...  # 0x1
        ExtendedFormat: QCborValue.DiagnosticNotationOption = ...  # 0x2

    class DiagnosticNotationOptions(object): ...

    class EncodingOption(object):
        NoTransformation: QCborValue.EncodingOption = ...  # 0x0
        SortKeysInMaps: QCborValue.EncodingOption = ...  # 0x1
        UseFloat: QCborValue.EncodingOption = ...  # 0x2
        UseFloat16: QCborValue.EncodingOption = ...  # 0x6
        UseIntegers: QCborValue.EncodingOption = ...  # 0x8

    class EncodingOptions(object): ...

    class Type(object):
        Invalid: QCborValue.Type = ...  # -0x1
        Integer: QCborValue.Type = ...  # 0x0
        ByteArray: QCborValue.Type = ...  # 0x40
        String: QCborValue.Type = ...  # 0x60
        Array: QCborValue.Type = ...  # 0x80
        Map: QCborValue.Type = ...  # 0xa0
        Tag: QCborValue.Type = ...  # 0xc0
        SimpleType: QCborValue.Type = ...  # 0x100
        False_: QCborValue.Type = ...  # 0x114
        True_: QCborValue.Type = ...  # 0x115
        Null: QCborValue.Type = ...  # 0x116
        Undefined: QCborValue.Type = ...  # 0x117
        Double: QCborValue.Type = ...  # 0x202
        DateTime: QCborValue.Type = ...  # 0x10000
        Url: QCborValue.Type = ...  # 0x10020
        RegularExpression: QCborValue.Type = ...  # 0x10023
        Uuid: QCborValue.Type = ...  # 0x10025
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, a: PySide2.QtCore.QCborArray): ...
    @typing.overload
    def __init__(self, b_: bool): ...
    @typing.overload
    def __init__(self, ba: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, dt: PySide2.QtCore.QDateTime): ...
    @typing.overload
    def __init__(self, i: int): ...
    @typing.overload
    def __init__(self, i: int): ...
    @typing.overload
    def __init__(self, m: PySide2.QtCore.QCborMap): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QCborValue): ...
    @typing.overload
    def __init__(self, rx: PySide2.QtCore.QRegularExpression): ...
    @typing.overload
    def __init__(self, s: str): ...
    @typing.overload
    def __init__(self, s: bytes): ...
    @typing.overload
    def __init__(self, st: PySide2.QtCore.QCborSimpleType): ...
    @typing.overload
    def __init__(
        self, t_: PySide2.QtCore.QCborKnownTags, tv: PySide2.QtCore.QCborValue = ...
    ): ...
    @typing.overload
    def __init__(self, t_: PySide2.QtCore.QCborValue.Type): ...
    @typing.overload
    def __init__(self, u: int): ...
    @typing.overload
    def __init__(self, url: PySide2.QtCore.QUrl): ...
    @typing.overload
    def __init__(self, uuid: PySide2.QtCore.QUuid): ...
    @typing.overload
    def __init__(self, v: float): ...
    def __copy__(self): ...
    def compare(self, other: PySide2.QtCore.QCborValue) -> int: ...
    @typing.overload
    @staticmethod
    def fromCbor(
        ba: PySide2.QtCore.QByteArray,
        error: typing.Optional[PySide2.QtCore.QCborParserError] = ...,
    ) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    @staticmethod
    def fromCbor(
        data: bytes,
        len: int,
        error: typing.Optional[PySide2.QtCore.QCborParserError] = ...,
    ) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    @staticmethod
    def fromCbor(
        data: bytearray,
        len: int,
        error: typing.Optional[PySide2.QtCore.QCborParserError] = ...,
    ) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    @staticmethod
    def fromCbor(
        reader: PySide2.QtCore.QCborStreamReader,
    ) -> PySide2.QtCore.QCborValue: ...
    @staticmethod
    def fromJsonValue(v: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QCborValue: ...
    @staticmethod
    def fromVariant(variant: typing.Any) -> PySide2.QtCore.QCborValue: ...
    def isArray(self) -> bool: ...
    def isBool(self) -> bool: ...
    def isByteArray(self) -> bool: ...
    def isContainer(self) -> bool: ...
    def isDateTime(self) -> bool: ...
    def isDouble(self) -> bool: ...
    def isFalse(self) -> bool: ...
    def isInteger(self) -> bool: ...
    def isInvalid(self) -> bool: ...
    def isMap(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isRegularExpression(self) -> bool: ...
    @typing.overload
    def isSimpleType(self) -> bool: ...
    @typing.overload
    def isSimpleType(self, st: PySide2.QtCore.QCborSimpleType) -> bool: ...
    def isString(self) -> bool: ...
    def isTag(self) -> bool: ...
    def isTrue(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def isUrl(self) -> bool: ...
    def isUuid(self) -> bool: ...
    def swap(self, other: PySide2.QtCore.QCborValue): ...
    def taggedValue(
        self, defaultValue: PySide2.QtCore.QCborValue = ...
    ) -> PySide2.QtCore.QCborValue: ...
    @typing.overload
    def toArray(self) -> PySide2.QtCore.QCborArray: ...
    @typing.overload
    def toArray(
        self, defaultValue: PySide2.QtCore.QCborArray
    ) -> PySide2.QtCore.QCborArray: ...
    def toBool(self, defaultValue: bool = ...) -> bool: ...
    def toByteArray(
        self, defaultValue: PySide2.QtCore.QByteArray = ...
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toCbor(
        self, opt: PySide2.QtCore.QCborValue.EncodingOptions = ...
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toCbor(
        self,
        writer: PySide2.QtCore.QCborStreamWriter,
        opt: PySide2.QtCore.QCborValue.EncodingOptions = ...,
    ): ...
    def toDateTime(
        self, defaultValue: PySide2.QtCore.QDateTime = ...
    ) -> PySide2.QtCore.QDateTime: ...
    def toDiagnosticNotation(
        self, opts: PySide2.QtCore.QCborValue.DiagnosticNotationOptions = ...
    ) -> str: ...
    def toDouble(self, defaultValue: float = ...) -> float: ...
    def toInteger(self, defaultValue: int = ...) -> int: ...
    def toJsonValue(self) -> PySide2.QtCore.QJsonValue: ...
    @typing.overload
    def toMap(self) -> PySide2.QtCore.QCborMap: ...
    @typing.overload
    def toMap(
        self, defaultValue: PySide2.QtCore.QCborMap
    ) -> PySide2.QtCore.QCborMap: ...
    def toRegularExpression(
        self, defaultValue: PySide2.QtCore.QRegularExpression = ...
    ) -> PySide2.QtCore.QRegularExpression: ...
    def toSimpleType(
        self, defaultValue: PySide2.QtCore.QCborSimpleType = ...
    ) -> PySide2.QtCore.QCborSimpleType: ...
    def toString(self, defaultValue: str = ...) -> str: ...
    def toUrl(self, defaultValue: PySide2.QtCore.QUrl = ...) -> PySide2.QtCore.QUrl: ...
    def toUuid(
        self, defaultValue: PySide2.QtCore.QUuid = ...
    ) -> PySide2.QtCore.QUuid: ...
    def toVariant(self) -> typing.Any: ...
    def type(self) -> PySide2.QtCore.QCborValue.Type: ...

class QChildEvent(PySide2.QtCore.QEvent):
    def __init__(
        self, type: PySide2.QtCore.QEvent.Type, child: PySide2.QtCore.QObject
    ): ...
    def added(self) -> bool: ...
    def child(self) -> PySide2.QtCore.QObject: ...
    def polished(self) -> bool: ...
    def removed(self) -> bool: ...

class QCollator(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QCollator): ...
    @typing.overload
    def __init__(self, locale: PySide2.QtCore.QLocale): ...
    def __call__(self, s1: str, s2: str) -> bool: ...
    def caseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity: ...
    @typing.overload
    def compare(self, s1: bytes, len1: int, s2: bytes, len2: int) -> int: ...
    @typing.overload
    def compare(self, s1: str, s2: str) -> int: ...
    @typing.overload
    def compare(self, s1: str, s2: str) -> int: ...
    def ignorePunctuation(self) -> bool: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def numericMode(self) -> bool: ...
    def setCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity): ...
    def setIgnorePunctuation(self, on: bool): ...
    def setLocale(self, locale: PySide2.QtCore.QLocale): ...
    def setNumericMode(self, on: bool): ...
    def sortKey(self, string: str) -> PySide2.QtCore.QCollatorSortKey: ...
    def swap(self, other: PySide2.QtCore.QCollator): ...

class QCollatorSortKey(Shiboken.Object):
    def __init__(self, other: PySide2.QtCore.QCollatorSortKey): ...
    def compare(self, key: PySide2.QtCore.QCollatorSortKey) -> int: ...
    def swap(self, other: PySide2.QtCore.QCollatorSortKey): ...

class QCommandLineOption(Shiboken.Object):
    HiddenFromHelp: QCommandLineOption = ...  # 0x1
    ShortOptionStyle: QCommandLineOption = ...  # 0x2

    class Flag(object):
        HiddenFromHelp: QCommandLineOption.Flag = ...  # 0x1
        ShortOptionStyle: QCommandLineOption.Flag = ...  # 0x2

    class Flags(object): ...

    @typing.overload
    def __init__(self, name: str): ...
    @typing.overload
    def __init__(
        self, name: str, description: str, valueName: str = ..., defaultValue: str = ...
    ): ...
    @typing.overload
    def __init__(self, names: typing.Sequence): ...
    @typing.overload
    def __init__(
        self,
        names: typing.Sequence,
        description: str,
        valueName: str = ...,
        defaultValue: str = ...,
    ): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QCommandLineOption): ...
    def defaultValues(self) -> typing.List: ...
    def description(self) -> str: ...
    def flags(self) -> PySide2.QtCore.QCommandLineOption.Flags: ...
    def isHidden(self) -> bool: ...
    def names(self) -> typing.List: ...
    def setDefaultValue(self, defaultValue: str): ...
    def setDefaultValues(self, defaultValues: typing.Sequence): ...
    def setDescription(self, description: str): ...
    def setFlags(self, aflags: PySide2.QtCore.QCommandLineOption.Flags): ...
    def setHidden(self, hidden: bool): ...
    def setValueName(self, name: str): ...
    def swap(self, other: PySide2.QtCore.QCommandLineOption): ...
    def valueName(self) -> str: ...

class QCommandLineParser(Shiboken.Object):
    ParseAsCompactedShortOptions: QCommandLineParser = ...  # 0x0
    ParseAsOptions: QCommandLineParser = ...  # 0x0
    ParseAsLongOptions: QCommandLineParser = ...  # 0x1
    ParseAsPositionalArguments: QCommandLineParser = ...  # 0x1

    class OptionsAfterPositionalArgumentsMode(object):
        ParseAsOptions: QCommandLineParser.OptionsAfterPositionalArgumentsMode = (
            ...
        )  # 0x0
        ParseAsPositionalArguments: QCommandLineParser.OptionsAfterPositionalArgumentsMode = (
            ...
        )  # 0x1

    class SingleDashWordOptionMode(object):
        ParseAsCompactedShortOptions: QCommandLineParser.SingleDashWordOptionMode = (
            ...
        )  # 0x0
        ParseAsLongOptions: QCommandLineParser.SingleDashWordOptionMode = ...  # 0x1
    def __init__(self): ...
    def addHelpOption(self) -> PySide2.QtCore.QCommandLineOption: ...
    def addOption(
        self, commandLineOption: PySide2.QtCore.QCommandLineOption
    ) -> bool: ...
    def addOptions(self, options: typing.Sequence) -> bool: ...
    def addPositionalArgument(self, name: str, description: str, syntax: str = ...): ...
    def addVersionOption(self) -> PySide2.QtCore.QCommandLineOption: ...
    def applicationDescription(self) -> str: ...
    def clearPositionalArguments(self): ...
    def errorText(self) -> str: ...
    def helpText(self) -> str: ...
    @typing.overload
    def isSet(self, name: str) -> bool: ...
    @typing.overload
    def isSet(self, option: PySide2.QtCore.QCommandLineOption) -> bool: ...
    def optionNames(self) -> typing.List: ...
    def parse(self, arguments: typing.Sequence) -> bool: ...
    def positionalArguments(self) -> typing.List: ...
    @typing.overload
    def process(self, app: PySide2.QtCore.QCoreApplication): ...
    @typing.overload
    def process(self, arguments: typing.Sequence): ...
    def setApplicationDescription(self, description: str): ...
    def setOptionsAfterPositionalArgumentsMode(
        self,
        mode: PySide2.QtCore.QCommandLineParser.OptionsAfterPositionalArgumentsMode,
    ): ...
    def setSingleDashWordOptionMode(
        self, parsingMode: PySide2.QtCore.QCommandLineParser.SingleDashWordOptionMode
    ): ...
    def showHelp(self, exitCode: int = ...): ...
    def showVersion(self): ...
    def unknownOptionNames(self) -> typing.List: ...
    @typing.overload
    def value(self, name: str) -> str: ...
    @typing.overload
    def value(self, option: PySide2.QtCore.QCommandLineOption) -> str: ...
    @typing.overload
    def values(self, name: str) -> typing.List: ...
    @typing.overload
    def values(self, option: PySide2.QtCore.QCommandLineOption) -> typing.List: ...

class QConcatenateTablesProxyModel(PySide2.QtCore.QAbstractItemModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def addSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel): ...
    def canDropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def data(
        self, index: PySide2.QtCore.QModelIndex, role: int = ...
    ) -> typing.Any: ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...
    ) -> typing.Any: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    def itemData(self, proxyIndex: PySide2.QtCore.QModelIndex) -> typing.Dict: ...
    def mapFromSource(
        self, sourceIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mapToSource(
        self, proxyIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mimeData(self, indexes: typing.List) -> PySide2.QtCore.QMimeData: ...
    def mimeTypes(self) -> typing.List: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def removeSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel): ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def setData(
        self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...
    ) -> bool: ...
    def setItemData(
        self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict
    ) -> bool: ...
    def sourceModels(self) -> typing.List: ...
    def span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize: ...

class QCoreApplication(PySide2.QtCore.QObject):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: typing.Sequence): ...
    @staticmethod
    def addLibraryPath(arg__1: str): ...
    @staticmethod
    def applicationDirPath() -> str: ...
    @staticmethod
    def applicationFilePath() -> str: ...
    @staticmethod
    def applicationName() -> str: ...
    @staticmethod
    def applicationPid() -> int: ...
    @staticmethod
    def applicationVersion() -> str: ...
    @staticmethod
    def arguments() -> typing.List: ...
    @staticmethod
    def closingDown() -> bool: ...
    def event(self, arg__1: PySide2.QtCore.QEvent) -> bool: ...
    @staticmethod
    def eventDispatcher() -> PySide2.QtCore.QAbstractEventDispatcher: ...
    @staticmethod
    def exec_() -> int: ...
    @staticmethod
    def exit(retcode: int = ...): ...
    @staticmethod
    def flush(): ...
    @staticmethod
    def hasPendingEvents() -> bool: ...
    def installNativeEventFilter(
        self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter
    ): ...
    @staticmethod
    def installTranslator(messageFile: PySide2.QtCore.QTranslator) -> bool: ...
    @staticmethod
    def instance() -> PySide2.QtCore.QCoreApplication: ...
    @staticmethod
    def isQuitLockEnabled() -> bool: ...
    @staticmethod
    def isSetuidAllowed() -> bool: ...
    @staticmethod
    def libraryPaths() -> typing.List: ...
    def notify(
        self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent
    ) -> bool: ...
    @staticmethod
    def organizationDomain() -> str: ...
    @staticmethod
    def organizationName() -> str: ...
    @staticmethod
    def postEvent(
        receiver: PySide2.QtCore.QObject,
        event: PySide2.QtCore.QEvent,
        priority: int = ...,
    ): ...
    @typing.overload
    @staticmethod
    def processEvents(
        flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags, maxtime: int
    ): ...
    @typing.overload
    @staticmethod
    def processEvents(flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags = ...): ...
    @staticmethod
    def quit(): ...
    @staticmethod
    def removeLibraryPath(arg__1: str): ...
    def removeNativeEventFilter(
        self, filterObj: PySide2.QtCore.QAbstractNativeEventFilter
    ): ...
    @staticmethod
    def removePostedEvents(receiver: PySide2.QtCore.QObject, eventType: int = ...): ...
    @staticmethod
    def removeTranslator(messageFile: PySide2.QtCore.QTranslator) -> bool: ...
    @staticmethod
    def sendEvent(
        receiver: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent
    ) -> bool: ...
    @staticmethod
    def sendPostedEvents(
        receiver: typing.Optional[PySide2.QtCore.QObject] = ..., event_type: int = ...
    ): ...
    @staticmethod
    def setApplicationName(application: str): ...
    @staticmethod
    def setApplicationVersion(version: str): ...
    @staticmethod
    def setAttribute(
        attribute: PySide2.QtCore.Qt.ApplicationAttribute, on: bool = ...
    ): ...
    @staticmethod
    def setEventDispatcher(
        eventDispatcher: PySide2.QtCore.QAbstractEventDispatcher,
    ): ...
    @staticmethod
    def setLibraryPaths(arg__1: typing.Sequence): ...
    @staticmethod
    def setOrganizationDomain(orgDomain: str): ...
    @staticmethod
    def setOrganizationName(orgName: str): ...
    @staticmethod
    def setQuitLockEnabled(enabled: bool): ...
    @staticmethod
    def setSetuidAllowed(allow: bool): ...
    def shutdown(self): ...
    @staticmethod
    def startingUp() -> bool: ...
    @staticmethod
    def testAttribute(attribute: PySide2.QtCore.Qt.ApplicationAttribute) -> bool: ...
    @staticmethod
    def translate(
        context: bytes,
        key: bytes,
        disambiguation: typing.Optional[bytes] = ...,
        n: int = ...,
    ) -> str: ...

class QCryptographicHash(Shiboken.Object):
    Md4: QCryptographicHash = ...  # 0x0
    Md5: QCryptographicHash = ...  # 0x1
    Sha1: QCryptographicHash = ...  # 0x2
    Sha224: QCryptographicHash = ...  # 0x3
    Sha256: QCryptographicHash = ...  # 0x4
    Sha384: QCryptographicHash = ...  # 0x5
    Sha512: QCryptographicHash = ...  # 0x6
    Keccak_224: QCryptographicHash = ...  # 0x7
    Keccak_256: QCryptographicHash = ...  # 0x8
    Keccak_384: QCryptographicHash = ...  # 0x9
    Keccak_512: QCryptographicHash = ...  # 0xa
    RealSha3_224: QCryptographicHash = ...  # 0xb
    Sha3_224: QCryptographicHash = ...  # 0xb
    RealSha3_256: QCryptographicHash = ...  # 0xc
    Sha3_256: QCryptographicHash = ...  # 0xc
    RealSha3_384: QCryptographicHash = ...  # 0xd
    Sha3_384: QCryptographicHash = ...  # 0xd
    RealSha3_512: QCryptographicHash = ...  # 0xe
    Sha3_512: QCryptographicHash = ...  # 0xe

    class Algorithm(object):
        Md4: QCryptographicHash.Algorithm = ...  # 0x0
        Md5: QCryptographicHash.Algorithm = ...  # 0x1
        Sha1: QCryptographicHash.Algorithm = ...  # 0x2
        Sha224: QCryptographicHash.Algorithm = ...  # 0x3
        Sha256: QCryptographicHash.Algorithm = ...  # 0x4
        Sha384: QCryptographicHash.Algorithm = ...  # 0x5
        Sha512: QCryptographicHash.Algorithm = ...  # 0x6
        Keccak_224: QCryptographicHash.Algorithm = ...  # 0x7
        Keccak_256: QCryptographicHash.Algorithm = ...  # 0x8
        Keccak_384: QCryptographicHash.Algorithm = ...  # 0x9
        Keccak_512: QCryptographicHash.Algorithm = ...  # 0xa
        RealSha3_224: QCryptographicHash.Algorithm = ...  # 0xb
        Sha3_224: QCryptographicHash.Algorithm = ...  # 0xb
        RealSha3_256: QCryptographicHash.Algorithm = ...  # 0xc
        Sha3_256: QCryptographicHash.Algorithm = ...  # 0xc
        RealSha3_384: QCryptographicHash.Algorithm = ...  # 0xd
        Sha3_384: QCryptographicHash.Algorithm = ...  # 0xd
        RealSha3_512: QCryptographicHash.Algorithm = ...  # 0xe
        Sha3_512: QCryptographicHash.Algorithm = ...  # 0xe
    def __init__(self, method: PySide2.QtCore.QCryptographicHash.Algorithm): ...
    @typing.overload
    def addData(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def addData(self, data: bytes, length: int): ...
    @typing.overload
    def addData(self, device: PySide2.QtCore.QIODevice) -> bool: ...
    @staticmethod
    def hash(
        data: PySide2.QtCore.QByteArray,
        method: PySide2.QtCore.QCryptographicHash.Algorithm,
    ) -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def hashLength(method: PySide2.QtCore.QCryptographicHash.Algorithm) -> int: ...
    def reset(self): ...
    def result(self) -> PySide2.QtCore.QByteArray: ...

class QDataStream(Shiboken.Object):
    BigEndian: QDataStream = ...  # 0x0
    Ok: QDataStream = ...  # 0x0
    SinglePrecision: QDataStream = ...  # 0x0
    DoublePrecision: QDataStream = ...  # 0x1
    LittleEndian: QDataStream = ...  # 0x1
    Qt_1_0: QDataStream = ...  # 0x1
    ReadPastEnd: QDataStream = ...  # 0x1
    Qt_2_0: QDataStream = ...  # 0x2
    ReadCorruptData: QDataStream = ...  # 0x2
    Qt_2_1: QDataStream = ...  # 0x3
    WriteFailed: QDataStream = ...  # 0x3
    Qt_3_0: QDataStream = ...  # 0x4
    Qt_3_1: QDataStream = ...  # 0x5
    Qt_3_3: QDataStream = ...  # 0x6
    Qt_4_0: QDataStream = ...  # 0x7
    Qt_4_1: QDataStream = ...  # 0x7
    Qt_4_2: QDataStream = ...  # 0x8
    Qt_4_3: QDataStream = ...  # 0x9
    Qt_4_4: QDataStream = ...  # 0xa
    Qt_4_5: QDataStream = ...  # 0xb
    Qt_4_6: QDataStream = ...  # 0xc
    Qt_4_7: QDataStream = ...  # 0xc
    Qt_4_8: QDataStream = ...  # 0xc
    Qt_4_9: QDataStream = ...  # 0xc
    Qt_5_0: QDataStream = ...  # 0xd
    Qt_5_1: QDataStream = ...  # 0xe
    Qt_5_2: QDataStream = ...  # 0xf
    Qt_5_3: QDataStream = ...  # 0xf
    Qt_5_4: QDataStream = ...  # 0x10
    Qt_5_5: QDataStream = ...  # 0x10
    Qt_5_10: QDataStream = ...  # 0x11
    Qt_5_11: QDataStream = ...  # 0x11
    Qt_5_6: QDataStream = ...  # 0x11
    Qt_5_7: QDataStream = ...  # 0x11
    Qt_5_8: QDataStream = ...  # 0x11
    Qt_5_9: QDataStream = ...  # 0x11
    Qt_5_12: QDataStream = ...  # 0x12
    Qt_5_13: QDataStream = ...  # 0x13
    Qt_5_14: QDataStream = ...  # 0x13
    Qt_5_15: QDataStream = ...  # 0x13
    Qt_DefaultCompiledVersion: QDataStream = ...  # 0x13

    class ByteOrder(object):
        BigEndian: QDataStream.ByteOrder = ...  # 0x0
        LittleEndian: QDataStream.ByteOrder = ...  # 0x1

    class FloatingPointPrecision(object):
        SinglePrecision: QDataStream.FloatingPointPrecision = ...  # 0x0
        DoublePrecision: QDataStream.FloatingPointPrecision = ...  # 0x1

    class Status(object):
        Ok: QDataStream.Status = ...  # 0x0
        ReadPastEnd: QDataStream.Status = ...  # 0x1
        ReadCorruptData: QDataStream.Status = ...  # 0x2
        WriteFailed: QDataStream.Status = ...  # 0x3

    class Version(object):
        Qt_1_0: QDataStream.Version = ...  # 0x1
        Qt_2_0: QDataStream.Version = ...  # 0x2
        Qt_2_1: QDataStream.Version = ...  # 0x3
        Qt_3_0: QDataStream.Version = ...  # 0x4
        Qt_3_1: QDataStream.Version = ...  # 0x5
        Qt_3_3: QDataStream.Version = ...  # 0x6
        Qt_4_0: QDataStream.Version = ...  # 0x7
        Qt_4_1: QDataStream.Version = ...  # 0x7
        Qt_4_2: QDataStream.Version = ...  # 0x8
        Qt_4_3: QDataStream.Version = ...  # 0x9
        Qt_4_4: QDataStream.Version = ...  # 0xa
        Qt_4_5: QDataStream.Version = ...  # 0xb
        Qt_4_6: QDataStream.Version = ...  # 0xc
        Qt_4_7: QDataStream.Version = ...  # 0xc
        Qt_4_8: QDataStream.Version = ...  # 0xc
        Qt_4_9: QDataStream.Version = ...  # 0xc
        Qt_5_0: QDataStream.Version = ...  # 0xd
        Qt_5_1: QDataStream.Version = ...  # 0xe
        Qt_5_2: QDataStream.Version = ...  # 0xf
        Qt_5_3: QDataStream.Version = ...  # 0xf
        Qt_5_4: QDataStream.Version = ...  # 0x10
        Qt_5_5: QDataStream.Version = ...  # 0x10
        Qt_5_10: QDataStream.Version = ...  # 0x11
        Qt_5_11: QDataStream.Version = ...  # 0x11
        Qt_5_6: QDataStream.Version = ...  # 0x11
        Qt_5_7: QDataStream.Version = ...  # 0x11
        Qt_5_8: QDataStream.Version = ...  # 0x11
        Qt_5_9: QDataStream.Version = ...  # 0x11
        Qt_5_12: QDataStream.Version = ...  # 0x12
        Qt_5_13: QDataStream.Version = ...  # 0x13
        Qt_5_14: QDataStream.Version = ...  # 0x13
        Qt_5_15: QDataStream.Version = ...  # 0x13
        Qt_DefaultCompiledVersion: QDataStream.Version = ...  # 0x13
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(
        self,
        arg__1: PySide2.QtCore.QByteArray,
        flags: PySide2.QtCore.QIODevice.OpenMode,
    ): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def __lshift__(self, arg__1: str): ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QBitArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QCborArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QCborMap
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QCborValue
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QDate
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QDateTime
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QEasingCurve
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QJsonArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QJsonDocument
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QJsonValue
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QLine
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QLineF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QLocale
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QMargins
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QMarginsF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QPoint
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QPointF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QRect
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QRectF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QSize
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QSizeF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QTime
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(self, arg__2: PySide2.QtCore.QUrl) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, arg__2: PySide2.QtCore.QUuid
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, re: PySide2.QtCore.QRegularExpression
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, regExp: PySide2.QtCore.QRegExp
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, tz: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __lshift__(
        self, version: PySide2.QtCore.QVersionNumber
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QBitArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QCborArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QCborMap
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QCborValue
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QDate
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QDateTime
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QEasingCurve
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QJsonArray
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QJsonDocument
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QJsonValue
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QLine
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QLineF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QLocale
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QMargins
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QMarginsF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QPoint
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QPointF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QRect
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QRectF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QSize
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QSizeF
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QTime
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(self, arg__2: PySide2.QtCore.QUrl) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, arg__2: PySide2.QtCore.QUuid
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, re: PySide2.QtCore.QRegularExpression
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, regExp: PySide2.QtCore.QRegExp
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, tz: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDataStream: ...
    @typing.overload
    def __rshift__(
        self, version: PySide2.QtCore.QVersionNumber
    ) -> PySide2.QtCore.QDataStream: ...
    def abortTransaction(self): ...
    def atEnd(self) -> bool: ...
    def byteOrder(self) -> PySide2.QtCore.QDataStream.ByteOrder: ...
    def commitTransaction(self) -> bool: ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def floatingPointPrecision(
        self,
    ) -> PySide2.QtCore.QDataStream.FloatingPointPrecision: ...
    def readBool(self) -> bool: ...
    def readDouble(self) -> float: ...
    def readFloat(self) -> float: ...
    def readInt16(self) -> int: ...
    def readInt32(self) -> int: ...
    def readInt64(self) -> int: ...
    def readInt8(self) -> int: ...
    def readQChar(self) -> str: ...
    def readQString(self) -> str: ...
    def readQStringList(self) -> typing.List: ...
    def readQVariant(self) -> typing.Any: ...
    def readRawData(self, arg__1: bytes, len: int) -> int: ...
    def readString(self) -> str: ...
    def readUInt16(self) -> int: ...
    def readUInt32(self) -> int: ...
    def readUInt64(self) -> int: ...
    def readUInt8(self) -> int: ...
    def resetStatus(self): ...
    def rollbackTransaction(self): ...
    def setByteOrder(self, arg__1: PySide2.QtCore.QDataStream.ByteOrder): ...
    def setDevice(self, arg__1: PySide2.QtCore.QIODevice): ...
    def setFloatingPointPrecision(
        self, precision: PySide2.QtCore.QDataStream.FloatingPointPrecision
    ): ...
    def setStatus(self, status: PySide2.QtCore.QDataStream.Status): ...
    def setVersion(self, arg__1: int): ...
    def skipRawData(self, len: int) -> int: ...
    def startTransaction(self): ...
    def status(self) -> PySide2.QtCore.QDataStream.Status: ...
    def unsetDevice(self): ...
    def version(self) -> int: ...
    def writeBool(self, arg__1: bool): ...
    def writeDouble(self, arg__1: float): ...
    def writeFloat(self, arg__1: float): ...
    def writeInt16(self, arg__1: int): ...
    def writeInt32(self, arg__1: int): ...
    def writeInt64(self, arg__1: int): ...
    def writeInt8(self, arg__1: int): ...
    def writeQChar(self, arg__1: str): ...
    def writeQString(self, arg__1: str): ...
    def writeQStringList(self, arg__1: typing.Sequence): ...
    def writeQVariant(self, arg__1: typing.Any): ...
    def writeRawData(self, arg__1: bytes, len: int) -> int: ...
    def writeString(self, arg__1: str): ...
    def writeUInt16(self, arg__1: int): ...
    def writeUInt32(self, arg__1: int): ...
    def writeUInt64(self, arg__1: int): ...
    def writeUInt8(self, arg__1: int): ...

class QDate(Shiboken.Object):
    DateFormat: QDate = ...  # 0x0
    StandaloneFormat: QDate = ...  # 0x1

    class MonthNameType(object):
        DateFormat: QDate.MonthNameType = ...  # 0x0
        StandaloneFormat: QDate.MonthNameType = ...  # 0x1
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QDate: PySide2.QtCore.QDate): ...
    @typing.overload
    def __init__(self, y: int, m: int, d: int): ...
    @typing.overload
    def __init__(self, y: int, m: int, d: int, cal: PySide2.QtCore.QCalendar): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def addDays(self, days: int) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def addMonths(self, months: int) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def addMonths(
        self, months: int, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def addYears(self, years: int) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def addYears(
        self, years: int, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QDate: ...
    @staticmethod
    def currentDate() -> PySide2.QtCore.QDate: ...
    @typing.overload
    def day(self) -> int: ...
    @typing.overload
    def day(self, cal: PySide2.QtCore.QCalendar) -> int: ...
    @typing.overload
    def dayOfWeek(self) -> int: ...
    @typing.overload
    def dayOfWeek(self, cal: PySide2.QtCore.QCalendar) -> int: ...
    @typing.overload
    def dayOfYear(self) -> int: ...
    @typing.overload
    def dayOfYear(self, cal: PySide2.QtCore.QCalendar) -> int: ...
    @typing.overload
    def daysInMonth(self) -> int: ...
    @typing.overload
    def daysInMonth(self, cal: PySide2.QtCore.QCalendar) -> int: ...
    @typing.overload
    def daysInYear(self) -> int: ...
    @typing.overload
    def daysInYear(self, cal: PySide2.QtCore.QCalendar) -> int: ...
    def daysTo(self, arg__1: PySide2.QtCore.QDate) -> int: ...
    @typing.overload
    def endOfDay(
        self, spec: PySide2.QtCore.Qt.TimeSpec = ..., offsetSeconds: int = ...
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    def endOfDay(self, zone: PySide2.QtCore.QTimeZone) -> PySide2.QtCore.QDateTime: ...
    @staticmethod
    def fromJulianDay(jd_: int) -> PySide2.QtCore.QDate: ...
    @typing.overload
    @staticmethod
    def fromString(
        s: str, f: PySide2.QtCore.Qt.DateFormat = ...
    ) -> PySide2.QtCore.QDate: ...
    @typing.overload
    @staticmethod
    def fromString(s: str, format: str) -> PySide2.QtCore.QDate: ...
    @typing.overload
    @staticmethod
    def fromString(
        s: str, format: str, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QDate: ...
    def getDate(self) -> typing.Tuple: ...
    @staticmethod
    def isLeapYear(year: int) -> bool: ...
    def isNull(self) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid() -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(y: int, m: int, d: int) -> bool: ...
    @staticmethod
    def longDayName(
        weekday: int, type: PySide2.QtCore.QDate.MonthNameType = ...
    ) -> str: ...
    @staticmethod
    def longMonthName(
        month: int, type: PySide2.QtCore.QDate.MonthNameType = ...
    ) -> str: ...
    @typing.overload
    def month(self) -> int: ...
    @typing.overload
    def month(self, cal: PySide2.QtCore.QCalendar) -> int: ...
    @typing.overload
    def setDate(self, year: int, month: int, day: int) -> bool: ...
    @typing.overload
    def setDate(
        self, year: int, month: int, day: int, cal: PySide2.QtCore.QCalendar
    ) -> bool: ...
    @staticmethod
    def shortDayName(
        weekday: int, type: PySide2.QtCore.QDate.MonthNameType = ...
    ) -> str: ...
    @staticmethod
    def shortMonthName(
        month: int, type: PySide2.QtCore.QDate.MonthNameType = ...
    ) -> str: ...
    @typing.overload
    def startOfDay(
        self, spec: PySide2.QtCore.Qt.TimeSpec = ..., offsetSeconds: int = ...
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    def startOfDay(
        self, zone: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDateTime: ...
    def toJulianDay(self) -> int: ...
    def toPython(self) -> object: ...
    @typing.overload
    def toString(
        self, format: PySide2.QtCore.Qt.DateFormat, cal: PySide2.QtCore.QCalendar
    ) -> str: ...
    @typing.overload
    def toString(self, format: PySide2.QtCore.Qt.DateFormat = ...) -> str: ...
    @typing.overload
    def toString(self, format: str) -> str: ...
    @typing.overload
    def toString(self, format: str, cal: PySide2.QtCore.QCalendar) -> str: ...
    def weekNumber(self) -> typing.Tuple: ...
    @typing.overload
    def year(self) -> int: ...
    @typing.overload
    def year(self, cal: PySide2.QtCore.QCalendar) -> int: ...

class QDateTime(Shiboken.Object):
    class YearRange(object):
        First: QDateTime.YearRange = ...  # -0x116bc370
        Last: QDateTime.YearRange = ...  # 0x116bd2d2
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QDate): ...
    @typing.overload
    def __init__(
        self,
        arg__1: PySide2.QtCore.QDate,
        arg__2: PySide2.QtCore.QTime,
        spec: PySide2.QtCore.Qt.TimeSpec = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        arg__1: int,
        arg__2: int,
        arg__3: int,
        arg__4: int,
        arg__5: int,
        arg__6: int,
    ): ...
    @typing.overload
    def __init__(
        self,
        arg__1: int,
        arg__2: int,
        arg__3: int,
        arg__4: int,
        arg__5: int,
        arg__6: int,
        arg__7: int,
        arg__8: int = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        date: PySide2.QtCore.QDate,
        time: PySide2.QtCore.QTime,
        spec: PySide2.QtCore.Qt.TimeSpec,
        offsetSeconds: int,
    ): ...
    @typing.overload
    def __init__(
        self,
        date: PySide2.QtCore.QDate,
        time: PySide2.QtCore.QTime,
        timeZone: PySide2.QtCore.QTimeZone,
    ): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QDateTime): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def addDays(self, days: int) -> PySide2.QtCore.QDateTime: ...
    def addMSecs(self, msecs: int) -> PySide2.QtCore.QDateTime: ...
    def addMonths(self, months: int) -> PySide2.QtCore.QDateTime: ...
    def addSecs(self, secs: int) -> PySide2.QtCore.QDateTime: ...
    def addYears(self, years: int) -> PySide2.QtCore.QDateTime: ...
    @staticmethod
    def currentDateTime() -> PySide2.QtCore.QDateTime: ...
    @staticmethod
    def currentDateTimeUtc() -> PySide2.QtCore.QDateTime: ...
    @staticmethod
    def currentMSecsSinceEpoch() -> int: ...
    @staticmethod
    def currentSecsSinceEpoch() -> int: ...
    def date(self) -> PySide2.QtCore.QDate: ...
    def daysTo(self, arg__1: PySide2.QtCore.QDateTime) -> int: ...
    @typing.overload
    @staticmethod
    def fromMSecsSinceEpoch(msecs: int) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromMSecsSinceEpoch(
        msecs: int, spec: PySide2.QtCore.Qt.TimeSpec, offsetFromUtc: int = ...
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromMSecsSinceEpoch(
        msecs: int, timeZone: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromSecsSinceEpoch(
        secs: int, spe: PySide2.QtCore.Qt.TimeSpec = ..., offsetFromUtc: int = ...
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromSecsSinceEpoch(
        secs: int, timeZone: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromString(
        s: str, f: PySide2.QtCore.Qt.DateFormat = ...
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromString(s: str, format: str) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromString(
        s: str, format: str, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromTime_t(secsSince1Jan1970UTC: int) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromTime_t(
        secsSince1Jan1970UTC: int,
        spec: PySide2.QtCore.Qt.TimeSpec,
        offsetFromUtc: int = ...,
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    @staticmethod
    def fromTime_t(
        secsSince1Jan1970UTC: int, timeZone: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDateTime: ...
    def isDaylightTime(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isValid(self) -> bool: ...
    def msecsTo(self, arg__1: PySide2.QtCore.QDateTime) -> int: ...
    def offsetFromUtc(self) -> int: ...
    def secsTo(self, arg__1: PySide2.QtCore.QDateTime) -> int: ...
    def setDate(self, date: PySide2.QtCore.QDate): ...
    def setMSecsSinceEpoch(self, msecs: int): ...
    def setOffsetFromUtc(self, offsetSeconds: int): ...
    def setSecsSinceEpoch(self, secs: int): ...
    def setTime(self, time: PySide2.QtCore.QTime): ...
    def setTimeSpec(self, spec: PySide2.QtCore.Qt.TimeSpec): ...
    def setTimeZone(self, toZone: PySide2.QtCore.QTimeZone): ...
    def setTime_t(self, secsSince1Jan1970UTC: int): ...
    def setUtcOffset(self, seconds: int): ...
    def swap(self, other: PySide2.QtCore.QDateTime): ...
    def time(self) -> PySide2.QtCore.QTime: ...
    def timeSpec(self) -> PySide2.QtCore.Qt.TimeSpec: ...
    def timeZone(self) -> PySide2.QtCore.QTimeZone: ...
    def timeZoneAbbreviation(self) -> str: ...
    def toLocalTime(self) -> PySide2.QtCore.QDateTime: ...
    def toMSecsSinceEpoch(self) -> int: ...
    def toOffsetFromUtc(self, offsetSeconds: int) -> PySide2.QtCore.QDateTime: ...
    def toPython(self) -> object: ...
    def toSecsSinceEpoch(self) -> int: ...
    @typing.overload
    def toString(self, format: PySide2.QtCore.Qt.DateFormat = ...) -> str: ...
    @typing.overload
    def toString(self, format: str) -> str: ...
    @typing.overload
    def toString(self, format: str, cal: PySide2.QtCore.QCalendar) -> str: ...
    def toTimeSpec(
        self, spec: PySide2.QtCore.Qt.TimeSpec
    ) -> PySide2.QtCore.QDateTime: ...
    def toTimeZone(
        self, toZone: PySide2.QtCore.QTimeZone
    ) -> PySide2.QtCore.QDateTime: ...
    def toTime_t(self) -> int: ...
    def toUTC(self) -> PySide2.QtCore.QDateTime: ...
    def utcOffset(self) -> int: ...

class QDeadlineTimer(Shiboken.Object):
    Forever: QDeadlineTimer = ...  # 0x0

    class ForeverConstant(object):
        Forever: QDeadlineTimer.ForeverConstant = ...  # 0x0
    @typing.overload
    def __init__(self, QDeadlineTimer: PySide2.QtCore.QDeadlineTimer): ...
    @typing.overload
    def __init__(
        self,
        arg__1: PySide2.QtCore.QDeadlineTimer.ForeverConstant,
        type_: PySide2.QtCore.Qt.TimerType = ...,
    ): ...
    @typing.overload
    def __init__(self, msecs: int, type: PySide2.QtCore.Qt.TimerType = ...): ...
    @typing.overload
    def __init__(self, type_: PySide2.QtCore.Qt.TimerType = ...): ...
    def __copy__(self): ...
    def __iadd__(self, msecs: int) -> PySide2.QtCore.QDeadlineTimer: ...
    def __isub__(self, msecs: int) -> PySide2.QtCore.QDeadlineTimer: ...
    def _q_data(self) -> typing.Tuple: ...
    @staticmethod
    def addNSecs(
        dt: PySide2.QtCore.QDeadlineTimer, nsecs: int
    ) -> PySide2.QtCore.QDeadlineTimer: ...
    @staticmethod
    def current(
        timerType: PySide2.QtCore.Qt.TimerType = ...,
    ) -> PySide2.QtCore.QDeadlineTimer: ...
    def deadline(self) -> int: ...
    def deadlineNSecs(self) -> int: ...
    def hasExpired(self) -> bool: ...
    def isForever(self) -> bool: ...
    def remainingTime(self) -> int: ...
    def remainingTimeNSecs(self) -> int: ...
    def setDeadline(self, msecs: int, timerType: PySide2.QtCore.Qt.TimerType = ...): ...
    def setPreciseDeadline(
        self, secs: int, nsecs: int = ..., type: PySide2.QtCore.Qt.TimerType = ...
    ): ...
    def setPreciseRemainingTime(
        self, secs: int, nsecs: int = ..., type: PySide2.QtCore.Qt.TimerType = ...
    ): ...
    def setRemainingTime(self, msecs: int, type: PySide2.QtCore.Qt.TimerType = ...): ...
    def setTimerType(self, type: PySide2.QtCore.Qt.TimerType): ...
    def swap(self, other: PySide2.QtCore.QDeadlineTimer): ...
    def timerType(self) -> PySide2.QtCore.Qt.TimerType: ...

class QDir(Shiboken.Object):
    NoFilter: QDir = ...  # -0x1
    NoSort: QDir = ...  # -0x1
    Name: QDir = ...  # 0x0
    Dirs: QDir = ...  # 0x1
    Time: QDir = ...  # 0x1
    Files: QDir = ...  # 0x2
    Size: QDir = ...  # 0x2
    SortByMask: QDir = ...  # 0x3
    Unsorted: QDir = ...  # 0x3
    DirsFirst: QDir = ...  # 0x4
    Drives: QDir = ...  # 0x4
    AllEntries: QDir = ...  # 0x7
    NoSymLinks: QDir = ...  # 0x8
    Reversed: QDir = ...  # 0x8
    TypeMask: QDir = ...  # 0xf
    IgnoreCase: QDir = ...  # 0x10
    Readable: QDir = ...  # 0x10
    DirsLast: QDir = ...  # 0x20
    Writable: QDir = ...  # 0x20
    Executable: QDir = ...  # 0x40
    LocaleAware: QDir = ...  # 0x40
    PermissionMask: QDir = ...  # 0x70
    Modified: QDir = ...  # 0x80
    Type: QDir = ...  # 0x80
    Hidden: QDir = ...  # 0x100
    System: QDir = ...  # 0x200
    AccessMask: QDir = ...  # 0x3f0
    AllDirs: QDir = ...  # 0x400
    CaseSensitive: QDir = ...  # 0x800
    NoDot: QDir = ...  # 0x2000
    NoDotDot: QDir = ...  # 0x4000
    NoDotAndDotDot: QDir = ...  # 0x6000

    class Filter(object):
        NoFilter: QDir.Filter = ...  # -0x1
        Dirs: QDir.Filter = ...  # 0x1
        Files: QDir.Filter = ...  # 0x2
        Drives: QDir.Filter = ...  # 0x4
        AllEntries: QDir.Filter = ...  # 0x7
        NoSymLinks: QDir.Filter = ...  # 0x8
        TypeMask: QDir.Filter = ...  # 0xf
        Readable: QDir.Filter = ...  # 0x10
        Writable: QDir.Filter = ...  # 0x20
        Executable: QDir.Filter = ...  # 0x40
        PermissionMask: QDir.Filter = ...  # 0x70
        Modified: QDir.Filter = ...  # 0x80
        Hidden: QDir.Filter = ...  # 0x100
        System: QDir.Filter = ...  # 0x200
        AccessMask: QDir.Filter = ...  # 0x3f0
        AllDirs: QDir.Filter = ...  # 0x400
        CaseSensitive: QDir.Filter = ...  # 0x800
        NoDot: QDir.Filter = ...  # 0x2000
        NoDotDot: QDir.Filter = ...  # 0x4000
        NoDotAndDotDot: QDir.Filter = ...  # 0x6000

    class Filters(object): ...

    class SortFlag(object):
        NoSort: QDir.SortFlag = ...  # -0x1
        Name: QDir.SortFlag = ...  # 0x0
        Time: QDir.SortFlag = ...  # 0x1
        Size: QDir.SortFlag = ...  # 0x2
        SortByMask: QDir.SortFlag = ...  # 0x3
        Unsorted: QDir.SortFlag = ...  # 0x3
        DirsFirst: QDir.SortFlag = ...  # 0x4
        Reversed: QDir.SortFlag = ...  # 0x8
        IgnoreCase: QDir.SortFlag = ...  # 0x10
        DirsLast: QDir.SortFlag = ...  # 0x20
        LocaleAware: QDir.SortFlag = ...  # 0x40
        Type: QDir.SortFlag = ...  # 0x80

    class SortFlags(object): ...

    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QDir): ...
    @typing.overload
    def __init__(
        self,
        path: str,
        nameFilter: str,
        sort: PySide2.QtCore.QDir.SortFlags = ...,
        filter: PySide2.QtCore.QDir.Filters = ...,
    ): ...
    @typing.overload
    def __init__(self, path: str = ...): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def absoluteFilePath(self, fileName: str) -> str: ...
    def absolutePath(self) -> str: ...
    @staticmethod
    def addResourceSearchPath(path: str): ...
    @staticmethod
    def addSearchPath(prefix: str, path: str): ...
    def canonicalPath(self) -> str: ...
    def cd(self, dirName: str) -> bool: ...
    def cdUp(self) -> bool: ...
    @staticmethod
    def cleanPath(path: str) -> str: ...
    def count(self) -> int: ...
    @staticmethod
    def current() -> PySide2.QtCore.QDir: ...
    @staticmethod
    def currentPath() -> str: ...
    def dirName(self) -> str: ...
    @staticmethod
    def drives() -> typing.List: ...
    @typing.overload
    def entryInfoList(
        self,
        filters: PySide2.QtCore.QDir.Filters = ...,
        sort: PySide2.QtCore.QDir.SortFlags = ...,
    ) -> typing.List: ...
    @typing.overload
    def entryInfoList(
        self,
        nameFilters: typing.Sequence,
        filters: PySide2.QtCore.QDir.Filters = ...,
        sort: PySide2.QtCore.QDir.SortFlags = ...,
    ) -> typing.List: ...
    @typing.overload
    def entryList(
        self,
        filters: PySide2.QtCore.QDir.Filters = ...,
        sort: PySide2.QtCore.QDir.SortFlags = ...,
    ) -> typing.List: ...
    @typing.overload
    def entryList(
        self,
        nameFilters: typing.Sequence,
        filters: PySide2.QtCore.QDir.Filters = ...,
        sort: PySide2.QtCore.QDir.SortFlags = ...,
    ) -> typing.List: ...
    @typing.overload
    def exists(self) -> bool: ...
    @typing.overload
    def exists(self, name: str) -> bool: ...
    def filePath(self, fileName: str) -> str: ...
    def filter(self) -> PySide2.QtCore.QDir.Filters: ...
    @staticmethod
    def fromNativeSeparators(pathName: str) -> str: ...
    @staticmethod
    def home() -> PySide2.QtCore.QDir: ...
    @staticmethod
    def homePath() -> str: ...
    def isAbsolute(self) -> bool: ...
    @staticmethod
    def isAbsolutePath(path: str) -> bool: ...
    def isEmpty(self, filters: PySide2.QtCore.QDir.Filters = ...) -> bool: ...
    def isReadable(self) -> bool: ...
    def isRelative(self) -> bool: ...
    @staticmethod
    def isRelativePath(path: str) -> bool: ...
    def isRoot(self) -> bool: ...
    @staticmethod
    def listSeparator() -> str: ...
    def makeAbsolute(self) -> bool: ...
    @typing.overload
    @staticmethod
    def match(filter: str, fileName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def match(filters: typing.Sequence, fileName: str) -> bool: ...
    def mkdir(self, dirName: str) -> bool: ...
    def mkpath(self, dirPath: str) -> bool: ...
    def nameFilters(self) -> typing.List: ...
    @staticmethod
    def nameFiltersFromString(nameFilter: str) -> typing.List: ...
    def path(self) -> str: ...
    def refresh(self): ...
    def relativeFilePath(self, fileName: str) -> str: ...
    def remove(self, fileName: str) -> bool: ...
    def removeRecursively(self) -> bool: ...
    def rename(self, oldName: str, newName: str) -> bool: ...
    def rmdir(self, dirName: str) -> bool: ...
    def rmpath(self, dirPath: str) -> bool: ...
    @staticmethod
    def root() -> PySide2.QtCore.QDir: ...
    @staticmethod
    def rootPath() -> str: ...
    @staticmethod
    def searchPaths(prefix: str) -> typing.List: ...
    @staticmethod
    def separator() -> str: ...
    @staticmethod
    def setCurrent(path: str) -> bool: ...
    def setFilter(self, filter: PySide2.QtCore.QDir.Filters): ...
    def setNameFilters(self, nameFilters: typing.Sequence): ...
    def setPath(self, path: str): ...
    @staticmethod
    def setSearchPaths(prefix: str, searchPaths: typing.Sequence): ...
    def setSorting(self, sort: PySide2.QtCore.QDir.SortFlags): ...
    def sorting(self) -> PySide2.QtCore.QDir.SortFlags: ...
    def swap(self, other: PySide2.QtCore.QDir): ...
    @staticmethod
    def temp() -> PySide2.QtCore.QDir: ...
    @staticmethod
    def tempPath() -> str: ...
    @staticmethod
    def toNativeSeparators(pathName: str) -> str: ...

class QDirIterator(Shiboken.Object):
    NoIteratorFlags: QDirIterator = ...  # 0x0
    FollowSymlinks: QDirIterator = ...  # 0x1
    Subdirectories: QDirIterator = ...  # 0x2

    class IteratorFlag(object):
        NoIteratorFlags: QDirIterator.IteratorFlag = ...  # 0x0
        FollowSymlinks: QDirIterator.IteratorFlag = ...  # 0x1
        Subdirectories: QDirIterator.IteratorFlag = ...  # 0x2

    class IteratorFlags(object): ...

    @typing.overload
    def __init__(
        self,
        dir: PySide2.QtCore.QDir,
        flags: PySide2.QtCore.QDirIterator.IteratorFlags = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        path: str,
        filter: PySide2.QtCore.QDir.Filters,
        flags: PySide2.QtCore.QDirIterator.IteratorFlags = ...,
    ): ...
    @typing.overload
    def __init__(
        self, path: str, flags: PySide2.QtCore.QDirIterator.IteratorFlags = ...
    ): ...
    @typing.overload
    def __init__(
        self,
        path: str,
        nameFilters: typing.Sequence,
        filters: PySide2.QtCore.QDir.Filters = ...,
        flags: PySide2.QtCore.QDirIterator.IteratorFlags = ...,
    ): ...
    def fileInfo(self) -> PySide2.QtCore.QFileInfo: ...
    def fileName(self) -> str: ...
    def filePath(self) -> str: ...
    def hasNext(self) -> bool: ...
    def next(self) -> str: ...
    def path(self) -> str: ...

class QDynamicPropertyChangeEvent(PySide2.QtCore.QEvent):
    def __init__(self, name: PySide2.QtCore.QByteArray): ...
    def propertyName(self) -> PySide2.QtCore.QByteArray: ...

class QEasingCurve(Shiboken.Object):
    Linear: QEasingCurve = ...  # 0x0
    InQuad: QEasingCurve = ...  # 0x1
    OutQuad: QEasingCurve = ...  # 0x2
    InOutQuad: QEasingCurve = ...  # 0x3
    OutInQuad: QEasingCurve = ...  # 0x4
    InCubic: QEasingCurve = ...  # 0x5
    OutCubic: QEasingCurve = ...  # 0x6
    InOutCubic: QEasingCurve = ...  # 0x7
    OutInCubic: QEasingCurve = ...  # 0x8
    InQuart: QEasingCurve = ...  # 0x9
    OutQuart: QEasingCurve = ...  # 0xa
    InOutQuart: QEasingCurve = ...  # 0xb
    OutInQuart: QEasingCurve = ...  # 0xc
    InQuint: QEasingCurve = ...  # 0xd
    OutQuint: QEasingCurve = ...  # 0xe
    InOutQuint: QEasingCurve = ...  # 0xf
    OutInQuint: QEasingCurve = ...  # 0x10
    InSine: QEasingCurve = ...  # 0x11
    OutSine: QEasingCurve = ...  # 0x12
    InOutSine: QEasingCurve = ...  # 0x13
    OutInSine: QEasingCurve = ...  # 0x14
    InExpo: QEasingCurve = ...  # 0x15
    OutExpo: QEasingCurve = ...  # 0x16
    InOutExpo: QEasingCurve = ...  # 0x17
    OutInExpo: QEasingCurve = ...  # 0x18
    InCirc: QEasingCurve = ...  # 0x19
    OutCirc: QEasingCurve = ...  # 0x1a
    InOutCirc: QEasingCurve = ...  # 0x1b
    OutInCirc: QEasingCurve = ...  # 0x1c
    InElastic: QEasingCurve = ...  # 0x1d
    OutElastic: QEasingCurve = ...  # 0x1e
    InOutElastic: QEasingCurve = ...  # 0x1f
    OutInElastic: QEasingCurve = ...  # 0x20
    InBack: QEasingCurve = ...  # 0x21
    OutBack: QEasingCurve = ...  # 0x22
    InOutBack: QEasingCurve = ...  # 0x23
    OutInBack: QEasingCurve = ...  # 0x24
    InBounce: QEasingCurve = ...  # 0x25
    OutBounce: QEasingCurve = ...  # 0x26
    InOutBounce: QEasingCurve = ...  # 0x27
    OutInBounce: QEasingCurve = ...  # 0x28
    InCurve: QEasingCurve = ...  # 0x29
    OutCurve: QEasingCurve = ...  # 0x2a
    SineCurve: QEasingCurve = ...  # 0x2b
    CosineCurve: QEasingCurve = ...  # 0x2c
    BezierSpline: QEasingCurve = ...  # 0x2d
    TCBSpline: QEasingCurve = ...  # 0x2e
    Custom: QEasingCurve = ...  # 0x2f
    NCurveTypes: QEasingCurve = ...  # 0x30

    class Type(object):
        Linear: QEasingCurve.Type = ...  # 0x0
        InQuad: QEasingCurve.Type = ...  # 0x1
        OutQuad: QEasingCurve.Type = ...  # 0x2
        InOutQuad: QEasingCurve.Type = ...  # 0x3
        OutInQuad: QEasingCurve.Type = ...  # 0x4
        InCubic: QEasingCurve.Type = ...  # 0x5
        OutCubic: QEasingCurve.Type = ...  # 0x6
        InOutCubic: QEasingCurve.Type = ...  # 0x7
        OutInCubic: QEasingCurve.Type = ...  # 0x8
        InQuart: QEasingCurve.Type = ...  # 0x9
        OutQuart: QEasingCurve.Type = ...  # 0xa
        InOutQuart: QEasingCurve.Type = ...  # 0xb
        OutInQuart: QEasingCurve.Type = ...  # 0xc
        InQuint: QEasingCurve.Type = ...  # 0xd
        OutQuint: QEasingCurve.Type = ...  # 0xe
        InOutQuint: QEasingCurve.Type = ...  # 0xf
        OutInQuint: QEasingCurve.Type = ...  # 0x10
        InSine: QEasingCurve.Type = ...  # 0x11
        OutSine: QEasingCurve.Type = ...  # 0x12
        InOutSine: QEasingCurve.Type = ...  # 0x13
        OutInSine: QEasingCurve.Type = ...  # 0x14
        InExpo: QEasingCurve.Type = ...  # 0x15
        OutExpo: QEasingCurve.Type = ...  # 0x16
        InOutExpo: QEasingCurve.Type = ...  # 0x17
        OutInExpo: QEasingCurve.Type = ...  # 0x18
        InCirc: QEasingCurve.Type = ...  # 0x19
        OutCirc: QEasingCurve.Type = ...  # 0x1a
        InOutCirc: QEasingCurve.Type = ...  # 0x1b
        OutInCirc: QEasingCurve.Type = ...  # 0x1c
        InElastic: QEasingCurve.Type = ...  # 0x1d
        OutElastic: QEasingCurve.Type = ...  # 0x1e
        InOutElastic: QEasingCurve.Type = ...  # 0x1f
        OutInElastic: QEasingCurve.Type = ...  # 0x20
        InBack: QEasingCurve.Type = ...  # 0x21
        OutBack: QEasingCurve.Type = ...  # 0x22
        InOutBack: QEasingCurve.Type = ...  # 0x23
        OutInBack: QEasingCurve.Type = ...  # 0x24
        InBounce: QEasingCurve.Type = ...  # 0x25
        OutBounce: QEasingCurve.Type = ...  # 0x26
        InOutBounce: QEasingCurve.Type = ...  # 0x27
        OutInBounce: QEasingCurve.Type = ...  # 0x28
        InCurve: QEasingCurve.Type = ...  # 0x29
        OutCurve: QEasingCurve.Type = ...  # 0x2a
        SineCurve: QEasingCurve.Type = ...  # 0x2b
        CosineCurve: QEasingCurve.Type = ...  # 0x2c
        BezierSpline: QEasingCurve.Type = ...  # 0x2d
        TCBSpline: QEasingCurve.Type = ...  # 0x2e
        Custom: QEasingCurve.Type = ...  # 0x2f
        NCurveTypes: QEasingCurve.Type = ...  # 0x30
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QEasingCurve): ...
    @typing.overload
    def __init__(self, type: PySide2.QtCore.QEasingCurve.Type = ...): ...
    def __copy__(self): ...
    def addCubicBezierSegment(
        self,
        c1: PySide2.QtCore.QPointF,
        c2: PySide2.QtCore.QPointF,
        endPoint: PySide2.QtCore.QPointF,
    ): ...
    def addTCBSegment(
        self, nextPoint: PySide2.QtCore.QPointF, t: float, c: float, b: float
    ): ...
    def amplitude(self) -> float: ...
    def customType(self) -> object: ...
    def overshoot(self) -> float: ...
    def period(self) -> float: ...
    def setAmplitude(self, amplitude: float): ...
    def setCustomType(self, arg__1: object): ...
    def setOvershoot(self, overshoot: float): ...
    def setPeriod(self, period: float): ...
    def setType(self, type: PySide2.QtCore.QEasingCurve.Type): ...
    def swap(self, other: PySide2.QtCore.QEasingCurve): ...
    def toCubicSpline(self) -> typing.List: ...
    def type(self) -> PySide2.QtCore.QEasingCurve.Type: ...
    def valueForProgress(self, progress: float) -> float: ...

class QElapsedTimer(Shiboken.Object):
    SystemTime: QElapsedTimer = ...  # 0x0
    MonotonicClock: QElapsedTimer = ...  # 0x1
    TickCounter: QElapsedTimer = ...  # 0x2
    MachAbsoluteTime: QElapsedTimer = ...  # 0x3
    PerformanceCounter: QElapsedTimer = ...  # 0x4

    class ClockType(object):
        SystemTime: QElapsedTimer.ClockType = ...  # 0x0
        MonotonicClock: QElapsedTimer.ClockType = ...  # 0x1
        TickCounter: QElapsedTimer.ClockType = ...  # 0x2
        MachAbsoluteTime: QElapsedTimer.ClockType = ...  # 0x3
        PerformanceCounter: QElapsedTimer.ClockType = ...  # 0x4
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QElapsedTimer: PySide2.QtCore.QElapsedTimer): ...
    def __copy__(self): ...
    @staticmethod
    def clockType() -> PySide2.QtCore.QElapsedTimer.ClockType: ...
    def elapsed(self) -> int: ...
    def hasExpired(self, timeout: int) -> bool: ...
    def invalidate(self): ...
    @staticmethod
    def isMonotonic() -> bool: ...
    def isValid(self) -> bool: ...
    def msecsSinceReference(self) -> int: ...
    def msecsTo(self, other: PySide2.QtCore.QElapsedTimer) -> int: ...
    def nsecsElapsed(self) -> int: ...
    def restart(self) -> int: ...
    def secsTo(self, other: PySide2.QtCore.QElapsedTimer) -> int: ...
    def start(self): ...

class QEvent(Shiboken.Object):
    None_: QEvent = ...  # 0x0
    Timer: QEvent = ...  # 0x1
    MouseButtonPress: QEvent = ...  # 0x2
    MouseButtonRelease: QEvent = ...  # 0x3
    MouseButtonDblClick: QEvent = ...  # 0x4
    MouseMove: QEvent = ...  # 0x5
    KeyPress: QEvent = ...  # 0x6
    KeyRelease: QEvent = ...  # 0x7
    FocusIn: QEvent = ...  # 0x8
    FocusOut: QEvent = ...  # 0x9
    Enter: QEvent = ...  # 0xa
    Leave: QEvent = ...  # 0xb
    Paint: QEvent = ...  # 0xc
    Move: QEvent = ...  # 0xd
    Resize: QEvent = ...  # 0xe
    Create: QEvent = ...  # 0xf
    Destroy: QEvent = ...  # 0x10
    Show: QEvent = ...  # 0x11
    Hide: QEvent = ...  # 0x12
    Close: QEvent = ...  # 0x13
    Quit: QEvent = ...  # 0x14
    ParentChange: QEvent = ...  # 0x15
    ThreadChange: QEvent = ...  # 0x16
    FocusAboutToChange: QEvent = ...  # 0x17
    WindowActivate: QEvent = ...  # 0x18
    WindowDeactivate: QEvent = ...  # 0x19
    ShowToParent: QEvent = ...  # 0x1a
    HideToParent: QEvent = ...  # 0x1b
    Wheel: QEvent = ...  # 0x1f
    WindowTitleChange: QEvent = ...  # 0x21
    WindowIconChange: QEvent = ...  # 0x22
    ApplicationWindowIconChange: QEvent = ...  # 0x23
    ApplicationFontChange: QEvent = ...  # 0x24
    ApplicationLayoutDirectionChange: QEvent = ...  # 0x25
    ApplicationPaletteChange: QEvent = ...  # 0x26
    PaletteChange: QEvent = ...  # 0x27
    Clipboard: QEvent = ...  # 0x28
    Speech: QEvent = ...  # 0x2a
    MetaCall: QEvent = ...  # 0x2b
    SockAct: QEvent = ...  # 0x32
    ShortcutOverride: QEvent = ...  # 0x33
    DeferredDelete: QEvent = ...  # 0x34
    DragEnter: QEvent = ...  # 0x3c
    DragMove: QEvent = ...  # 0x3d
    DragLeave: QEvent = ...  # 0x3e
    Drop: QEvent = ...  # 0x3f
    DragResponse: QEvent = ...  # 0x40
    ChildAdded: QEvent = ...  # 0x44
    ChildPolished: QEvent = ...  # 0x45
    ChildRemoved: QEvent = ...  # 0x47
    ShowWindowRequest: QEvent = ...  # 0x49
    PolishRequest: QEvent = ...  # 0x4a
    Polish: QEvent = ...  # 0x4b
    LayoutRequest: QEvent = ...  # 0x4c
    UpdateRequest: QEvent = ...  # 0x4d
    UpdateLater: QEvent = ...  # 0x4e
    EmbeddingControl: QEvent = ...  # 0x4f
    ActivateControl: QEvent = ...  # 0x50
    DeactivateControl: QEvent = ...  # 0x51
    ContextMenu: QEvent = ...  # 0x52
    InputMethod: QEvent = ...  # 0x53
    TabletMove: QEvent = ...  # 0x57
    LocaleChange: QEvent = ...  # 0x58
    LanguageChange: QEvent = ...  # 0x59
    LayoutDirectionChange: QEvent = ...  # 0x5a
    Style: QEvent = ...  # 0x5b
    TabletPress: QEvent = ...  # 0x5c
    TabletRelease: QEvent = ...  # 0x5d
    OkRequest: QEvent = ...  # 0x5e
    HelpRequest: QEvent = ...  # 0x5f
    IconDrag: QEvent = ...  # 0x60
    FontChange: QEvent = ...  # 0x61
    EnabledChange: QEvent = ...  # 0x62
    ActivationChange: QEvent = ...  # 0x63
    StyleChange: QEvent = ...  # 0x64
    IconTextChange: QEvent = ...  # 0x65
    ModifiedChange: QEvent = ...  # 0x66
    WindowBlocked: QEvent = ...  # 0x67
    WindowUnblocked: QEvent = ...  # 0x68
    WindowStateChange: QEvent = ...  # 0x69
    ReadOnlyChange: QEvent = ...  # 0x6a
    MouseTrackingChange: QEvent = ...  # 0x6d
    ToolTip: QEvent = ...  # 0x6e
    WhatsThis: QEvent = ...  # 0x6f
    StatusTip: QEvent = ...  # 0x70
    ActionChanged: QEvent = ...  # 0x71
    ActionAdded: QEvent = ...  # 0x72
    ActionRemoved: QEvent = ...  # 0x73
    FileOpen: QEvent = ...  # 0x74
    Shortcut: QEvent = ...  # 0x75
    WhatsThisClicked: QEvent = ...  # 0x76
    ToolBarChange: QEvent = ...  # 0x78
    ApplicationActivate: QEvent = ...  # 0x79
    ApplicationActivated: QEvent = ...  # 0x79
    ApplicationDeactivate: QEvent = ...  # 0x7a
    ApplicationDeactivated: QEvent = ...  # 0x7a
    QueryWhatsThis: QEvent = ...  # 0x7b
    EnterWhatsThisMode: QEvent = ...  # 0x7c
    LeaveWhatsThisMode: QEvent = ...  # 0x7d
    ZOrderChange: QEvent = ...  # 0x7e
    HoverEnter: QEvent = ...  # 0x7f
    HoverLeave: QEvent = ...  # 0x80
    HoverMove: QEvent = ...  # 0x81
    ParentAboutToChange: QEvent = ...  # 0x83
    WinEventAct: QEvent = ...  # 0x84
    AcceptDropsChange: QEvent = ...  # 0x98
    ZeroTimerEvent: QEvent = ...  # 0x9a
    GraphicsSceneMouseMove: QEvent = ...  # 0x9b
    GraphicsSceneMousePress: QEvent = ...  # 0x9c
    GraphicsSceneMouseRelease: QEvent = ...  # 0x9d
    GraphicsSceneMouseDoubleClick: QEvent = ...  # 0x9e
    GraphicsSceneContextMenu: QEvent = ...  # 0x9f
    GraphicsSceneHoverEnter: QEvent = ...  # 0xa0
    GraphicsSceneHoverMove: QEvent = ...  # 0xa1
    GraphicsSceneHoverLeave: QEvent = ...  # 0xa2
    GraphicsSceneHelp: QEvent = ...  # 0xa3
    GraphicsSceneDragEnter: QEvent = ...  # 0xa4
    GraphicsSceneDragMove: QEvent = ...  # 0xa5
    GraphicsSceneDragLeave: QEvent = ...  # 0xa6
    GraphicsSceneDrop: QEvent = ...  # 0xa7
    GraphicsSceneWheel: QEvent = ...  # 0xa8
    KeyboardLayoutChange: QEvent = ...  # 0xa9
    DynamicPropertyChange: QEvent = ...  # 0xaa
    TabletEnterProximity: QEvent = ...  # 0xab
    TabletLeaveProximity: QEvent = ...  # 0xac
    NonClientAreaMouseMove: QEvent = ...  # 0xad
    NonClientAreaMouseButtonPress: QEvent = ...  # 0xae
    NonClientAreaMouseButtonRelease: QEvent = ...  # 0xaf
    NonClientAreaMouseButtonDblClick: QEvent = ...  # 0xb0
    MacSizeChange: QEvent = ...  # 0xb1
    ContentsRectChange: QEvent = ...  # 0xb2
    MacGLWindowChange: QEvent = ...  # 0xb3
    FutureCallOut: QEvent = ...  # 0xb4
    GraphicsSceneResize: QEvent = ...  # 0xb5
    GraphicsSceneMove: QEvent = ...  # 0xb6
    CursorChange: QEvent = ...  # 0xb7
    ToolTipChange: QEvent = ...  # 0xb8
    NetworkReplyUpdated: QEvent = ...  # 0xb9
    GrabMouse: QEvent = ...  # 0xba
    UngrabMouse: QEvent = ...  # 0xbb
    GrabKeyboard: QEvent = ...  # 0xbc
    UngrabKeyboard: QEvent = ...  # 0xbd
    MacGLClearDrawable: QEvent = ...  # 0xbf
    StateMachineSignal: QEvent = ...  # 0xc0
    StateMachineWrapped: QEvent = ...  # 0xc1
    TouchBegin: QEvent = ...  # 0xc2
    TouchUpdate: QEvent = ...  # 0xc3
    TouchEnd: QEvent = ...  # 0xc4
    NativeGesture: QEvent = ...  # 0xc5
    Gesture: QEvent = ...  # 0xc6
    RequestSoftwareInputPanel: QEvent = ...  # 0xc7
    CloseSoftwareInputPanel: QEvent = ...  # 0xc8
    GestureOverride: QEvent = ...  # 0xca
    WinIdChange: QEvent = ...  # 0xcb
    ScrollPrepare: QEvent = ...  # 0xcc
    Scroll: QEvent = ...  # 0xcd
    Expose: QEvent = ...  # 0xce
    InputMethodQuery: QEvent = ...  # 0xcf
    OrientationChange: QEvent = ...  # 0xd0
    TouchCancel: QEvent = ...  # 0xd1
    ThemeChange: QEvent = ...  # 0xd2
    SockClose: QEvent = ...  # 0xd3
    PlatformPanel: QEvent = ...  # 0xd4
    StyleAnimationUpdate: QEvent = ...  # 0xd5
    ApplicationStateChange: QEvent = ...  # 0xd6
    WindowChangeInternal: QEvent = ...  # 0xd7
    ScreenChangeInternal: QEvent = ...  # 0xd8
    PlatformSurface: QEvent = ...  # 0xd9
    Pointer: QEvent = ...  # 0xda
    TabletTrackingChange: QEvent = ...  # 0xdb
    User: QEvent = ...  # 0x3e8
    MaxUser: QEvent = ...  # 0xffff

    class Type(object):
        None_: QEvent.Type = ...  # 0x0
        Timer: QEvent.Type = ...  # 0x1
        MouseButtonPress: QEvent.Type = ...  # 0x2
        MouseButtonRelease: QEvent.Type = ...  # 0x3
        MouseButtonDblClick: QEvent.Type = ...  # 0x4
        MouseMove: QEvent.Type = ...  # 0x5
        KeyPress: QEvent.Type = ...  # 0x6
        KeyRelease: QEvent.Type = ...  # 0x7
        FocusIn: QEvent.Type = ...  # 0x8
        FocusOut: QEvent.Type = ...  # 0x9
        Enter: QEvent.Type = ...  # 0xa
        Leave: QEvent.Type = ...  # 0xb
        Paint: QEvent.Type = ...  # 0xc
        Move: QEvent.Type = ...  # 0xd
        Resize: QEvent.Type = ...  # 0xe
        Create: QEvent.Type = ...  # 0xf
        Destroy: QEvent.Type = ...  # 0x10
        Show: QEvent.Type = ...  # 0x11
        Hide: QEvent.Type = ...  # 0x12
        Close: QEvent.Type = ...  # 0x13
        Quit: QEvent.Type = ...  # 0x14
        ParentChange: QEvent.Type = ...  # 0x15
        ThreadChange: QEvent.Type = ...  # 0x16
        FocusAboutToChange: QEvent.Type = ...  # 0x17
        WindowActivate: QEvent.Type = ...  # 0x18
        WindowDeactivate: QEvent.Type = ...  # 0x19
        ShowToParent: QEvent.Type = ...  # 0x1a
        HideToParent: QEvent.Type = ...  # 0x1b
        Wheel: QEvent.Type = ...  # 0x1f
        WindowTitleChange: QEvent.Type = ...  # 0x21
        WindowIconChange: QEvent.Type = ...  # 0x22
        ApplicationWindowIconChange: QEvent.Type = ...  # 0x23
        ApplicationFontChange: QEvent.Type = ...  # 0x24
        ApplicationLayoutDirectionChange: QEvent.Type = ...  # 0x25
        ApplicationPaletteChange: QEvent.Type = ...  # 0x26
        PaletteChange: QEvent.Type = ...  # 0x27
        Clipboard: QEvent.Type = ...  # 0x28
        Speech: QEvent.Type = ...  # 0x2a
        MetaCall: QEvent.Type = ...  # 0x2b
        SockAct: QEvent.Type = ...  # 0x32
        ShortcutOverride: QEvent.Type = ...  # 0x33
        DeferredDelete: QEvent.Type = ...  # 0x34
        DragEnter: QEvent.Type = ...  # 0x3c
        DragMove: QEvent.Type = ...  # 0x3d
        DragLeave: QEvent.Type = ...  # 0x3e
        Drop: QEvent.Type = ...  # 0x3f
        DragResponse: QEvent.Type = ...  # 0x40
        ChildAdded: QEvent.Type = ...  # 0x44
        ChildPolished: QEvent.Type = ...  # 0x45
        ChildRemoved: QEvent.Type = ...  # 0x47
        ShowWindowRequest: QEvent.Type = ...  # 0x49
        PolishRequest: QEvent.Type = ...  # 0x4a
        Polish: QEvent.Type = ...  # 0x4b
        LayoutRequest: QEvent.Type = ...  # 0x4c
        UpdateRequest: QEvent.Type = ...  # 0x4d
        UpdateLater: QEvent.Type = ...  # 0x4e
        EmbeddingControl: QEvent.Type = ...  # 0x4f
        ActivateControl: QEvent.Type = ...  # 0x50
        DeactivateControl: QEvent.Type = ...  # 0x51
        ContextMenu: QEvent.Type = ...  # 0x52
        InputMethod: QEvent.Type = ...  # 0x53
        TabletMove: QEvent.Type = ...  # 0x57
        LocaleChange: QEvent.Type = ...  # 0x58
        LanguageChange: QEvent.Type = ...  # 0x59
        LayoutDirectionChange: QEvent.Type = ...  # 0x5a
        Style: QEvent.Type = ...  # 0x5b
        TabletPress: QEvent.Type = ...  # 0x5c
        TabletRelease: QEvent.Type = ...  # 0x5d
        OkRequest: QEvent.Type = ...  # 0x5e
        HelpRequest: QEvent.Type = ...  # 0x5f
        IconDrag: QEvent.Type = ...  # 0x60
        FontChange: QEvent.Type = ...  # 0x61
        EnabledChange: QEvent.Type = ...  # 0x62
        ActivationChange: QEvent.Type = ...  # 0x63
        StyleChange: QEvent.Type = ...  # 0x64
        IconTextChange: QEvent.Type = ...  # 0x65
        ModifiedChange: QEvent.Type = ...  # 0x66
        WindowBlocked: QEvent.Type = ...  # 0x67
        WindowUnblocked: QEvent.Type = ...  # 0x68
        WindowStateChange: QEvent.Type = ...  # 0x69
        ReadOnlyChange: QEvent.Type = ...  # 0x6a
        MouseTrackingChange: QEvent.Type = ...  # 0x6d
        ToolTip: QEvent.Type = ...  # 0x6e
        WhatsThis: QEvent.Type = ...  # 0x6f
        StatusTip: QEvent.Type = ...  # 0x70
        ActionChanged: QEvent.Type = ...  # 0x71
        ActionAdded: QEvent.Type = ...  # 0x72
        ActionRemoved: QEvent.Type = ...  # 0x73
        FileOpen: QEvent.Type = ...  # 0x74
        Shortcut: QEvent.Type = ...  # 0x75
        WhatsThisClicked: QEvent.Type = ...  # 0x76
        ToolBarChange: QEvent.Type = ...  # 0x78
        ApplicationActivate: QEvent.Type = ...  # 0x79
        ApplicationActivated: QEvent.Type = ...  # 0x79
        ApplicationDeactivate: QEvent.Type = ...  # 0x7a
        ApplicationDeactivated: QEvent.Type = ...  # 0x7a
        QueryWhatsThis: QEvent.Type = ...  # 0x7b
        EnterWhatsThisMode: QEvent.Type = ...  # 0x7c
        LeaveWhatsThisMode: QEvent.Type = ...  # 0x7d
        ZOrderChange: QEvent.Type = ...  # 0x7e
        HoverEnter: QEvent.Type = ...  # 0x7f
        HoverLeave: QEvent.Type = ...  # 0x80
        HoverMove: QEvent.Type = ...  # 0x81
        ParentAboutToChange: QEvent.Type = ...  # 0x83
        WinEventAct: QEvent.Type = ...  # 0x84
        AcceptDropsChange: QEvent.Type = ...  # 0x98
        ZeroTimerEvent: QEvent.Type = ...  # 0x9a
        GraphicsSceneMouseMove: QEvent.Type = ...  # 0x9b
        GraphicsSceneMousePress: QEvent.Type = ...  # 0x9c
        GraphicsSceneMouseRelease: QEvent.Type = ...  # 0x9d
        GraphicsSceneMouseDoubleClick: QEvent.Type = ...  # 0x9e
        GraphicsSceneContextMenu: QEvent.Type = ...  # 0x9f
        GraphicsSceneHoverEnter: QEvent.Type = ...  # 0xa0
        GraphicsSceneHoverMove: QEvent.Type = ...  # 0xa1
        GraphicsSceneHoverLeave: QEvent.Type = ...  # 0xa2
        GraphicsSceneHelp: QEvent.Type = ...  # 0xa3
        GraphicsSceneDragEnter: QEvent.Type = ...  # 0xa4
        GraphicsSceneDragMove: QEvent.Type = ...  # 0xa5
        GraphicsSceneDragLeave: QEvent.Type = ...  # 0xa6
        GraphicsSceneDrop: QEvent.Type = ...  # 0xa7
        GraphicsSceneWheel: QEvent.Type = ...  # 0xa8
        KeyboardLayoutChange: QEvent.Type = ...  # 0xa9
        DynamicPropertyChange: QEvent.Type = ...  # 0xaa
        TabletEnterProximity: QEvent.Type = ...  # 0xab
        TabletLeaveProximity: QEvent.Type = ...  # 0xac
        NonClientAreaMouseMove: QEvent.Type = ...  # 0xad
        NonClientAreaMouseButtonPress: QEvent.Type = ...  # 0xae
        NonClientAreaMouseButtonRelease: QEvent.Type = ...  # 0xaf
        NonClientAreaMouseButtonDblClick: QEvent.Type = ...  # 0xb0
        MacSizeChange: QEvent.Type = ...  # 0xb1
        ContentsRectChange: QEvent.Type = ...  # 0xb2
        MacGLWindowChange: QEvent.Type = ...  # 0xb3
        FutureCallOut: QEvent.Type = ...  # 0xb4
        GraphicsSceneResize: QEvent.Type = ...  # 0xb5
        GraphicsSceneMove: QEvent.Type = ...  # 0xb6
        CursorChange: QEvent.Type = ...  # 0xb7
        ToolTipChange: QEvent.Type = ...  # 0xb8
        NetworkReplyUpdated: QEvent.Type = ...  # 0xb9
        GrabMouse: QEvent.Type = ...  # 0xba
        UngrabMouse: QEvent.Type = ...  # 0xbb
        GrabKeyboard: QEvent.Type = ...  # 0xbc
        UngrabKeyboard: QEvent.Type = ...  # 0xbd
        MacGLClearDrawable: QEvent.Type = ...  # 0xbf
        StateMachineSignal: QEvent.Type = ...  # 0xc0
        StateMachineWrapped: QEvent.Type = ...  # 0xc1
        TouchBegin: QEvent.Type = ...  # 0xc2
        TouchUpdate: QEvent.Type = ...  # 0xc3
        TouchEnd: QEvent.Type = ...  # 0xc4
        NativeGesture: QEvent.Type = ...  # 0xc5
        Gesture: QEvent.Type = ...  # 0xc6
        RequestSoftwareInputPanel: QEvent.Type = ...  # 0xc7
        CloseSoftwareInputPanel: QEvent.Type = ...  # 0xc8
        GestureOverride: QEvent.Type = ...  # 0xca
        WinIdChange: QEvent.Type = ...  # 0xcb
        ScrollPrepare: QEvent.Type = ...  # 0xcc
        Scroll: QEvent.Type = ...  # 0xcd
        Expose: QEvent.Type = ...  # 0xce
        InputMethodQuery: QEvent.Type = ...  # 0xcf
        OrientationChange: QEvent.Type = ...  # 0xd0
        TouchCancel: QEvent.Type = ...  # 0xd1
        ThemeChange: QEvent.Type = ...  # 0xd2
        SockClose: QEvent.Type = ...  # 0xd3
        PlatformPanel: QEvent.Type = ...  # 0xd4
        StyleAnimationUpdate: QEvent.Type = ...  # 0xd5
        ApplicationStateChange: QEvent.Type = ...  # 0xd6
        WindowChangeInternal: QEvent.Type = ...  # 0xd7
        ScreenChangeInternal: QEvent.Type = ...  # 0xd8
        PlatformSurface: QEvent.Type = ...  # 0xd9
        Pointer: QEvent.Type = ...  # 0xda
        TabletTrackingChange: QEvent.Type = ...  # 0xdb
        User: QEvent.Type = ...  # 0x3e8
        MaxUser: QEvent.Type = ...  # 0xffff
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QEvent): ...
    @typing.overload
    def __init__(self, type: PySide2.QtCore.QEvent.Type): ...
    def accept(self): ...
    def ignore(self): ...
    def isAccepted(self) -> bool: ...
    @staticmethod
    def registerEventType(hint: int = ...) -> int: ...
    def setAccepted(self, accepted: bool): ...
    def spontaneous(self) -> bool: ...
    def type(self) -> PySide2.QtCore.QEvent.Type: ...

class QEventLoop(PySide2.QtCore.QObject):
    AllEvents: QEventLoop = ...  # 0x0
    ExcludeUserInputEvents: QEventLoop = ...  # 0x1
    ExcludeSocketNotifiers: QEventLoop = ...  # 0x2
    WaitForMoreEvents: QEventLoop = ...  # 0x4
    X11ExcludeTimers: QEventLoop = ...  # 0x8
    EventLoopExec: QEventLoop = ...  # 0x20
    DialogExec: QEventLoop = ...  # 0x40

    class ProcessEventsFlag(object):
        AllEvents: QEventLoop.ProcessEventsFlag = ...  # 0x0
        ExcludeUserInputEvents: QEventLoop.ProcessEventsFlag = ...  # 0x1
        ExcludeSocketNotifiers: QEventLoop.ProcessEventsFlag = ...  # 0x2
        WaitForMoreEvents: QEventLoop.ProcessEventsFlag = ...  # 0x4
        X11ExcludeTimers: QEventLoop.ProcessEventsFlag = ...  # 0x8
        EventLoopExec: QEventLoop.ProcessEventsFlag = ...  # 0x20
        DialogExec: QEventLoop.ProcessEventsFlag = ...  # 0x40

    class ProcessEventsFlags(object): ...

    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def exec_(
        self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags = ...
    ) -> int: ...
    def exit(self, returnCode: int = ...): ...
    def isRunning(self) -> bool: ...
    @typing.overload
    def processEvents(
        self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags, maximumTime: int
    ): ...
    @typing.overload
    def processEvents(
        self, flags: PySide2.QtCore.QEventLoop.ProcessEventsFlags = ...
    ) -> bool: ...
    def quit(self): ...
    def wakeUp(self): ...

class QEventTransition(PySide2.QtCore.QAbstractTransition):
    @typing.overload
    def __init__(
        self,
        object: PySide2.QtCore.QObject,
        type: PySide2.QtCore.QEvent.Type,
        sourceState: typing.Optional[PySide2.QtCore.QState] = ...,
    ): ...
    @typing.overload
    def __init__(self, sourceState: typing.Optional[PySide2.QtCore.QState] = ...): ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def eventSource(self) -> PySide2.QtCore.QObject: ...
    def eventTest(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def eventType(self) -> PySide2.QtCore.QEvent.Type: ...
    def onTransition(self, event: PySide2.QtCore.QEvent): ...
    def setEventSource(self, object: PySide2.QtCore.QObject): ...
    def setEventType(self, type: PySide2.QtCore.QEvent.Type): ...

class QFactoryInterface(Shiboken.Object):
    def __init__(self): ...
    def keys(self) -> typing.List: ...

class QFile(PySide2.QtCore.QFileDevice):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, name: str): ...
    @typing.overload
    def __init__(self, name: str, parent: PySide2.QtCore.QObject): ...
    @typing.overload
    def __init__(self, parent: PySide2.QtCore.QObject): ...
    @typing.overload
    @staticmethod
    def copy(fileName: str, newName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def copy(newName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def decodeName(localFileName: PySide2.QtCore.QByteArray) -> str: ...
    @typing.overload
    @staticmethod
    def decodeName(localFileName: bytes) -> str: ...
    @staticmethod
    def encodeName(fileName: str) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def exists() -> bool: ...
    @typing.overload
    @staticmethod
    def exists(fileName: str) -> bool: ...
    def fileName(self) -> str: ...
    @typing.overload
    @staticmethod
    def link(newName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def link(oldname: str, newName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def moveToTrash() -> bool: ...
    @typing.overload
    @staticmethod
    def moveToTrash(fileName: str) -> typing.Tuple: ...
    @typing.overload
    def open(
        self,
        fd: int,
        ioFlags: PySide2.QtCore.QIODevice.OpenMode,
        handleFlags: PySide2.QtCore.QFileDevice.FileHandleFlags = ...,
    ) -> bool: ...
    @typing.overload
    def open(self, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool: ...
    @typing.overload
    @staticmethod
    def permissions() -> PySide2.QtCore.QFileDevice.Permissions: ...
    @typing.overload
    @staticmethod
    def permissions(filename: str) -> PySide2.QtCore.QFileDevice.Permissions: ...
    @typing.overload
    @staticmethod
    def readLink() -> str: ...
    @typing.overload
    @staticmethod
    def readLink(fileName: str) -> str: ...
    @typing.overload
    @staticmethod
    def remove() -> bool: ...
    @typing.overload
    @staticmethod
    def remove(fileName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def rename(newName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def rename(oldName: str, newName: str) -> bool: ...
    @typing.overload
    @staticmethod
    def resize(filename: str, sz: int) -> bool: ...
    @typing.overload
    @staticmethod
    def resize(sz: int) -> bool: ...
    def setFileName(self, name: str): ...
    @typing.overload
    @staticmethod
    def setPermissions(
        filename: str, permissionSpec: PySide2.QtCore.QFileDevice.Permissions
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def setPermissions(
        permissionSpec: PySide2.QtCore.QFileDevice.Permissions,
    ) -> bool: ...
    def size(self) -> int: ...
    @typing.overload
    @staticmethod
    def symLinkTarget() -> str: ...
    @typing.overload
    @staticmethod
    def symLinkTarget(fileName: str) -> str: ...

class QFileDevice(PySide2.QtCore.QIODevice):
    DontCloseHandle: QFileDevice = ...  # 0x0
    FileAccessTime: QFileDevice = ...  # 0x0
    NoError: QFileDevice = ...  # 0x0
    NoOptions: QFileDevice = ...  # 0x0
    AutoCloseHandle: QFileDevice = ...  # 0x1
    ExeOther: QFileDevice = ...  # 0x1
    FileBirthTime: QFileDevice = ...  # 0x1
    MapPrivateOption: QFileDevice = ...  # 0x1
    ReadError: QFileDevice = ...  # 0x1
    FileMetadataChangeTime: QFileDevice = ...  # 0x2
    WriteError: QFileDevice = ...  # 0x2
    WriteOther: QFileDevice = ...  # 0x2
    FatalError: QFileDevice = ...  # 0x3
    FileModificationTime: QFileDevice = ...  # 0x3
    ReadOther: QFileDevice = ...  # 0x4
    ResourceError: QFileDevice = ...  # 0x4
    OpenError: QFileDevice = ...  # 0x5
    AbortError: QFileDevice = ...  # 0x6
    TimeOutError: QFileDevice = ...  # 0x7
    UnspecifiedError: QFileDevice = ...  # 0x8
    RemoveError: QFileDevice = ...  # 0x9
    RenameError: QFileDevice = ...  # 0xa
    PositionError: QFileDevice = ...  # 0xb
    ResizeError: QFileDevice = ...  # 0xc
    PermissionsError: QFileDevice = ...  # 0xd
    CopyError: QFileDevice = ...  # 0xe
    ExeGroup: QFileDevice = ...  # 0x10
    WriteGroup: QFileDevice = ...  # 0x20
    ReadGroup: QFileDevice = ...  # 0x40
    ExeUser: QFileDevice = ...  # 0x100
    WriteUser: QFileDevice = ...  # 0x200
    ReadUser: QFileDevice = ...  # 0x400
    ExeOwner: QFileDevice = ...  # 0x1000
    WriteOwner: QFileDevice = ...  # 0x2000
    ReadOwner: QFileDevice = ...  # 0x4000

    class FileError(object):
        NoError: QFileDevice.FileError = ...  # 0x0
        ReadError: QFileDevice.FileError = ...  # 0x1
        WriteError: QFileDevice.FileError = ...  # 0x2
        FatalError: QFileDevice.FileError = ...  # 0x3
        ResourceError: QFileDevice.FileError = ...  # 0x4
        OpenError: QFileDevice.FileError = ...  # 0x5
        AbortError: QFileDevice.FileError = ...  # 0x6
        TimeOutError: QFileDevice.FileError = ...  # 0x7
        UnspecifiedError: QFileDevice.FileError = ...  # 0x8
        RemoveError: QFileDevice.FileError = ...  # 0x9
        RenameError: QFileDevice.FileError = ...  # 0xa
        PositionError: QFileDevice.FileError = ...  # 0xb
        ResizeError: QFileDevice.FileError = ...  # 0xc
        PermissionsError: QFileDevice.FileError = ...  # 0xd
        CopyError: QFileDevice.FileError = ...  # 0xe

    class FileHandleFlag(object):
        DontCloseHandle: QFileDevice.FileHandleFlag = ...  # 0x0
        AutoCloseHandle: QFileDevice.FileHandleFlag = ...  # 0x1

    class FileHandleFlags(object): ...

    class FileTime(object):
        FileAccessTime: QFileDevice.FileTime = ...  # 0x0
        FileBirthTime: QFileDevice.FileTime = ...  # 0x1
        FileMetadataChangeTime: QFileDevice.FileTime = ...  # 0x2
        FileModificationTime: QFileDevice.FileTime = ...  # 0x3

    class MemoryMapFlags(object):
        NoOptions: QFileDevice.MemoryMapFlags = ...  # 0x0
        MapPrivateOption: QFileDevice.MemoryMapFlags = ...  # 0x1

    class Permission(object):
        ExeOther: QFileDevice.Permission = ...  # 0x1
        WriteOther: QFileDevice.Permission = ...  # 0x2
        ReadOther: QFileDevice.Permission = ...  # 0x4
        ExeGroup: QFileDevice.Permission = ...  # 0x10
        WriteGroup: QFileDevice.Permission = ...  # 0x20
        ReadGroup: QFileDevice.Permission = ...  # 0x40
        ExeUser: QFileDevice.Permission = ...  # 0x100
        WriteUser: QFileDevice.Permission = ...  # 0x200
        ReadUser: QFileDevice.Permission = ...  # 0x400
        ExeOwner: QFileDevice.Permission = ...  # 0x1000
        WriteOwner: QFileDevice.Permission = ...  # 0x2000
        ReadOwner: QFileDevice.Permission = ...  # 0x4000

    class Permissions(object): ...

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parent: PySide2.QtCore.QObject): ...
    def atEnd(self) -> bool: ...
    def close(self): ...
    def error(self) -> PySide2.QtCore.QFileDevice.FileError: ...
    def fileName(self) -> str: ...
    def fileTime(
        self, time: PySide2.QtCore.QFileDevice.FileTime
    ) -> PySide2.QtCore.QDateTime: ...
    def flush(self) -> bool: ...
    def handle(self) -> int: ...
    def isSequential(self) -> bool: ...
    def map(
        self,
        offset: int,
        size: int,
        flags: PySide2.QtCore.QFileDevice.MemoryMapFlags = ...,
    ) -> bytes: ...
    def permissions(self) -> PySide2.QtCore.QFileDevice.Permissions: ...
    def pos(self) -> int: ...
    def readData(self, data: bytes, maxlen: int) -> int: ...
    def readLineData(self, data: bytes, maxlen: int) -> int: ...
    def resize(self, sz: int) -> bool: ...
    def seek(self, offset: int) -> bool: ...
    def setFileTime(
        self,
        newDate: PySide2.QtCore.QDateTime,
        fileTime: PySide2.QtCore.QFileDevice.FileTime,
    ) -> bool: ...
    def setPermissions(
        self, permissionSpec: PySide2.QtCore.QFileDevice.Permissions
    ) -> bool: ...
    def size(self) -> int: ...
    def unmap(self, address: bytes) -> bool: ...
    def unsetError(self): ...
    def writeData(self, data: bytes, len: int) -> int: ...

class QFileInfo(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dir: PySide2.QtCore.QDir, file: str): ...
    @typing.overload
    def __init__(self, file: PySide2.QtCore.QFile): ...
    @typing.overload
    def __init__(self, file: str): ...
    @typing.overload
    def __init__(self, fileinfo: PySide2.QtCore.QFileInfo): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def absoluteDir(self) -> PySide2.QtCore.QDir: ...
    def absoluteFilePath(self) -> str: ...
    def absolutePath(self) -> str: ...
    def baseName(self) -> str: ...
    def birthTime(self) -> PySide2.QtCore.QDateTime: ...
    def bundleName(self) -> str: ...
    def caching(self) -> bool: ...
    def canonicalFilePath(self) -> str: ...
    def canonicalPath(self) -> str: ...
    def completeBaseName(self) -> str: ...
    def completeSuffix(self) -> str: ...
    def created(self) -> PySide2.QtCore.QDateTime: ...
    def dir(self) -> PySide2.QtCore.QDir: ...
    @typing.overload
    @staticmethod
    def exists() -> bool: ...
    @typing.overload
    @staticmethod
    def exists(file: str) -> bool: ...
    def fileName(self) -> str: ...
    def filePath(self) -> str: ...
    def group(self) -> str: ...
    def groupId(self) -> int: ...
    def isAbsolute(self) -> bool: ...
    def isBundle(self) -> bool: ...
    def isDir(self) -> bool: ...
    def isExecutable(self) -> bool: ...
    def isFile(self) -> bool: ...
    def isHidden(self) -> bool: ...
    def isJunction(self) -> bool: ...
    def isNativePath(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isRelative(self) -> bool: ...
    def isRoot(self) -> bool: ...
    def isShortcut(self) -> bool: ...
    def isSymLink(self) -> bool: ...
    def isSymbolicLink(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def lastModified(self) -> PySide2.QtCore.QDateTime: ...
    def lastRead(self) -> PySide2.QtCore.QDateTime: ...
    def makeAbsolute(self) -> bool: ...
    def metadataChangeTime(self) -> PySide2.QtCore.QDateTime: ...
    def owner(self) -> str: ...
    def ownerId(self) -> int: ...
    def path(self) -> str: ...
    def readLink(self) -> str: ...
    def refresh(self): ...
    def setCaching(self, on: bool): ...
    @typing.overload
    def setFile(self, dir: PySide2.QtCore.QDir, file: str): ...
    @typing.overload
    def setFile(self, file: PySide2.QtCore.QFile): ...
    @typing.overload
    def setFile(self, file: str): ...
    def size(self) -> int: ...
    def suffix(self) -> str: ...
    def swap(self, other: PySide2.QtCore.QFileInfo): ...
    def symLinkTarget(self) -> str: ...

class QFileSelector(PySide2.QtCore.QObject):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def allSelectors(self) -> typing.List: ...
    def extraSelectors(self) -> typing.List: ...
    @typing.overload
    def select(self, filePath: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def select(self, filePath: str) -> str: ...
    def setExtraSelectors(self, list: typing.Sequence): ...

class QFileSystemWatcher(PySide2.QtCore.QObject):
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    @typing.overload
    def __init__(
        self,
        paths: typing.Sequence,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    def addPath(self, file: str) -> bool: ...
    def addPaths(self, files: typing.Sequence) -> typing.List: ...
    def directories(self) -> typing.List: ...
    def files(self) -> typing.List: ...
    def removePath(self, file: str) -> bool: ...
    def removePaths(self, files: typing.Sequence) -> typing.List: ...

class QFinalState(PySide2.QtCore.QAbstractState):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QState] = ...): ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def onEntry(self, event: PySide2.QtCore.QEvent): ...
    def onExit(self, event: PySide2.QtCore.QEvent): ...

class QGenericArgument(Shiboken.Object):
    @typing.overload
    def __init__(self, QGenericArgument: PySide2.QtCore.QGenericArgument): ...
    @typing.overload
    def __init__(
        self, aName: typing.Optional[bytes] = ..., aData: typing.Optional[int] = ...
    ): ...
    def __copy__(self): ...
    def data(self) -> int: ...
    def name(self) -> bytes: ...

class QGenericReturnArgument(PySide2.QtCore.QGenericArgument):
    @typing.overload
    def __init__(
        self, QGenericReturnArgument: PySide2.QtCore.QGenericReturnArgument
    ): ...
    @typing.overload
    def __init__(
        self, aName: typing.Optional[bytes] = ..., aData: typing.Optional[int] = ...
    ): ...
    def __copy__(self): ...

class QHistoryState(PySide2.QtCore.QAbstractState):
    ShallowHistory: QHistoryState = ...  # 0x0
    DeepHistory: QHistoryState = ...  # 0x1

    class HistoryType(object):
        ShallowHistory: QHistoryState.HistoryType = ...  # 0x0
        DeepHistory: QHistoryState.HistoryType = ...  # 0x1
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QState] = ...): ...
    @typing.overload
    def __init__(
        self,
        type: PySide2.QtCore.QHistoryState.HistoryType,
        parent: typing.Optional[PySide2.QtCore.QState] = ...,
    ): ...
    def defaultState(self) -> PySide2.QtCore.QAbstractState: ...
    def defaultTransition(self) -> PySide2.QtCore.QAbstractTransition: ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def historyType(self) -> PySide2.QtCore.QHistoryState.HistoryType: ...
    def onEntry(self, event: PySide2.QtCore.QEvent): ...
    def onExit(self, event: PySide2.QtCore.QEvent): ...
    def setDefaultState(self, state: PySide2.QtCore.QAbstractState): ...
    def setDefaultTransition(self, transition: PySide2.QtCore.QAbstractTransition): ...
    def setHistoryType(self, type: PySide2.QtCore.QHistoryState.HistoryType): ...

class QIODevice(PySide2.QtCore.QObject):
    NotOpen: QIODevice = ...  # 0x0
    ReadOnly: QIODevice = ...  # 0x1
    WriteOnly: QIODevice = ...  # 0x2
    ReadWrite: QIODevice = ...  # 0x3
    Append: QIODevice = ...  # 0x4
    Truncate: QIODevice = ...  # 0x8
    Text: QIODevice = ...  # 0x10
    Unbuffered: QIODevice = ...  # 0x20
    NewOnly: QIODevice = ...  # 0x40
    ExistingOnly: QIODevice = ...  # 0x80

    class OpenMode(object): ...

    class OpenModeFlag(object):
        NotOpen: QIODevice.OpenModeFlag = ...  # 0x0
        ReadOnly: QIODevice.OpenModeFlag = ...  # 0x1
        WriteOnly: QIODevice.OpenModeFlag = ...  # 0x2
        ReadWrite: QIODevice.OpenModeFlag = ...  # 0x3
        Append: QIODevice.OpenModeFlag = ...  # 0x4
        Truncate: QIODevice.OpenModeFlag = ...  # 0x8
        Text: QIODevice.OpenModeFlag = ...  # 0x10
        Unbuffered: QIODevice.OpenModeFlag = ...  # 0x20
        NewOnly: QIODevice.OpenModeFlag = ...  # 0x40
        ExistingOnly: QIODevice.OpenModeFlag = ...  # 0x80
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parent: PySide2.QtCore.QObject): ...
    def atEnd(self) -> bool: ...
    def bytesAvailable(self) -> int: ...
    def bytesToWrite(self) -> int: ...
    def canReadLine(self) -> bool: ...
    def close(self): ...
    def commitTransaction(self): ...
    def currentReadChannel(self) -> int: ...
    def currentWriteChannel(self) -> int: ...
    def errorString(self) -> str: ...
    def getChar(self, c: bytes) -> bool: ...
    def isOpen(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isSequential(self) -> bool: ...
    def isTextModeEnabled(self) -> bool: ...
    def isTransactionStarted(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def open(self, mode: PySide2.QtCore.QIODevice.OpenMode) -> bool: ...
    def openMode(self) -> PySide2.QtCore.QIODevice.OpenMode: ...
    def peek(self, maxlen: int) -> PySide2.QtCore.QByteArray: ...
    def pos(self) -> int: ...
    def putChar(self, c: int) -> bool: ...
    def read(self, maxlen: int) -> PySide2.QtCore.QByteArray: ...
    def readAll(self) -> PySide2.QtCore.QByteArray: ...
    def readChannelCount(self) -> int: ...
    def readData(self, data: bytes, maxlen: int) -> int: ...
    def readLine(self, maxlen: int = ...) -> PySide2.QtCore.QByteArray: ...
    def readLineData(self, data: bytes, maxlen: int) -> int: ...
    def reset(self) -> bool: ...
    def rollbackTransaction(self): ...
    def seek(self, pos: int) -> bool: ...
    def setCurrentReadChannel(self, channel: int): ...
    def setCurrentWriteChannel(self, channel: int): ...
    def setErrorString(self, errorString: str): ...
    def setOpenMode(self, openMode: PySide2.QtCore.QIODevice.OpenMode): ...
    def setTextModeEnabled(self, enabled: bool): ...
    def size(self) -> int: ...
    def skip(self, maxSize: int) -> int: ...
    def startTransaction(self): ...
    def ungetChar(self, c: int): ...
    def waitForBytesWritten(self, msecs: int) -> bool: ...
    def waitForReadyRead(self, msecs: int) -> bool: ...
    def write(self, data: PySide2.QtCore.QByteArray) -> int: ...
    def writeChannelCount(self) -> int: ...
    def writeData(self, data: bytes, len: int) -> int: ...

class QIdentityProxyModel(PySide2.QtCore.QAbstractProxyModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...
    ) -> typing.Any: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    def insertColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def insertRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def mapFromSource(
        self, sourceIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mapSelectionFromSource(
        self, selection: PySide2.QtCore.QItemSelection
    ) -> PySide2.QtCore.QItemSelection: ...
    def mapSelectionToSource(
        self, selection: PySide2.QtCore.QItemSelection
    ) -> PySide2.QtCore.QItemSelection: ...
    def mapToSource(
        self, proxyIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def match(
        self,
        start: PySide2.QtCore.QModelIndex,
        role: int,
        value: typing.Any,
        hits: int = ...,
        flags: PySide2.QtCore.Qt.MatchFlags = ...,
    ) -> typing.List: ...
    def moveColumns(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceColumn: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    def moveRows(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceRow: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, child: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def removeColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def removeRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def setSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel): ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...

class QItemSelection(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QItemSelection: PySide2.QtCore.QItemSelection): ...
    @typing.overload
    def __init__(
        self,
        topLeft: PySide2.QtCore.QModelIndex,
        bottomRight: PySide2.QtCore.QModelIndex,
    ): ...
    def __add__(self, l: typing.Sequence) -> typing.List: ...
    def __copy__(self): ...
    @typing.overload
    def __iadd__(self, l: typing.Sequence) -> typing.List: ...
    @typing.overload
    def __iadd__(self, t: PySide2.QtCore.QItemSelectionRange) -> typing.List: ...
    @typing.overload
    def __lshift__(self, l: typing.Sequence) -> typing.List: ...
    @typing.overload
    def __lshift__(self, t: PySide2.QtCore.QItemSelectionRange) -> typing.List: ...
    @typing.overload
    def append(self, t: PySide2.QtCore.QItemSelectionRange): ...
    @typing.overload
    def append(self, t: typing.Sequence): ...
    def at(self, i: int) -> PySide2.QtCore.QItemSelectionRange: ...
    def back(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def clear(self): ...
    def constFirst(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def constLast(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def contains(self, index: PySide2.QtCore.QModelIndex) -> bool: ...
    @typing.overload
    def count(self) -> int: ...
    @typing.overload
    def count(self, t: PySide2.QtCore.QItemSelectionRange) -> int: ...
    def detachShared(self): ...
    def empty(self) -> bool: ...
    def endsWith(self, t: PySide2.QtCore.QItemSelectionRange) -> bool: ...
    def first(self) -> PySide2.QtCore.QItemSelectionRange: ...
    @staticmethod
    def fromSet(set: typing.Set) -> typing.List: ...
    @staticmethod
    def fromVector(vector: typing.List) -> typing.List: ...
    def front(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def indexOf(
        self, t: PySide2.QtCore.QItemSelectionRange, from_: int = ...
    ) -> int: ...
    def indexes(self) -> typing.List: ...
    def insert(self, i: int, t: PySide2.QtCore.QItemSelectionRange): ...
    def isEmpty(self) -> bool: ...
    def isSharedWith(self, other: typing.Sequence) -> bool: ...
    def last(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def lastIndexOf(
        self, t: PySide2.QtCore.QItemSelectionRange, from_: int = ...
    ) -> int: ...
    def length(self) -> int: ...
    def merge(
        self,
        other: PySide2.QtCore.QItemSelection,
        command: PySide2.QtCore.QItemSelectionModel.SelectionFlags,
    ): ...
    def mid(self, pos: int, length: int = ...) -> typing.List: ...
    def move(self, from_: int, to: int): ...
    def pop_back(self): ...
    def pop_front(self): ...
    def prepend(self, t: PySide2.QtCore.QItemSelectionRange): ...
    def push_back(self, t: PySide2.QtCore.QItemSelectionRange): ...
    def push_front(self, t: PySide2.QtCore.QItemSelectionRange): ...
    def removeAll(self, t: PySide2.QtCore.QItemSelectionRange) -> int: ...
    def removeAt(self, i: int): ...
    def removeFirst(self): ...
    def removeLast(self): ...
    def removeOne(self, t: PySide2.QtCore.QItemSelectionRange) -> bool: ...
    def replace(self, i: int, t: PySide2.QtCore.QItemSelectionRange): ...
    def reserve(self, size: int): ...
    def select(
        self,
        topLeft: PySide2.QtCore.QModelIndex,
        bottomRight: PySide2.QtCore.QModelIndex,
    ): ...
    def setSharable(self, sharable: bool): ...
    def size(self) -> int: ...
    @staticmethod
    def split(
        range: PySide2.QtCore.QItemSelectionRange,
        other: PySide2.QtCore.QItemSelectionRange,
        result: PySide2.QtCore.QItemSelection,
    ): ...
    def startsWith(self, t: PySide2.QtCore.QItemSelectionRange) -> bool: ...
    @typing.overload
    def swap(self, i: int, j: int): ...
    @typing.overload
    def swap(self, other: typing.Sequence): ...
    def swapItemsAt(self, i: int, j: int): ...
    def takeAt(self, i: int) -> PySide2.QtCore.QItemSelectionRange: ...
    def takeFirst(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def takeLast(self) -> PySide2.QtCore.QItemSelectionRange: ...
    def toSet(self) -> typing.Set: ...
    def toVector(self) -> typing.List: ...
    @typing.overload
    def value(self, i: int) -> PySide2.QtCore.QItemSelectionRange: ...
    @typing.overload
    def value(
        self, i: int, defaultValue: PySide2.QtCore.QItemSelectionRange
    ) -> PySide2.QtCore.QItemSelectionRange: ...

class QItemSelectionModel(PySide2.QtCore.QObject):
    NoUpdate: QItemSelectionModel = ...  # 0x0
    Clear: QItemSelectionModel = ...  # 0x1
    Select: QItemSelectionModel = ...  # 0x2
    ClearAndSelect: QItemSelectionModel = ...  # 0x3
    Deselect: QItemSelectionModel = ...  # 0x4
    Toggle: QItemSelectionModel = ...  # 0x8
    Current: QItemSelectionModel = ...  # 0x10
    SelectCurrent: QItemSelectionModel = ...  # 0x12
    ToggleCurrent: QItemSelectionModel = ...  # 0x18
    Rows: QItemSelectionModel = ...  # 0x20
    Columns: QItemSelectionModel = ...  # 0x40

    class SelectionFlag(object):
        NoUpdate: QItemSelectionModel.SelectionFlag = ...  # 0x0
        Clear: QItemSelectionModel.SelectionFlag = ...  # 0x1
        Select: QItemSelectionModel.SelectionFlag = ...  # 0x2
        ClearAndSelect: QItemSelectionModel.SelectionFlag = ...  # 0x3
        Deselect: QItemSelectionModel.SelectionFlag = ...  # 0x4
        Toggle: QItemSelectionModel.SelectionFlag = ...  # 0x8
        Current: QItemSelectionModel.SelectionFlag = ...  # 0x10
        SelectCurrent: QItemSelectionModel.SelectionFlag = ...  # 0x12
        ToggleCurrent: QItemSelectionModel.SelectionFlag = ...  # 0x18
        Rows: QItemSelectionModel.SelectionFlag = ...  # 0x20
        Columns: QItemSelectionModel.SelectionFlag = ...  # 0x40

    class SelectionFlags(object): ...

    @typing.overload
    def __init__(
        self, model: PySide2.QtCore.QAbstractItemModel, parent: PySide2.QtCore.QObject
    ): ...
    @typing.overload
    def __init__(
        self, model: typing.Optional[PySide2.QtCore.QAbstractItemModel] = ...
    ): ...
    def clear(self): ...
    def clearCurrentIndex(self): ...
    def clearSelection(self): ...
    def columnIntersectsSelection(
        self, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def currentIndex(self) -> PySide2.QtCore.QModelIndex: ...
    def emitSelectionChanged(
        self,
        newSelection: PySide2.QtCore.QItemSelection,
        oldSelection: PySide2.QtCore.QItemSelection,
    ): ...
    def hasSelection(self) -> bool: ...
    def isColumnSelected(
        self, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def isRowSelected(
        self, row: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def isSelected(self, index: PySide2.QtCore.QModelIndex) -> bool: ...
    def model(self) -> PySide2.QtCore.QAbstractItemModel: ...
    def reset(self): ...
    def rowIntersectsSelection(
        self, row: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    @typing.overload
    def select(
        self,
        index: PySide2.QtCore.QModelIndex,
        command: PySide2.QtCore.QItemSelectionModel.SelectionFlags,
    ): ...
    @typing.overload
    def select(
        self,
        selection: PySide2.QtCore.QItemSelection,
        command: PySide2.QtCore.QItemSelectionModel.SelectionFlags,
    ): ...
    def selectedColumns(self, row: int = ...) -> typing.List: ...
    def selectedIndexes(self) -> typing.List: ...
    def selectedRows(self, column: int = ...) -> typing.List: ...
    def selection(self) -> PySide2.QtCore.QItemSelection: ...
    def setCurrentIndex(
        self,
        index: PySide2.QtCore.QModelIndex,
        command: PySide2.QtCore.QItemSelectionModel.SelectionFlags,
    ): ...
    def setModel(self, model: PySide2.QtCore.QAbstractItemModel): ...

class QItemSelectionRange(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, index: PySide2.QtCore.QModelIndex): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QItemSelectionRange): ...
    @typing.overload
    def __init__(
        self, topL: PySide2.QtCore.QModelIndex, bottomR: PySide2.QtCore.QModelIndex
    ): ...
    def __copy__(self): ...
    def bottom(self) -> int: ...
    def bottomRight(self) -> PySide2.QtCore.QPersistentModelIndex: ...
    @typing.overload
    def contains(self, index: PySide2.QtCore.QModelIndex) -> bool: ...
    @typing.overload
    def contains(
        self, row: int, column: int, parentIndex: PySide2.QtCore.QModelIndex
    ) -> bool: ...
    def height(self) -> int: ...
    def indexes(self) -> typing.List: ...
    def intersected(
        self, other: PySide2.QtCore.QItemSelectionRange
    ) -> PySide2.QtCore.QItemSelectionRange: ...
    def intersects(self, other: PySide2.QtCore.QItemSelectionRange) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def left(self) -> int: ...
    def model(self) -> PySide2.QtCore.QAbstractItemModel: ...
    def parent(self) -> PySide2.QtCore.QModelIndex: ...
    def right(self) -> int: ...
    def swap(self, other: PySide2.QtCore.QItemSelectionRange): ...
    def top(self) -> int: ...
    def topLeft(self) -> PySide2.QtCore.QPersistentModelIndex: ...
    def width(self) -> int: ...

class QJsonArray(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QJsonArray): ...
    def __add__(self, v: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QJsonArray: ...
    def __copy__(self): ...
    def __iadd__(self, v: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QJsonArray: ...
    def __lshift__(self, v: PySide2.QtCore.QJsonValue) -> PySide2.QtCore.QJsonArray: ...
    def append(self, value: PySide2.QtCore.QJsonValue): ...
    def at(self, i: int) -> PySide2.QtCore.QJsonValue: ...
    def contains(self, element: PySide2.QtCore.QJsonValue) -> bool: ...
    def count(self) -> int: ...
    def empty(self) -> bool: ...
    def first(self) -> PySide2.QtCore.QJsonValue: ...
    @staticmethod
    def fromStringList(list: typing.Sequence) -> PySide2.QtCore.QJsonArray: ...
    @staticmethod
    def fromVariantList(list: typing.Sequence) -> PySide2.QtCore.QJsonArray: ...
    def insert(self, i: int, value: PySide2.QtCore.QJsonValue): ...
    def isEmpty(self) -> bool: ...
    def last(self) -> PySide2.QtCore.QJsonValue: ...
    def pop_back(self): ...
    def pop_front(self): ...
    def prepend(self, value: PySide2.QtCore.QJsonValue): ...
    def push_back(self, t: PySide2.QtCore.QJsonValue): ...
    def push_front(self, t: PySide2.QtCore.QJsonValue): ...
    def removeAt(self, i: int): ...
    def removeFirst(self): ...
    def removeLast(self): ...
    def replace(self, i: int, value: PySide2.QtCore.QJsonValue): ...
    def size(self) -> int: ...
    def swap(self, other: PySide2.QtCore.QJsonArray): ...
    def takeAt(self, i: int) -> PySide2.QtCore.QJsonValue: ...
    def toVariantList(self) -> typing.List: ...

class QJsonDocument(Shiboken.Object):
    Indented: QJsonDocument = ...  # 0x0
    Validate: QJsonDocument = ...  # 0x0
    BypassValidation: QJsonDocument = ...  # 0x1
    Compact: QJsonDocument = ...  # 0x1

    class DataValidation(object):
        Validate: QJsonDocument.DataValidation = ...  # 0x0
        BypassValidation: QJsonDocument.DataValidation = ...  # 0x1

    class JsonFormat(object):
        Indented: QJsonDocument.JsonFormat = ...  # 0x0
        Compact: QJsonDocument.JsonFormat = ...  # 0x1
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, array: PySide2.QtCore.QJsonArray): ...
    @typing.overload
    def __init__(self, object: typing.Dict): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QJsonDocument): ...
    def __copy__(self): ...
    def array(self) -> PySide2.QtCore.QJsonArray: ...
    @staticmethod
    def fromBinaryData(
        data: PySide2.QtCore.QByteArray,
        validation: PySide2.QtCore.QJsonDocument.DataValidation = ...,
    ) -> PySide2.QtCore.QJsonDocument: ...
    @staticmethod
    def fromJson(
        json: PySide2.QtCore.QByteArray,
        error: typing.Optional[PySide2.QtCore.QJsonParseError] = ...,
    ) -> PySide2.QtCore.QJsonDocument: ...
    @staticmethod
    def fromRawData(
        data: bytes,
        size: int,
        validation: PySide2.QtCore.QJsonDocument.DataValidation = ...,
    ) -> PySide2.QtCore.QJsonDocument: ...
    @staticmethod
    def fromVariant(variant: typing.Any) -> PySide2.QtCore.QJsonDocument: ...
    def isArray(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isObject(self) -> bool: ...
    def object(self) -> typing.Dict: ...
    def rawData(self) -> typing.Tuple: ...
    def setArray(self, array: PySide2.QtCore.QJsonArray): ...
    def setObject(self, object: typing.Dict): ...
    def swap(self, other: PySide2.QtCore.QJsonDocument): ...
    def toBinaryData(self) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toJson(self) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toJson(
        self, format: PySide2.QtCore.QJsonDocument.JsonFormat
    ) -> PySide2.QtCore.QByteArray: ...
    def toVariant(self) -> typing.Any: ...

class QJsonParseError(Shiboken.Object):
    NoError: QJsonParseError = ...  # 0x0
    UnterminatedObject: QJsonParseError = ...  # 0x1
    MissingNameSeparator: QJsonParseError = ...  # 0x2
    UnterminatedArray: QJsonParseError = ...  # 0x3
    MissingValueSeparator: QJsonParseError = ...  # 0x4
    IllegalValue: QJsonParseError = ...  # 0x5
    TerminationByNumber: QJsonParseError = ...  # 0x6
    IllegalNumber: QJsonParseError = ...  # 0x7
    IllegalEscapeSequence: QJsonParseError = ...  # 0x8
    IllegalUTF8String: QJsonParseError = ...  # 0x9
    UnterminatedString: QJsonParseError = ...  # 0xa
    MissingObject: QJsonParseError = ...  # 0xb
    DeepNesting: QJsonParseError = ...  # 0xc
    DocumentTooLarge: QJsonParseError = ...  # 0xd
    GarbageAtEnd: QJsonParseError = ...  # 0xe

    class ParseError(object):
        NoError: QJsonParseError.ParseError = ...  # 0x0
        UnterminatedObject: QJsonParseError.ParseError = ...  # 0x1
        MissingNameSeparator: QJsonParseError.ParseError = ...  # 0x2
        UnterminatedArray: QJsonParseError.ParseError = ...  # 0x3
        MissingValueSeparator: QJsonParseError.ParseError = ...  # 0x4
        IllegalValue: QJsonParseError.ParseError = ...  # 0x5
        TerminationByNumber: QJsonParseError.ParseError = ...  # 0x6
        IllegalNumber: QJsonParseError.ParseError = ...  # 0x7
        IllegalEscapeSequence: QJsonParseError.ParseError = ...  # 0x8
        IllegalUTF8String: QJsonParseError.ParseError = ...  # 0x9
        UnterminatedString: QJsonParseError.ParseError = ...  # 0xa
        MissingObject: QJsonParseError.ParseError = ...  # 0xb
        DeepNesting: QJsonParseError.ParseError = ...  # 0xc
        DocumentTooLarge: QJsonParseError.ParseError = ...  # 0xd
        GarbageAtEnd: QJsonParseError.ParseError = ...  # 0xe
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QJsonParseError: PySide2.QtCore.QJsonParseError): ...
    def __copy__(self): ...
    def errorString(self) -> str: ...

class QJsonValue(Shiboken.Object):
    Null: QJsonValue = ...  # 0x0
    Bool: QJsonValue = ...  # 0x1
    Double: QJsonValue = ...  # 0x2
    String: QJsonValue = ...  # 0x3
    Array: QJsonValue = ...  # 0x4
    Object: QJsonValue = ...  # 0x5
    Undefined: QJsonValue = ...  # 0x80

    class Type(object):
        Null: QJsonValue.Type = ...  # 0x0
        Bool: QJsonValue.Type = ...  # 0x1
        Double: QJsonValue.Type = ...  # 0x2
        String: QJsonValue.Type = ...  # 0x3
        Array: QJsonValue.Type = ...  # 0x4
        Object: QJsonValue.Type = ...  # 0x5
        Undefined: QJsonValue.Type = ...  # 0x80
    @typing.overload
    def __init__(self, a: PySide2.QtCore.QJsonArray): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QJsonValue.Type = ...): ...
    @typing.overload
    def __init__(self, b: bool): ...
    @typing.overload
    def __init__(self, n: float): ...
    @typing.overload
    def __init__(self, n: int): ...
    @typing.overload
    def __init__(self, o: typing.Dict): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QJsonValue): ...
    @typing.overload
    def __init__(self, s: str): ...
    @typing.overload
    def __init__(self, s: bytes): ...
    @typing.overload
    def __init__(self, v: int): ...
    def __copy__(self): ...
    @staticmethod
    def fromVariant(variant: typing.Any) -> PySide2.QtCore.QJsonValue: ...
    def isArray(self) -> bool: ...
    def isBool(self) -> bool: ...
    def isDouble(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isObject(self) -> bool: ...
    def isString(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def swap(self, other: PySide2.QtCore.QJsonValue): ...
    @typing.overload
    def toArray(self) -> PySide2.QtCore.QJsonArray: ...
    @typing.overload
    def toArray(
        self, defaultValue: PySide2.QtCore.QJsonArray
    ) -> PySide2.QtCore.QJsonArray: ...
    def toBool(self, defaultValue: bool = ...) -> bool: ...
    def toDouble(self, defaultValue: float = ...) -> float: ...
    def toInt(self, defaultValue: int = ...) -> int: ...
    @typing.overload
    def toObject(self) -> typing.Dict: ...
    @typing.overload
    def toObject(self, defaultValue: typing.Dict) -> typing.Dict: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, defaultValue: str) -> str: ...
    def toVariant(self) -> typing.Any: ...
    def type(self) -> PySide2.QtCore.QJsonValue.Type: ...

class QLibraryInfo(Shiboken.Object):
    PrefixPath: QLibraryInfo = ...  # 0x0
    DocumentationPath: QLibraryInfo = ...  # 0x1
    HeadersPath: QLibraryInfo = ...  # 0x2
    LibrariesPath: QLibraryInfo = ...  # 0x3
    LibraryExecutablesPath: QLibraryInfo = ...  # 0x4
    BinariesPath: QLibraryInfo = ...  # 0x5
    PluginsPath: QLibraryInfo = ...  # 0x6
    ImportsPath: QLibraryInfo = ...  # 0x7
    Qml2ImportsPath: QLibraryInfo = ...  # 0x8
    ArchDataPath: QLibraryInfo = ...  # 0x9
    DataPath: QLibraryInfo = ...  # 0xa
    TranslationsPath: QLibraryInfo = ...  # 0xb
    ExamplesPath: QLibraryInfo = ...  # 0xc
    TestsPath: QLibraryInfo = ...  # 0xd
    SettingsPath: QLibraryInfo = ...  # 0x64

    class LibraryLocation(object):
        PrefixPath: QLibraryInfo.LibraryLocation = ...  # 0x0
        DocumentationPath: QLibraryInfo.LibraryLocation = ...  # 0x1
        HeadersPath: QLibraryInfo.LibraryLocation = ...  # 0x2
        LibrariesPath: QLibraryInfo.LibraryLocation = ...  # 0x3
        LibraryExecutablesPath: QLibraryInfo.LibraryLocation = ...  # 0x4
        BinariesPath: QLibraryInfo.LibraryLocation = ...  # 0x5
        PluginsPath: QLibraryInfo.LibraryLocation = ...  # 0x6
        ImportsPath: QLibraryInfo.LibraryLocation = ...  # 0x7
        Qml2ImportsPath: QLibraryInfo.LibraryLocation = ...  # 0x8
        ArchDataPath: QLibraryInfo.LibraryLocation = ...  # 0x9
        DataPath: QLibraryInfo.LibraryLocation = ...  # 0xa
        TranslationsPath: QLibraryInfo.LibraryLocation = ...  # 0xb
        ExamplesPath: QLibraryInfo.LibraryLocation = ...  # 0xc
        TestsPath: QLibraryInfo.LibraryLocation = ...  # 0xd
        SettingsPath: QLibraryInfo.LibraryLocation = ...  # 0x64
    @staticmethod
    def build() -> bytes: ...
    @staticmethod
    def buildDate() -> PySide2.QtCore.QDate: ...
    @staticmethod
    def isDebugBuild() -> bool: ...
    @staticmethod
    def licensedProducts() -> str: ...
    @staticmethod
    def licensee() -> str: ...
    @staticmethod
    def location(arg__1: PySide2.QtCore.QLibraryInfo.LibraryLocation) -> str: ...
    @staticmethod
    def platformPluginArguments(platformName: str) -> typing.List: ...
    @staticmethod
    def version() -> PySide2.QtCore.QVersionNumber: ...

class QLine(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QLine: PySide2.QtCore.QLine): ...
    @typing.overload
    def __init__(self, pt1: PySide2.QtCore.QPoint, pt2: PySide2.QtCore.QPoint): ...
    @typing.overload
    def __init__(self, x1: int, y1: int, x2: int, y2: int): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def center(self) -> PySide2.QtCore.QPoint: ...
    def dx(self) -> int: ...
    def dy(self) -> int: ...
    def isNull(self) -> bool: ...
    def p1(self) -> PySide2.QtCore.QPoint: ...
    def p2(self) -> PySide2.QtCore.QPoint: ...
    def setLine(self, x1: int, y1: int, x2: int, y2: int): ...
    def setP1(self, p1: PySide2.QtCore.QPoint): ...
    def setP2(self, p2: PySide2.QtCore.QPoint): ...
    def setPoints(self, p1: PySide2.QtCore.QPoint, p2: PySide2.QtCore.QPoint): ...
    def toTuple(self) -> object: ...
    @typing.overload
    def translate(self, dx: int, dy: int): ...
    @typing.overload
    def translate(self, p: PySide2.QtCore.QPoint): ...
    @typing.overload
    def translated(self, dx: int, dy: int) -> PySide2.QtCore.QLine: ...
    @typing.overload
    def translated(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QLine: ...
    def x1(self) -> int: ...
    def x2(self) -> int: ...
    def y1(self) -> int: ...
    def y2(self) -> int: ...

class QLineF(Shiboken.Object):
    NoIntersection: QLineF = ...  # 0x0
    BoundedIntersection: QLineF = ...  # 0x1
    UnboundedIntersection: QLineF = ...  # 0x2

    class IntersectType(object):
        NoIntersection: QLineF.IntersectType = ...  # 0x0
        BoundedIntersection: QLineF.IntersectType = ...  # 0x1
        UnboundedIntersection: QLineF.IntersectType = ...  # 0x2
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QLineF: PySide2.QtCore.QLineF): ...
    @typing.overload
    def __init__(self, line: PySide2.QtCore.QLine): ...
    @typing.overload
    def __init__(self, pt1: PySide2.QtCore.QPointF, pt2: PySide2.QtCore.QPointF): ...
    @typing.overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    @typing.overload
    def angle(self) -> float: ...
    @typing.overload
    def angle(self, l: PySide2.QtCore.QLineF) -> float: ...
    def angleTo(self, l: PySide2.QtCore.QLineF) -> float: ...
    def center(self) -> PySide2.QtCore.QPointF: ...
    def dx(self) -> float: ...
    def dy(self) -> float: ...
    @staticmethod
    def fromPolar(length: float, angle: float) -> PySide2.QtCore.QLineF: ...
    def intersect(
        self, l: PySide2.QtCore.QLineF, intersectionPoint: PySide2.QtCore.QPointF
    ) -> PySide2.QtCore.QLineF.IntersectType: ...
    def intersects(
        self, l: PySide2.QtCore.QLineF, intersectionPoint: PySide2.QtCore.QPointF
    ) -> PySide2.QtCore.QLineF.IntersectType: ...
    def isNull(self) -> bool: ...
    def length(self) -> float: ...
    def normalVector(self) -> PySide2.QtCore.QLineF: ...
    def p1(self) -> PySide2.QtCore.QPointF: ...
    def p2(self) -> PySide2.QtCore.QPointF: ...
    def pointAt(self, t: float) -> PySide2.QtCore.QPointF: ...
    def setAngle(self, angle: float): ...
    def setLength(self, len: float): ...
    def setLine(self, x1: float, y1: float, x2: float, y2: float): ...
    def setP1(self, p1: PySide2.QtCore.QPointF): ...
    def setP2(self, p2: PySide2.QtCore.QPointF): ...
    def setPoints(self, p1: PySide2.QtCore.QPointF, p2: PySide2.QtCore.QPointF): ...
    def toLine(self) -> PySide2.QtCore.QLine: ...
    def toTuple(self) -> object: ...
    @typing.overload
    def translate(self, dx: float, dy: float): ...
    @typing.overload
    def translate(self, p: PySide2.QtCore.QPointF): ...
    @typing.overload
    def translated(self, dx: float, dy: float) -> PySide2.QtCore.QLineF: ...
    @typing.overload
    def translated(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QLineF: ...
    def unitVector(self) -> PySide2.QtCore.QLineF: ...
    def x1(self) -> float: ...
    def x2(self) -> float: ...
    def y1(self) -> float: ...
    def y2(self) -> float: ...

class QLocale(Shiboken.Object):
    FloatingPointShortest: QLocale = ...  # -0x80
    AnyCountry: QLocale = ...  # 0x0
    AnyLanguage: QLocale = ...  # 0x0
    AnyScript: QLocale = ...  # 0x0
    CurrencyIsoCode: QLocale = ...  # 0x0
    DataSizeIecFormat: QLocale = ...  # 0x0
    DefaultNumberOptions: QLocale = ...  # 0x0
    LongFormat: QLocale = ...  # 0x0
    MetricSystem: QLocale = ...  # 0x0
    StandardQuotation: QLocale = ...  # 0x0
    Afghanistan: QLocale = ...  # 0x1
    AlternateQuotation: QLocale = ...  # 0x1
    ArabicScript: QLocale = ...  # 0x1
    C: QLocale = ...  # 0x1
    CurrencySymbol: QLocale = ...  # 0x1
    DataSizeBase1000: QLocale = ...  # 0x1
    ImperialSystem: QLocale = ...  # 0x1
    ImperialUSSystem: QLocale = ...  # 0x1
    OmitGroupSeparator: QLocale = ...  # 0x1
    ShortFormat: QLocale = ...  # 0x1
    Abkhazian: QLocale = ...  # 0x2
    Albania: QLocale = ...  # 0x2
    CurrencyDisplayName: QLocale = ...  # 0x2
    CyrillicScript: QLocale = ...  # 0x2
    DataSizeSIQuantifiers: QLocale = ...  # 0x2
    DataSizeTraditionalFormat: QLocale = ...  # 0x2
    ImperialUKSystem: QLocale = ...  # 0x2
    NarrowFormat: QLocale = ...  # 0x2
    RejectGroupSeparator: QLocale = ...  # 0x2
    Afan: QLocale = ...  # 0x3
    Algeria: QLocale = ...  # 0x3
    DataSizeSIFormat: QLocale = ...  # 0x3
    DeseretScript: QLocale = ...  # 0x3
    Oromo: QLocale = ...  # 0x3
    Afar: QLocale = ...  # 0x4
    AmericanSamoa: QLocale = ...  # 0x4
    GurmukhiScript: QLocale = ...  # 0x4
    OmitLeadingZeroInExponent: QLocale = ...  # 0x4
    Afrikaans: QLocale = ...  # 0x5
    Andorra: QLocale = ...  # 0x5
    SimplifiedChineseScript: QLocale = ...  # 0x5
    SimplifiedHanScript: QLocale = ...  # 0x5
    Albanian: QLocale = ...  # 0x6
    Angola: QLocale = ...  # 0x6
    TraditionalChineseScript: QLocale = ...  # 0x6
    TraditionalHanScript: QLocale = ...  # 0x6
    Amharic: QLocale = ...  # 0x7
    Anguilla: QLocale = ...  # 0x7
    LatinScript: QLocale = ...  # 0x7
    Antarctica: QLocale = ...  # 0x8
    Arabic: QLocale = ...  # 0x8
    MongolianScript: QLocale = ...  # 0x8
    RejectLeadingZeroInExponent: QLocale = ...  # 0x8
    AntiguaAndBarbuda: QLocale = ...  # 0x9
    Armenian: QLocale = ...  # 0x9
    TifinaghScript: QLocale = ...  # 0x9
    Argentina: QLocale = ...  # 0xa
    ArmenianScript: QLocale = ...  # 0xa
    Assamese: QLocale = ...  # 0xa
    Armenia: QLocale = ...  # 0xb
    Aymara: QLocale = ...  # 0xb
    BengaliScript: QLocale = ...  # 0xb
    Aruba: QLocale = ...  # 0xc
    Azerbaijani: QLocale = ...  # 0xc
    CherokeeScript: QLocale = ...  # 0xc
    Australia: QLocale = ...  # 0xd
    Bashkir: QLocale = ...  # 0xd
    DevanagariScript: QLocale = ...  # 0xd
    Austria: QLocale = ...  # 0xe
    Basque: QLocale = ...  # 0xe
    EthiopicScript: QLocale = ...  # 0xe
    Azerbaijan: QLocale = ...  # 0xf
    Bengali: QLocale = ...  # 0xf
    GeorgianScript: QLocale = ...  # 0xf
    Bahamas: QLocale = ...  # 0x10
    Bhutani: QLocale = ...  # 0x10
    Dzongkha: QLocale = ...  # 0x10
    GreekScript: QLocale = ...  # 0x10
    IncludeTrailingZeroesAfterDot: QLocale = ...  # 0x10
    Bahrain: QLocale = ...  # 0x11
    Bihari: QLocale = ...  # 0x11
    GujaratiScript: QLocale = ...  # 0x11
    Bangladesh: QLocale = ...  # 0x12
    Bislama: QLocale = ...  # 0x12
    HebrewScript: QLocale = ...  # 0x12
    Barbados: QLocale = ...  # 0x13
    Breton: QLocale = ...  # 0x13
    JapaneseScript: QLocale = ...  # 0x13
    Belarus: QLocale = ...  # 0x14
    Bulgarian: QLocale = ...  # 0x14
    KhmerScript: QLocale = ...  # 0x14
    Belgium: QLocale = ...  # 0x15
    Burmese: QLocale = ...  # 0x15
    KannadaScript: QLocale = ...  # 0x15
    Belarusian: QLocale = ...  # 0x16
    Belize: QLocale = ...  # 0x16
    Byelorussian: QLocale = ...  # 0x16
    KoreanScript: QLocale = ...  # 0x16
    Benin: QLocale = ...  # 0x17
    Cambodian: QLocale = ...  # 0x17
    Khmer: QLocale = ...  # 0x17
    LaoScript: QLocale = ...  # 0x17
    Bermuda: QLocale = ...  # 0x18
    Catalan: QLocale = ...  # 0x18
    MalayalamScript: QLocale = ...  # 0x18
    Bhutan: QLocale = ...  # 0x19
    Chinese: QLocale = ...  # 0x19
    MyanmarScript: QLocale = ...  # 0x19
    Bolivia: QLocale = ...  # 0x1a
    Corsican: QLocale = ...  # 0x1a
    OriyaScript: QLocale = ...  # 0x1a
    BosniaAndHerzegowina: QLocale = ...  # 0x1b
    Croatian: QLocale = ...  # 0x1b
    TamilScript: QLocale = ...  # 0x1b
    Botswana: QLocale = ...  # 0x1c
    Czech: QLocale = ...  # 0x1c
    TeluguScript: QLocale = ...  # 0x1c
    BouvetIsland: QLocale = ...  # 0x1d
    Danish: QLocale = ...  # 0x1d
    ThaanaScript: QLocale = ...  # 0x1d
    Brazil: QLocale = ...  # 0x1e
    Dutch: QLocale = ...  # 0x1e
    ThaiScript: QLocale = ...  # 0x1e
    BritishIndianOceanTerritory: QLocale = ...  # 0x1f
    English: QLocale = ...  # 0x1f
    TibetanScript: QLocale = ...  # 0x1f
    Brunei: QLocale = ...  # 0x20
    Esperanto: QLocale = ...  # 0x20
    RejectTrailingZeroesAfterDot: QLocale = ...  # 0x20
    SinhalaScript: QLocale = ...  # 0x20
    Bulgaria: QLocale = ...  # 0x21
    Estonian: QLocale = ...  # 0x21
    SyriacScript: QLocale = ...  # 0x21
    BurkinaFaso: QLocale = ...  # 0x22
    Faroese: QLocale = ...  # 0x22
    YiScript: QLocale = ...  # 0x22
    Burundi: QLocale = ...  # 0x23
    Fijian: QLocale = ...  # 0x23
    VaiScript: QLocale = ...  # 0x23
    AvestanScript: QLocale = ...  # 0x24
    Cambodia: QLocale = ...  # 0x24
    Finnish: QLocale = ...  # 0x24
    BalineseScript: QLocale = ...  # 0x25
    Cameroon: QLocale = ...  # 0x25
    French: QLocale = ...  # 0x25
    BamumScript: QLocale = ...  # 0x26
    Canada: QLocale = ...  # 0x26
    Frisian: QLocale = ...  # 0x26
    WesternFrisian: QLocale = ...  # 0x26
    BatakScript: QLocale = ...  # 0x27
    CapeVerde: QLocale = ...  # 0x27
    Gaelic: QLocale = ...  # 0x27
    BopomofoScript: QLocale = ...  # 0x28
    CaymanIslands: QLocale = ...  # 0x28
    Galician: QLocale = ...  # 0x28
    BrahmiScript: QLocale = ...  # 0x29
    CentralAfricanRepublic: QLocale = ...  # 0x29
    Georgian: QLocale = ...  # 0x29
    BugineseScript: QLocale = ...  # 0x2a
    Chad: QLocale = ...  # 0x2a
    German: QLocale = ...  # 0x2a
    BuhidScript: QLocale = ...  # 0x2b
    Chile: QLocale = ...  # 0x2b
    Greek: QLocale = ...  # 0x2b
    CanadianAboriginalScript: QLocale = ...  # 0x2c
    China: QLocale = ...  # 0x2c
    Greenlandic: QLocale = ...  # 0x2c
    CarianScript: QLocale = ...  # 0x2d
    ChristmasIsland: QLocale = ...  # 0x2d
    Guarani: QLocale = ...  # 0x2d
    ChakmaScript: QLocale = ...  # 0x2e
    CocosIslands: QLocale = ...  # 0x2e
    Gujarati: QLocale = ...  # 0x2e
    ChamScript: QLocale = ...  # 0x2f
    Colombia: QLocale = ...  # 0x2f
    Hausa: QLocale = ...  # 0x2f
    Comoros: QLocale = ...  # 0x30
    CopticScript: QLocale = ...  # 0x30
    Hebrew: QLocale = ...  # 0x30
    CongoKinshasa: QLocale = ...  # 0x31
    CypriotScript: QLocale = ...  # 0x31
    DemocraticRepublicOfCongo: QLocale = ...  # 0x31
    Hindi: QLocale = ...  # 0x31
    CongoBrazzaville: QLocale = ...  # 0x32
    EgyptianHieroglyphsScript: QLocale = ...  # 0x32
    Hungarian: QLocale = ...  # 0x32
    PeoplesRepublicOfCongo: QLocale = ...  # 0x32
    CookIslands: QLocale = ...  # 0x33
    FraserScript: QLocale = ...  # 0x33
    Icelandic: QLocale = ...  # 0x33
    CostaRica: QLocale = ...  # 0x34
    GlagoliticScript: QLocale = ...  # 0x34
    Indonesian: QLocale = ...  # 0x34
    GothicScript: QLocale = ...  # 0x35
    Interlingua: QLocale = ...  # 0x35
    IvoryCoast: QLocale = ...  # 0x35
    Croatia: QLocale = ...  # 0x36
    HanScript: QLocale = ...  # 0x36
    Interlingue: QLocale = ...  # 0x36
    Cuba: QLocale = ...  # 0x37
    HangulScript: QLocale = ...  # 0x37
    Inuktitut: QLocale = ...  # 0x37
    Cyprus: QLocale = ...  # 0x38
    HanunooScript: QLocale = ...  # 0x38
    Inupiak: QLocale = ...  # 0x38
    CzechRepublic: QLocale = ...  # 0x39
    ImperialAramaicScript: QLocale = ...  # 0x39
    Irish: QLocale = ...  # 0x39
    Denmark: QLocale = ...  # 0x3a
    InscriptionalPahlaviScript: QLocale = ...  # 0x3a
    Italian: QLocale = ...  # 0x3a
    Djibouti: QLocale = ...  # 0x3b
    InscriptionalParthianScript: QLocale = ...  # 0x3b
    Japanese: QLocale = ...  # 0x3b
    Dominica: QLocale = ...  # 0x3c
    Javanese: QLocale = ...  # 0x3c
    JavaneseScript: QLocale = ...  # 0x3c
    DominicanRepublic: QLocale = ...  # 0x3d
    KaithiScript: QLocale = ...  # 0x3d
    Kannada: QLocale = ...  # 0x3d
    EastTimor: QLocale = ...  # 0x3e
    Kashmiri: QLocale = ...  # 0x3e
    KatakanaScript: QLocale = ...  # 0x3e
    Ecuador: QLocale = ...  # 0x3f
    KayahLiScript: QLocale = ...  # 0x3f
    Kazakh: QLocale = ...  # 0x3f
    Egypt: QLocale = ...  # 0x40
    KharoshthiScript: QLocale = ...  # 0x40
    Kinyarwanda: QLocale = ...  # 0x40
    ElSalvador: QLocale = ...  # 0x41
    Kirghiz: QLocale = ...  # 0x41
    LannaScript: QLocale = ...  # 0x41
    EquatorialGuinea: QLocale = ...  # 0x42
    Korean: QLocale = ...  # 0x42
    LepchaScript: QLocale = ...  # 0x42
    Eritrea: QLocale = ...  # 0x43
    Kurdish: QLocale = ...  # 0x43
    LimbuScript: QLocale = ...  # 0x43
    Estonia: QLocale = ...  # 0x44
    Kurundi: QLocale = ...  # 0x44
    LinearBScript: QLocale = ...  # 0x44
    Rundi: QLocale = ...  # 0x44
    Ethiopia: QLocale = ...  # 0x45
    Lao: QLocale = ...  # 0x45
    LycianScript: QLocale = ...  # 0x45
    FalklandIslands: QLocale = ...  # 0x46
    Latin: QLocale = ...  # 0x46
    LydianScript: QLocale = ...  # 0x46
    FaroeIslands: QLocale = ...  # 0x47
    Latvian: QLocale = ...  # 0x47
    MandaeanScript: QLocale = ...  # 0x47
    Fiji: QLocale = ...  # 0x48
    Lingala: QLocale = ...  # 0x48
    MeiteiMayekScript: QLocale = ...  # 0x48
    Finland: QLocale = ...  # 0x49
    Lithuanian: QLocale = ...  # 0x49
    MeroiticScript: QLocale = ...  # 0x49
    France: QLocale = ...  # 0x4a
    Macedonian: QLocale = ...  # 0x4a
    MeroiticCursiveScript: QLocale = ...  # 0x4a
    Guernsey: QLocale = ...  # 0x4b
    Malagasy: QLocale = ...  # 0x4b
    NkoScript: QLocale = ...  # 0x4b
    FrenchGuiana: QLocale = ...  # 0x4c
    Malay: QLocale = ...  # 0x4c
    NewTaiLueScript: QLocale = ...  # 0x4c
    FrenchPolynesia: QLocale = ...  # 0x4d
    Malayalam: QLocale = ...  # 0x4d
    OghamScript: QLocale = ...  # 0x4d
    FrenchSouthernTerritories: QLocale = ...  # 0x4e
    Maltese: QLocale = ...  # 0x4e
    OlChikiScript: QLocale = ...  # 0x4e
    Gabon: QLocale = ...  # 0x4f
    Maori: QLocale = ...  # 0x4f
    OldItalicScript: QLocale = ...  # 0x4f
    Gambia: QLocale = ...  # 0x50
    Marathi: QLocale = ...  # 0x50
    OldPersianScript: QLocale = ...  # 0x50
    Georgia: QLocale = ...  # 0x51
    Marshallese: QLocale = ...  # 0x51
    OldSouthArabianScript: QLocale = ...  # 0x51
    Germany: QLocale = ...  # 0x52
    Mongolian: QLocale = ...  # 0x52
    OrkhonScript: QLocale = ...  # 0x52
    Ghana: QLocale = ...  # 0x53
    NauruLanguage: QLocale = ...  # 0x53
    OsmanyaScript: QLocale = ...  # 0x53
    Gibraltar: QLocale = ...  # 0x54
    Nepali: QLocale = ...  # 0x54
    PhagsPaScript: QLocale = ...  # 0x54
    Greece: QLocale = ...  # 0x55
    Norwegian: QLocale = ...  # 0x55
    NorwegianBokmal: QLocale = ...  # 0x55
    PhoenicianScript: QLocale = ...  # 0x55
    Greenland: QLocale = ...  # 0x56
    Occitan: QLocale = ...  # 0x56
    PollardPhoneticScript: QLocale = ...  # 0x56
    Grenada: QLocale = ...  # 0x57
    Oriya: QLocale = ...  # 0x57
    RejangScript: QLocale = ...  # 0x57
    Guadeloupe: QLocale = ...  # 0x58
    Pashto: QLocale = ...  # 0x58
    RunicScript: QLocale = ...  # 0x58
    Guam: QLocale = ...  # 0x59
    Persian: QLocale = ...  # 0x59
    SamaritanScript: QLocale = ...  # 0x59
    Guatemala: QLocale = ...  # 0x5a
    Polish: QLocale = ...  # 0x5a
    SaurashtraScript: QLocale = ...  # 0x5a
    Guinea: QLocale = ...  # 0x5b
    Portuguese: QLocale = ...  # 0x5b
    SharadaScript: QLocale = ...  # 0x5b
    GuineaBissau: QLocale = ...  # 0x5c
    Punjabi: QLocale = ...  # 0x5c
    ShavianScript: QLocale = ...  # 0x5c
    Guyana: QLocale = ...  # 0x5d
    Quechua: QLocale = ...  # 0x5d
    SoraSompengScript: QLocale = ...  # 0x5d
    CuneiformScript: QLocale = ...  # 0x5e
    Haiti: QLocale = ...  # 0x5e
    RhaetoRomance: QLocale = ...  # 0x5e
    Romansh: QLocale = ...  # 0x5e
    HeardAndMcDonaldIslands: QLocale = ...  # 0x5f
    Moldavian: QLocale = ...  # 0x5f
    Romanian: QLocale = ...  # 0x5f
    SundaneseScript: QLocale = ...  # 0x5f
    Honduras: QLocale = ...  # 0x60
    Russian: QLocale = ...  # 0x60
    SylotiNagriScript: QLocale = ...  # 0x60
    HongKong: QLocale = ...  # 0x61
    Samoan: QLocale = ...  # 0x61
    TagalogScript: QLocale = ...  # 0x61
    Hungary: QLocale = ...  # 0x62
    Sango: QLocale = ...  # 0x62
    TagbanwaScript: QLocale = ...  # 0x62
    Iceland: QLocale = ...  # 0x63
    Sanskrit: QLocale = ...  # 0x63
    TaiLeScript: QLocale = ...  # 0x63
    India: QLocale = ...  # 0x64
    Serbian: QLocale = ...  # 0x64
    SerboCroatian: QLocale = ...  # 0x64
    TaiVietScript: QLocale = ...  # 0x64
    Indonesia: QLocale = ...  # 0x65
    Ossetic: QLocale = ...  # 0x65
    TakriScript: QLocale = ...  # 0x65
    Iran: QLocale = ...  # 0x66
    SouthernSotho: QLocale = ...  # 0x66
    UgariticScript: QLocale = ...  # 0x66
    BrailleScript: QLocale = ...  # 0x67
    Iraq: QLocale = ...  # 0x67
    Tswana: QLocale = ...  # 0x67
    HiraganaScript: QLocale = ...  # 0x68
    Ireland: QLocale = ...  # 0x68
    Shona: QLocale = ...  # 0x68
    CaucasianAlbanianScript: QLocale = ...  # 0x69
    Israel: QLocale = ...  # 0x69
    Sindhi: QLocale = ...  # 0x69
    BassaVahScript: QLocale = ...  # 0x6a
    Italy: QLocale = ...  # 0x6a
    Sinhala: QLocale = ...  # 0x6a
    DuployanScript: QLocale = ...  # 0x6b
    Jamaica: QLocale = ...  # 0x6b
    Swati: QLocale = ...  # 0x6b
    ElbasanScript: QLocale = ...  # 0x6c
    Japan: QLocale = ...  # 0x6c
    Slovak: QLocale = ...  # 0x6c
    GranthaScript: QLocale = ...  # 0x6d
    Jordan: QLocale = ...  # 0x6d
    Slovenian: QLocale = ...  # 0x6d
    Kazakhstan: QLocale = ...  # 0x6e
    PahawhHmongScript: QLocale = ...  # 0x6e
    Somali: QLocale = ...  # 0x6e
    Kenya: QLocale = ...  # 0x6f
    KhojkiScript: QLocale = ...  # 0x6f
    Spanish: QLocale = ...  # 0x6f
    Kiribati: QLocale = ...  # 0x70
    LinearAScript: QLocale = ...  # 0x70
    Sundanese: QLocale = ...  # 0x70
    DemocraticRepublicOfKorea: QLocale = ...  # 0x71
    MahajaniScript: QLocale = ...  # 0x71
    NorthKorea: QLocale = ...  # 0x71
    Swahili: QLocale = ...  # 0x71
    ManichaeanScript: QLocale = ...  # 0x72
    RepublicOfKorea: QLocale = ...  # 0x72
    SouthKorea: QLocale = ...  # 0x72
    Swedish: QLocale = ...  # 0x72
    Kuwait: QLocale = ...  # 0x73
    MendeKikakuiScript: QLocale = ...  # 0x73
    Sardinian: QLocale = ...  # 0x73
    Kyrgyzstan: QLocale = ...  # 0x74
    ModiScript: QLocale = ...  # 0x74
    Tajik: QLocale = ...  # 0x74
    Laos: QLocale = ...  # 0x75
    MroScript: QLocale = ...  # 0x75
    Tamil: QLocale = ...  # 0x75
    Latvia: QLocale = ...  # 0x76
    OldNorthArabianScript: QLocale = ...  # 0x76
    Tatar: QLocale = ...  # 0x76
    Lebanon: QLocale = ...  # 0x77
    NabataeanScript: QLocale = ...  # 0x77
    Telugu: QLocale = ...  # 0x77
    Lesotho: QLocale = ...  # 0x78
    PalmyreneScript: QLocale = ...  # 0x78
    Thai: QLocale = ...  # 0x78
    Liberia: QLocale = ...  # 0x79
    PauCinHauScript: QLocale = ...  # 0x79
    Tibetan: QLocale = ...  # 0x79
    Libya: QLocale = ...  # 0x7a
    OldPermicScript: QLocale = ...  # 0x7a
    Tigrinya: QLocale = ...  # 0x7a
    Liechtenstein: QLocale = ...  # 0x7b
    PsalterPahlaviScript: QLocale = ...  # 0x7b
    Tongan: QLocale = ...  # 0x7b
    Lithuania: QLocale = ...  # 0x7c
    SiddhamScript: QLocale = ...  # 0x7c
    Tsonga: QLocale = ...  # 0x7c
    KhudawadiScript: QLocale = ...  # 0x7d
    Luxembourg: QLocale = ...  # 0x7d
    Turkish: QLocale = ...  # 0x7d
    Macau: QLocale = ...  # 0x7e
    TirhutaScript: QLocale = ...  # 0x7e
    Turkmen: QLocale = ...  # 0x7e
    Macedonia: QLocale = ...  # 0x7f
    Tahitian: QLocale = ...  # 0x7f
    VarangKshitiScript: QLocale = ...  # 0x7f
    AhomScript: QLocale = ...  # 0x80
    Madagascar: QLocale = ...  # 0x80
    Uighur: QLocale = ...  # 0x80
    Uigur: QLocale = ...  # 0x80
    AnatolianHieroglyphsScript: QLocale = ...  # 0x81
    Malawi: QLocale = ...  # 0x81
    Ukrainian: QLocale = ...  # 0x81
    HatranScript: QLocale = ...  # 0x82
    Malaysia: QLocale = ...  # 0x82
    Urdu: QLocale = ...  # 0x82
    Maldives: QLocale = ...  # 0x83
    MultaniScript: QLocale = ...  # 0x83
    Uzbek: QLocale = ...  # 0x83
    Mali: QLocale = ...  # 0x84
    OldHungarianScript: QLocale = ...  # 0x84
    Vietnamese: QLocale = ...  # 0x84
    Malta: QLocale = ...  # 0x85
    SignWritingScript: QLocale = ...  # 0x85
    Volapuk: QLocale = ...  # 0x85
    AdlamScript: QLocale = ...  # 0x86
    MarshallIslands: QLocale = ...  # 0x86
    Welsh: QLocale = ...  # 0x86
    BhaiksukiScript: QLocale = ...  # 0x87
    Martinique: QLocale = ...  # 0x87
    Wolof: QLocale = ...  # 0x87
    MarchenScript: QLocale = ...  # 0x88
    Mauritania: QLocale = ...  # 0x88
    Xhosa: QLocale = ...  # 0x88
    Mauritius: QLocale = ...  # 0x89
    NewaScript: QLocale = ...  # 0x89
    Yiddish: QLocale = ...  # 0x89
    Mayotte: QLocale = ...  # 0x8a
    OsageScript: QLocale = ...  # 0x8a
    Yoruba: QLocale = ...  # 0x8a
    Mexico: QLocale = ...  # 0x8b
    TangutScript: QLocale = ...  # 0x8b
    Zhuang: QLocale = ...  # 0x8b
    HanWithBopomofoScript: QLocale = ...  # 0x8c
    Micronesia: QLocale = ...  # 0x8c
    Zulu: QLocale = ...  # 0x8c
    JamoScript: QLocale = ...  # 0x8d
    LastScript: QLocale = ...  # 0x8d
    Moldova: QLocale = ...  # 0x8d
    NorwegianNynorsk: QLocale = ...  # 0x8d
    Bosnian: QLocale = ...  # 0x8e
    Monaco: QLocale = ...  # 0x8e
    Divehi: QLocale = ...  # 0x8f
    Mongolia: QLocale = ...  # 0x8f
    Manx: QLocale = ...  # 0x90
    Montserrat: QLocale = ...  # 0x90
    Cornish: QLocale = ...  # 0x91
    Morocco: QLocale = ...  # 0x91
    Akan: QLocale = ...  # 0x92
    Mozambique: QLocale = ...  # 0x92
    Twi: QLocale = ...  # 0x92
    Konkani: QLocale = ...  # 0x93
    Myanmar: QLocale = ...  # 0x93
    Ga: QLocale = ...  # 0x94
    Namibia: QLocale = ...  # 0x94
    Igbo: QLocale = ...  # 0x95
    NauruCountry: QLocale = ...  # 0x95
    Kamba: QLocale = ...  # 0x96
    Nepal: QLocale = ...  # 0x96
    Netherlands: QLocale = ...  # 0x97
    Syriac: QLocale = ...  # 0x97
    Blin: QLocale = ...  # 0x98
    CuraSao: QLocale = ...  # 0x98
    Geez: QLocale = ...  # 0x99
    NewCaledonia: QLocale = ...  # 0x99
    Koro: QLocale = ...  # 0x9a
    NewZealand: QLocale = ...  # 0x9a
    Nicaragua: QLocale = ...  # 0x9b
    Sidamo: QLocale = ...  # 0x9b
    Atsam: QLocale = ...  # 0x9c
    Niger: QLocale = ...  # 0x9c
    Nigeria: QLocale = ...  # 0x9d
    Tigre: QLocale = ...  # 0x9d
    Jju: QLocale = ...  # 0x9e
    Niue: QLocale = ...  # 0x9e
    Friulian: QLocale = ...  # 0x9f
    NorfolkIsland: QLocale = ...  # 0x9f
    NorthernMarianaIslands: QLocale = ...  # 0xa0
    Venda: QLocale = ...  # 0xa0
    Ewe: QLocale = ...  # 0xa1
    Norway: QLocale = ...  # 0xa1
    Oman: QLocale = ...  # 0xa2
    Walamo: QLocale = ...  # 0xa2
    Hawaiian: QLocale = ...  # 0xa3
    Pakistan: QLocale = ...  # 0xa3
    Palau: QLocale = ...  # 0xa4
    Tyap: QLocale = ...  # 0xa4
    Chewa: QLocale = ...  # 0xa5
    Nyanja: QLocale = ...  # 0xa5
    PalestinianTerritories: QLocale = ...  # 0xa5
    Filipino: QLocale = ...  # 0xa6
    Panama: QLocale = ...  # 0xa6
    Tagalog: QLocale = ...  # 0xa6
    PapuaNewGuinea: QLocale = ...  # 0xa7
    SwissGerman: QLocale = ...  # 0xa7
    Paraguay: QLocale = ...  # 0xa8
    SichuanYi: QLocale = ...  # 0xa8
    Kpelle: QLocale = ...  # 0xa9
    Peru: QLocale = ...  # 0xa9
    LowGerman: QLocale = ...  # 0xaa
    Philippines: QLocale = ...  # 0xaa
    Pitcairn: QLocale = ...  # 0xab
    SouthNdebele: QLocale = ...  # 0xab
    NorthernSotho: QLocale = ...  # 0xac
    Poland: QLocale = ...  # 0xac
    NorthernSami: QLocale = ...  # 0xad
    Portugal: QLocale = ...  # 0xad
    PuertoRico: QLocale = ...  # 0xae
    Taroko: QLocale = ...  # 0xae
    Gusii: QLocale = ...  # 0xaf
    Qatar: QLocale = ...  # 0xaf
    Reunion: QLocale = ...  # 0xb0
    Taita: QLocale = ...  # 0xb0
    Fulah: QLocale = ...  # 0xb1
    Romania: QLocale = ...  # 0xb1
    Kikuyu: QLocale = ...  # 0xb2
    Russia: QLocale = ...  # 0xb2
    RussianFederation: QLocale = ...  # 0xb2
    Rwanda: QLocale = ...  # 0xb3
    Samburu: QLocale = ...  # 0xb3
    SaintKittsAndNevis: QLocale = ...  # 0xb4
    Sena: QLocale = ...  # 0xb4
    NorthNdebele: QLocale = ...  # 0xb5
    SaintLucia: QLocale = ...  # 0xb5
    Rombo: QLocale = ...  # 0xb6
    SaintVincentAndTheGrenadines: QLocale = ...  # 0xb6
    Samoa: QLocale = ...  # 0xb7
    Tachelhit: QLocale = ...  # 0xb7
    Kabyle: QLocale = ...  # 0xb8
    SanMarino: QLocale = ...  # 0xb8
    Nyankole: QLocale = ...  # 0xb9
    SaoTomeAndPrincipe: QLocale = ...  # 0xb9
    Bena: QLocale = ...  # 0xba
    SaudiArabia: QLocale = ...  # 0xba
    Senegal: QLocale = ...  # 0xbb
    Vunjo: QLocale = ...  # 0xbb
    Bambara: QLocale = ...  # 0xbc
    Seychelles: QLocale = ...  # 0xbc
    Embu: QLocale = ...  # 0xbd
    SierraLeone: QLocale = ...  # 0xbd
    Cherokee: QLocale = ...  # 0xbe
    Singapore: QLocale = ...  # 0xbe
    Morisyen: QLocale = ...  # 0xbf
    Slovakia: QLocale = ...  # 0xbf
    Makonde: QLocale = ...  # 0xc0
    Slovenia: QLocale = ...  # 0xc0
    Langi: QLocale = ...  # 0xc1
    SolomonIslands: QLocale = ...  # 0xc1
    Ganda: QLocale = ...  # 0xc2
    Somalia: QLocale = ...  # 0xc2
    Bemba: QLocale = ...  # 0xc3
    SouthAfrica: QLocale = ...  # 0xc3
    Kabuverdianu: QLocale = ...  # 0xc4
    SouthGeorgiaAndTheSouthSandwichIslands: QLocale = ...  # 0xc4
    Meru: QLocale = ...  # 0xc5
    Spain: QLocale = ...  # 0xc5
    Kalenjin: QLocale = ...  # 0xc6
    SriLanka: QLocale = ...  # 0xc6
    Nama: QLocale = ...  # 0xc7
    SaintHelena: QLocale = ...  # 0xc7
    Machame: QLocale = ...  # 0xc8
    SaintPierreAndMiquelon: QLocale = ...  # 0xc8
    Colognian: QLocale = ...  # 0xc9
    Sudan: QLocale = ...  # 0xc9
    Masai: QLocale = ...  # 0xca
    Suriname: QLocale = ...  # 0xca
    Soga: QLocale = ...  # 0xcb
    SvalbardAndJanMayenIslands: QLocale = ...  # 0xcb
    Luyia: QLocale = ...  # 0xcc
    Swaziland: QLocale = ...  # 0xcc
    Asu: QLocale = ...  # 0xcd
    Sweden: QLocale = ...  # 0xcd
    Switzerland: QLocale = ...  # 0xce
    Teso: QLocale = ...  # 0xce
    Saho: QLocale = ...  # 0xcf
    Syria: QLocale = ...  # 0xcf
    SyrianArabRepublic: QLocale = ...  # 0xcf
    KoyraChiini: QLocale = ...  # 0xd0
    Taiwan: QLocale = ...  # 0xd0
    Rwa: QLocale = ...  # 0xd1
    Tajikistan: QLocale = ...  # 0xd1
    Luo: QLocale = ...  # 0xd2
    Tanzania: QLocale = ...  # 0xd2
    Chiga: QLocale = ...  # 0xd3
    Thailand: QLocale = ...  # 0xd3
    CentralMoroccoTamazight: QLocale = ...  # 0xd4
    Togo: QLocale = ...  # 0xd4
    KoyraboroSenni: QLocale = ...  # 0xd5
    Tokelau: QLocale = ...  # 0xd5
    TokelauCountry: QLocale = ...  # 0xd5
    Shambala: QLocale = ...  # 0xd6
    Tonga: QLocale = ...  # 0xd6
    Bodo: QLocale = ...  # 0xd7
    TrinidadAndTobago: QLocale = ...  # 0xd7
    Avaric: QLocale = ...  # 0xd8
    Tunisia: QLocale = ...  # 0xd8
    Chamorro: QLocale = ...  # 0xd9
    Turkey: QLocale = ...  # 0xd9
    Chechen: QLocale = ...  # 0xda
    Turkmenistan: QLocale = ...  # 0xda
    Church: QLocale = ...  # 0xdb
    TurksAndCaicosIslands: QLocale = ...  # 0xdb
    Chuvash: QLocale = ...  # 0xdc
    Tuvalu: QLocale = ...  # 0xdc
    TuvaluCountry: QLocale = ...  # 0xdc
    Cree: QLocale = ...  # 0xdd
    Uganda: QLocale = ...  # 0xdd
    Haitian: QLocale = ...  # 0xde
    Ukraine: QLocale = ...  # 0xde
    Herero: QLocale = ...  # 0xdf
    UnitedArabEmirates: QLocale = ...  # 0xdf
    HiriMotu: QLocale = ...  # 0xe0
    UnitedKingdom: QLocale = ...  # 0xe0
    Kanuri: QLocale = ...  # 0xe1
    UnitedStates: QLocale = ...  # 0xe1
    Komi: QLocale = ...  # 0xe2
    UnitedStatesMinorOutlyingIslands: QLocale = ...  # 0xe2
    Kongo: QLocale = ...  # 0xe3
    Uruguay: QLocale = ...  # 0xe3
    Kwanyama: QLocale = ...  # 0xe4
    Uzbekistan: QLocale = ...  # 0xe4
    Limburgish: QLocale = ...  # 0xe5
    Vanuatu: QLocale = ...  # 0xe5
    LubaKatanga: QLocale = ...  # 0xe6
    VaticanCityState: QLocale = ...  # 0xe6
    Luxembourgish: QLocale = ...  # 0xe7
    Venezuela: QLocale = ...  # 0xe7
    Navaho: QLocale = ...  # 0xe8
    Vietnam: QLocale = ...  # 0xe8
    BritishVirginIslands: QLocale = ...  # 0xe9
    Ndonga: QLocale = ...  # 0xe9
    Ojibwa: QLocale = ...  # 0xea
    UnitedStatesVirginIslands: QLocale = ...  # 0xea
    Pali: QLocale = ...  # 0xeb
    WallisAndFutunaIslands: QLocale = ...  # 0xeb
    Walloon: QLocale = ...  # 0xec
    WesternSahara: QLocale = ...  # 0xec
    Aghem: QLocale = ...  # 0xed
    Yemen: QLocale = ...  # 0xed
    Basaa: QLocale = ...  # 0xee
    CanaryIslands: QLocale = ...  # 0xee
    Zambia: QLocale = ...  # 0xef
    Zarma: QLocale = ...  # 0xef
    Duala: QLocale = ...  # 0xf0
    Zimbabwe: QLocale = ...  # 0xf0
    ClippertonIsland: QLocale = ...  # 0xf1
    JolaFonyi: QLocale = ...  # 0xf1
    Ewondo: QLocale = ...  # 0xf2
    Montenegro: QLocale = ...  # 0xf2
    Bafia: QLocale = ...  # 0xf3
    Serbia: QLocale = ...  # 0xf3
    MakhuwaMeetto: QLocale = ...  # 0xf4
    SaintBarthelemy: QLocale = ...  # 0xf4
    Mundang: QLocale = ...  # 0xf5
    SaintMartin: QLocale = ...  # 0xf5
    Kwasio: QLocale = ...  # 0xf6
    LatinAmerica: QLocale = ...  # 0xf6
    LatinAmericaAndTheCaribbean: QLocale = ...  # 0xf6
    AscensionIsland: QLocale = ...  # 0xf7
    Nuer: QLocale = ...  # 0xf7
    AlandIslands: QLocale = ...  # 0xf8
    Sakha: QLocale = ...  # 0xf8
    DiegoGarcia: QLocale = ...  # 0xf9
    Sangu: QLocale = ...  # 0xf9
    CeutaAndMelilla: QLocale = ...  # 0xfa
    CongoSwahili: QLocale = ...  # 0xfa
    IsleOfMan: QLocale = ...  # 0xfb
    Tasawaq: QLocale = ...  # 0xfb
    Jersey: QLocale = ...  # 0xfc
    Vai: QLocale = ...  # 0xfc
    TristanDaCunha: QLocale = ...  # 0xfd
    Walser: QLocale = ...  # 0xfd
    SouthSudan: QLocale = ...  # 0xfe
    Yangben: QLocale = ...  # 0xfe
    Avestan: QLocale = ...  # 0xff
    Bonaire: QLocale = ...  # 0xff
    Asturian: QLocale = ...  # 0x100
    SintMaarten: QLocale = ...  # 0x100
    Kosovo: QLocale = ...  # 0x101
    Ngomba: QLocale = ...  # 0x101
    EuropeanUnion: QLocale = ...  # 0x102
    Kako: QLocale = ...  # 0x102
    Meta: QLocale = ...  # 0x103
    OutlyingOceania: QLocale = ...  # 0x103
    Ngiemboon: QLocale = ...  # 0x104
    World: QLocale = ...  # 0x104
    Aragonese: QLocale = ...  # 0x105
    Europe: QLocale = ...  # 0x105
    LastCountry: QLocale = ...  # 0x105
    Akkadian: QLocale = ...  # 0x106
    AncientEgyptian: QLocale = ...  # 0x107
    AncientGreek: QLocale = ...  # 0x108
    Aramaic: QLocale = ...  # 0x109
    Balinese: QLocale = ...  # 0x10a
    Bamun: QLocale = ...  # 0x10b
    BatakToba: QLocale = ...  # 0x10c
    Buginese: QLocale = ...  # 0x10d
    Buhid: QLocale = ...  # 0x10e
    Carian: QLocale = ...  # 0x10f
    Chakma: QLocale = ...  # 0x110
    ClassicalMandaic: QLocale = ...  # 0x111
    Coptic: QLocale = ...  # 0x112
    Dogri: QLocale = ...  # 0x113
    EasternCham: QLocale = ...  # 0x114
    EasternKayah: QLocale = ...  # 0x115
    Etruscan: QLocale = ...  # 0x116
    Gothic: QLocale = ...  # 0x117
    Hanunoo: QLocale = ...  # 0x118
    Ingush: QLocale = ...  # 0x119
    LargeFloweryMiao: QLocale = ...  # 0x11a
    Lepcha: QLocale = ...  # 0x11b
    Limbu: QLocale = ...  # 0x11c
    Lisu: QLocale = ...  # 0x11d
    Lu: QLocale = ...  # 0x11e
    Lycian: QLocale = ...  # 0x11f
    Lydian: QLocale = ...  # 0x120
    Mandingo: QLocale = ...  # 0x121
    Manipuri: QLocale = ...  # 0x122
    Meroitic: QLocale = ...  # 0x123
    NorthernThai: QLocale = ...  # 0x124
    OldIrish: QLocale = ...  # 0x125
    OldNorse: QLocale = ...  # 0x126
    OldPersian: QLocale = ...  # 0x127
    OldTurkish: QLocale = ...  # 0x128
    Pahlavi: QLocale = ...  # 0x129
    Parthian: QLocale = ...  # 0x12a
    Phoenician: QLocale = ...  # 0x12b
    PrakritLanguage: QLocale = ...  # 0x12c
    Rejang: QLocale = ...  # 0x12d
    Sabaean: QLocale = ...  # 0x12e
    Samaritan: QLocale = ...  # 0x12f
    Santali: QLocale = ...  # 0x130
    Saurashtra: QLocale = ...  # 0x131
    Sora: QLocale = ...  # 0x132
    Sylheti: QLocale = ...  # 0x133
    Tagbanwa: QLocale = ...  # 0x134
    TaiDam: QLocale = ...  # 0x135
    TaiNua: QLocale = ...  # 0x136
    Ugaritic: QLocale = ...  # 0x137
    Akoose: QLocale = ...  # 0x138
    Lakota: QLocale = ...  # 0x139
    StandardMoroccanTamazight: QLocale = ...  # 0x13a
    Mapuche: QLocale = ...  # 0x13b
    CentralKurdish: QLocale = ...  # 0x13c
    LowerSorbian: QLocale = ...  # 0x13d
    UpperSorbian: QLocale = ...  # 0x13e
    Kenyang: QLocale = ...  # 0x13f
    Mohawk: QLocale = ...  # 0x140
    Nko: QLocale = ...  # 0x141
    Prussian: QLocale = ...  # 0x142
    Kiche: QLocale = ...  # 0x143
    SouthernSami: QLocale = ...  # 0x144
    LuleSami: QLocale = ...  # 0x145
    InariSami: QLocale = ...  # 0x146
    SkoltSami: QLocale = ...  # 0x147
    Warlpiri: QLocale = ...  # 0x148
    ManichaeanMiddlePersian: QLocale = ...  # 0x149
    Mende: QLocale = ...  # 0x14a
    AncientNorthArabian: QLocale = ...  # 0x14b
    LinearA: QLocale = ...  # 0x14c
    HmongNjua: QLocale = ...  # 0x14d
    Ho: QLocale = ...  # 0x14e
    Lezghian: QLocale = ...  # 0x14f
    Bassa: QLocale = ...  # 0x150
    Mono: QLocale = ...  # 0x151
    TedimChin: QLocale = ...  # 0x152
    Maithili: QLocale = ...  # 0x153
    Ahom: QLocale = ...  # 0x154
    AmericanSignLanguage: QLocale = ...  # 0x155
    ArdhamagadhiPrakrit: QLocale = ...  # 0x156
    Bhojpuri: QLocale = ...  # 0x157
    HieroglyphicLuwian: QLocale = ...  # 0x158
    LiteraryChinese: QLocale = ...  # 0x159
    Mazanderani: QLocale = ...  # 0x15a
    Mru: QLocale = ...  # 0x15b
    Newari: QLocale = ...  # 0x15c
    NorthernLuri: QLocale = ...  # 0x15d
    Palauan: QLocale = ...  # 0x15e
    Papiamento: QLocale = ...  # 0x15f
    Saraiki: QLocale = ...  # 0x160
    TokelauLanguage: QLocale = ...  # 0x161
    TokPisin: QLocale = ...  # 0x162
    TuvaluLanguage: QLocale = ...  # 0x163
    UncodedLanguages: QLocale = ...  # 0x164
    Cantonese: QLocale = ...  # 0x165
    Osage: QLocale = ...  # 0x166
    Tangut: QLocale = ...  # 0x167
    Ido: QLocale = ...  # 0x168
    Lojban: QLocale = ...  # 0x169
    Sicilian: QLocale = ...  # 0x16a
    SouthernKurdish: QLocale = ...  # 0x16b
    WesternBalochi: QLocale = ...  # 0x16c
    Cebuano: QLocale = ...  # 0x16d
    Erzya: QLocale = ...  # 0x16e
    Chickasaw: QLocale = ...  # 0x16f
    Muscogee: QLocale = ...  # 0x170
    LastLanguage: QLocale = ...  # 0x171
    Silesian: QLocale = ...  # 0x171

    class Country(object):
        AnyCountry: QLocale.Country = ...  # 0x0
        Afghanistan: QLocale.Country = ...  # 0x1
        Albania: QLocale.Country = ...  # 0x2
        Algeria: QLocale.Country = ...  # 0x3
        AmericanSamoa: QLocale.Country = ...  # 0x4
        Andorra: QLocale.Country = ...  # 0x5
        Angola: QLocale.Country = ...  # 0x6
        Anguilla: QLocale.Country = ...  # 0x7
        Antarctica: QLocale.Country = ...  # 0x8
        AntiguaAndBarbuda: QLocale.Country = ...  # 0x9
        Argentina: QLocale.Country = ...  # 0xa
        Armenia: QLocale.Country = ...  # 0xb
        Aruba: QLocale.Country = ...  # 0xc
        Australia: QLocale.Country = ...  # 0xd
        Austria: QLocale.Country = ...  # 0xe
        Azerbaijan: QLocale.Country = ...  # 0xf
        Bahamas: QLocale.Country = ...  # 0x10
        Bahrain: QLocale.Country = ...  # 0x11
        Bangladesh: QLocale.Country = ...  # 0x12
        Barbados: QLocale.Country = ...  # 0x13
        Belarus: QLocale.Country = ...  # 0x14
        Belgium: QLocale.Country = ...  # 0x15
        Belize: QLocale.Country = ...  # 0x16
        Benin: QLocale.Country = ...  # 0x17
        Bermuda: QLocale.Country = ...  # 0x18
        Bhutan: QLocale.Country = ...  # 0x19
        Bolivia: QLocale.Country = ...  # 0x1a
        BosniaAndHerzegowina: QLocale.Country = ...  # 0x1b
        Botswana: QLocale.Country = ...  # 0x1c
        BouvetIsland: QLocale.Country = ...  # 0x1d
        Brazil: QLocale.Country = ...  # 0x1e
        BritishIndianOceanTerritory: QLocale.Country = ...  # 0x1f
        Brunei: QLocale.Country = ...  # 0x20
        Bulgaria: QLocale.Country = ...  # 0x21
        BurkinaFaso: QLocale.Country = ...  # 0x22
        Burundi: QLocale.Country = ...  # 0x23
        Cambodia: QLocale.Country = ...  # 0x24
        Cameroon: QLocale.Country = ...  # 0x25
        Canada: QLocale.Country = ...  # 0x26
        CapeVerde: QLocale.Country = ...  # 0x27
        CaymanIslands: QLocale.Country = ...  # 0x28
        CentralAfricanRepublic: QLocale.Country = ...  # 0x29
        Chad: QLocale.Country = ...  # 0x2a
        Chile: QLocale.Country = ...  # 0x2b
        China: QLocale.Country = ...  # 0x2c
        ChristmasIsland: QLocale.Country = ...  # 0x2d
        CocosIslands: QLocale.Country = ...  # 0x2e
        Colombia: QLocale.Country = ...  # 0x2f
        Comoros: QLocale.Country = ...  # 0x30
        CongoKinshasa: QLocale.Country = ...  # 0x31
        DemocraticRepublicOfCongo: QLocale.Country = ...  # 0x31
        CongoBrazzaville: QLocale.Country = ...  # 0x32
        PeoplesRepublicOfCongo: QLocale.Country = ...  # 0x32
        CookIslands: QLocale.Country = ...  # 0x33
        CostaRica: QLocale.Country = ...  # 0x34
        IvoryCoast: QLocale.Country = ...  # 0x35
        Croatia: QLocale.Country = ...  # 0x36
        Cuba: QLocale.Country = ...  # 0x37
        Cyprus: QLocale.Country = ...  # 0x38
        CzechRepublic: QLocale.Country = ...  # 0x39
        Denmark: QLocale.Country = ...  # 0x3a
        Djibouti: QLocale.Country = ...  # 0x3b
        Dominica: QLocale.Country = ...  # 0x3c
        DominicanRepublic: QLocale.Country = ...  # 0x3d
        EastTimor: QLocale.Country = ...  # 0x3e
        Ecuador: QLocale.Country = ...  # 0x3f
        Egypt: QLocale.Country = ...  # 0x40
        ElSalvador: QLocale.Country = ...  # 0x41
        EquatorialGuinea: QLocale.Country = ...  # 0x42
        Eritrea: QLocale.Country = ...  # 0x43
        Estonia: QLocale.Country = ...  # 0x44
        Ethiopia: QLocale.Country = ...  # 0x45
        FalklandIslands: QLocale.Country = ...  # 0x46
        FaroeIslands: QLocale.Country = ...  # 0x47
        Fiji: QLocale.Country = ...  # 0x48
        Finland: QLocale.Country = ...  # 0x49
        France: QLocale.Country = ...  # 0x4a
        Guernsey: QLocale.Country = ...  # 0x4b
        FrenchGuiana: QLocale.Country = ...  # 0x4c
        FrenchPolynesia: QLocale.Country = ...  # 0x4d
        FrenchSouthernTerritories: QLocale.Country = ...  # 0x4e
        Gabon: QLocale.Country = ...  # 0x4f
        Gambia: QLocale.Country = ...  # 0x50
        Georgia: QLocale.Country = ...  # 0x51
        Germany: QLocale.Country = ...  # 0x52
        Ghana: QLocale.Country = ...  # 0x53
        Gibraltar: QLocale.Country = ...  # 0x54
        Greece: QLocale.Country = ...  # 0x55
        Greenland: QLocale.Country = ...  # 0x56
        Grenada: QLocale.Country = ...  # 0x57
        Guadeloupe: QLocale.Country = ...  # 0x58
        Guam: QLocale.Country = ...  # 0x59
        Guatemala: QLocale.Country = ...  # 0x5a
        Guinea: QLocale.Country = ...  # 0x5b
        GuineaBissau: QLocale.Country = ...  # 0x5c
        Guyana: QLocale.Country = ...  # 0x5d
        Haiti: QLocale.Country = ...  # 0x5e
        HeardAndMcDonaldIslands: QLocale.Country = ...  # 0x5f
        Honduras: QLocale.Country = ...  # 0x60
        HongKong: QLocale.Country = ...  # 0x61
        Hungary: QLocale.Country = ...  # 0x62
        Iceland: QLocale.Country = ...  # 0x63
        India: QLocale.Country = ...  # 0x64
        Indonesia: QLocale.Country = ...  # 0x65
        Iran: QLocale.Country = ...  # 0x66
        Iraq: QLocale.Country = ...  # 0x67
        Ireland: QLocale.Country = ...  # 0x68
        Israel: QLocale.Country = ...  # 0x69
        Italy: QLocale.Country = ...  # 0x6a
        Jamaica: QLocale.Country = ...  # 0x6b
        Japan: QLocale.Country = ...  # 0x6c
        Jordan: QLocale.Country = ...  # 0x6d
        Kazakhstan: QLocale.Country = ...  # 0x6e
        Kenya: QLocale.Country = ...  # 0x6f
        Kiribati: QLocale.Country = ...  # 0x70
        DemocraticRepublicOfKorea: QLocale.Country = ...  # 0x71
        NorthKorea: QLocale.Country = ...  # 0x71
        RepublicOfKorea: QLocale.Country = ...  # 0x72
        SouthKorea: QLocale.Country = ...  # 0x72
        Kuwait: QLocale.Country = ...  # 0x73
        Kyrgyzstan: QLocale.Country = ...  # 0x74
        Laos: QLocale.Country = ...  # 0x75
        Latvia: QLocale.Country = ...  # 0x76
        Lebanon: QLocale.Country = ...  # 0x77
        Lesotho: QLocale.Country = ...  # 0x78
        Liberia: QLocale.Country = ...  # 0x79
        Libya: QLocale.Country = ...  # 0x7a
        Liechtenstein: QLocale.Country = ...  # 0x7b
        Lithuania: QLocale.Country = ...  # 0x7c
        Luxembourg: QLocale.Country = ...  # 0x7d
        Macau: QLocale.Country = ...  # 0x7e
        Macedonia: QLocale.Country = ...  # 0x7f
        Madagascar: QLocale.Country = ...  # 0x80
        Malawi: QLocale.Country = ...  # 0x81
        Malaysia: QLocale.Country = ...  # 0x82
        Maldives: QLocale.Country = ...  # 0x83
        Mali: QLocale.Country = ...  # 0x84
        Malta: QLocale.Country = ...  # 0x85
        MarshallIslands: QLocale.Country = ...  # 0x86
        Martinique: QLocale.Country = ...  # 0x87
        Mauritania: QLocale.Country = ...  # 0x88
        Mauritius: QLocale.Country = ...  # 0x89
        Mayotte: QLocale.Country = ...  # 0x8a
        Mexico: QLocale.Country = ...  # 0x8b
        Micronesia: QLocale.Country = ...  # 0x8c
        Moldova: QLocale.Country = ...  # 0x8d
        Monaco: QLocale.Country = ...  # 0x8e
        Mongolia: QLocale.Country = ...  # 0x8f
        Montserrat: QLocale.Country = ...  # 0x90
        Morocco: QLocale.Country = ...  # 0x91
        Mozambique: QLocale.Country = ...  # 0x92
        Myanmar: QLocale.Country = ...  # 0x93
        Namibia: QLocale.Country = ...  # 0x94
        NauruCountry: QLocale.Country = ...  # 0x95
        Nepal: QLocale.Country = ...  # 0x96
        Netherlands: QLocale.Country = ...  # 0x97
        CuraSao: QLocale.Country = ...  # 0x98
        NewCaledonia: QLocale.Country = ...  # 0x99
        NewZealand: QLocale.Country = ...  # 0x9a
        Nicaragua: QLocale.Country = ...  # 0x9b
        Niger: QLocale.Country = ...  # 0x9c
        Nigeria: QLocale.Country = ...  # 0x9d
        Niue: QLocale.Country = ...  # 0x9e
        NorfolkIsland: QLocale.Country = ...  # 0x9f
        NorthernMarianaIslands: QLocale.Country = ...  # 0xa0
        Norway: QLocale.Country = ...  # 0xa1
        Oman: QLocale.Country = ...  # 0xa2
        Pakistan: QLocale.Country = ...  # 0xa3
        Palau: QLocale.Country = ...  # 0xa4
        PalestinianTerritories: QLocale.Country = ...  # 0xa5
        Panama: QLocale.Country = ...  # 0xa6
        PapuaNewGuinea: QLocale.Country = ...  # 0xa7
        Paraguay: QLocale.Country = ...  # 0xa8
        Peru: QLocale.Country = ...  # 0xa9
        Philippines: QLocale.Country = ...  # 0xaa
        Pitcairn: QLocale.Country = ...  # 0xab
        Poland: QLocale.Country = ...  # 0xac
        Portugal: QLocale.Country = ...  # 0xad
        PuertoRico: QLocale.Country = ...  # 0xae
        Qatar: QLocale.Country = ...  # 0xaf
        Reunion: QLocale.Country = ...  # 0xb0
        Romania: QLocale.Country = ...  # 0xb1
        Russia: QLocale.Country = ...  # 0xb2
        RussianFederation: QLocale.Country = ...  # 0xb2
        Rwanda: QLocale.Country = ...  # 0xb3
        SaintKittsAndNevis: QLocale.Country = ...  # 0xb4
        SaintLucia: QLocale.Country = ...  # 0xb5
        SaintVincentAndTheGrenadines: QLocale.Country = ...  # 0xb6
        Samoa: QLocale.Country = ...  # 0xb7
        SanMarino: QLocale.Country = ...  # 0xb8
        SaoTomeAndPrincipe: QLocale.Country = ...  # 0xb9
        SaudiArabia: QLocale.Country = ...  # 0xba
        Senegal: QLocale.Country = ...  # 0xbb
        Seychelles: QLocale.Country = ...  # 0xbc
        SierraLeone: QLocale.Country = ...  # 0xbd
        Singapore: QLocale.Country = ...  # 0xbe
        Slovakia: QLocale.Country = ...  # 0xbf
        Slovenia: QLocale.Country = ...  # 0xc0
        SolomonIslands: QLocale.Country = ...  # 0xc1
        Somalia: QLocale.Country = ...  # 0xc2
        SouthAfrica: QLocale.Country = ...  # 0xc3
        SouthGeorgiaAndTheSouthSandwichIslands: QLocale.Country = ...  # 0xc4
        Spain: QLocale.Country = ...  # 0xc5
        SriLanka: QLocale.Country = ...  # 0xc6
        SaintHelena: QLocale.Country = ...  # 0xc7
        SaintPierreAndMiquelon: QLocale.Country = ...  # 0xc8
        Sudan: QLocale.Country = ...  # 0xc9
        Suriname: QLocale.Country = ...  # 0xca
        SvalbardAndJanMayenIslands: QLocale.Country = ...  # 0xcb
        Swaziland: QLocale.Country = ...  # 0xcc
        Sweden: QLocale.Country = ...  # 0xcd
        Switzerland: QLocale.Country = ...  # 0xce
        Syria: QLocale.Country = ...  # 0xcf
        SyrianArabRepublic: QLocale.Country = ...  # 0xcf
        Taiwan: QLocale.Country = ...  # 0xd0
        Tajikistan: QLocale.Country = ...  # 0xd1
        Tanzania: QLocale.Country = ...  # 0xd2
        Thailand: QLocale.Country = ...  # 0xd3
        Togo: QLocale.Country = ...  # 0xd4
        Tokelau: QLocale.Country = ...  # 0xd5
        TokelauCountry: QLocale.Country = ...  # 0xd5
        Tonga: QLocale.Country = ...  # 0xd6
        TrinidadAndTobago: QLocale.Country = ...  # 0xd7
        Tunisia: QLocale.Country = ...  # 0xd8
        Turkey: QLocale.Country = ...  # 0xd9
        Turkmenistan: QLocale.Country = ...  # 0xda
        TurksAndCaicosIslands: QLocale.Country = ...  # 0xdb
        Tuvalu: QLocale.Country = ...  # 0xdc
        TuvaluCountry: QLocale.Country = ...  # 0xdc
        Uganda: QLocale.Country = ...  # 0xdd
        Ukraine: QLocale.Country = ...  # 0xde
        UnitedArabEmirates: QLocale.Country = ...  # 0xdf
        UnitedKingdom: QLocale.Country = ...  # 0xe0
        UnitedStates: QLocale.Country = ...  # 0xe1
        UnitedStatesMinorOutlyingIslands: QLocale.Country = ...  # 0xe2
        Uruguay: QLocale.Country = ...  # 0xe3
        Uzbekistan: QLocale.Country = ...  # 0xe4
        Vanuatu: QLocale.Country = ...  # 0xe5
        VaticanCityState: QLocale.Country = ...  # 0xe6
        Venezuela: QLocale.Country = ...  # 0xe7
        Vietnam: QLocale.Country = ...  # 0xe8
        BritishVirginIslands: QLocale.Country = ...  # 0xe9
        UnitedStatesVirginIslands: QLocale.Country = ...  # 0xea
        WallisAndFutunaIslands: QLocale.Country = ...  # 0xeb
        WesternSahara: QLocale.Country = ...  # 0xec
        Yemen: QLocale.Country = ...  # 0xed
        CanaryIslands: QLocale.Country = ...  # 0xee
        Zambia: QLocale.Country = ...  # 0xef
        Zimbabwe: QLocale.Country = ...  # 0xf0
        ClippertonIsland: QLocale.Country = ...  # 0xf1
        Montenegro: QLocale.Country = ...  # 0xf2
        Serbia: QLocale.Country = ...  # 0xf3
        SaintBarthelemy: QLocale.Country = ...  # 0xf4
        SaintMartin: QLocale.Country = ...  # 0xf5
        LatinAmerica: QLocale.Country = ...  # 0xf6
        LatinAmericaAndTheCaribbean: QLocale.Country = ...  # 0xf6
        AscensionIsland: QLocale.Country = ...  # 0xf7
        AlandIslands: QLocale.Country = ...  # 0xf8
        DiegoGarcia: QLocale.Country = ...  # 0xf9
        CeutaAndMelilla: QLocale.Country = ...  # 0xfa
        IsleOfMan: QLocale.Country = ...  # 0xfb
        Jersey: QLocale.Country = ...  # 0xfc
        TristanDaCunha: QLocale.Country = ...  # 0xfd
        SouthSudan: QLocale.Country = ...  # 0xfe
        Bonaire: QLocale.Country = ...  # 0xff
        SintMaarten: QLocale.Country = ...  # 0x100
        Kosovo: QLocale.Country = ...  # 0x101
        EuropeanUnion: QLocale.Country = ...  # 0x102
        OutlyingOceania: QLocale.Country = ...  # 0x103
        World: QLocale.Country = ...  # 0x104
        Europe: QLocale.Country = ...  # 0x105
        LastCountry: QLocale.Country = ...  # 0x105

    class CurrencySymbolFormat(object):
        CurrencyIsoCode: QLocale.CurrencySymbolFormat = ...  # 0x0
        CurrencySymbol: QLocale.CurrencySymbolFormat = ...  # 0x1
        CurrencyDisplayName: QLocale.CurrencySymbolFormat = ...  # 0x2

    class DataSizeFormat(object):
        DataSizeIecFormat: QLocale.DataSizeFormat = ...  # 0x0
        DataSizeBase1000: QLocale.DataSizeFormat = ...  # 0x1
        DataSizeSIQuantifiers: QLocale.DataSizeFormat = ...  # 0x2
        DataSizeTraditionalFormat: QLocale.DataSizeFormat = ...  # 0x2
        DataSizeSIFormat: QLocale.DataSizeFormat = ...  # 0x3

    class DataSizeFormats(object): ...

    class FloatingPointPrecisionOption(object):
        FloatingPointShortest: QLocale.FloatingPointPrecisionOption = ...  # -0x80

    class FormatType(object):
        LongFormat: QLocale.FormatType = ...  # 0x0
        ShortFormat: QLocale.FormatType = ...  # 0x1
        NarrowFormat: QLocale.FormatType = ...  # 0x2

    class Language(object):
        AnyLanguage: QLocale.Language = ...  # 0x0
        C: QLocale.Language = ...  # 0x1
        Abkhazian: QLocale.Language = ...  # 0x2
        Afan: QLocale.Language = ...  # 0x3
        Oromo: QLocale.Language = ...  # 0x3
        Afar: QLocale.Language = ...  # 0x4
        Afrikaans: QLocale.Language = ...  # 0x5
        Albanian: QLocale.Language = ...  # 0x6
        Amharic: QLocale.Language = ...  # 0x7
        Arabic: QLocale.Language = ...  # 0x8
        Armenian: QLocale.Language = ...  # 0x9
        Assamese: QLocale.Language = ...  # 0xa
        Aymara: QLocale.Language = ...  # 0xb
        Azerbaijani: QLocale.Language = ...  # 0xc
        Bashkir: QLocale.Language = ...  # 0xd
        Basque: QLocale.Language = ...  # 0xe
        Bengali: QLocale.Language = ...  # 0xf
        Bhutani: QLocale.Language = ...  # 0x10
        Dzongkha: QLocale.Language = ...  # 0x10
        Bihari: QLocale.Language = ...  # 0x11
        Bislama: QLocale.Language = ...  # 0x12
        Breton: QLocale.Language = ...  # 0x13
        Bulgarian: QLocale.Language = ...  # 0x14
        Burmese: QLocale.Language = ...  # 0x15
        Belarusian: QLocale.Language = ...  # 0x16
        Byelorussian: QLocale.Language = ...  # 0x16
        Cambodian: QLocale.Language = ...  # 0x17
        Khmer: QLocale.Language = ...  # 0x17
        Catalan: QLocale.Language = ...  # 0x18
        Chinese: QLocale.Language = ...  # 0x19
        Corsican: QLocale.Language = ...  # 0x1a
        Croatian: QLocale.Language = ...  # 0x1b
        Czech: QLocale.Language = ...  # 0x1c
        Danish: QLocale.Language = ...  # 0x1d
        Dutch: QLocale.Language = ...  # 0x1e
        English: QLocale.Language = ...  # 0x1f
        Esperanto: QLocale.Language = ...  # 0x20
        Estonian: QLocale.Language = ...  # 0x21
        Faroese: QLocale.Language = ...  # 0x22
        Fijian: QLocale.Language = ...  # 0x23
        Finnish: QLocale.Language = ...  # 0x24
        French: QLocale.Language = ...  # 0x25
        Frisian: QLocale.Language = ...  # 0x26
        WesternFrisian: QLocale.Language = ...  # 0x26
        Gaelic: QLocale.Language = ...  # 0x27
        Galician: QLocale.Language = ...  # 0x28
        Georgian: QLocale.Language = ...  # 0x29
        German: QLocale.Language = ...  # 0x2a
        Greek: QLocale.Language = ...  # 0x2b
        Greenlandic: QLocale.Language = ...  # 0x2c
        Guarani: QLocale.Language = ...  # 0x2d
        Gujarati: QLocale.Language = ...  # 0x2e
        Hausa: QLocale.Language = ...  # 0x2f
        Hebrew: QLocale.Language = ...  # 0x30
        Hindi: QLocale.Language = ...  # 0x31
        Hungarian: QLocale.Language = ...  # 0x32
        Icelandic: QLocale.Language = ...  # 0x33
        Indonesian: QLocale.Language = ...  # 0x34
        Interlingua: QLocale.Language = ...  # 0x35
        Interlingue: QLocale.Language = ...  # 0x36
        Inuktitut: QLocale.Language = ...  # 0x37
        Inupiak: QLocale.Language = ...  # 0x38
        Irish: QLocale.Language = ...  # 0x39
        Italian: QLocale.Language = ...  # 0x3a
        Japanese: QLocale.Language = ...  # 0x3b
        Javanese: QLocale.Language = ...  # 0x3c
        Kannada: QLocale.Language = ...  # 0x3d
        Kashmiri: QLocale.Language = ...  # 0x3e
        Kazakh: QLocale.Language = ...  # 0x3f
        Kinyarwanda: QLocale.Language = ...  # 0x40
        Kirghiz: QLocale.Language = ...  # 0x41
        Korean: QLocale.Language = ...  # 0x42
        Kurdish: QLocale.Language = ...  # 0x43
        Kurundi: QLocale.Language = ...  # 0x44
        Rundi: QLocale.Language = ...  # 0x44
        Lao: QLocale.Language = ...  # 0x45
        Latin: QLocale.Language = ...  # 0x46
        Latvian: QLocale.Language = ...  # 0x47
        Lingala: QLocale.Language = ...  # 0x48
        Lithuanian: QLocale.Language = ...  # 0x49
        Macedonian: QLocale.Language = ...  # 0x4a
        Malagasy: QLocale.Language = ...  # 0x4b
        Malay: QLocale.Language = ...  # 0x4c
        Malayalam: QLocale.Language = ...  # 0x4d
        Maltese: QLocale.Language = ...  # 0x4e
        Maori: QLocale.Language = ...  # 0x4f
        Marathi: QLocale.Language = ...  # 0x50
        Marshallese: QLocale.Language = ...  # 0x51
        Mongolian: QLocale.Language = ...  # 0x52
        NauruLanguage: QLocale.Language = ...  # 0x53
        Nepali: QLocale.Language = ...  # 0x54
        Norwegian: QLocale.Language = ...  # 0x55
        NorwegianBokmal: QLocale.Language = ...  # 0x55
        Occitan: QLocale.Language = ...  # 0x56
        Oriya: QLocale.Language = ...  # 0x57
        Pashto: QLocale.Language = ...  # 0x58
        Persian: QLocale.Language = ...  # 0x59
        Polish: QLocale.Language = ...  # 0x5a
        Portuguese: QLocale.Language = ...  # 0x5b
        Punjabi: QLocale.Language = ...  # 0x5c
        Quechua: QLocale.Language = ...  # 0x5d
        RhaetoRomance: QLocale.Language = ...  # 0x5e
        Romansh: QLocale.Language = ...  # 0x5e
        Moldavian: QLocale.Language = ...  # 0x5f
        Romanian: QLocale.Language = ...  # 0x5f
        Russian: QLocale.Language = ...  # 0x60
        Samoan: QLocale.Language = ...  # 0x61
        Sango: QLocale.Language = ...  # 0x62
        Sanskrit: QLocale.Language = ...  # 0x63
        Serbian: QLocale.Language = ...  # 0x64
        SerboCroatian: QLocale.Language = ...  # 0x64
        Ossetic: QLocale.Language = ...  # 0x65
        SouthernSotho: QLocale.Language = ...  # 0x66
        Tswana: QLocale.Language = ...  # 0x67
        Shona: QLocale.Language = ...  # 0x68
        Sindhi: QLocale.Language = ...  # 0x69
        Sinhala: QLocale.Language = ...  # 0x6a
        Swati: QLocale.Language = ...  # 0x6b
        Slovak: QLocale.Language = ...  # 0x6c
        Slovenian: QLocale.Language = ...  # 0x6d
        Somali: QLocale.Language = ...  # 0x6e
        Spanish: QLocale.Language = ...  # 0x6f
        Sundanese: QLocale.Language = ...  # 0x70
        Swahili: QLocale.Language = ...  # 0x71
        Swedish: QLocale.Language = ...  # 0x72
        Sardinian: QLocale.Language = ...  # 0x73
        Tajik: QLocale.Language = ...  # 0x74
        Tamil: QLocale.Language = ...  # 0x75
        Tatar: QLocale.Language = ...  # 0x76
        Telugu: QLocale.Language = ...  # 0x77
        Thai: QLocale.Language = ...  # 0x78
        Tibetan: QLocale.Language = ...  # 0x79
        Tigrinya: QLocale.Language = ...  # 0x7a
        Tongan: QLocale.Language = ...  # 0x7b
        Tsonga: QLocale.Language = ...  # 0x7c
        Turkish: QLocale.Language = ...  # 0x7d
        Turkmen: QLocale.Language = ...  # 0x7e
        Tahitian: QLocale.Language = ...  # 0x7f
        Uighur: QLocale.Language = ...  # 0x80
        Uigur: QLocale.Language = ...  # 0x80
        Ukrainian: QLocale.Language = ...  # 0x81
        Urdu: QLocale.Language = ...  # 0x82
        Uzbek: QLocale.Language = ...  # 0x83
        Vietnamese: QLocale.Language = ...  # 0x84
        Volapuk: QLocale.Language = ...  # 0x85
        Welsh: QLocale.Language = ...  # 0x86
        Wolof: QLocale.Language = ...  # 0x87
        Xhosa: QLocale.Language = ...  # 0x88
        Yiddish: QLocale.Language = ...  # 0x89
        Yoruba: QLocale.Language = ...  # 0x8a
        Zhuang: QLocale.Language = ...  # 0x8b
        Zulu: QLocale.Language = ...  # 0x8c
        NorwegianNynorsk: QLocale.Language = ...  # 0x8d
        Bosnian: QLocale.Language = ...  # 0x8e
        Divehi: QLocale.Language = ...  # 0x8f
        Manx: QLocale.Language = ...  # 0x90
        Cornish: QLocale.Language = ...  # 0x91
        Akan: QLocale.Language = ...  # 0x92
        Twi: QLocale.Language = ...  # 0x92
        Konkani: QLocale.Language = ...  # 0x93
        Ga: QLocale.Language = ...  # 0x94
        Igbo: QLocale.Language = ...  # 0x95
        Kamba: QLocale.Language = ...  # 0x96
        Syriac: QLocale.Language = ...  # 0x97
        Blin: QLocale.Language = ...  # 0x98
        Geez: QLocale.Language = ...  # 0x99
        Koro: QLocale.Language = ...  # 0x9a
        Sidamo: QLocale.Language = ...  # 0x9b
        Atsam: QLocale.Language = ...  # 0x9c
        Tigre: QLocale.Language = ...  # 0x9d
        Jju: QLocale.Language = ...  # 0x9e
        Friulian: QLocale.Language = ...  # 0x9f
        Venda: QLocale.Language = ...  # 0xa0
        Ewe: QLocale.Language = ...  # 0xa1
        Walamo: QLocale.Language = ...  # 0xa2
        Hawaiian: QLocale.Language = ...  # 0xa3
        Tyap: QLocale.Language = ...  # 0xa4
        Chewa: QLocale.Language = ...  # 0xa5
        Nyanja: QLocale.Language = ...  # 0xa5
        Filipino: QLocale.Language = ...  # 0xa6
        Tagalog: QLocale.Language = ...  # 0xa6
        SwissGerman: QLocale.Language = ...  # 0xa7
        SichuanYi: QLocale.Language = ...  # 0xa8
        Kpelle: QLocale.Language = ...  # 0xa9
        LowGerman: QLocale.Language = ...  # 0xaa
        SouthNdebele: QLocale.Language = ...  # 0xab
        NorthernSotho: QLocale.Language = ...  # 0xac
        NorthernSami: QLocale.Language = ...  # 0xad
        Taroko: QLocale.Language = ...  # 0xae
        Gusii: QLocale.Language = ...  # 0xaf
        Taita: QLocale.Language = ...  # 0xb0
        Fulah: QLocale.Language = ...  # 0xb1
        Kikuyu: QLocale.Language = ...  # 0xb2
        Samburu: QLocale.Language = ...  # 0xb3
        Sena: QLocale.Language = ...  # 0xb4
        NorthNdebele: QLocale.Language = ...  # 0xb5
        Rombo: QLocale.Language = ...  # 0xb6
        Tachelhit: QLocale.Language = ...  # 0xb7
        Kabyle: QLocale.Language = ...  # 0xb8
        Nyankole: QLocale.Language = ...  # 0xb9
        Bena: QLocale.Language = ...  # 0xba
        Vunjo: QLocale.Language = ...  # 0xbb
        Bambara: QLocale.Language = ...  # 0xbc
        Embu: QLocale.Language = ...  # 0xbd
        Cherokee: QLocale.Language = ...  # 0xbe
        Morisyen: QLocale.Language = ...  # 0xbf
        Makonde: QLocale.Language = ...  # 0xc0
        Langi: QLocale.Language = ...  # 0xc1
        Ganda: QLocale.Language = ...  # 0xc2
        Bemba: QLocale.Language = ...  # 0xc3
        Kabuverdianu: QLocale.Language = ...  # 0xc4
        Meru: QLocale.Language = ...  # 0xc5
        Kalenjin: QLocale.Language = ...  # 0xc6
        Nama: QLocale.Language = ...  # 0xc7
        Machame: QLocale.Language = ...  # 0xc8
        Colognian: QLocale.Language = ...  # 0xc9
        Masai: QLocale.Language = ...  # 0xca
        Soga: QLocale.Language = ...  # 0xcb
        Luyia: QLocale.Language = ...  # 0xcc
        Asu: QLocale.Language = ...  # 0xcd
        Teso: QLocale.Language = ...  # 0xce
        Saho: QLocale.Language = ...  # 0xcf
        KoyraChiini: QLocale.Language = ...  # 0xd0
        Rwa: QLocale.Language = ...  # 0xd1
        Luo: QLocale.Language = ...  # 0xd2
        Chiga: QLocale.Language = ...  # 0xd3
        CentralMoroccoTamazight: QLocale.Language = ...  # 0xd4
        KoyraboroSenni: QLocale.Language = ...  # 0xd5
        Shambala: QLocale.Language = ...  # 0xd6
        Bodo: QLocale.Language = ...  # 0xd7
        Avaric: QLocale.Language = ...  # 0xd8
        Chamorro: QLocale.Language = ...  # 0xd9
        Chechen: QLocale.Language = ...  # 0xda
        Church: QLocale.Language = ...  # 0xdb
        Chuvash: QLocale.Language = ...  # 0xdc
        Cree: QLocale.Language = ...  # 0xdd
        Haitian: QLocale.Language = ...  # 0xde
        Herero: QLocale.Language = ...  # 0xdf
        HiriMotu: QLocale.Language = ...  # 0xe0
        Kanuri: QLocale.Language = ...  # 0xe1
        Komi: QLocale.Language = ...  # 0xe2
        Kongo: QLocale.Language = ...  # 0xe3
        Kwanyama: QLocale.Language = ...  # 0xe4
        Limburgish: QLocale.Language = ...  # 0xe5
        LubaKatanga: QLocale.Language = ...  # 0xe6
        Luxembourgish: QLocale.Language = ...  # 0xe7
        Navaho: QLocale.Language = ...  # 0xe8
        Ndonga: QLocale.Language = ...  # 0xe9
        Ojibwa: QLocale.Language = ...  # 0xea
        Pali: QLocale.Language = ...  # 0xeb
        Walloon: QLocale.Language = ...  # 0xec
        Aghem: QLocale.Language = ...  # 0xed
        Basaa: QLocale.Language = ...  # 0xee
        Zarma: QLocale.Language = ...  # 0xef
        Duala: QLocale.Language = ...  # 0xf0
        JolaFonyi: QLocale.Language = ...  # 0xf1
        Ewondo: QLocale.Language = ...  # 0xf2
        Bafia: QLocale.Language = ...  # 0xf3
        MakhuwaMeetto: QLocale.Language = ...  # 0xf4
        Mundang: QLocale.Language = ...  # 0xf5
        Kwasio: QLocale.Language = ...  # 0xf6
        Nuer: QLocale.Language = ...  # 0xf7
        Sakha: QLocale.Language = ...  # 0xf8
        Sangu: QLocale.Language = ...  # 0xf9
        CongoSwahili: QLocale.Language = ...  # 0xfa
        Tasawaq: QLocale.Language = ...  # 0xfb
        Vai: QLocale.Language = ...  # 0xfc
        Walser: QLocale.Language = ...  # 0xfd
        Yangben: QLocale.Language = ...  # 0xfe
        Avestan: QLocale.Language = ...  # 0xff
        Asturian: QLocale.Language = ...  # 0x100
        Ngomba: QLocale.Language = ...  # 0x101
        Kako: QLocale.Language = ...  # 0x102
        Meta: QLocale.Language = ...  # 0x103
        Ngiemboon: QLocale.Language = ...  # 0x104
        Aragonese: QLocale.Language = ...  # 0x105
        Akkadian: QLocale.Language = ...  # 0x106
        AncientEgyptian: QLocale.Language = ...  # 0x107
        AncientGreek: QLocale.Language = ...  # 0x108
        Aramaic: QLocale.Language = ...  # 0x109
        Balinese: QLocale.Language = ...  # 0x10a
        Bamun: QLocale.Language = ...  # 0x10b
        BatakToba: QLocale.Language = ...  # 0x10c
        Buginese: QLocale.Language = ...  # 0x10d
        Buhid: QLocale.Language = ...  # 0x10e
        Carian: QLocale.Language = ...  # 0x10f
        Chakma: QLocale.Language = ...  # 0x110
        ClassicalMandaic: QLocale.Language = ...  # 0x111
        Coptic: QLocale.Language = ...  # 0x112
        Dogri: QLocale.Language = ...  # 0x113
        EasternCham: QLocale.Language = ...  # 0x114
        EasternKayah: QLocale.Language = ...  # 0x115
        Etruscan: QLocale.Language = ...  # 0x116
        Gothic: QLocale.Language = ...  # 0x117
        Hanunoo: QLocale.Language = ...  # 0x118
        Ingush: QLocale.Language = ...  # 0x119
        LargeFloweryMiao: QLocale.Language = ...  # 0x11a
        Lepcha: QLocale.Language = ...  # 0x11b
        Limbu: QLocale.Language = ...  # 0x11c
        Lisu: QLocale.Language = ...  # 0x11d
        Lu: QLocale.Language = ...  # 0x11e
        Lycian: QLocale.Language = ...  # 0x11f
        Lydian: QLocale.Language = ...  # 0x120
        Mandingo: QLocale.Language = ...  # 0x121
        Manipuri: QLocale.Language = ...  # 0x122
        Meroitic: QLocale.Language = ...  # 0x123
        NorthernThai: QLocale.Language = ...  # 0x124
        OldIrish: QLocale.Language = ...  # 0x125
        OldNorse: QLocale.Language = ...  # 0x126
        OldPersian: QLocale.Language = ...  # 0x127
        OldTurkish: QLocale.Language = ...  # 0x128
        Pahlavi: QLocale.Language = ...  # 0x129
        Parthian: QLocale.Language = ...  # 0x12a
        Phoenician: QLocale.Language = ...  # 0x12b
        PrakritLanguage: QLocale.Language = ...  # 0x12c
        Rejang: QLocale.Language = ...  # 0x12d
        Sabaean: QLocale.Language = ...  # 0x12e
        Samaritan: QLocale.Language = ...  # 0x12f
        Santali: QLocale.Language = ...  # 0x130
        Saurashtra: QLocale.Language = ...  # 0x131
        Sora: QLocale.Language = ...  # 0x132
        Sylheti: QLocale.Language = ...  # 0x133
        Tagbanwa: QLocale.Language = ...  # 0x134
        TaiDam: QLocale.Language = ...  # 0x135
        TaiNua: QLocale.Language = ...  # 0x136
        Ugaritic: QLocale.Language = ...  # 0x137
        Akoose: QLocale.Language = ...  # 0x138
        Lakota: QLocale.Language = ...  # 0x139
        StandardMoroccanTamazight: QLocale.Language = ...  # 0x13a
        Mapuche: QLocale.Language = ...  # 0x13b
        CentralKurdish: QLocale.Language = ...  # 0x13c
        LowerSorbian: QLocale.Language = ...  # 0x13d
        UpperSorbian: QLocale.Language = ...  # 0x13e
        Kenyang: QLocale.Language = ...  # 0x13f
        Mohawk: QLocale.Language = ...  # 0x140
        Nko: QLocale.Language = ...  # 0x141
        Prussian: QLocale.Language = ...  # 0x142
        Kiche: QLocale.Language = ...  # 0x143
        SouthernSami: QLocale.Language = ...  # 0x144
        LuleSami: QLocale.Language = ...  # 0x145
        InariSami: QLocale.Language = ...  # 0x146
        SkoltSami: QLocale.Language = ...  # 0x147
        Warlpiri: QLocale.Language = ...  # 0x148
        ManichaeanMiddlePersian: QLocale.Language = ...  # 0x149
        Mende: QLocale.Language = ...  # 0x14a
        AncientNorthArabian: QLocale.Language = ...  # 0x14b
        LinearA: QLocale.Language = ...  # 0x14c
        HmongNjua: QLocale.Language = ...  # 0x14d
        Ho: QLocale.Language = ...  # 0x14e
        Lezghian: QLocale.Language = ...  # 0x14f
        Bassa: QLocale.Language = ...  # 0x150
        Mono: QLocale.Language = ...  # 0x151
        TedimChin: QLocale.Language = ...  # 0x152
        Maithili: QLocale.Language = ...  # 0x153
        Ahom: QLocale.Language = ...  # 0x154
        AmericanSignLanguage: QLocale.Language = ...  # 0x155
        ArdhamagadhiPrakrit: QLocale.Language = ...  # 0x156
        Bhojpuri: QLocale.Language = ...  # 0x157
        HieroglyphicLuwian: QLocale.Language = ...  # 0x158
        LiteraryChinese: QLocale.Language = ...  # 0x159
        Mazanderani: QLocale.Language = ...  # 0x15a
        Mru: QLocale.Language = ...  # 0x15b
        Newari: QLocale.Language = ...  # 0x15c
        NorthernLuri: QLocale.Language = ...  # 0x15d
        Palauan: QLocale.Language = ...  # 0x15e
        Papiamento: QLocale.Language = ...  # 0x15f
        Saraiki: QLocale.Language = ...  # 0x160
        TokelauLanguage: QLocale.Language = ...  # 0x161
        TokPisin: QLocale.Language = ...  # 0x162
        TuvaluLanguage: QLocale.Language = ...  # 0x163
        UncodedLanguages: QLocale.Language = ...  # 0x164
        Cantonese: QLocale.Language = ...  # 0x165
        Osage: QLocale.Language = ...  # 0x166
        Tangut: QLocale.Language = ...  # 0x167
        Ido: QLocale.Language = ...  # 0x168
        Lojban: QLocale.Language = ...  # 0x169
        Sicilian: QLocale.Language = ...  # 0x16a
        SouthernKurdish: QLocale.Language = ...  # 0x16b
        WesternBalochi: QLocale.Language = ...  # 0x16c
        Cebuano: QLocale.Language = ...  # 0x16d
        Erzya: QLocale.Language = ...  # 0x16e
        Chickasaw: QLocale.Language = ...  # 0x16f
        Muscogee: QLocale.Language = ...  # 0x170
        LastLanguage: QLocale.Language = ...  # 0x171
        Silesian: QLocale.Language = ...  # 0x171

    class MeasurementSystem(object):
        MetricSystem: QLocale.MeasurementSystem = ...  # 0x0
        ImperialSystem: QLocale.MeasurementSystem = ...  # 0x1
        ImperialUSSystem: QLocale.MeasurementSystem = ...  # 0x1
        ImperialUKSystem: QLocale.MeasurementSystem = ...  # 0x2

    class NumberOption(object):
        DefaultNumberOptions: QLocale.NumberOption = ...  # 0x0
        OmitGroupSeparator: QLocale.NumberOption = ...  # 0x1
        RejectGroupSeparator: QLocale.NumberOption = ...  # 0x2
        OmitLeadingZeroInExponent: QLocale.NumberOption = ...  # 0x4
        RejectLeadingZeroInExponent: QLocale.NumberOption = ...  # 0x8
        IncludeTrailingZeroesAfterDot: QLocale.NumberOption = ...  # 0x10
        RejectTrailingZeroesAfterDot: QLocale.NumberOption = ...  # 0x20

    class NumberOptions(object): ...

    class QuotationStyle(object):
        StandardQuotation: QLocale.QuotationStyle = ...  # 0x0
        AlternateQuotation: QLocale.QuotationStyle = ...  # 0x1

    class Script(object):
        AnyScript: QLocale.Script = ...  # 0x0
        ArabicScript: QLocale.Script = ...  # 0x1
        CyrillicScript: QLocale.Script = ...  # 0x2
        DeseretScript: QLocale.Script = ...  # 0x3
        GurmukhiScript: QLocale.Script = ...  # 0x4
        SimplifiedChineseScript: QLocale.Script = ...  # 0x5
        SimplifiedHanScript: QLocale.Script = ...  # 0x5
        TraditionalChineseScript: QLocale.Script = ...  # 0x6
        TraditionalHanScript: QLocale.Script = ...  # 0x6
        LatinScript: QLocale.Script = ...  # 0x7
        MongolianScript: QLocale.Script = ...  # 0x8
        TifinaghScript: QLocale.Script = ...  # 0x9
        ArmenianScript: QLocale.Script = ...  # 0xa
        BengaliScript: QLocale.Script = ...  # 0xb
        CherokeeScript: QLocale.Script = ...  # 0xc
        DevanagariScript: QLocale.Script = ...  # 0xd
        EthiopicScript: QLocale.Script = ...  # 0xe
        GeorgianScript: QLocale.Script = ...  # 0xf
        GreekScript: QLocale.Script = ...  # 0x10
        GujaratiScript: QLocale.Script = ...  # 0x11
        HebrewScript: QLocale.Script = ...  # 0x12
        JapaneseScript: QLocale.Script = ...  # 0x13
        KhmerScript: QLocale.Script = ...  # 0x14
        KannadaScript: QLocale.Script = ...  # 0x15
        KoreanScript: QLocale.Script = ...  # 0x16
        LaoScript: QLocale.Script = ...  # 0x17
        MalayalamScript: QLocale.Script = ...  # 0x18
        MyanmarScript: QLocale.Script = ...  # 0x19
        OriyaScript: QLocale.Script = ...  # 0x1a
        TamilScript: QLocale.Script = ...  # 0x1b
        TeluguScript: QLocale.Script = ...  # 0x1c
        ThaanaScript: QLocale.Script = ...  # 0x1d
        ThaiScript: QLocale.Script = ...  # 0x1e
        TibetanScript: QLocale.Script = ...  # 0x1f
        SinhalaScript: QLocale.Script = ...  # 0x20
        SyriacScript: QLocale.Script = ...  # 0x21
        YiScript: QLocale.Script = ...  # 0x22
        VaiScript: QLocale.Script = ...  # 0x23
        AvestanScript: QLocale.Script = ...  # 0x24
        BalineseScript: QLocale.Script = ...  # 0x25
        BamumScript: QLocale.Script = ...  # 0x26
        BatakScript: QLocale.Script = ...  # 0x27
        BopomofoScript: QLocale.Script = ...  # 0x28
        BrahmiScript: QLocale.Script = ...  # 0x29
        BugineseScript: QLocale.Script = ...  # 0x2a
        BuhidScript: QLocale.Script = ...  # 0x2b
        CanadianAboriginalScript: QLocale.Script = ...  # 0x2c
        CarianScript: QLocale.Script = ...  # 0x2d
        ChakmaScript: QLocale.Script = ...  # 0x2e
        ChamScript: QLocale.Script = ...  # 0x2f
        CopticScript: QLocale.Script = ...  # 0x30
        CypriotScript: QLocale.Script = ...  # 0x31
        EgyptianHieroglyphsScript: QLocale.Script = ...  # 0x32
        FraserScript: QLocale.Script = ...  # 0x33
        GlagoliticScript: QLocale.Script = ...  # 0x34
        GothicScript: QLocale.Script = ...  # 0x35
        HanScript: QLocale.Script = ...  # 0x36
        HangulScript: QLocale.Script = ...  # 0x37
        HanunooScript: QLocale.Script = ...  # 0x38
        ImperialAramaicScript: QLocale.Script = ...  # 0x39
        InscriptionalPahlaviScript: QLocale.Script = ...  # 0x3a
        InscriptionalParthianScript: QLocale.Script = ...  # 0x3b
        JavaneseScript: QLocale.Script = ...  # 0x3c
        KaithiScript: QLocale.Script = ...  # 0x3d
        KatakanaScript: QLocale.Script = ...  # 0x3e
        KayahLiScript: QLocale.Script = ...  # 0x3f
        KharoshthiScript: QLocale.Script = ...  # 0x40
        LannaScript: QLocale.Script = ...  # 0x41
        LepchaScript: QLocale.Script = ...  # 0x42
        LimbuScript: QLocale.Script = ...  # 0x43
        LinearBScript: QLocale.Script = ...  # 0x44
        LycianScript: QLocale.Script = ...  # 0x45
        LydianScript: QLocale.Script = ...  # 0x46
        MandaeanScript: QLocale.Script = ...  # 0x47
        MeiteiMayekScript: QLocale.Script = ...  # 0x48
        MeroiticScript: QLocale.Script = ...  # 0x49
        MeroiticCursiveScript: QLocale.Script = ...  # 0x4a
        NkoScript: QLocale.Script = ...  # 0x4b
        NewTaiLueScript: QLocale.Script = ...  # 0x4c
        OghamScript: QLocale.Script = ...  # 0x4d
        OlChikiScript: QLocale.Script = ...  # 0x4e
        OldItalicScript: QLocale.Script = ...  # 0x4f
        OldPersianScript: QLocale.Script = ...  # 0x50
        OldSouthArabianScript: QLocale.Script = ...  # 0x51
        OrkhonScript: QLocale.Script = ...  # 0x52
        OsmanyaScript: QLocale.Script = ...  # 0x53
        PhagsPaScript: QLocale.Script = ...  # 0x54
        PhoenicianScript: QLocale.Script = ...  # 0x55
        PollardPhoneticScript: QLocale.Script = ...  # 0x56
        RejangScript: QLocale.Script = ...  # 0x57
        RunicScript: QLocale.Script = ...  # 0x58
        SamaritanScript: QLocale.Script = ...  # 0x59
        SaurashtraScript: QLocale.Script = ...  # 0x5a
        SharadaScript: QLocale.Script = ...  # 0x5b
        ShavianScript: QLocale.Script = ...  # 0x5c
        SoraSompengScript: QLocale.Script = ...  # 0x5d
        CuneiformScript: QLocale.Script = ...  # 0x5e
        SundaneseScript: QLocale.Script = ...  # 0x5f
        SylotiNagriScript: QLocale.Script = ...  # 0x60
        TagalogScript: QLocale.Script = ...  # 0x61
        TagbanwaScript: QLocale.Script = ...  # 0x62
        TaiLeScript: QLocale.Script = ...  # 0x63
        TaiVietScript: QLocale.Script = ...  # 0x64
        TakriScript: QLocale.Script = ...  # 0x65
        UgariticScript: QLocale.Script = ...  # 0x66
        BrailleScript: QLocale.Script = ...  # 0x67
        HiraganaScript: QLocale.Script = ...  # 0x68
        CaucasianAlbanianScript: QLocale.Script = ...  # 0x69
        BassaVahScript: QLocale.Script = ...  # 0x6a
        DuployanScript: QLocale.Script = ...  # 0x6b
        ElbasanScript: QLocale.Script = ...  # 0x6c
        GranthaScript: QLocale.Script = ...  # 0x6d
        PahawhHmongScript: QLocale.Script = ...  # 0x6e
        KhojkiScript: QLocale.Script = ...  # 0x6f
        LinearAScript: QLocale.Script = ...  # 0x70
        MahajaniScript: QLocale.Script = ...  # 0x71
        ManichaeanScript: QLocale.Script = ...  # 0x72
        MendeKikakuiScript: QLocale.Script = ...  # 0x73
        ModiScript: QLocale.Script = ...  # 0x74
        MroScript: QLocale.Script = ...  # 0x75
        OldNorthArabianScript: QLocale.Script = ...  # 0x76
        NabataeanScript: QLocale.Script = ...  # 0x77
        PalmyreneScript: QLocale.Script = ...  # 0x78
        PauCinHauScript: QLocale.Script = ...  # 0x79
        OldPermicScript: QLocale.Script = ...  # 0x7a
        PsalterPahlaviScript: QLocale.Script = ...  # 0x7b
        SiddhamScript: QLocale.Script = ...  # 0x7c
        KhudawadiScript: QLocale.Script = ...  # 0x7d
        TirhutaScript: QLocale.Script = ...  # 0x7e
        VarangKshitiScript: QLocale.Script = ...  # 0x7f
        AhomScript: QLocale.Script = ...  # 0x80
        AnatolianHieroglyphsScript: QLocale.Script = ...  # 0x81
        HatranScript: QLocale.Script = ...  # 0x82
        MultaniScript: QLocale.Script = ...  # 0x83
        OldHungarianScript: QLocale.Script = ...  # 0x84
        SignWritingScript: QLocale.Script = ...  # 0x85
        AdlamScript: QLocale.Script = ...  # 0x86
        BhaiksukiScript: QLocale.Script = ...  # 0x87
        MarchenScript: QLocale.Script = ...  # 0x88
        NewaScript: QLocale.Script = ...  # 0x89
        OsageScript: QLocale.Script = ...  # 0x8a
        TangutScript: QLocale.Script = ...  # 0x8b
        HanWithBopomofoScript: QLocale.Script = ...  # 0x8c
        JamoScript: QLocale.Script = ...  # 0x8d
        LastScript: QLocale.Script = ...  # 0x8d
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self,
        language: PySide2.QtCore.QLocale.Language,
        country: PySide2.QtCore.QLocale.Country = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        language: PySide2.QtCore.QLocale.Language,
        script: PySide2.QtCore.QLocale.Script,
        country: PySide2.QtCore.QLocale.Country,
    ): ...
    @typing.overload
    def __init__(self, name: str): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QLocale): ...
    def __copy__(self): ...
    def amText(self) -> str: ...
    def bcp47Name(self) -> str: ...
    @staticmethod
    def c() -> PySide2.QtCore.QLocale: ...
    def collation(self) -> PySide2.QtCore.QLocale: ...
    @staticmethod
    def countriesForLanguage(lang: PySide2.QtCore.QLocale.Language) -> typing.List: ...
    def country(self) -> PySide2.QtCore.QLocale.Country: ...
    @staticmethod
    def countryToString(country: PySide2.QtCore.QLocale.Country) -> str: ...
    def createSeparatedList(self, strl: typing.Sequence) -> str: ...
    def currencySymbol(
        self, arg__1: PySide2.QtCore.QLocale.CurrencySymbolFormat = ...
    ) -> str: ...
    def dateFormat(self, format: PySide2.QtCore.QLocale.FormatType = ...) -> str: ...
    def dateTimeFormat(
        self, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> str: ...
    def dayName(
        self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> str: ...
    def decimalPoint(self) -> str: ...
    def exponential(self) -> str: ...
    def firstDayOfWeek(self) -> PySide2.QtCore.Qt.DayOfWeek: ...
    def formattedDataSize(
        self,
        bytes: int,
        precision: int = ...,
        format: PySide2.QtCore.QLocale.DataSizeFormats = ...,
    ) -> str: ...
    def groupSeparator(self) -> str: ...
    def language(self) -> PySide2.QtCore.QLocale.Language: ...
    @staticmethod
    def languageToString(language: PySide2.QtCore.QLocale.Language) -> str: ...
    @staticmethod
    def matchingLocales(
        language: PySide2.QtCore.QLocale.Language,
        script: PySide2.QtCore.QLocale.Script,
        country: PySide2.QtCore.QLocale.Country,
    ) -> typing.List: ...
    def measurementSystem(self) -> PySide2.QtCore.QLocale.MeasurementSystem: ...
    def monthName(
        self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> str: ...
    def name(self) -> str: ...
    def nativeCountryName(self) -> str: ...
    def nativeLanguageName(self) -> str: ...
    def negativeSign(self) -> str: ...
    def numberOptions(self) -> PySide2.QtCore.QLocale.NumberOptions: ...
    def percent(self) -> str: ...
    def pmText(self) -> str: ...
    def positiveSign(self) -> str: ...
    @typing.overload
    def quoteString(
        self, str: str, style: PySide2.QtCore.QLocale.QuotationStyle = ...
    ) -> str: ...
    @typing.overload
    def quoteString(
        self, str: str, style: PySide2.QtCore.QLocale.QuotationStyle = ...
    ) -> str: ...
    def script(self) -> PySide2.QtCore.QLocale.Script: ...
    @staticmethod
    def scriptToString(script: PySide2.QtCore.QLocale.Script) -> str: ...
    @staticmethod
    def setDefault(locale: PySide2.QtCore.QLocale): ...
    def setNumberOptions(self, options: PySide2.QtCore.QLocale.NumberOptions): ...
    def standaloneDayName(
        self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> str: ...
    def standaloneMonthName(
        self, arg__1: int, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> str: ...
    def swap(self, other: PySide2.QtCore.QLocale): ...
    @staticmethod
    def system() -> PySide2.QtCore.QLocale: ...
    def textDirection(self) -> PySide2.QtCore.Qt.LayoutDirection: ...
    def timeFormat(self, format: PySide2.QtCore.QLocale.FormatType = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: float, symbol: str, precision: int) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: float, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: int, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: int, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: int, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: int, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: int, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, arg__1: int, symbol: str = ...) -> str: ...
    @typing.overload
    def toCurrencyString(self, i: float, symbol: str, precision: int) -> str: ...
    @typing.overload
    def toCurrencyString(self, i: float, symbol: str = ...) -> str: ...
    @typing.overload
    def toDate(
        self,
        string: str,
        format: PySide2.QtCore.QLocale.FormatType,
        cal: PySide2.QtCore.QCalendar,
    ) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def toDate(
        self, string: str, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def toDate(self, string: str, format: str) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def toDate(
        self, string: str, format: str, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QDate: ...
    @typing.overload
    def toDateTime(
        self,
        string: str,
        format: PySide2.QtCore.QLocale.FormatType,
        cal: PySide2.QtCore.QCalendar,
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    def toDateTime(
        self, string: str, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    def toDateTime(self, string: str, format: str) -> PySide2.QtCore.QDateTime: ...
    @typing.overload
    def toDateTime(
        self, string: str, format: str, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QDateTime: ...
    def toDouble(self, s: str) -> typing.Tuple: ...
    def toFloat(self, s: str) -> typing.Tuple: ...
    def toInt(self, s: str) -> typing.Tuple: ...
    @typing.overload
    def toLong(self, s: str) -> typing.Tuple: ...
    @typing.overload
    def toLong(self, s: str) -> typing.Tuple: ...
    def toLongLong(self, s: str) -> typing.Tuple: ...
    def toLower(self, str: str) -> str: ...
    def toShort(self, s: str) -> typing.Tuple: ...
    @typing.overload
    def toString(
        self,
        date: PySide2.QtCore.QDate,
        format: PySide2.QtCore.QLocale.FormatType,
        cal: PySide2.QtCore.QCalendar,
    ) -> str: ...
    @typing.overload
    def toString(
        self,
        date: PySide2.QtCore.QDate,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...
    @typing.overload
    def toString(self, date: PySide2.QtCore.QDate, formatStr: str) -> str: ...
    @typing.overload
    def toString(
        self,
        dateTime: PySide2.QtCore.QDateTime,
        format: PySide2.QtCore.QLocale.FormatType,
        cal: PySide2.QtCore.QCalendar,
    ) -> str: ...
    @typing.overload
    def toString(
        self,
        dateTime: PySide2.QtCore.QDateTime,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...
    @typing.overload
    def toString(self, dateTime: PySide2.QtCore.QDateTime, format: str) -> str: ...
    @typing.overload
    def toString(self, i: float, f: int = ..., prec: int = ...) -> str: ...
    @typing.overload
    def toString(self, i: float, f: int = ..., prec: int = ...) -> str: ...
    @typing.overload
    def toString(self, i: int) -> str: ...
    @typing.overload
    def toString(self, i: int) -> str: ...
    @typing.overload
    def toString(self, i: int) -> str: ...
    @typing.overload
    def toString(self, i: int) -> str: ...
    @typing.overload
    def toString(self, i: int) -> str: ...
    @typing.overload
    def toString(
        self,
        time: PySide2.QtCore.QTime,
        format: PySide2.QtCore.QLocale.FormatType = ...,
    ) -> str: ...
    @typing.overload
    def toString(self, time: PySide2.QtCore.QTime, formatStr: str) -> str: ...
    @typing.overload
    def toTime(
        self,
        string: str,
        format: PySide2.QtCore.QLocale.FormatType,
        cal: PySide2.QtCore.QCalendar,
    ) -> PySide2.QtCore.QTime: ...
    @typing.overload
    def toTime(
        self, string: str, format: PySide2.QtCore.QLocale.FormatType = ...
    ) -> PySide2.QtCore.QTime: ...
    @typing.overload
    def toTime(self, string: str, format: str) -> PySide2.QtCore.QTime: ...
    @typing.overload
    def toTime(
        self, string: str, format: str, cal: PySide2.QtCore.QCalendar
    ) -> PySide2.QtCore.QTime: ...
    def toUInt(self, s: str) -> typing.Tuple: ...
    @typing.overload
    def toULong(self, s: str) -> typing.Tuple: ...
    @typing.overload
    def toULong(self, s: str) -> typing.Tuple: ...
    def toULongLong(self, s: str) -> typing.Tuple: ...
    def toUShort(self, s: str) -> typing.Tuple: ...
    def toUpper(self, str: str) -> str: ...
    def uiLanguages(self) -> typing.List: ...
    def weekdays(self) -> typing.List: ...
    def zeroDigit(self) -> str: ...

class QLockFile(Shiboken.Object):
    NoError: QLockFile = ...  # 0x0
    LockFailedError: QLockFile = ...  # 0x1
    PermissionError: QLockFile = ...  # 0x2
    UnknownError: QLockFile = ...  # 0x3

    class LockError(object):
        NoError: QLockFile.LockError = ...  # 0x0
        LockFailedError: QLockFile.LockError = ...  # 0x1
        PermissionError: QLockFile.LockError = ...  # 0x2
        UnknownError: QLockFile.LockError = ...  # 0x3
    def __init__(self, fileName: str): ...
    def error(self) -> PySide2.QtCore.QLockFile.LockError: ...
    def getLockInfo(self) -> typing.Tuple: ...
    def isLocked(self) -> bool: ...
    def lock(self) -> bool: ...
    def removeStaleLockFile(self) -> bool: ...
    def setStaleLockTime(self, arg__1: int): ...
    def staleLockTime(self) -> int: ...
    def tryLock(self, timeout: int = ...) -> bool: ...
    def unlock(self): ...

class QMargins(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QMargins: PySide2.QtCore.QMargins): ...
    @typing.overload
    def __init__(self, left: int, top: int, right: int, bottom: int): ...
    @typing.overload
    def __add__(self, lhs: int) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __add__(self, m2: PySide2.QtCore.QMargins) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __add__(self, rhs: int) -> PySide2.QtCore.QMargins: ...
    def __copy__(self): ...
    @typing.overload
    def __iadd__(self, arg__1: int) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __iadd__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __imul__(self, arg__1: int) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __imul__(self, arg__1: float) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __isub__(self, arg__1: int) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __isub__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __mul__(self, factor: int) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __mul__(self, factor: float) -> PySide2.QtCore.QMargins: ...
    def __neg__(self) -> PySide2.QtCore.QMargins: ...
    def __pos__(self) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __sub__(self, m2: PySide2.QtCore.QMargins) -> PySide2.QtCore.QMargins: ...
    @typing.overload
    def __sub__(self, rhs: int) -> PySide2.QtCore.QMargins: ...
    def bottom(self) -> int: ...
    def isNull(self) -> bool: ...
    def left(self) -> int: ...
    def right(self) -> int: ...
    def setBottom(self, bottom: int): ...
    def setLeft(self, left: int): ...
    def setRight(self, right: int): ...
    def setTop(self, top: int): ...
    def top(self) -> int: ...

class QMarginsF(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QMarginsF: PySide2.QtCore.QMarginsF): ...
    @typing.overload
    def __init__(self, left: float, top: float, right: float, bottom: float): ...
    @typing.overload
    def __init__(self, margins: PySide2.QtCore.QMargins): ...
    @typing.overload
    def __add__(self, lhs: float) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __add__(self, rhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __add__(self, rhs: float) -> PySide2.QtCore.QMarginsF: ...
    def __copy__(self): ...
    @typing.overload
    def __iadd__(self, addend: float) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __iadd__(
        self, margins: PySide2.QtCore.QMarginsF
    ) -> PySide2.QtCore.QMarginsF: ...
    def __imul__(self, factor: float) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __isub__(
        self, margins: PySide2.QtCore.QMarginsF
    ) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __isub__(self, subtrahend: float) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __mul__(self, lhs: float) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __mul__(self, rhs: float) -> PySide2.QtCore.QMarginsF: ...
    def __neg__(self) -> PySide2.QtCore.QMarginsF: ...
    def __pos__(self) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __sub__(self, rhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QMarginsF: ...
    @typing.overload
    def __sub__(self, rhs: float) -> PySide2.QtCore.QMarginsF: ...
    def bottom(self) -> float: ...
    def isNull(self) -> bool: ...
    def left(self) -> float: ...
    def right(self) -> float: ...
    def setBottom(self, bottom: float): ...
    def setLeft(self, left: float): ...
    def setRight(self, right: float): ...
    def setTop(self, top: float): ...
    def toMargins(self) -> PySide2.QtCore.QMargins: ...
    def top(self) -> float: ...

class QMessageAuthenticationCode(Shiboken.Object):
    def __init__(
        self,
        method: PySide2.QtCore.QCryptographicHash.Algorithm,
        key: PySide2.QtCore.QByteArray = ...,
    ): ...
    @typing.overload
    def addData(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def addData(self, data: bytes, length: int): ...
    @typing.overload
    def addData(self, device: PySide2.QtCore.QIODevice) -> bool: ...
    @staticmethod
    def hash(
        message: PySide2.QtCore.QByteArray,
        key: PySide2.QtCore.QByteArray,
        method: PySide2.QtCore.QCryptographicHash.Algorithm,
    ) -> PySide2.QtCore.QByteArray: ...
    def reset(self): ...
    def result(self) -> PySide2.QtCore.QByteArray: ...
    def setKey(self, key: PySide2.QtCore.QByteArray): ...

class QMessageLogContext(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self, fileName: bytes, lineNumber: int, functionName: bytes, categoryName: bytes
    ): ...

class QMetaClassInfo(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QMetaClassInfo: PySide2.QtCore.QMetaClassInfo): ...
    def __copy__(self): ...
    def name(self) -> bytes: ...
    def value(self) -> bytes: ...

class QMetaEnum(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QMetaEnum: PySide2.QtCore.QMetaEnum): ...
    def __copy__(self): ...
    def enumName(self) -> bytes: ...
    def isFlag(self) -> bool: ...
    def isScoped(self) -> bool: ...
    def isValid(self) -> bool: ...
    def key(self, index: int) -> bytes: ...
    def keyCount(self) -> int: ...
    def keyToValue(self, key: bytes) -> typing.Tuple: ...
    def keysToValue(self, keys: bytes) -> typing.Tuple: ...
    def name(self) -> bytes: ...
    def scope(self) -> bytes: ...
    def value(self, index: int) -> int: ...
    def valueToKey(self, value: int) -> bytes: ...
    def valueToKeys(self, value: int) -> PySide2.QtCore.QByteArray: ...

class QMetaMethod(Shiboken.Object):
    Method: QMetaMethod = ...  # 0x0
    Private: QMetaMethod = ...  # 0x0
    Protected: QMetaMethod = ...  # 0x1
    Signal: QMetaMethod = ...  # 0x1
    Public: QMetaMethod = ...  # 0x2
    Slot: QMetaMethod = ...  # 0x2
    Constructor: QMetaMethod = ...  # 0x3

    class Access(object):
        Private: QMetaMethod.Access = ...  # 0x0
        Protected: QMetaMethod.Access = ...  # 0x1
        Public: QMetaMethod.Access = ...  # 0x2

    class MethodType(object):
        Method: QMetaMethod.MethodType = ...  # 0x0
        Signal: QMetaMethod.MethodType = ...  # 0x1
        Slot: QMetaMethod.MethodType = ...  # 0x2
        Constructor: QMetaMethod.MethodType = ...  # 0x3
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QMetaMethod: PySide2.QtCore.QMetaMethod): ...
    def __copy__(self): ...
    def access(self) -> PySide2.QtCore.QMetaMethod.Access: ...
    def enclosingMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
    @typing.overload
    def invoke(
        self,
        object: PySide2.QtCore.QObject,
        connectionType: PySide2.QtCore.Qt.ConnectionType,
        returnValue: PySide2.QtCore.QGenericReturnArgument,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    def invoke(
        self,
        object: PySide2.QtCore.QObject,
        connectionType: PySide2.QtCore.Qt.ConnectionType,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    def invoke(
        self,
        object: PySide2.QtCore.QObject,
        returnValue: PySide2.QtCore.QGenericReturnArgument,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    def invoke(
        self,
        object: PySide2.QtCore.QObject,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    def invokeOnGadget(
        self,
        gadget: int,
        returnValue: PySide2.QtCore.QGenericReturnArgument,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    def invokeOnGadget(
        self,
        gadget: int,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    def isValid(self) -> bool: ...
    def methodIndex(self) -> int: ...
    def methodSignature(self) -> PySide2.QtCore.QByteArray: ...
    def methodType(self) -> PySide2.QtCore.QMetaMethod.MethodType: ...
    def name(self) -> PySide2.QtCore.QByteArray: ...
    def parameterCount(self) -> int: ...
    def parameterNames(self) -> typing.List: ...
    def parameterType(self, index: int) -> int: ...
    def parameterTypes(self) -> typing.List: ...
    def returnType(self) -> int: ...
    def revision(self) -> int: ...
    def tag(self) -> bytes: ...
    def typeName(self) -> bytes: ...

class QMetaObject(Shiboken.Object):
    InvokeMetaMethod: QMetaObject = ...  # 0x0
    ReadProperty: QMetaObject = ...  # 0x1
    WriteProperty: QMetaObject = ...  # 0x2
    ResetProperty: QMetaObject = ...  # 0x3
    QueryPropertyDesignable: QMetaObject = ...  # 0x4
    QueryPropertyScriptable: QMetaObject = ...  # 0x5
    QueryPropertyStored: QMetaObject = ...  # 0x6
    QueryPropertyEditable: QMetaObject = ...  # 0x7
    QueryPropertyUser: QMetaObject = ...  # 0x8
    CreateInstance: QMetaObject = ...  # 0x9
    IndexOfMethod: QMetaObject = ...  # 0xa
    RegisterPropertyMetaType: QMetaObject = ...  # 0xb
    RegisterMethodArgumentMetaType: QMetaObject = ...  # 0xc

    class Call(object):
        InvokeMetaMethod: QMetaObject.Call = ...  # 0x0
        ReadProperty: QMetaObject.Call = ...  # 0x1
        WriteProperty: QMetaObject.Call = ...  # 0x2
        ResetProperty: QMetaObject.Call = ...  # 0x3
        QueryPropertyDesignable: QMetaObject.Call = ...  # 0x4
        QueryPropertyScriptable: QMetaObject.Call = ...  # 0x5
        QueryPropertyStored: QMetaObject.Call = ...  # 0x6
        QueryPropertyEditable: QMetaObject.Call = ...  # 0x7
        QueryPropertyUser: QMetaObject.Call = ...  # 0x8
        CreateInstance: QMetaObject.Call = ...  # 0x9
        IndexOfMethod: QMetaObject.Call = ...  # 0xa
        RegisterPropertyMetaType: QMetaObject.Call = ...  # 0xb
        RegisterMethodArgumentMetaType: QMetaObject.Call = ...  # 0xc

    class Connection(Shiboken.Object):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, other: PySide2.QtCore.QMetaObject.Connection): ...

    def __init__(self): ...
    def cast(self, obj: PySide2.QtCore.QObject) -> PySide2.QtCore.QObject: ...
    @typing.overload
    @staticmethod
    def checkConnectArgs(
        signal: PySide2.QtCore.QMetaMethod, method: PySide2.QtCore.QMetaMethod
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def checkConnectArgs(signal: bytes, method: bytes) -> bool: ...
    def classInfo(self, index: int) -> PySide2.QtCore.QMetaClassInfo: ...
    def classInfoCount(self) -> int: ...
    def classInfoOffset(self) -> int: ...
    def className(self) -> bytes: ...
    @staticmethod
    def connectSlotsByName(o: PySide2.QtCore.QObject): ...
    def constructor(self, index: int) -> PySide2.QtCore.QMetaMethod: ...
    def constructorCount(self) -> int: ...
    @staticmethod
    def disconnect(
        sender: PySide2.QtCore.QObject,
        signal_index: int,
        receiver: PySide2.QtCore.QObject,
        method_index: int,
    ) -> bool: ...
    @staticmethod
    def disconnectOne(
        sender: PySide2.QtCore.QObject,
        signal_index: int,
        receiver: PySide2.QtCore.QObject,
        method_index: int,
    ) -> bool: ...
    def enumerator(self, index: int) -> PySide2.QtCore.QMetaEnum: ...
    def enumeratorCount(self) -> int: ...
    def enumeratorOffset(self) -> int: ...
    def indexOfClassInfo(self, name: bytes) -> int: ...
    def indexOfConstructor(self, constructor: bytes) -> int: ...
    def indexOfEnumerator(self, name: bytes) -> int: ...
    def indexOfMethod(self, method: bytes) -> int: ...
    def indexOfProperty(self, name: bytes) -> int: ...
    def indexOfSignal(self, signal: bytes) -> int: ...
    def indexOfSlot(self, slot: bytes) -> int: ...
    def inherits(self, metaObject: PySide2.QtCore.QMetaObject) -> bool: ...
    @typing.overload
    @staticmethod
    def invokeMethod(
        obj: PySide2.QtCore.QObject,
        member: bytes,
        arg__3: PySide2.QtCore.Qt.ConnectionType,
        ret: PySide2.QtCore.QGenericReturnArgument,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def invokeMethod(
        obj: PySide2.QtCore.QObject,
        member: bytes,
        ret: PySide2.QtCore.QGenericReturnArgument,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def invokeMethod(
        obj: PySide2.QtCore.QObject,
        member: bytes,
        type: PySide2.QtCore.Qt.ConnectionType,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def invokeMethod(
        obj: PySide2.QtCore.QObject,
        member: bytes,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> bool: ...
    def method(self, index: int) -> PySide2.QtCore.QMetaMethod: ...
    def methodCount(self) -> int: ...
    def methodOffset(self) -> int: ...
    def newInstance(
        self,
        val0: PySide2.QtCore.QGenericArgument = ...,
        val1: PySide2.QtCore.QGenericArgument = ...,
        val2: PySide2.QtCore.QGenericArgument = ...,
        val3: PySide2.QtCore.QGenericArgument = ...,
        val4: PySide2.QtCore.QGenericArgument = ...,
        val5: PySide2.QtCore.QGenericArgument = ...,
        val6: PySide2.QtCore.QGenericArgument = ...,
        val7: PySide2.QtCore.QGenericArgument = ...,
        val8: PySide2.QtCore.QGenericArgument = ...,
        val9: PySide2.QtCore.QGenericArgument = ...,
    ) -> PySide2.QtCore.QObject: ...
    @staticmethod
    def normalizedSignature(method: bytes) -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def normalizedType(type: bytes) -> PySide2.QtCore.QByteArray: ...
    def property(self, index: int) -> PySide2.QtCore.QMetaProperty: ...
    def propertyCount(self) -> int: ...
    def propertyOffset(self) -> int: ...
    def superClass(self) -> PySide2.QtCore.QMetaObject: ...
    def userProperty(self) -> PySide2.QtCore.QMetaProperty: ...

class QMetaProperty(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QMetaProperty: PySide2.QtCore.QMetaProperty): ...
    def __copy__(self): ...
    def enumerator(self) -> PySide2.QtCore.QMetaEnum: ...
    def hasNotifySignal(self) -> bool: ...
    def hasStdCppSet(self) -> bool: ...
    def isConstant(self) -> bool: ...
    def isDesignable(
        self, obj: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> bool: ...
    def isEditable(
        self, obj: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> bool: ...
    def isEnumType(self) -> bool: ...
    def isFinal(self) -> bool: ...
    def isFlagType(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isRequired(self) -> bool: ...
    def isResettable(self) -> bool: ...
    def isScriptable(
        self, obj: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> bool: ...
    def isStored(self, obj: typing.Optional[PySide2.QtCore.QObject] = ...) -> bool: ...
    def isUser(self, obj: typing.Optional[PySide2.QtCore.QObject] = ...) -> bool: ...
    def isValid(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def name(self) -> bytes: ...
    def notifySignal(self) -> PySide2.QtCore.QMetaMethod: ...
    def notifySignalIndex(self) -> int: ...
    def propertyIndex(self) -> int: ...
    def read(self, obj: PySide2.QtCore.QObject) -> typing.Any: ...
    def readOnGadget(self, gadget: int) -> typing.Any: ...
    def relativePropertyIndex(self) -> int: ...
    def reset(self, obj: PySide2.QtCore.QObject) -> bool: ...
    def resetOnGadget(self, gadget: int) -> bool: ...
    def revision(self) -> int: ...
    def type(self) -> type: ...
    def typeName(self) -> bytes: ...
    def userType(self) -> int: ...
    def write(self, obj: PySide2.QtCore.QObject, value: typing.Any) -> bool: ...
    def writeOnGadget(self, gadget: int, value: typing.Any) -> bool: ...

class QMimeData(PySide2.QtCore.QObject):
    def __init__(self): ...
    def clear(self): ...
    def colorData(self) -> typing.Any: ...
    def data(self, mimetype: str) -> PySide2.QtCore.QByteArray: ...
    def formats(self) -> typing.List: ...
    def hasColor(self) -> bool: ...
    def hasFormat(self, mimetype: str) -> bool: ...
    def hasHtml(self) -> bool: ...
    def hasImage(self) -> bool: ...
    def hasText(self) -> bool: ...
    def hasUrls(self) -> bool: ...
    def html(self) -> str: ...
    def imageData(self) -> typing.Any: ...
    def removeFormat(self, mimetype: str): ...
    def retrieveData(self, mimetype: str, preferredType: type) -> typing.Any: ...
    def setColorData(self, color: typing.Any): ...
    def setData(self, mimetype: str, data: PySide2.QtCore.QByteArray): ...
    def setHtml(self, html: str): ...
    def setImageData(self, image: typing.Any): ...
    def setText(self, text: str): ...
    def setUrls(self, urls: typing.Sequence): ...
    def text(self) -> str: ...
    def urls(self) -> typing.List: ...

class QMimeDatabase(Shiboken.Object):
    MatchDefault: QMimeDatabase = ...  # 0x0
    MatchExtension: QMimeDatabase = ...  # 0x1
    MatchContent: QMimeDatabase = ...  # 0x2

    class MatchMode(object):
        MatchDefault: QMimeDatabase.MatchMode = ...  # 0x0
        MatchExtension: QMimeDatabase.MatchMode = ...  # 0x1
        MatchContent: QMimeDatabase.MatchMode = ...  # 0x2
    def __init__(self): ...
    def allMimeTypes(self) -> typing.List: ...
    @typing.overload
    def mimeTypeForData(
        self, data: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QMimeType: ...
    @typing.overload
    def mimeTypeForData(
        self, device: PySide2.QtCore.QIODevice
    ) -> PySide2.QtCore.QMimeType: ...
    @typing.overload
    def mimeTypeForFile(
        self,
        fileInfo: PySide2.QtCore.QFileInfo,
        mode: PySide2.QtCore.QMimeDatabase.MatchMode = ...,
    ) -> PySide2.QtCore.QMimeType: ...
    @typing.overload
    def mimeTypeForFile(
        self, fileName: str, mode: PySide2.QtCore.QMimeDatabase.MatchMode = ...
    ) -> PySide2.QtCore.QMimeType: ...
    @typing.overload
    def mimeTypeForFileNameAndData(
        self, fileName: str, data: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QMimeType: ...
    @typing.overload
    def mimeTypeForFileNameAndData(
        self, fileName: str, device: PySide2.QtCore.QIODevice
    ) -> PySide2.QtCore.QMimeType: ...
    def mimeTypeForName(self, nameOrAlias: str) -> PySide2.QtCore.QMimeType: ...
    def mimeTypeForUrl(self, url: PySide2.QtCore.QUrl) -> PySide2.QtCore.QMimeType: ...
    def mimeTypesForFileName(self, fileName: str) -> typing.List: ...
    def suffixForFileName(self, fileName: str) -> str: ...

class QMimeType(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QMimeType): ...
    def __copy__(self): ...
    def aliases(self) -> typing.List: ...
    def allAncestors(self) -> typing.List: ...
    def comment(self) -> str: ...
    def filterString(self) -> str: ...
    def genericIconName(self) -> str: ...
    def globPatterns(self) -> typing.List: ...
    def iconName(self) -> str: ...
    def inherits(self, mimeTypeName: str) -> bool: ...
    def isDefault(self) -> bool: ...
    def isValid(self) -> bool: ...
    def name(self) -> str: ...
    def parentMimeTypes(self) -> typing.List: ...
    def preferredSuffix(self) -> str: ...
    def suffixes(self) -> typing.List: ...
    def swap(self, other: PySide2.QtCore.QMimeType): ...

class QModelIndex(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QModelIndex: PySide2.QtCore.QModelIndex): ...
    def __copy__(self): ...
    def child(self, row: int, column: int) -> PySide2.QtCore.QModelIndex: ...
    def column(self) -> int: ...
    def data(self, role: int = ...) -> typing.Any: ...
    def flags(self) -> PySide2.QtCore.Qt.ItemFlags: ...
    def internalId(self) -> int: ...
    def internalPointer(self) -> int: ...
    def isValid(self) -> bool: ...
    def model(self) -> PySide2.QtCore.QAbstractItemModel: ...
    def parent(self) -> PySide2.QtCore.QModelIndex: ...
    def row(self) -> int: ...
    def sibling(self, row: int, column: int) -> PySide2.QtCore.QModelIndex: ...
    def siblingAtColumn(self, column: int) -> PySide2.QtCore.QModelIndex: ...
    def siblingAtRow(self, row: int) -> PySide2.QtCore.QModelIndex: ...

class QMutex(PySide2.QtCore.QBasicMutex):
    NonRecursive: QMutex = ...  # 0x0
    Recursive: QMutex = ...  # 0x1

    class RecursionMode(object):
        NonRecursive: QMutex.RecursionMode = ...  # 0x0
        Recursive: QMutex.RecursionMode = ...  # 0x1
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mode: PySide2.QtCore.QMutex.RecursionMode): ...
    def isRecursive(self) -> bool: ...
    def lock(self): ...
    @typing.overload
    def tryLock(self) -> bool: ...
    @typing.overload
    def tryLock(self, timeout: int = ...) -> bool: ...
    def try_lock(self) -> bool: ...
    def unlock(self): ...

class QMutexLocker(Shiboken.Object):
    @typing.overload
    def __init__(self, m: PySide2.QtCore.QBasicMutex): ...
    @typing.overload
    def __init__(self, m: PySide2.QtCore.QRecursiveMutex): ...
    def __enter__(self): ...
    def __exit__(self, arg__1: object, arg__2: object, arg__3: object): ...
    def mutex(self) -> PySide2.QtCore.QMutex: ...
    def relock(self): ...
    def unlock(self): ...

class QObject(Shiboken.Object):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def blockSignals(self, b: bool) -> bool: ...
    def childEvent(self, event: PySide2.QtCore.QChildEvent): ...
    def children(self) -> typing.List: ...
    @typing.overload
    @staticmethod
    def connect(
        arg__1: PySide2.QtCore.QObject,
        arg__2: bytes,
        arg__3: typing.Callable,
        type: PySide2.QtCore.Qt.ConnectionType = ...,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def connect(
        arg__1: bytes,
        arg__2: typing.Callable,
        type: PySide2.QtCore.Qt.ConnectionType = ...,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def connect(
        arg__1: bytes,
        arg__2: PySide2.QtCore.QObject,
        arg__3: bytes,
        type: PySide2.QtCore.Qt.ConnectionType = ...,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def connect(
        sender: PySide2.QtCore.QObject,
        signal: PySide2.QtCore.QMetaMethod,
        receiver: PySide2.QtCore.QObject,
        method: PySide2.QtCore.QMetaMethod,
        type: PySide2.QtCore.Qt.ConnectionType = ...,
    ) -> PySide2.QtCore.QMetaObject.Connection: ...
    @typing.overload
    @staticmethod
    def connect(
        sender: PySide2.QtCore.QObject,
        signal: bytes,
        member: bytes,
        type: PySide2.QtCore.Qt.ConnectionType = ...,
    ) -> PySide2.QtCore.QMetaObject.Connection: ...
    @typing.overload
    @staticmethod
    def connect(
        sender: PySide2.QtCore.QObject,
        signal: bytes,
        receiver: PySide2.QtCore.QObject,
        member: bytes,
        type: PySide2.QtCore.Qt.ConnectionType = ...,
    ) -> PySide2.QtCore.QMetaObject.Connection: ...
    def connectNotify(self, signal: PySide2.QtCore.QMetaMethod): ...
    def customEvent(self, event: PySide2.QtCore.QEvent): ...
    def deleteLater(self): ...
    @typing.overload
    @staticmethod
    def disconnect(arg__1: PySide2.QtCore.QMetaObject.Connection) -> bool: ...
    @typing.overload
    @staticmethod
    def disconnect(
        arg__1: PySide2.QtCore.QObject, arg__2: bytes, arg__3: typing.Callable
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def disconnect(arg__1: bytes, arg__2: typing.Callable) -> bool: ...
    @typing.overload
    @staticmethod
    def disconnect(
        receiver: PySide2.QtCore.QObject, member: typing.Optional[bytes] = ...
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def disconnect(
        sender: PySide2.QtCore.QObject,
        signal: PySide2.QtCore.QMetaMethod,
        receiver: PySide2.QtCore.QObject,
        member: PySide2.QtCore.QMetaMethod,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def disconnect(
        sender: PySide2.QtCore.QObject,
        signal: bytes,
        receiver: PySide2.QtCore.QObject,
        member: bytes,
    ) -> bool: ...
    @typing.overload
    @staticmethod
    def disconnect(
        signal: bytes, receiver: PySide2.QtCore.QObject, member: bytes
    ) -> bool: ...
    def disconnectNotify(self, signal: PySide2.QtCore.QMetaMethod): ...
    def dumpObjectInfo(self): ...
    def dumpObjectTree(self): ...
    def dynamicPropertyNames(self) -> typing.List: ...
    def emit(self, arg__1: bytes, *args: None) -> bool: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def eventFilter(
        self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent
    ) -> bool: ...
    def findChild(self, arg__1: type, arg__2: str = ...) -> object: ...
    @typing.overload
    def findChildren(
        self, arg__1: type, arg__2: PySide2.QtCore.QRegExp
    ) -> typing.Iterable: ...
    @typing.overload
    def findChildren(self, arg__1: type, arg__2: str = ...) -> typing.Iterable: ...
    def inherits(self, classname: bytes) -> bool: ...
    def installEventFilter(self, filterObj: PySide2.QtCore.QObject): ...
    def isSignalConnected(self, signal: PySide2.QtCore.QMetaMethod) -> bool: ...
    def isWidgetType(self) -> bool: ...
    def isWindowType(self) -> bool: ...
    def killTimer(self, id: int): ...
    def metaObject(self) -> PySide2.QtCore.QMetaObject: ...
    def moveToThread(self, thread: PySide2.QtCore.QThread): ...
    def objectName(self) -> str: ...
    def parent(self) -> PySide2.QtCore.QObject: ...
    def property(self, name: bytes) -> typing.Any: ...
    def receivers(self, signal: bytes) -> int: ...
    @staticmethod
    def registerUserData() -> int: ...
    def removeEventFilter(self, obj: PySide2.QtCore.QObject): ...
    def sender(self) -> PySide2.QtCore.QObject: ...
    def senderSignalIndex(self) -> int: ...
    def setObjectName(self, name: str): ...
    def setParent(self, parent: PySide2.QtCore.QObject): ...
    def setProperty(self, name: bytes, value: typing.Any) -> bool: ...
    def signalsBlocked(self) -> bool: ...
    def startTimer(
        self, interval: int, timerType: PySide2.QtCore.Qt.TimerType = ...
    ) -> int: ...
    def thread(self) -> PySide2.QtCore.QThread: ...
    def timerEvent(self, event: PySide2.QtCore.QTimerEvent): ...
    def tr(self, arg__1: bytes, arg__2: bytes = ..., arg__3: int = ...) -> str: ...

class QOperatingSystemVersion(Shiboken.Object):
    Unknown: QOperatingSystemVersion = ...  # 0x0
    Windows: QOperatingSystemVersion = ...  # 0x1
    MacOS: QOperatingSystemVersion = ...  # 0x2
    IOS: QOperatingSystemVersion = ...  # 0x3
    TvOS: QOperatingSystemVersion = ...  # 0x4
    WatchOS: QOperatingSystemVersion = ...  # 0x5
    Android: QOperatingSystemVersion = ...  # 0x6

    class OSType(object):
        Unknown: QOperatingSystemVersion.OSType = ...  # 0x0
        Windows: QOperatingSystemVersion.OSType = ...  # 0x1
        MacOS: QOperatingSystemVersion.OSType = ...  # 0x2
        IOS: QOperatingSystemVersion.OSType = ...  # 0x3
        TvOS: QOperatingSystemVersion.OSType = ...  # 0x4
        WatchOS: QOperatingSystemVersion.OSType = ...  # 0x5
        Android: QOperatingSystemVersion.OSType = ...  # 0x6
    @typing.overload
    def __init__(
        self, QOperatingSystemVersion: PySide2.QtCore.QOperatingSystemVersion
    ): ...
    @typing.overload
    def __init__(
        self,
        osType: PySide2.QtCore.QOperatingSystemVersion.OSType,
        vmajor: int,
        vminor: int = ...,
        vmicro: int = ...,
    ): ...
    def __copy__(self): ...
    @staticmethod
    def current() -> PySide2.QtCore.QOperatingSystemVersion: ...
    @staticmethod
    def currentType() -> PySide2.QtCore.QOperatingSystemVersion.OSType: ...
    def majorVersion(self) -> int: ...
    def microVersion(self) -> int: ...
    def minorVersion(self) -> int: ...
    def name(self) -> str: ...
    def segmentCount(self) -> int: ...
    def type(self) -> PySide2.QtCore.QOperatingSystemVersion.OSType: ...

class QParallelAnimationGroup(PySide2.QtCore.QAnimationGroup):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def duration(self) -> int: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def updateCurrentTime(self, currentTime: int): ...
    def updateDirection(
        self, direction: PySide2.QtCore.QAbstractAnimation.Direction
    ): ...
    def updateState(
        self,
        newState: PySide2.QtCore.QAbstractAnimation.State,
        oldState: PySide2.QtCore.QAbstractAnimation.State,
    ): ...

class QPauseAnimation(PySide2.QtCore.QAbstractAnimation):
    @typing.overload
    def __init__(
        self, msecs: int, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def duration(self) -> int: ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def setDuration(self, msecs: int): ...
    def updateCurrentTime(self, arg__1: int): ...

class QPersistentModelIndex(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, index: PySide2.QtCore.QModelIndex): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QPersistentModelIndex): ...
    def __copy__(self): ...
    def child(self, row: int, column: int) -> PySide2.QtCore.QModelIndex: ...
    def column(self) -> int: ...
    def data(self, role: int = ...) -> typing.Any: ...
    def flags(self) -> PySide2.QtCore.Qt.ItemFlags: ...
    def internalId(self) -> int: ...
    def internalPointer(self) -> int: ...
    def isValid(self) -> bool: ...
    def model(self) -> PySide2.QtCore.QAbstractItemModel: ...
    def parent(self) -> PySide2.QtCore.QModelIndex: ...
    def row(self) -> int: ...
    def sibling(self, row: int, column: int) -> PySide2.QtCore.QModelIndex: ...
    def swap(self, other: PySide2.QtCore.QPersistentModelIndex): ...

class QPluginLoader(PySide2.QtCore.QObject):
    @typing.overload
    def __init__(
        self, fileName: str, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def errorString(self) -> str: ...
    def fileName(self) -> str: ...
    def instance(self) -> PySide2.QtCore.QObject: ...
    def isLoaded(self) -> bool: ...
    def load(self) -> bool: ...
    def metaData(self) -> typing.Dict: ...
    def setFileName(self, fileName: str): ...
    @staticmethod
    def staticInstances() -> typing.List: ...
    def unload(self) -> bool: ...

class QPoint(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QPoint: PySide2.QtCore.QPoint): ...
    @typing.overload
    def __init__(self, xpos: int, ypos: int): ...
    def __add__(self, p2: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint: ...
    def __copy__(self): ...
    def __iadd__(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def __imul__(self, factor: float) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def __imul__(self, factor: float) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def __imul__(self, factor: int) -> PySide2.QtCore.QPoint: ...
    def __isub__(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def __mul__(self, factor: float) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def __mul__(self, factor: float) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def __mul__(self, factor: int) -> PySide2.QtCore.QPoint: ...
    def __neg__(self) -> PySide2.QtCore.QPoint: ...
    def __pos__(self) -> PySide2.QtCore.QPoint: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, p2: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint: ...
    @staticmethod
    def dotProduct(p1: PySide2.QtCore.QPoint, p2: PySide2.QtCore.QPoint) -> int: ...
    def isNull(self) -> bool: ...
    def manhattanLength(self) -> int: ...
    def setX(self, x: int): ...
    def setY(self, y: int): ...
    def toTuple(self) -> object: ...
    def transposed(self) -> PySide2.QtCore.QPoint: ...
    def x(self) -> int: ...
    def y(self) -> int: ...

class QPointF(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QPointF: PySide2.QtCore.QPointF): ...
    @typing.overload
    def __init__(self, p: PySide2.QtCore.QPoint): ...
    @typing.overload
    def __init__(self, xpos: float, ypos: float): ...
    def __add__(self, p2: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF: ...
    def __copy__(self): ...
    def __iadd__(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF: ...
    def __imul__(self, c: float) -> PySide2.QtCore.QPointF: ...
    def __isub__(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF: ...
    def __mul__(self, c: float) -> PySide2.QtCore.QPointF: ...
    def __neg__(self) -> PySide2.QtCore.QPointF: ...
    def __pos__(self) -> PySide2.QtCore.QPointF: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, p2: PySide2.QtCore.QPointF) -> PySide2.QtCore.QPointF: ...
    @staticmethod
    def dotProduct(p1: PySide2.QtCore.QPointF, p2: PySide2.QtCore.QPointF) -> float: ...
    def isNull(self) -> bool: ...
    def manhattanLength(self) -> float: ...
    def setX(self, x: float): ...
    def setY(self, y: float): ...
    def toPoint(self) -> PySide2.QtCore.QPoint: ...
    def toTuple(self) -> object: ...
    def transposed(self) -> PySide2.QtCore.QPointF: ...
    def x(self) -> float: ...
    def y(self) -> float: ...

class QProcess(PySide2.QtCore.QIODevice):
    FailedToStart: QProcess = ...  # 0x0
    ManagedInputChannel: QProcess = ...  # 0x0
    NormalExit: QProcess = ...  # 0x0
    NotRunning: QProcess = ...  # 0x0
    SeparateChannels: QProcess = ...  # 0x0
    StandardOutput: QProcess = ...  # 0x0
    CrashExit: QProcess = ...  # 0x1
    Crashed: QProcess = ...  # 0x1
    ForwardedInputChannel: QProcess = ...  # 0x1
    MergedChannels: QProcess = ...  # 0x1
    StandardError: QProcess = ...  # 0x1
    Starting: QProcess = ...  # 0x1
    ForwardedChannels: QProcess = ...  # 0x2
    Running: QProcess = ...  # 0x2
    Timedout: QProcess = ...  # 0x2
    ForwardedOutputChannel: QProcess = ...  # 0x3
    ReadError: QProcess = ...  # 0x3
    ForwardedErrorChannel: QProcess = ...  # 0x4
    WriteError: QProcess = ...  # 0x4
    UnknownError: QProcess = ...  # 0x5

    class ExitStatus(object):
        NormalExit: QProcess.ExitStatus = ...  # 0x0
        CrashExit: QProcess.ExitStatus = ...  # 0x1

    class InputChannelMode(object):
        ManagedInputChannel: QProcess.InputChannelMode = ...  # 0x0
        ForwardedInputChannel: QProcess.InputChannelMode = ...  # 0x1

    class ProcessChannel(object):
        StandardOutput: QProcess.ProcessChannel = ...  # 0x0
        StandardError: QProcess.ProcessChannel = ...  # 0x1

    class ProcessChannelMode(object):
        SeparateChannels: QProcess.ProcessChannelMode = ...  # 0x0
        MergedChannels: QProcess.ProcessChannelMode = ...  # 0x1
        ForwardedChannels: QProcess.ProcessChannelMode = ...  # 0x2
        ForwardedOutputChannel: QProcess.ProcessChannelMode = ...  # 0x3
        ForwardedErrorChannel: QProcess.ProcessChannelMode = ...  # 0x4

    class ProcessError(object):
        FailedToStart: QProcess.ProcessError = ...  # 0x0
        Crashed: QProcess.ProcessError = ...  # 0x1
        Timedout: QProcess.ProcessError = ...  # 0x2
        ReadError: QProcess.ProcessError = ...  # 0x3
        WriteError: QProcess.ProcessError = ...  # 0x4
        UnknownError: QProcess.ProcessError = ...  # 0x5

    class ProcessState(object):
        NotRunning: QProcess.ProcessState = ...  # 0x0
        Starting: QProcess.ProcessState = ...  # 0x1
        Running: QProcess.ProcessState = ...  # 0x2
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def arguments(self) -> typing.List: ...
    def atEnd(self) -> bool: ...
    def bytesAvailable(self) -> int: ...
    def bytesToWrite(self) -> int: ...
    def canReadLine(self) -> bool: ...
    def close(self): ...
    def closeReadChannel(self, channel: PySide2.QtCore.QProcess.ProcessChannel): ...
    def closeWriteChannel(self): ...
    def environment(self) -> typing.List: ...
    def error(self) -> PySide2.QtCore.QProcess.ProcessError: ...
    @typing.overload
    @staticmethod
    def execute(command: str) -> int: ...
    @typing.overload
    @staticmethod
    def execute(program: str, arguments: typing.Sequence) -> int: ...
    def exitCode(self) -> int: ...
    def exitStatus(self) -> PySide2.QtCore.QProcess.ExitStatus: ...
    def inputChannelMode(self) -> PySide2.QtCore.QProcess.InputChannelMode: ...
    def isSequential(self) -> bool: ...
    def kill(self): ...
    def nativeArguments(self) -> str: ...
    @staticmethod
    def nullDevice() -> str: ...
    def open(self, mode: PySide2.QtCore.QIODevice.OpenMode = ...) -> bool: ...
    def pid(self) -> int: ...
    def processChannelMode(self) -> PySide2.QtCore.QProcess.ProcessChannelMode: ...
    def processEnvironment(self) -> PySide2.QtCore.QProcessEnvironment: ...
    def processId(self) -> int: ...
    def program(self) -> str: ...
    def readAllStandardError(self) -> PySide2.QtCore.QByteArray: ...
    def readAllStandardOutput(self) -> PySide2.QtCore.QByteArray: ...
    def readChannel(self) -> PySide2.QtCore.QProcess.ProcessChannel: ...
    def readData(self, data: bytes, maxlen: int) -> int: ...
    def setArguments(self, arguments: typing.Sequence): ...
    def setEnvironment(self, environment: typing.Sequence): ...
    def setInputChannelMode(self, mode: PySide2.QtCore.QProcess.InputChannelMode): ...
    def setNativeArguments(self, arguments: str): ...
    def setProcessChannelMode(
        self, mode: PySide2.QtCore.QProcess.ProcessChannelMode
    ): ...
    def setProcessEnvironment(
        self, environment: PySide2.QtCore.QProcessEnvironment
    ): ...
    def setProcessState(self, state: PySide2.QtCore.QProcess.ProcessState): ...
    def setProgram(self, program: str): ...
    def setReadChannel(self, channel: PySide2.QtCore.QProcess.ProcessChannel): ...
    def setStandardErrorFile(
        self, fileName: str, mode: PySide2.QtCore.QIODevice.OpenMode = ...
    ): ...
    def setStandardInputFile(self, fileName: str): ...
    def setStandardOutputFile(
        self, fileName: str, mode: PySide2.QtCore.QIODevice.OpenMode = ...
    ): ...
    def setStandardOutputProcess(self, destination: PySide2.QtCore.QProcess): ...
    def setWorkingDirectory(self, dir: str): ...
    def setupChildProcess(self): ...
    @typing.overload
    def start(self, command: str, mode: PySide2.QtCore.QIODevice.OpenMode = ...): ...
    @typing.overload
    def start(self, mode: PySide2.QtCore.QIODevice.OpenMode = ...): ...
    @typing.overload
    def start(
        self,
        program: str,
        arguments: typing.Sequence,
        mode: PySide2.QtCore.QIODevice.OpenMode = ...,
    ): ...
    @typing.overload
    @staticmethod
    def startDetached(command: str) -> bool: ...
    @typing.overload
    @staticmethod
    def startDetached() -> typing.Tuple: ...
    @typing.overload
    @staticmethod
    def startDetached(program: str, arguments: typing.Sequence) -> bool: ...
    @typing.overload
    @staticmethod
    def startDetached(
        program: str, arguments: typing.Sequence, workingDirectory: str
    ) -> typing.Tuple: ...
    def state(self) -> PySide2.QtCore.QProcess.ProcessState: ...
    @staticmethod
    def systemEnvironment() -> typing.List: ...
    def terminate(self): ...
    def waitForBytesWritten(self, msecs: int = ...) -> bool: ...
    def waitForFinished(self, msecs: int = ...) -> bool: ...
    def waitForReadyRead(self, msecs: int = ...) -> bool: ...
    def waitForStarted(self, msecs: int = ...) -> bool: ...
    def workingDirectory(self) -> str: ...
    def writeData(self, data: bytes, len: int) -> int: ...

class QProcessEnvironment(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QProcessEnvironment): ...
    def __copy__(self): ...
    def clear(self): ...
    def contains(self, name: str) -> bool: ...
    @typing.overload
    def insert(self, e: PySide2.QtCore.QProcessEnvironment): ...
    @typing.overload
    def insert(self, name: str, value: str): ...
    def isEmpty(self) -> bool: ...
    def keys(self) -> typing.List: ...
    def remove(self, name: str): ...
    def swap(self, other: PySide2.QtCore.QProcessEnvironment): ...
    @staticmethod
    def systemEnvironment() -> PySide2.QtCore.QProcessEnvironment: ...
    def toStringList(self) -> typing.List: ...
    def value(self, name: str, defaultValue: str = ...) -> str: ...

class QPropertyAnimation(PySide2.QtCore.QVariantAnimation):
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    @typing.overload
    def __init__(
        self,
        target: PySide2.QtCore.QObject,
        propertyName: PySide2.QtCore.QByteArray,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def propertyName(self) -> PySide2.QtCore.QByteArray: ...
    def setPropertyName(self, propertyName: PySide2.QtCore.QByteArray): ...
    def setTargetObject(self, target: PySide2.QtCore.QObject): ...
    def targetObject(self) -> PySide2.QtCore.QObject: ...
    def updateCurrentValue(self, value: typing.Any): ...
    def updateState(
        self,
        newState: PySide2.QtCore.QAbstractAnimation.State,
        oldState: PySide2.QtCore.QAbstractAnimation.State,
    ): ...

class QRandomGenerator(Shiboken.Object):
    @typing.overload
    def __init__(self, begin: int, end: int): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QRandomGenerator): ...
    @typing.overload
    def __init__(self, seedBuffer: int, len: int): ...
    @typing.overload
    def __init__(self, seedValue: int = ...): ...
    @typing.overload
    def bounded(self, highest: float) -> float: ...
    @typing.overload
    def bounded(self, highest: int) -> int: ...
    @typing.overload
    def bounded(self, highest: int) -> int: ...
    @typing.overload
    def bounded(self, lowest: int, highest: int) -> int: ...
    @typing.overload
    def bounded(self, lowest: int, highest: int) -> int: ...
    def discard(self, z: int): ...
    def generate(self) -> int: ...
    def generate64(self) -> int: ...
    def generateDouble(self) -> float: ...
    @staticmethod
    def global_() -> PySide2.QtCore.QRandomGenerator: ...
    @staticmethod
    def max() -> int: ...
    @staticmethod
    def min() -> int: ...
    @staticmethod
    def securelySeeded() -> PySide2.QtCore.QRandomGenerator: ...
    def seed(self, s: int = ...): ...
    @staticmethod
    def system() -> PySide2.QtCore.QRandomGenerator: ...

class QRandomGenerator64(PySide2.QtCore.QRandomGenerator):
    @typing.overload
    def __init__(self, begin: int, end: int): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QRandomGenerator): ...
    @typing.overload
    def __init__(self, seedBuffer: int, len: int): ...
    @typing.overload
    def __init__(self, seedValue: int = ...): ...
    def discard(self, z: int): ...
    def generate(self) -> int: ...
    @staticmethod
    def global_() -> PySide2.QtCore.QRandomGenerator64: ...
    @staticmethod
    def max() -> int: ...
    @staticmethod
    def min() -> int: ...
    @staticmethod
    def securelySeeded() -> PySide2.QtCore.QRandomGenerator64: ...
    @staticmethod
    def system() -> PySide2.QtCore.QRandomGenerator64: ...

class QReadLocker(Shiboken.Object):
    def __init__(self, readWriteLock: PySide2.QtCore.QReadWriteLock): ...
    def __enter__(self): ...
    def __exit__(self, arg__1: object, arg__2: object, arg__3: object): ...
    def readWriteLock(self) -> PySide2.QtCore.QReadWriteLock: ...
    def relock(self): ...
    def unlock(self): ...

class QReadWriteLock(Shiboken.Object):
    NonRecursive: QReadWriteLock = ...  # 0x0
    Recursive: QReadWriteLock = ...  # 0x1

    class RecursionMode(object):
        NonRecursive: QReadWriteLock.RecursionMode = ...  # 0x0
        Recursive: QReadWriteLock.RecursionMode = ...  # 0x1
    def __init__(
        self, recursionMode: PySide2.QtCore.QReadWriteLock.RecursionMode = ...
    ): ...
    def lockForRead(self): ...
    def lockForWrite(self): ...
    @typing.overload
    def tryLockForRead(self) -> bool: ...
    @typing.overload
    def tryLockForRead(self, timeout: int) -> bool: ...
    @typing.overload
    def tryLockForWrite(self) -> bool: ...
    @typing.overload
    def tryLockForWrite(self, timeout: int) -> bool: ...
    def unlock(self): ...

class QRect(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QRect: PySide2.QtCore.QRect): ...
    @typing.overload
    def __init__(self, left: int, top: int, width: int, height: int): ...
    @typing.overload
    def __init__(
        self, topleft: PySide2.QtCore.QPoint, bottomright: PySide2.QtCore.QPoint
    ): ...
    @typing.overload
    def __init__(self, topleft: PySide2.QtCore.QPoint, size: PySide2.QtCore.QSize): ...
    def __add__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect: ...
    def __and__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect: ...
    def __copy__(self): ...
    def __iadd__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect: ...
    def __iand__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect: ...
    def __ior__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect: ...
    def __isub__(self, margins: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect: ...
    def __or__(self, r: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, rhs: PySide2.QtCore.QMargins) -> PySide2.QtCore.QRect: ...
    def adjust(self, x1: int, y1: int, x2: int, y2: int): ...
    def adjusted(self, x1: int, y1: int, x2: int, y2: int) -> PySide2.QtCore.QRect: ...
    def bottom(self) -> int: ...
    def bottomLeft(self) -> PySide2.QtCore.QPoint: ...
    def bottomRight(self) -> PySide2.QtCore.QPoint: ...
    def center(self) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def contains(self, p: PySide2.QtCore.QPoint, proper: bool = ...) -> bool: ...
    @typing.overload
    def contains(self, r: PySide2.QtCore.QRect, proper: bool = ...) -> bool: ...
    @typing.overload
    def contains(self, x: int, y: int) -> bool: ...
    @typing.overload
    def contains(self, x: int, y: int, proper: bool) -> bool: ...
    def getCoords(self) -> typing.Tuple: ...
    def getRect(self) -> typing.Tuple: ...
    def height(self) -> int: ...
    def intersected(self, other: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect: ...
    def intersects(self, r: PySide2.QtCore.QRect) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isValid(self) -> bool: ...
    def left(self) -> int: ...
    def marginsAdded(
        self, margins: PySide2.QtCore.QMargins
    ) -> PySide2.QtCore.QRect: ...
    def marginsRemoved(
        self, margins: PySide2.QtCore.QMargins
    ) -> PySide2.QtCore.QRect: ...
    def moveBottom(self, pos: int): ...
    def moveBottomLeft(self, p: PySide2.QtCore.QPoint): ...
    def moveBottomRight(self, p: PySide2.QtCore.QPoint): ...
    def moveCenter(self, p: PySide2.QtCore.QPoint): ...
    def moveLeft(self, pos: int): ...
    def moveRight(self, pos: int): ...
    @typing.overload
    def moveTo(self, p: PySide2.QtCore.QPoint): ...
    @typing.overload
    def moveTo(self, x: int, t: int): ...
    def moveTop(self, pos: int): ...
    def moveTopLeft(self, p: PySide2.QtCore.QPoint): ...
    def moveTopRight(self, p: PySide2.QtCore.QPoint): ...
    def normalized(self) -> PySide2.QtCore.QRect: ...
    def right(self) -> int: ...
    def setBottom(self, pos: int): ...
    def setBottomLeft(self, p: PySide2.QtCore.QPoint): ...
    def setBottomRight(self, p: PySide2.QtCore.QPoint): ...
    def setCoords(self, x1: int, y1: int, x2: int, y2: int): ...
    def setHeight(self, h: int): ...
    def setLeft(self, pos: int): ...
    def setRect(self, x: int, y: int, w: int, h: int): ...
    def setRight(self, pos: int): ...
    def setSize(self, s: PySide2.QtCore.QSize): ...
    def setTop(self, pos: int): ...
    def setTopLeft(self, p: PySide2.QtCore.QPoint): ...
    def setTopRight(self, p: PySide2.QtCore.QPoint): ...
    def setWidth(self, w: int): ...
    def setX(self, x: int): ...
    def setY(self, y: int): ...
    def size(self) -> PySide2.QtCore.QSize: ...
    def top(self) -> int: ...
    def topLeft(self) -> PySide2.QtCore.QPoint: ...
    def topRight(self) -> PySide2.QtCore.QPoint: ...
    @typing.overload
    def translate(self, dx: int, dy: int): ...
    @typing.overload
    def translate(self, p: PySide2.QtCore.QPoint): ...
    @typing.overload
    def translated(self, dx: int, dy: int) -> PySide2.QtCore.QRect: ...
    @typing.overload
    def translated(self, p: PySide2.QtCore.QPoint) -> PySide2.QtCore.QRect: ...
    def transposed(self) -> PySide2.QtCore.QRect: ...
    def united(self, other: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect: ...
    def width(self) -> int: ...
    def x(self) -> int: ...
    def y(self) -> int: ...

class QRectF(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QRectF: PySide2.QtCore.QRectF): ...
    @typing.overload
    def __init__(self, left: float, top: float, width: float, height: float): ...
    @typing.overload
    def __init__(self, rect: PySide2.QtCore.QRect): ...
    @typing.overload
    def __init__(
        self, topleft: PySide2.QtCore.QPointF, bottomRight: PySide2.QtCore.QPointF
    ): ...
    @typing.overload
    def __init__(
        self, topleft: PySide2.QtCore.QPointF, size: PySide2.QtCore.QSizeF
    ): ...
    @typing.overload
    def __add__(self, lhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF: ...
    @typing.overload
    def __add__(self, rhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF: ...
    def __and__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF: ...
    def __copy__(self): ...
    def __iadd__(self, margins: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF: ...
    def __iand__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF: ...
    def __ior__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF: ...
    def __isub__(self, margins: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF: ...
    def __or__(self, r: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, rhs: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QRectF: ...
    def adjust(self, x1: float, y1: float, x2: float, y2: float): ...
    def adjusted(
        self, x1: float, y1: float, x2: float, y2: float
    ) -> PySide2.QtCore.QRectF: ...
    def bottom(self) -> float: ...
    def bottomLeft(self) -> PySide2.QtCore.QPointF: ...
    def bottomRight(self) -> PySide2.QtCore.QPointF: ...
    def center(self) -> PySide2.QtCore.QPointF: ...
    @typing.overload
    def contains(self, p: PySide2.QtCore.QPointF) -> bool: ...
    @typing.overload
    def contains(self, r: PySide2.QtCore.QRectF) -> bool: ...
    @typing.overload
    def contains(self, x: float, y: float) -> bool: ...
    def getCoords(self) -> typing.Tuple: ...
    def getRect(self) -> typing.Tuple: ...
    def height(self) -> float: ...
    def intersected(self, other: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF: ...
    def intersects(self, r: PySide2.QtCore.QRectF) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isValid(self) -> bool: ...
    def left(self) -> float: ...
    def marginsAdded(
        self, margins: PySide2.QtCore.QMarginsF
    ) -> PySide2.QtCore.QRectF: ...
    def marginsRemoved(
        self, margins: PySide2.QtCore.QMarginsF
    ) -> PySide2.QtCore.QRectF: ...
    def moveBottom(self, pos: float): ...
    def moveBottomLeft(self, p: PySide2.QtCore.QPointF): ...
    def moveBottomRight(self, p: PySide2.QtCore.QPointF): ...
    def moveCenter(self, p: PySide2.QtCore.QPointF): ...
    def moveLeft(self, pos: float): ...
    def moveRight(self, pos: float): ...
    @typing.overload
    def moveTo(self, p: PySide2.QtCore.QPointF): ...
    @typing.overload
    def moveTo(self, x: float, y: float): ...
    def moveTop(self, pos: float): ...
    def moveTopLeft(self, p: PySide2.QtCore.QPointF): ...
    def moveTopRight(self, p: PySide2.QtCore.QPointF): ...
    def normalized(self) -> PySide2.QtCore.QRectF: ...
    def right(self) -> float: ...
    def setBottom(self, pos: float): ...
    def setBottomLeft(self, p: PySide2.QtCore.QPointF): ...
    def setBottomRight(self, p: PySide2.QtCore.QPointF): ...
    def setCoords(self, x1: float, y1: float, x2: float, y2: float): ...
    def setHeight(self, h: float): ...
    def setLeft(self, pos: float): ...
    def setRect(self, x: float, y: float, w: float, h: float): ...
    def setRight(self, pos: float): ...
    def setSize(self, s: PySide2.QtCore.QSizeF): ...
    def setTop(self, pos: float): ...
    def setTopLeft(self, p: PySide2.QtCore.QPointF): ...
    def setTopRight(self, p: PySide2.QtCore.QPointF): ...
    def setWidth(self, w: float): ...
    def setX(self, pos: float): ...
    def setY(self, pos: float): ...
    def size(self) -> PySide2.QtCore.QSizeF: ...
    def toAlignedRect(self) -> PySide2.QtCore.QRect: ...
    def toRect(self) -> PySide2.QtCore.QRect: ...
    def top(self) -> float: ...
    def topLeft(self) -> PySide2.QtCore.QPointF: ...
    def topRight(self) -> PySide2.QtCore.QPointF: ...
    @typing.overload
    def translate(self, dx: float, dy: float): ...
    @typing.overload
    def translate(self, p: PySide2.QtCore.QPointF): ...
    @typing.overload
    def translated(self, dx: float, dy: float) -> PySide2.QtCore.QRectF: ...
    @typing.overload
    def translated(self, p: PySide2.QtCore.QPointF) -> PySide2.QtCore.QRectF: ...
    def transposed(self) -> PySide2.QtCore.QRectF: ...
    def united(self, other: PySide2.QtCore.QRectF) -> PySide2.QtCore.QRectF: ...
    def width(self) -> float: ...
    def x(self) -> float: ...
    def y(self) -> float: ...

class QRecursiveMutex(Shiboken.Object):
    def __init__(self): ...

class QRegExp(Shiboken.Object):
    CaretAtZero: QRegExp = ...  # 0x0
    RegExp: QRegExp = ...  # 0x0
    CaretAtOffset: QRegExp = ...  # 0x1
    Wildcard: QRegExp = ...  # 0x1
    CaretWontMatch: QRegExp = ...  # 0x2
    FixedString: QRegExp = ...  # 0x2
    RegExp2: QRegExp = ...  # 0x3
    WildcardUnix: QRegExp = ...  # 0x4
    W3CXmlSchema11: QRegExp = ...  # 0x5

    class CaretMode(object):
        CaretAtZero: QRegExp.CaretMode = ...  # 0x0
        CaretAtOffset: QRegExp.CaretMode = ...  # 0x1
        CaretWontMatch: QRegExp.CaretMode = ...  # 0x2

    class PatternSyntax(object):
        RegExp: QRegExp.PatternSyntax = ...  # 0x0
        Wildcard: QRegExp.PatternSyntax = ...  # 0x1
        FixedString: QRegExp.PatternSyntax = ...  # 0x2
        RegExp2: QRegExp.PatternSyntax = ...  # 0x3
        WildcardUnix: QRegExp.PatternSyntax = ...  # 0x4
        W3CXmlSchema11: QRegExp.PatternSyntax = ...  # 0x5
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self,
        pattern: str,
        cs: PySide2.QtCore.Qt.CaseSensitivity = ...,
        syntax: PySide2.QtCore.QRegExp.PatternSyntax = ...,
    ): ...
    @typing.overload
    def __init__(self, rx: PySide2.QtCore.QRegExp): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def cap(self, nth: int = ...) -> str: ...
    def captureCount(self) -> int: ...
    def capturedTexts(self) -> typing.List: ...
    def caseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity: ...
    def errorString(self) -> str: ...
    @staticmethod
    def escape(str: str) -> str: ...
    def exactMatch(self, str: str) -> bool: ...
    def indexIn(
        self,
        str: str,
        offset: int = ...,
        caretMode: PySide2.QtCore.QRegExp.CaretMode = ...,
    ) -> int: ...
    def isEmpty(self) -> bool: ...
    def isMinimal(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastIndexIn(
        self,
        str: str,
        offset: int = ...,
        caretMode: PySide2.QtCore.QRegExp.CaretMode = ...,
    ) -> int: ...
    def matchedLength(self) -> int: ...
    def pattern(self) -> str: ...
    def patternSyntax(self) -> PySide2.QtCore.QRegExp.PatternSyntax: ...
    def pos(self, nth: int = ...) -> int: ...
    def replace(self, sourceString: str, after: str) -> str: ...
    def setCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity): ...
    def setMinimal(self, minimal: bool): ...
    def setPattern(self, pattern: str): ...
    def setPatternSyntax(self, syntax: PySide2.QtCore.QRegExp.PatternSyntax): ...
    def swap(self, other: PySide2.QtCore.QRegExp): ...

class QRegularExpression(Shiboken.Object):
    NoMatchOption: QRegularExpression = ...  # 0x0
    NoPatternOption: QRegularExpression = ...  # 0x0
    NormalMatch: QRegularExpression = ...  # 0x0
    AnchoredMatchOption: QRegularExpression = ...  # 0x1
    CaseInsensitiveOption: QRegularExpression = ...  # 0x1
    PartialPreferCompleteMatch: QRegularExpression = ...  # 0x1
    DontCheckSubjectStringMatchOption: QRegularExpression = ...  # 0x2
    DotMatchesEverythingOption: QRegularExpression = ...  # 0x2
    PartialPreferFirstMatch: QRegularExpression = ...  # 0x2
    NoMatch: QRegularExpression = ...  # 0x3
    MultilineOption: QRegularExpression = ...  # 0x4
    ExtendedPatternSyntaxOption: QRegularExpression = ...  # 0x8
    InvertedGreedinessOption: QRegularExpression = ...  # 0x10
    DontCaptureOption: QRegularExpression = ...  # 0x20
    UseUnicodePropertiesOption: QRegularExpression = ...  # 0x40
    OptimizeOnFirstUsageOption: QRegularExpression = ...  # 0x80
    DontAutomaticallyOptimizeOption: QRegularExpression = ...  # 0x100

    class MatchOption(object):
        NoMatchOption: QRegularExpression.MatchOption = ...  # 0x0
        AnchoredMatchOption: QRegularExpression.MatchOption = ...  # 0x1
        DontCheckSubjectStringMatchOption: QRegularExpression.MatchOption = ...  # 0x2

    class MatchOptions(object): ...

    class MatchType(object):
        NormalMatch: QRegularExpression.MatchType = ...  # 0x0
        PartialPreferCompleteMatch: QRegularExpression.MatchType = ...  # 0x1
        PartialPreferFirstMatch: QRegularExpression.MatchType = ...  # 0x2
        NoMatch: QRegularExpression.MatchType = ...  # 0x3

    class PatternOption(object):
        NoPatternOption: QRegularExpression.PatternOption = ...  # 0x0
        CaseInsensitiveOption: QRegularExpression.PatternOption = ...  # 0x1
        DotMatchesEverythingOption: QRegularExpression.PatternOption = ...  # 0x2
        MultilineOption: QRegularExpression.PatternOption = ...  # 0x4
        ExtendedPatternSyntaxOption: QRegularExpression.PatternOption = ...  # 0x8
        InvertedGreedinessOption: QRegularExpression.PatternOption = ...  # 0x10
        DontCaptureOption: QRegularExpression.PatternOption = ...  # 0x20
        UseUnicodePropertiesOption: QRegularExpression.PatternOption = ...  # 0x40
        OptimizeOnFirstUsageOption: QRegularExpression.PatternOption = ...  # 0x80
        DontAutomaticallyOptimizeOption: QRegularExpression.PatternOption = ...  # 0x100

    class PatternOptions(object): ...

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self,
        pattern: str,
        options: PySide2.QtCore.QRegularExpression.PatternOptions = ...,
    ): ...
    @typing.overload
    def __init__(self, re: PySide2.QtCore.QRegularExpression): ...
    def __copy__(self): ...
    @staticmethod
    def anchoredPattern(expression: str) -> str: ...
    def captureCount(self) -> int: ...
    def errorString(self) -> str: ...
    @staticmethod
    def escape(str: str) -> str: ...
    @typing.overload
    def globalMatch(
        self,
        subject: str,
        offset: int = ...,
        matchType: PySide2.QtCore.QRegularExpression.MatchType = ...,
        matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = ...,
    ) -> PySide2.QtCore.QRegularExpressionMatchIterator: ...
    @typing.overload
    def globalMatch(
        self,
        subjectRef: str,
        offset: int = ...,
        matchType: PySide2.QtCore.QRegularExpression.MatchType = ...,
        matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = ...,
    ) -> PySide2.QtCore.QRegularExpressionMatchIterator: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def match(
        self,
        subject: str,
        offset: int = ...,
        matchType: PySide2.QtCore.QRegularExpression.MatchType = ...,
        matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = ...,
    ) -> PySide2.QtCore.QRegularExpressionMatch: ...
    @typing.overload
    def match(
        self,
        subjectRef: str,
        offset: int = ...,
        matchType: PySide2.QtCore.QRegularExpression.MatchType = ...,
        matchOptions: PySide2.QtCore.QRegularExpression.MatchOptions = ...,
    ) -> PySide2.QtCore.QRegularExpressionMatch: ...
    def namedCaptureGroups(self) -> typing.List: ...
    def optimize(self): ...
    def pattern(self) -> str: ...
    def patternErrorOffset(self) -> int: ...
    def patternOptions(self) -> PySide2.QtCore.QRegularExpression.PatternOptions: ...
    def setPattern(self, pattern: str): ...
    def setPatternOptions(
        self, options: PySide2.QtCore.QRegularExpression.PatternOptions
    ): ...
    def swap(self, other: PySide2.QtCore.QRegularExpression): ...
    @staticmethod
    def wildcardToRegularExpression(str: str) -> str: ...

class QRegularExpressionMatch(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, match: PySide2.QtCore.QRegularExpressionMatch): ...
    def __copy__(self): ...
    @typing.overload
    def captured(self, name: str) -> str: ...
    @typing.overload
    def captured(self, nth: int = ...) -> str: ...
    @typing.overload
    def capturedEnd(self, name: str) -> int: ...
    @typing.overload
    def capturedEnd(self, nth: int = ...) -> int: ...
    @typing.overload
    def capturedLength(self, name: str) -> int: ...
    @typing.overload
    def capturedLength(self, nth: int = ...) -> int: ...
    @typing.overload
    def capturedRef(self, name: str) -> str: ...
    @typing.overload
    def capturedRef(self, nth: int = ...) -> str: ...
    @typing.overload
    def capturedStart(self, name: str) -> int: ...
    @typing.overload
    def capturedStart(self, nth: int = ...) -> int: ...
    def capturedTexts(self) -> typing.List: ...
    def hasMatch(self) -> bool: ...
    def hasPartialMatch(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastCapturedIndex(self) -> int: ...
    def matchOptions(self) -> PySide2.QtCore.QRegularExpression.MatchOptions: ...
    def matchType(self) -> PySide2.QtCore.QRegularExpression.MatchType: ...
    def regularExpression(self) -> PySide2.QtCore.QRegularExpression: ...
    def swap(self, other: PySide2.QtCore.QRegularExpressionMatch): ...

class QRegularExpressionMatchIterator(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, iterator: PySide2.QtCore.QRegularExpressionMatchIterator): ...
    def __copy__(self): ...
    def hasNext(self) -> bool: ...
    def isValid(self) -> bool: ...
    def matchOptions(self) -> PySide2.QtCore.QRegularExpression.MatchOptions: ...
    def matchType(self) -> PySide2.QtCore.QRegularExpression.MatchType: ...
    def next(self) -> PySide2.QtCore.QRegularExpressionMatch: ...
    def peekNext(self) -> PySide2.QtCore.QRegularExpressionMatch: ...
    def regularExpression(self) -> PySide2.QtCore.QRegularExpression: ...
    def swap(self, other: PySide2.QtCore.QRegularExpressionMatchIterator): ...

class QResource(Shiboken.Object):
    NoCompression: QResource = ...  # 0x0
    ZlibCompression: QResource = ...  # 0x1
    ZstdCompression: QResource = ...  # 0x2

    class Compression(object):
        NoCompression: QResource.Compression = ...  # 0x0
        ZlibCompression: QResource.Compression = ...  # 0x1
        ZstdCompression: QResource.Compression = ...  # 0x2
    def __init__(self, file: str = ..., locale: PySide2.QtCore.QLocale = ...): ...
    def absoluteFilePath(self) -> str: ...
    @staticmethod
    def addSearchPath(path: str): ...
    def children(self) -> typing.List: ...
    def compressionAlgorithm(self) -> PySide2.QtCore.QResource.Compression: ...
    def data(self) -> bytes: ...
    def fileName(self) -> str: ...
    def isCompressed(self) -> bool: ...
    def isDir(self) -> bool: ...
    def isFile(self) -> bool: ...
    def isValid(self) -> bool: ...
    def lastModified(self) -> PySide2.QtCore.QDateTime: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    @staticmethod
    def registerResource(rccFilename: str, resourceRoot: str = ...) -> bool: ...
    @staticmethod
    def registerResourceData(rccData: bytes, resourceRoot: str = ...) -> bool: ...
    @staticmethod
    def searchPaths() -> typing.List: ...
    def setFileName(self, file: str): ...
    def setLocale(self, locale: PySide2.QtCore.QLocale): ...
    def size(self) -> int: ...
    def uncompressedData(self) -> PySide2.QtCore.QByteArray: ...
    def uncompressedSize(self) -> int: ...
    @staticmethod
    def unregisterResource(rccFilename: str, resourceRoot: str = ...) -> bool: ...
    @staticmethod
    def unregisterResourceData(rccData: bytes, resourceRoot: str = ...) -> bool: ...

class QRunnable(Shiboken.Object):
    def __init__(self): ...
    def autoDelete(self) -> bool: ...
    def run(self): ...
    def setAutoDelete(self, _autoDelete: bool): ...

class QSaveFile(PySide2.QtCore.QFileDevice):
    @typing.overload
    def __init__(self, name: str): ...
    @typing.overload
    def __init__(self, name: str, parent: PySide2.QtCore.QObject): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def cancelWriting(self): ...
    def close(self): ...
    def commit(self) -> bool: ...
    def directWriteFallback(self) -> bool: ...
    def fileName(self) -> str: ...
    def open(self, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool: ...
    def setDirectWriteFallback(self, enabled: bool): ...
    def setFileName(self, name: str): ...
    def writeData(self, data: bytes, len: int) -> int: ...

class QSemaphore(Shiboken.Object):
    def __init__(self, n: int = ...): ...
    def acquire(self, n: int = ...): ...
    def available(self) -> int: ...
    def release(self, n: int = ...): ...
    @typing.overload
    def tryAcquire(self, n: int, timeout: int) -> bool: ...
    @typing.overload
    def tryAcquire(self, n: int = ...) -> bool: ...

class QSemaphoreReleaser(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, sem: PySide2.QtCore.QSemaphore, n: int = ...): ...
    def cancel(self) -> PySide2.QtCore.QSemaphore: ...
    def semaphore(self) -> PySide2.QtCore.QSemaphore: ...
    def swap(self, other: PySide2.QtCore.QSemaphoreReleaser): ...

class QSequentialAnimationGroup(PySide2.QtCore.QAnimationGroup):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def addPause(self, msecs: int) -> PySide2.QtCore.QPauseAnimation: ...
    def currentAnimation(self) -> PySide2.QtCore.QAbstractAnimation: ...
    def duration(self) -> int: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def insertPause(self, index: int, msecs: int) -> PySide2.QtCore.QPauseAnimation: ...
    def updateCurrentTime(self, arg__1: int): ...
    def updateDirection(
        self, direction: PySide2.QtCore.QAbstractAnimation.Direction
    ): ...
    def updateState(
        self,
        newState: PySide2.QtCore.QAbstractAnimation.State,
        oldState: PySide2.QtCore.QAbstractAnimation.State,
    ): ...

class QSettings(PySide2.QtCore.QObject):
    NativeFormat: QSettings = ...  # 0x0
    NoError: QSettings = ...  # 0x0
    UserScope: QSettings = ...  # 0x0
    AccessError: QSettings = ...  # 0x1
    IniFormat: QSettings = ...  # 0x1
    SystemScope: QSettings = ...  # 0x1
    FormatError: QSettings = ...  # 0x2
    Registry32Format: QSettings = ...  # 0x2
    Registry64Format: QSettings = ...  # 0x3
    InvalidFormat: QSettings = ...  # 0x10
    CustomFormat1: QSettings = ...  # 0x11
    CustomFormat2: QSettings = ...  # 0x12
    CustomFormat3: QSettings = ...  # 0x13
    CustomFormat4: QSettings = ...  # 0x14
    CustomFormat5: QSettings = ...  # 0x15
    CustomFormat6: QSettings = ...  # 0x16
    CustomFormat7: QSettings = ...  # 0x17
    CustomFormat8: QSettings = ...  # 0x18
    CustomFormat9: QSettings = ...  # 0x19
    CustomFormat10: QSettings = ...  # 0x1a
    CustomFormat11: QSettings = ...  # 0x1b
    CustomFormat12: QSettings = ...  # 0x1c
    CustomFormat13: QSettings = ...  # 0x1d
    CustomFormat14: QSettings = ...  # 0x1e
    CustomFormat15: QSettings = ...  # 0x1f
    CustomFormat16: QSettings = ...  # 0x20

    class Format(object):
        NativeFormat: QSettings.Format = ...  # 0x0
        IniFormat: QSettings.Format = ...  # 0x1
        Registry32Format: QSettings.Format = ...  # 0x2
        Registry64Format: QSettings.Format = ...  # 0x3
        InvalidFormat: QSettings.Format = ...  # 0x10
        CustomFormat1: QSettings.Format = ...  # 0x11
        CustomFormat2: QSettings.Format = ...  # 0x12
        CustomFormat3: QSettings.Format = ...  # 0x13
        CustomFormat4: QSettings.Format = ...  # 0x14
        CustomFormat5: QSettings.Format = ...  # 0x15
        CustomFormat6: QSettings.Format = ...  # 0x16
        CustomFormat7: QSettings.Format = ...  # 0x17
        CustomFormat8: QSettings.Format = ...  # 0x18
        CustomFormat9: QSettings.Format = ...  # 0x19
        CustomFormat10: QSettings.Format = ...  # 0x1a
        CustomFormat11: QSettings.Format = ...  # 0x1b
        CustomFormat12: QSettings.Format = ...  # 0x1c
        CustomFormat13: QSettings.Format = ...  # 0x1d
        CustomFormat14: QSettings.Format = ...  # 0x1e
        CustomFormat15: QSettings.Format = ...  # 0x1f
        CustomFormat16: QSettings.Format = ...  # 0x20

    class Scope(object):
        UserScope: QSettings.Scope = ...  # 0x0
        SystemScope: QSettings.Scope = ...  # 0x1

    class Status(object):
        NoError: QSettings.Status = ...  # 0x0
        AccessError: QSettings.Status = ...  # 0x1
        FormatError: QSettings.Status = ...  # 0x2
    @typing.overload
    def __init__(
        self,
        fileName: str,
        format: PySide2.QtCore.QSettings.Format,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        format: PySide2.QtCore.QSettings.Format,
        scope: PySide2.QtCore.QSettings.Scope,
        organization: str,
        application: str = ...,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        organization: str,
        application: str = ...,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    @typing.overload
    def __init__(
        self,
        scope: PySide2.QtCore.QSettings.Scope,
        organization: str,
        application: str = ...,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        scope: PySide2.QtCore.QSettings.Scope,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    def allKeys(self) -> typing.List: ...
    def applicationName(self) -> str: ...
    def beginGroup(self, prefix: str): ...
    def beginReadArray(self, prefix: str) -> int: ...
    def beginWriteArray(self, prefix: str, size: int = ...): ...
    def childGroups(self) -> typing.List: ...
    def childKeys(self) -> typing.List: ...
    def clear(self): ...
    def contains(self, key: str) -> bool: ...
    @staticmethod
    def defaultFormat() -> PySide2.QtCore.QSettings.Format: ...
    def endArray(self): ...
    def endGroup(self): ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def fallbacksEnabled(self) -> bool: ...
    def fileName(self) -> str: ...
    def format(self) -> PySide2.QtCore.QSettings.Format: ...
    def group(self) -> str: ...
    def iniCodec(self) -> PySide2.QtCore.QTextCodec: ...
    def isAtomicSyncRequired(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def organizationName(self) -> str: ...
    def remove(self, key: str): ...
    def scope(self) -> PySide2.QtCore.QSettings.Scope: ...
    def setArrayIndex(self, i: int): ...
    def setAtomicSyncRequired(self, enable: bool): ...
    @staticmethod
    def setDefaultFormat(format: PySide2.QtCore.QSettings.Format): ...
    def setFallbacksEnabled(self, b: bool): ...
    @typing.overload
    def setIniCodec(self, codec: PySide2.QtCore.QTextCodec): ...
    @typing.overload
    def setIniCodec(self, codecName: bytes): ...
    @staticmethod
    def setPath(
        format: PySide2.QtCore.QSettings.Format,
        scope: PySide2.QtCore.QSettings.Scope,
        path: str,
    ): ...
    def setValue(self, key: str, value: typing.Any): ...
    def status(self) -> PySide2.QtCore.QSettings.Status: ...
    def sync(self): ...
    def value(
        self,
        arg__1: str,
        defaultValue: typing.Optional[typing.Any] = ...,
        type: object = ...,
    ) -> object: ...

class QSignalBlocker(Shiboken.Object):
    def __init__(self, o: PySide2.QtCore.QObject): ...
    def reblock(self): ...
    def unblock(self): ...

class QSignalMapper(PySide2.QtCore.QObject):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    @typing.overload
    def map(self): ...
    @typing.overload
    def map(self, sender: PySide2.QtCore.QObject): ...
    @typing.overload
    def mapping(self, id: int) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def mapping(self, object: PySide2.QtCore.QObject) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def mapping(self, text: str) -> PySide2.QtCore.QObject: ...
    def removeMappings(self, sender: PySide2.QtCore.QObject): ...
    @typing.overload
    def setMapping(self, sender: PySide2.QtCore.QObject, id: int): ...
    @typing.overload
    def setMapping(
        self, sender: PySide2.QtCore.QObject, object: PySide2.QtCore.QObject
    ): ...
    @typing.overload
    def setMapping(self, sender: PySide2.QtCore.QObject, text: str): ...

class QSignalTransition(PySide2.QtCore.QAbstractTransition):
    @typing.overload
    def __init__(
        self, arg__1: object, arg__2: typing.Optional[PySide2.QtCore.QState] = ...
    ) -> PySide2.QtCore.QSignalTransition: ...
    @typing.overload
    def __init__(
        self,
        sender: PySide2.QtCore.QObject,
        signal: bytes,
        sourceState: typing.Optional[PySide2.QtCore.QState] = ...,
    ): ...
    @typing.overload
    def __init__(self, sourceState: typing.Optional[PySide2.QtCore.QState] = ...): ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def eventTest(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def onTransition(self, event: PySide2.QtCore.QEvent): ...
    def senderObject(self) -> PySide2.QtCore.QObject: ...
    def setSenderObject(self, sender: PySide2.QtCore.QObject): ...
    def setSignal(self, signal: PySide2.QtCore.QByteArray): ...
    def signal(self) -> PySide2.QtCore.QByteArray: ...

class QSize(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QSize: PySide2.QtCore.QSize): ...
    @typing.overload
    def __init__(self, w: int, h: int): ...
    def __add__(self, s2: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize: ...
    def __copy__(self): ...
    def __iadd__(self, arg__1: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize: ...
    def __imul__(self, c: float) -> PySide2.QtCore.QSize: ...
    def __isub__(self, arg__1: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize: ...
    def __mul__(self, c: float) -> PySide2.QtCore.QSize: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, s2: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize: ...
    def boundedTo(self, arg__1: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize: ...
    def expandedTo(self, arg__1: PySide2.QtCore.QSize) -> PySide2.QtCore.QSize: ...
    def grownBy(self, m: PySide2.QtCore.QMargins) -> PySide2.QtCore.QSize: ...
    def height(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def scale(
        self, s: PySide2.QtCore.QSize, mode: PySide2.QtCore.Qt.AspectRatioMode
    ): ...
    @typing.overload
    def scale(self, w: int, h: int, mode: PySide2.QtCore.Qt.AspectRatioMode): ...
    @typing.overload
    def scaled(
        self, s: PySide2.QtCore.QSize, mode: PySide2.QtCore.Qt.AspectRatioMode
    ) -> PySide2.QtCore.QSize: ...
    @typing.overload
    def scaled(
        self, w: int, h: int, mode: PySide2.QtCore.Qt.AspectRatioMode
    ) -> PySide2.QtCore.QSize: ...
    def setHeight(self, h: int): ...
    def setWidth(self, w: int): ...
    def shrunkBy(self, m: PySide2.QtCore.QMargins) -> PySide2.QtCore.QSize: ...
    def toTuple(self) -> object: ...
    def transpose(self): ...
    def transposed(self) -> PySide2.QtCore.QSize: ...
    def width(self) -> int: ...

class QSizeF(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QSizeF: PySide2.QtCore.QSizeF): ...
    @typing.overload
    def __init__(self, sz: PySide2.QtCore.QSize): ...
    @typing.overload
    def __init__(self, w: float, h: float): ...
    def __add__(self, s2: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QSizeF: ...
    def __copy__(self): ...
    def __iadd__(self, arg__1: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QSizeF: ...
    def __imul__(self, c: float) -> PySide2.QtCore.QSizeF: ...
    def __isub__(self, arg__1: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QSizeF: ...
    def __mul__(self, c: float) -> PySide2.QtCore.QSizeF: ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def __sub__(self, s2: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QSizeF: ...
    def boundedTo(self, arg__1: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QSizeF: ...
    def expandedTo(self, arg__1: PySide2.QtCore.QSizeF) -> PySide2.QtCore.QSizeF: ...
    def grownBy(self, m: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QSizeF: ...
    def height(self) -> float: ...
    def isEmpty(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def scale(
        self, s: PySide2.QtCore.QSizeF, mode: PySide2.QtCore.Qt.AspectRatioMode
    ): ...
    @typing.overload
    def scale(self, w: float, h: float, mode: PySide2.QtCore.Qt.AspectRatioMode): ...
    @typing.overload
    def scaled(
        self, s: PySide2.QtCore.QSizeF, mode: PySide2.QtCore.Qt.AspectRatioMode
    ) -> PySide2.QtCore.QSizeF: ...
    @typing.overload
    def scaled(
        self, w: float, h: float, mode: PySide2.QtCore.Qt.AspectRatioMode
    ) -> PySide2.QtCore.QSizeF: ...
    def setHeight(self, h: float): ...
    def setWidth(self, w: float): ...
    def shrunkBy(self, m: PySide2.QtCore.QMarginsF) -> PySide2.QtCore.QSizeF: ...
    def toSize(self) -> PySide2.QtCore.QSize: ...
    def toTuple(self) -> object: ...
    def transpose(self): ...
    def transposed(self) -> PySide2.QtCore.QSizeF: ...
    def width(self) -> float: ...

class QSocketNotifier(PySide2.QtCore.QObject):
    Read: QSocketNotifier = ...  # 0x0
    Write: QSocketNotifier = ...  # 0x1
    Exception: QSocketNotifier = ...  # 0x2

    class Type(object):
        Read: QSocketNotifier.Type = ...  # 0x0
        Write: QSocketNotifier.Type = ...  # 0x1
        Exception: QSocketNotifier.Type = ...  # 0x2
    @typing.overload
    def __init__(
        self,
        arg__1: object,
        arg__2: PySide2.QtCore.QSocketNotifier.Type,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        socket: int,
        arg__2: PySide2.QtCore.QSocketNotifier.Type,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    def event(self, arg__1: PySide2.QtCore.QEvent) -> bool: ...
    def isEnabled(self) -> bool: ...
    def setEnabled(self, arg__1: bool): ...
    def socket(self) -> int: ...
    def type(self) -> PySide2.QtCore.QSocketNotifier.Type: ...

class QSortFilterProxyModel(PySide2.QtCore.QAbstractProxyModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def buddy(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def canFetchMore(self, parent: PySide2.QtCore.QModelIndex) -> bool: ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def data(
        self, index: PySide2.QtCore.QModelIndex, role: int = ...
    ) -> typing.Any: ...
    def dropMimeData(
        self,
        data: PySide2.QtCore.QMimeData,
        action: PySide2.QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def dynamicSortFilter(self) -> bool: ...
    def fetchMore(self, parent: PySide2.QtCore.QModelIndex): ...
    def filterAcceptsColumn(
        self, source_column: int, source_parent: PySide2.QtCore.QModelIndex
    ) -> bool: ...
    def filterAcceptsRow(
        self, source_row: int, source_parent: PySide2.QtCore.QModelIndex
    ) -> bool: ...
    def filterCaseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity: ...
    def filterKeyColumn(self) -> int: ...
    def filterRegExp(self) -> PySide2.QtCore.QRegExp: ...
    def filterRegularExpression(self) -> PySide2.QtCore.QRegularExpression: ...
    def filterRole(self) -> int: ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent: PySide2.QtCore.QModelIndex = ...) -> bool: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...
    ) -> typing.Any: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    def insertColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def insertRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def invalidate(self): ...
    def invalidateFilter(self): ...
    def isRecursiveFilteringEnabled(self) -> bool: ...
    def isSortLocaleAware(self) -> bool: ...
    def lessThan(
        self,
        source_left: PySide2.QtCore.QModelIndex,
        source_right: PySide2.QtCore.QModelIndex,
    ) -> bool: ...
    def mapFromSource(
        self, sourceIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mapSelectionFromSource(
        self, sourceSelection: PySide2.QtCore.QItemSelection
    ) -> PySide2.QtCore.QItemSelection: ...
    def mapSelectionToSource(
        self, proxySelection: PySide2.QtCore.QItemSelection
    ) -> PySide2.QtCore.QItemSelection: ...
    def mapToSource(
        self, proxyIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def match(
        self,
        start: PySide2.QtCore.QModelIndex,
        role: int,
        value: typing.Any,
        hits: int = ...,
        flags: PySide2.QtCore.Qt.MatchFlags = ...,
    ) -> typing.List: ...
    def mimeData(self, indexes: typing.List) -> PySide2.QtCore.QMimeData: ...
    def mimeTypes(self) -> typing.List: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, child: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def removeColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def removeRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def setData(
        self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...
    ) -> bool: ...
    def setDynamicSortFilter(self, enable: bool): ...
    def setFilterCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity): ...
    def setFilterFixedString(self, pattern: str): ...
    def setFilterKeyColumn(self, column: int): ...
    @typing.overload
    def setFilterRegExp(self, pattern: str): ...
    @typing.overload
    def setFilterRegExp(self, regExp: PySide2.QtCore.QRegExp): ...
    @typing.overload
    def setFilterRegularExpression(self, pattern: str): ...
    @typing.overload
    def setFilterRegularExpression(
        self, regularExpression: PySide2.QtCore.QRegularExpression
    ): ...
    def setFilterRole(self, role: int): ...
    def setFilterWildcard(self, pattern: str): ...
    def setHeaderData(
        self,
        section: int,
        orientation: PySide2.QtCore.Qt.Orientation,
        value: typing.Any,
        role: int = ...,
    ) -> bool: ...
    def setRecursiveFilteringEnabled(self, recursive: bool): ...
    def setSortCaseSensitivity(self, cs: PySide2.QtCore.Qt.CaseSensitivity): ...
    def setSortLocaleAware(self, on: bool): ...
    def setSortRole(self, role: int): ...
    def setSourceModel(self, sourceModel: PySide2.QtCore.QAbstractItemModel): ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = ...): ...
    def sortCaseSensitivity(self) -> PySide2.QtCore.Qt.CaseSensitivity: ...
    def sortColumn(self) -> int: ...
    def sortOrder(self) -> PySide2.QtCore.Qt.SortOrder: ...
    def sortRole(self) -> int: ...
    def span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize: ...
    def supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions: ...

class QStandardPaths(Shiboken.Object):
    DesktopLocation: QStandardPaths = ...  # 0x0
    LocateFile: QStandardPaths = ...  # 0x0
    DocumentsLocation: QStandardPaths = ...  # 0x1
    LocateDirectory: QStandardPaths = ...  # 0x1
    FontsLocation: QStandardPaths = ...  # 0x2
    ApplicationsLocation: QStandardPaths = ...  # 0x3
    MusicLocation: QStandardPaths = ...  # 0x4
    MoviesLocation: QStandardPaths = ...  # 0x5
    PicturesLocation: QStandardPaths = ...  # 0x6
    TempLocation: QStandardPaths = ...  # 0x7
    HomeLocation: QStandardPaths = ...  # 0x8
    AppLocalDataLocation: QStandardPaths = ...  # 0x9
    DataLocation: QStandardPaths = ...  # 0x9
    CacheLocation: QStandardPaths = ...  # 0xa
    GenericDataLocation: QStandardPaths = ...  # 0xb
    RuntimeLocation: QStandardPaths = ...  # 0xc
    ConfigLocation: QStandardPaths = ...  # 0xd
    DownloadLocation: QStandardPaths = ...  # 0xe
    GenericCacheLocation: QStandardPaths = ...  # 0xf
    GenericConfigLocation: QStandardPaths = ...  # 0x10
    AppDataLocation: QStandardPaths = ...  # 0x11
    AppConfigLocation: QStandardPaths = ...  # 0x12

    class LocateOption(object):
        LocateFile: QStandardPaths.LocateOption = ...  # 0x0
        LocateDirectory: QStandardPaths.LocateOption = ...  # 0x1

    class LocateOptions(object): ...

    class StandardLocation(object):
        DesktopLocation: QStandardPaths.StandardLocation = ...  # 0x0
        DocumentsLocation: QStandardPaths.StandardLocation = ...  # 0x1
        FontsLocation: QStandardPaths.StandardLocation = ...  # 0x2
        ApplicationsLocation: QStandardPaths.StandardLocation = ...  # 0x3
        MusicLocation: QStandardPaths.StandardLocation = ...  # 0x4
        MoviesLocation: QStandardPaths.StandardLocation = ...  # 0x5
        PicturesLocation: QStandardPaths.StandardLocation = ...  # 0x6
        TempLocation: QStandardPaths.StandardLocation = ...  # 0x7
        HomeLocation: QStandardPaths.StandardLocation = ...  # 0x8
        AppLocalDataLocation: QStandardPaths.StandardLocation = ...  # 0x9
        DataLocation: QStandardPaths.StandardLocation = ...  # 0x9
        CacheLocation: QStandardPaths.StandardLocation = ...  # 0xa
        GenericDataLocation: QStandardPaths.StandardLocation = ...  # 0xb
        RuntimeLocation: QStandardPaths.StandardLocation = ...  # 0xc
        ConfigLocation: QStandardPaths.StandardLocation = ...  # 0xd
        DownloadLocation: QStandardPaths.StandardLocation = ...  # 0xe
        GenericCacheLocation: QStandardPaths.StandardLocation = ...  # 0xf
        GenericConfigLocation: QStandardPaths.StandardLocation = ...  # 0x10
        AppDataLocation: QStandardPaths.StandardLocation = ...  # 0x11
        AppConfigLocation: QStandardPaths.StandardLocation = ...  # 0x12
    @staticmethod
    def displayName(type: PySide2.QtCore.QStandardPaths.StandardLocation) -> str: ...
    @staticmethod
    def enableTestMode(testMode: bool): ...
    @staticmethod
    def findExecutable(executableName: str, paths: typing.Sequence = ...) -> str: ...
    @staticmethod
    def isTestModeEnabled() -> bool: ...
    @staticmethod
    def locate(
        type: PySide2.QtCore.QStandardPaths.StandardLocation,
        fileName: str,
        options: PySide2.QtCore.QStandardPaths.LocateOptions = ...,
    ) -> str: ...
    @staticmethod
    def locateAll(
        type: PySide2.QtCore.QStandardPaths.StandardLocation,
        fileName: str,
        options: PySide2.QtCore.QStandardPaths.LocateOptions = ...,
    ) -> typing.List: ...
    @staticmethod
    def setTestModeEnabled(testMode: bool): ...
    @staticmethod
    def standardLocations(
        type: PySide2.QtCore.QStandardPaths.StandardLocation,
    ) -> typing.List: ...
    @staticmethod
    def writableLocation(
        type: PySide2.QtCore.QStandardPaths.StandardLocation,
    ) -> str: ...

class QState(PySide2.QtCore.QAbstractState):
    DontRestoreProperties: QState = ...  # 0x0
    ExclusiveStates: QState = ...  # 0x0
    ParallelStates: QState = ...  # 0x1
    RestoreProperties: QState = ...  # 0x1

    class ChildMode(object):
        ExclusiveStates: QState.ChildMode = ...  # 0x0
        ParallelStates: QState.ChildMode = ...  # 0x1

    class RestorePolicy(object):
        DontRestoreProperties: QState.RestorePolicy = ...  # 0x0
        RestoreProperties: QState.RestorePolicy = ...  # 0x1
    @typing.overload
    def __init__(
        self,
        childMode: PySide2.QtCore.QState.ChildMode,
        parent: typing.Optional[PySide2.QtCore.QState] = ...,
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QState] = ...): ...
    @typing.overload
    def addTransition(
        self, arg__1: object, arg__2: PySide2.QtCore.QAbstractState
    ) -> PySide2.QtCore.QSignalTransition: ...
    @typing.overload
    def addTransition(
        self,
        sender: PySide2.QtCore.QObject,
        signal: bytes,
        target: PySide2.QtCore.QAbstractState,
    ) -> PySide2.QtCore.QSignalTransition: ...
    @typing.overload
    def addTransition(
        self, target: PySide2.QtCore.QAbstractState
    ) -> PySide2.QtCore.QAbstractTransition: ...
    @typing.overload
    def addTransition(self, transition: PySide2.QtCore.QAbstractTransition): ...
    def assignProperty(
        self, object: PySide2.QtCore.QObject, name: bytes, value: typing.Any
    ): ...
    def childMode(self) -> PySide2.QtCore.QState.ChildMode: ...
    def errorState(self) -> PySide2.QtCore.QAbstractState: ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def initialState(self) -> PySide2.QtCore.QAbstractState: ...
    def onEntry(self, event: PySide2.QtCore.QEvent): ...
    def onExit(self, event: PySide2.QtCore.QEvent): ...
    def removeTransition(self, transition: PySide2.QtCore.QAbstractTransition): ...
    def setChildMode(self, mode: PySide2.QtCore.QState.ChildMode): ...
    def setErrorState(self, state: PySide2.QtCore.QAbstractState): ...
    def setInitialState(self, state: PySide2.QtCore.QAbstractState): ...
    def transitions(self) -> typing.List: ...

class QStateMachine(PySide2.QtCore.QState):
    NoError: QStateMachine = ...  # 0x0
    NormalPriority: QStateMachine = ...  # 0x0
    HighPriority: QStateMachine = ...  # 0x1
    NoInitialStateError: QStateMachine = ...  # 0x1
    NoDefaultStateInHistoryStateError: QStateMachine = ...  # 0x2
    NoCommonAncestorForTransitionError: QStateMachine = ...  # 0x3
    StateMachineChildModeSetToParallelError: QStateMachine = ...  # 0x4

    class Error(object):
        NoError: QStateMachine.Error = ...  # 0x0
        NoInitialStateError: QStateMachine.Error = ...  # 0x1
        NoDefaultStateInHistoryStateError: QStateMachine.Error = ...  # 0x2
        NoCommonAncestorForTransitionError: QStateMachine.Error = ...  # 0x3
        StateMachineChildModeSetToParallelError: QStateMachine.Error = ...  # 0x4

    class EventPriority(object):
        NormalPriority: QStateMachine.EventPriority = ...  # 0x0
        HighPriority: QStateMachine.EventPriority = ...  # 0x1

    class SignalEvent(PySide2.QtCore.QEvent):
        @typing.overload
        def __init__(self, SignalEvent: PySide2.QtCore.QStateMachine.SignalEvent): ...
        @typing.overload
        def __init__(
            self,
            sender: PySide2.QtCore.QObject,
            signalIndex: int,
            arguments: typing.Sequence,
        ): ...
        def __copy__(self): ...
        def arguments(self) -> typing.List: ...
        def sender(self) -> PySide2.QtCore.QObject: ...
        def signalIndex(self) -> int: ...

    class WrappedEvent(PySide2.QtCore.QEvent):
        @typing.overload
        def __init__(self, WrappedEvent: PySide2.QtCore.QStateMachine.WrappedEvent): ...
        @typing.overload
        def __init__(
            self, object: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent
        ): ...
        def __copy__(self): ...
        def event(self) -> PySide2.QtCore.QEvent: ...
        def object(self) -> PySide2.QtCore.QObject: ...

    @typing.overload
    def __init__(
        self,
        childMode: PySide2.QtCore.QState.ChildMode,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def addDefaultAnimation(self, animation: PySide2.QtCore.QAbstractAnimation): ...
    def addState(self, state: PySide2.QtCore.QAbstractState): ...
    def beginMicrostep(self, event: PySide2.QtCore.QEvent): ...
    def beginSelectTransitions(self, event: PySide2.QtCore.QEvent): ...
    def cancelDelayedEvent(self, id: int) -> bool: ...
    def clearError(self): ...
    @typing.overload
    def configuration(self) -> typing.Set: ...
    @typing.overload
    def configuration(self) -> typing.List: ...
    def defaultAnimations(self) -> typing.List: ...
    def endMicrostep(self, event: PySide2.QtCore.QEvent): ...
    def endSelectTransitions(self, event: PySide2.QtCore.QEvent): ...
    def error(self) -> PySide2.QtCore.QStateMachine.Error: ...
    def errorString(self) -> str: ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def eventFilter(
        self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent
    ) -> bool: ...
    def globalRestorePolicy(self) -> PySide2.QtCore.QState.RestorePolicy: ...
    def isAnimated(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def onEntry(self, event: PySide2.QtCore.QEvent): ...
    def onExit(self, event: PySide2.QtCore.QEvent): ...
    def postDelayedEvent(self, event: PySide2.QtCore.QEvent, delay: int) -> int: ...
    def postEvent(
        self,
        event: PySide2.QtCore.QEvent,
        priority: PySide2.QtCore.QStateMachine.EventPriority = ...,
    ): ...
    def removeDefaultAnimation(self, animation: PySide2.QtCore.QAbstractAnimation): ...
    def removeState(self, state: PySide2.QtCore.QAbstractState): ...
    def setAnimated(self, enabled: bool): ...
    def setGlobalRestorePolicy(
        self, restorePolicy: PySide2.QtCore.QState.RestorePolicy
    ): ...
    def setRunning(self, running: bool): ...
    def start(self): ...
    def stop(self): ...

class QStorageInfo(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, dir: PySide2.QtCore.QDir): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QStorageInfo): ...
    @typing.overload
    def __init__(self, path: str): ...
    def __copy__(self): ...
    def blockSize(self) -> int: ...
    def bytesAvailable(self) -> int: ...
    def bytesFree(self) -> int: ...
    def bytesTotal(self) -> int: ...
    def device(self) -> PySide2.QtCore.QByteArray: ...
    def displayName(self) -> str: ...
    def fileSystemType(self) -> PySide2.QtCore.QByteArray: ...
    def isReadOnly(self) -> bool: ...
    def isReady(self) -> bool: ...
    def isRoot(self) -> bool: ...
    def isValid(self) -> bool: ...
    @staticmethod
    def mountedVolumes() -> typing.List: ...
    def name(self) -> str: ...
    def refresh(self): ...
    @staticmethod
    def root() -> PySide2.QtCore.QStorageInfo: ...
    def rootPath(self) -> str: ...
    def setPath(self, path: str): ...
    def subvolume(self) -> PySide2.QtCore.QByteArray: ...
    def swap(self, other: PySide2.QtCore.QStorageInfo): ...

class QStringListModel(PySide2.QtCore.QAbstractListModel):
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    @typing.overload
    def __init__(
        self,
        strings: typing.Sequence,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ): ...
    def data(
        self, index: PySide2.QtCore.QModelIndex, role: int = ...
    ) -> typing.Any: ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def insertRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict: ...
    def moveRows(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceRow: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    def removeRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def setData(
        self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...
    ) -> bool: ...
    def setItemData(
        self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict
    ) -> bool: ...
    def setStringList(self, strings: typing.Sequence): ...
    def sibling(
        self, row: int, column: int, idx: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = ...): ...
    def stringList(self) -> typing.List: ...
    def supportedDropActions(self) -> PySide2.QtCore.Qt.DropActions: ...

class QSysInfo(Shiboken.Object):
    BigEndian: QSysInfo = ...  # 0x0
    WV_None: QSysInfo = ...  # 0x0
    ByteOrder: QSysInfo = ...  # 0x1
    LittleEndian: QSysInfo = ...  # 0x1
    WV_32s: QSysInfo = ...  # 0x1
    WV_95: QSysInfo = ...  # 0x2
    WV_98: QSysInfo = ...  # 0x3
    WV_Me: QSysInfo = ...  # 0x4
    WV_DOS_based: QSysInfo = ...  # 0xf
    WV_4_0: QSysInfo = ...  # 0x10
    WV_NT: QSysInfo = ...  # 0x10
    WV_2000: QSysInfo = ...  # 0x20
    WV_5_0: QSysInfo = ...  # 0x20
    WV_5_1: QSysInfo = ...  # 0x30
    WV_XP: QSysInfo = ...  # 0x30
    WV_2003: QSysInfo = ...  # 0x40
    WV_5_2: QSysInfo = ...  # 0x40
    WordSize: QSysInfo = ...  # 0x40
    WV_6_0: QSysInfo = ...  # 0x80
    WV_VISTA: QSysInfo = ...  # 0x80
    WV_6_1: QSysInfo = ...  # 0x90
    WV_WINDOWS7: QSysInfo = ...  # 0x90
    WV_6_2: QSysInfo = ...  # 0xa0
    WV_WINDOWS8: QSysInfo = ...  # 0xa0
    WV_6_3: QSysInfo = ...  # 0xb0
    WV_WINDOWS8_1: QSysInfo = ...  # 0xb0
    WV_10_0: QSysInfo = ...  # 0xc0
    WV_WINDOWS10: QSysInfo = ...  # 0xc0
    WindowsVersion: QSysInfo = ...  # 0xc0
    WV_NT_based: QSysInfo = ...  # 0xf0
    WV_CE: QSysInfo = ...  # 0x100
    WV_CENET: QSysInfo = ...  # 0x200
    WV_CE_5: QSysInfo = ...  # 0x300
    WV_CE_6: QSysInfo = ...  # 0x400
    WV_CE_based: QSysInfo = ...  # 0xf00

    class Endian(object):
        BigEndian: QSysInfo.Endian = ...  # 0x0
        ByteOrder: QSysInfo.Endian = ...  # 0x1
        LittleEndian: QSysInfo.Endian = ...  # 0x1

    class Sizes(object):
        WordSize: QSysInfo.Sizes = ...  # 0x40

    class WinVersion(object):
        WV_None: QSysInfo.WinVersion = ...  # 0x0
        WV_32s: QSysInfo.WinVersion = ...  # 0x1
        WV_95: QSysInfo.WinVersion = ...  # 0x2
        WV_98: QSysInfo.WinVersion = ...  # 0x3
        WV_Me: QSysInfo.WinVersion = ...  # 0x4
        WV_DOS_based: QSysInfo.WinVersion = ...  # 0xf
        WV_4_0: QSysInfo.WinVersion = ...  # 0x10
        WV_NT: QSysInfo.WinVersion = ...  # 0x10
        WV_2000: QSysInfo.WinVersion = ...  # 0x20
        WV_5_0: QSysInfo.WinVersion = ...  # 0x20
        WV_5_1: QSysInfo.WinVersion = ...  # 0x30
        WV_XP: QSysInfo.WinVersion = ...  # 0x30
        WV_2003: QSysInfo.WinVersion = ...  # 0x40
        WV_5_2: QSysInfo.WinVersion = ...  # 0x40
        WV_6_0: QSysInfo.WinVersion = ...  # 0x80
        WV_VISTA: QSysInfo.WinVersion = ...  # 0x80
        WV_6_1: QSysInfo.WinVersion = ...  # 0x90
        WV_WINDOWS7: QSysInfo.WinVersion = ...  # 0x90
        WV_6_2: QSysInfo.WinVersion = ...  # 0xa0
        WV_WINDOWS8: QSysInfo.WinVersion = ...  # 0xa0
        WV_6_3: QSysInfo.WinVersion = ...  # 0xb0
        WV_WINDOWS8_1: QSysInfo.WinVersion = ...  # 0xb0
        WV_10_0: QSysInfo.WinVersion = ...  # 0xc0
        WV_WINDOWS10: QSysInfo.WinVersion = ...  # 0xc0
        WV_NT_based: QSysInfo.WinVersion = ...  # 0xf0
        WV_CE: QSysInfo.WinVersion = ...  # 0x100
        WV_CENET: QSysInfo.WinVersion = ...  # 0x200
        WV_CE_5: QSysInfo.WinVersion = ...  # 0x300
        WV_CE_6: QSysInfo.WinVersion = ...  # 0x400
        WV_CE_based: QSysInfo.WinVersion = ...  # 0xf00
    def __init__(self): ...
    @staticmethod
    def bootUniqueId() -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def buildAbi() -> str: ...
    @staticmethod
    def buildCpuArchitecture() -> str: ...
    @staticmethod
    def currentCpuArchitecture() -> str: ...
    @staticmethod
    def kernelType() -> str: ...
    @staticmethod
    def kernelVersion() -> str: ...
    @staticmethod
    def machineHostName() -> str: ...
    @staticmethod
    def machineUniqueId() -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def prettyProductName() -> str: ...
    @staticmethod
    def productType() -> str: ...
    @staticmethod
    def productVersion() -> str: ...
    @staticmethod
    def windowsVersion() -> PySide2.QtCore.QSysInfo.WinVersion: ...

class QSystemSemaphore(Shiboken.Object):
    NoError: QSystemSemaphore = ...  # 0x0
    Open: QSystemSemaphore = ...  # 0x0
    Create: QSystemSemaphore = ...  # 0x1
    PermissionDenied: QSystemSemaphore = ...  # 0x1
    KeyError: QSystemSemaphore = ...  # 0x2
    AlreadyExists: QSystemSemaphore = ...  # 0x3
    NotFound: QSystemSemaphore = ...  # 0x4
    OutOfResources: QSystemSemaphore = ...  # 0x5
    UnknownError: QSystemSemaphore = ...  # 0x6

    class AccessMode(object):
        Open: QSystemSemaphore.AccessMode = ...  # 0x0
        Create: QSystemSemaphore.AccessMode = ...  # 0x1

    class SystemSemaphoreError(object):
        NoError: QSystemSemaphore.SystemSemaphoreError = ...  # 0x0
        PermissionDenied: QSystemSemaphore.SystemSemaphoreError = ...  # 0x1
        KeyError: QSystemSemaphore.SystemSemaphoreError = ...  # 0x2
        AlreadyExists: QSystemSemaphore.SystemSemaphoreError = ...  # 0x3
        NotFound: QSystemSemaphore.SystemSemaphoreError = ...  # 0x4
        OutOfResources: QSystemSemaphore.SystemSemaphoreError = ...  # 0x5
        UnknownError: QSystemSemaphore.SystemSemaphoreError = ...  # 0x6
    def __init__(
        self,
        key: str,
        initialValue: int = ...,
        mode: PySide2.QtCore.QSystemSemaphore.AccessMode = ...,
    ): ...
    def acquire(self) -> bool: ...
    def error(self) -> PySide2.QtCore.QSystemSemaphore.SystemSemaphoreError: ...
    def errorString(self) -> str: ...
    def key(self) -> str: ...
    def release(self, n: int = ...) -> bool: ...
    def setKey(
        self,
        key: str,
        initialValue: int = ...,
        mode: PySide2.QtCore.QSystemSemaphore.AccessMode = ...,
    ): ...

class QTemporaryDir(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, templateName: str): ...
    def autoRemove(self) -> bool: ...
    def errorString(self) -> str: ...
    def filePath(self, fileName: str) -> str: ...
    def isValid(self) -> bool: ...
    def path(self) -> str: ...
    def remove(self) -> bool: ...
    def setAutoRemove(self, b: bool): ...

class QTemporaryFile(PySide2.QtCore.QFile):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parent: PySide2.QtCore.QObject): ...
    @typing.overload
    def __init__(self, templateName: str): ...
    @typing.overload
    def __init__(self, templateName: str, parent: PySide2.QtCore.QObject): ...
    def autoRemove(self) -> bool: ...
    @typing.overload
    @staticmethod
    def createLocalFile(
        file: PySide2.QtCore.QFile,
    ) -> PySide2.QtCore.QTemporaryFile: ...
    @typing.overload
    @staticmethod
    def createLocalFile(fileName: str) -> PySide2.QtCore.QTemporaryFile: ...
    @typing.overload
    @staticmethod
    def createNativeFile(
        file: PySide2.QtCore.QFile,
    ) -> PySide2.QtCore.QTemporaryFile: ...
    @typing.overload
    @staticmethod
    def createNativeFile(fileName: str) -> PySide2.QtCore.QTemporaryFile: ...
    def fileName(self) -> str: ...
    def fileTemplate(self) -> str: ...
    @typing.overload
    def open(self) -> bool: ...
    @typing.overload
    def open(self, flags: PySide2.QtCore.QIODevice.OpenMode) -> bool: ...
    def rename(self, newName: str) -> bool: ...
    def setAutoRemove(self, b: bool): ...
    def setFileTemplate(self, name: str): ...

class QTextBoundaryFinder(Shiboken.Object):
    Grapheme: QTextBoundaryFinder = ...  # 0x0
    NotAtBoundary: QTextBoundaryFinder = ...  # 0x0
    Word: QTextBoundaryFinder = ...  # 0x1
    Sentence: QTextBoundaryFinder = ...  # 0x2
    Line: QTextBoundaryFinder = ...  # 0x3
    BreakOpportunity: QTextBoundaryFinder = ...  # 0x1f
    StartOfItem: QTextBoundaryFinder = ...  # 0x20
    EndOfItem: QTextBoundaryFinder = ...  # 0x40
    MandatoryBreak: QTextBoundaryFinder = ...  # 0x80
    SoftHyphen: QTextBoundaryFinder = ...  # 0x100

    class BoundaryReason(object):
        NotAtBoundary: QTextBoundaryFinder.BoundaryReason = ...  # 0x0
        BreakOpportunity: QTextBoundaryFinder.BoundaryReason = ...  # 0x1f
        StartOfItem: QTextBoundaryFinder.BoundaryReason = ...  # 0x20
        EndOfItem: QTextBoundaryFinder.BoundaryReason = ...  # 0x40
        MandatoryBreak: QTextBoundaryFinder.BoundaryReason = ...  # 0x80
        SoftHyphen: QTextBoundaryFinder.BoundaryReason = ...  # 0x100

    class BoundaryReasons(object): ...

    class BoundaryType(object):
        Grapheme: QTextBoundaryFinder.BoundaryType = ...  # 0x0
        Word: QTextBoundaryFinder.BoundaryType = ...  # 0x1
        Sentence: QTextBoundaryFinder.BoundaryType = ...  # 0x2
        Line: QTextBoundaryFinder.BoundaryType = ...  # 0x3
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QTextBoundaryFinder): ...
    @typing.overload
    def __init__(
        self, type: PySide2.QtCore.QTextBoundaryFinder.BoundaryType, string: str
    ): ...
    def __copy__(self): ...
    def boundaryReasons(self) -> PySide2.QtCore.QTextBoundaryFinder.BoundaryReasons: ...
    def isAtBoundary(self) -> bool: ...
    def isValid(self) -> bool: ...
    def position(self) -> int: ...
    def setPosition(self, position: int): ...
    def string(self) -> str: ...
    def toEnd(self): ...
    def toNextBoundary(self) -> int: ...
    def toPreviousBoundary(self) -> int: ...
    def toStart(self): ...
    def type(self) -> PySide2.QtCore.QTextBoundaryFinder.BoundaryType: ...

class QTextCodec(Shiboken.Object):
    ConvertInvalidToNull: QTextCodec = ...  # -0x80000000
    DefaultConversion: QTextCodec = ...  # 0x0
    IgnoreHeader: QTextCodec = ...  # 0x1
    FreeFunction: QTextCodec = ...  # 0x2

    class ConversionFlag(object):
        ConvertInvalidToNull: QTextCodec.ConversionFlag = ...  # -0x80000000
        DefaultConversion: QTextCodec.ConversionFlag = ...  # 0x0
        IgnoreHeader: QTextCodec.ConversionFlag = ...  # 0x1
        FreeFunction: QTextCodec.ConversionFlag = ...  # 0x2

    class ConversionFlags(object): ...

    class ConverterState(Shiboken.Object):
        def __init__(self, f: PySide2.QtCore.QTextCodec.ConversionFlags = ...): ...

    def __init__(self): ...
    def aliases(self) -> typing.List: ...
    @staticmethod
    def availableCodecs() -> typing.List: ...
    @staticmethod
    def availableMibs() -> typing.List: ...
    @typing.overload
    def canEncode(self, arg__1: str) -> bool: ...
    @typing.overload
    def canEncode(self, arg__1: str) -> bool: ...
    @typing.overload
    @staticmethod
    def codecForHtml(ba: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec: ...
    @typing.overload
    @staticmethod
    def codecForHtml(
        ba: PySide2.QtCore.QByteArray, defaultCodec: PySide2.QtCore.QTextCodec
    ) -> PySide2.QtCore.QTextCodec: ...
    @staticmethod
    def codecForLocale() -> PySide2.QtCore.QTextCodec: ...
    @staticmethod
    def codecForMib(mib: int) -> PySide2.QtCore.QTextCodec: ...
    @typing.overload
    @staticmethod
    def codecForName(name: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec: ...
    @typing.overload
    @staticmethod
    def codecForName(name: bytes) -> PySide2.QtCore.QTextCodec: ...
    @typing.overload
    @staticmethod
    def codecForUtfText(ba: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QTextCodec: ...
    @typing.overload
    @staticmethod
    def codecForUtfText(
        ba: PySide2.QtCore.QByteArray, defaultCodec: PySide2.QtCore.QTextCodec
    ) -> PySide2.QtCore.QTextCodec: ...
    def convertToUnicode(
        self, in_: bytes, length: int, state: PySide2.QtCore.QTextCodec.ConverterState
    ) -> str: ...
    def fromUnicode(self, uc: str) -> PySide2.QtCore.QByteArray: ...
    def makeDecoder(
        self, flags: PySide2.QtCore.QTextCodec.ConversionFlags = ...
    ) -> PySide2.QtCore.QTextDecoder: ...
    def makeEncoder(
        self, flags: PySide2.QtCore.QTextCodec.ConversionFlags = ...
    ) -> PySide2.QtCore.QTextEncoder: ...
    def mibEnum(self) -> int: ...
    def name(self) -> PySide2.QtCore.QByteArray: ...
    @staticmethod
    def setCodecForLocale(c: PySide2.QtCore.QTextCodec): ...
    @typing.overload
    def toUnicode(self, arg__1: PySide2.QtCore.QByteArray) -> str: ...
    @typing.overload
    def toUnicode(self, chars: bytes) -> str: ...
    @typing.overload
    def toUnicode(
        self,
        in_: bytes,
        length: int,
        state: typing.Optional[PySide2.QtCore.QTextCodec.ConverterState] = ...,
    ) -> str: ...

class QTextDecoder(Shiboken.Object):
    @typing.overload
    def __init__(self, codec: PySide2.QtCore.QTextCodec): ...
    @typing.overload
    def __init__(
        self,
        codec: PySide2.QtCore.QTextCodec,
        flags: PySide2.QtCore.QTextCodec.ConversionFlags,
    ): ...
    def hasFailure(self) -> bool: ...
    def needsMoreData(self) -> bool: ...
    def toUnicode(self, ba: PySide2.QtCore.QByteArray) -> str: ...

class QTextEncoder(Shiboken.Object):
    @typing.overload
    def __init__(self, codec: PySide2.QtCore.QTextCodec): ...
    @typing.overload
    def __init__(
        self,
        codec: PySide2.QtCore.QTextCodec,
        flags: PySide2.QtCore.QTextCodec.ConversionFlags,
    ): ...
    def fromUnicode(self, str: str) -> PySide2.QtCore.QByteArray: ...
    def hasFailure(self) -> bool: ...

class QTextStream(Shiboken.Object):
    AlignLeft: QTextStream = ...  # 0x0
    Ok: QTextStream = ...  # 0x0
    SmartNotation: QTextStream = ...  # 0x0
    AlignRight: QTextStream = ...  # 0x1
    FixedNotation: QTextStream = ...  # 0x1
    ReadPastEnd: QTextStream = ...  # 0x1
    ShowBase: QTextStream = ...  # 0x1
    AlignCenter: QTextStream = ...  # 0x2
    ForcePoint: QTextStream = ...  # 0x2
    ReadCorruptData: QTextStream = ...  # 0x2
    ScientificNotation: QTextStream = ...  # 0x2
    AlignAccountingStyle: QTextStream = ...  # 0x3
    WriteFailed: QTextStream = ...  # 0x3
    ForceSign: QTextStream = ...  # 0x4
    UppercaseBase: QTextStream = ...  # 0x8
    UppercaseDigits: QTextStream = ...  # 0x10

    class FieldAlignment(object):
        AlignLeft: QTextStream.FieldAlignment = ...  # 0x0
        AlignRight: QTextStream.FieldAlignment = ...  # 0x1
        AlignCenter: QTextStream.FieldAlignment = ...  # 0x2
        AlignAccountingStyle: QTextStream.FieldAlignment = ...  # 0x3

    class NumberFlag(object):
        ShowBase: QTextStream.NumberFlag = ...  # 0x1
        ForcePoint: QTextStream.NumberFlag = ...  # 0x2
        ForceSign: QTextStream.NumberFlag = ...  # 0x4
        UppercaseBase: QTextStream.NumberFlag = ...  # 0x8
        UppercaseDigits: QTextStream.NumberFlag = ...  # 0x10

    class NumberFlags(object): ...

    class RealNumberNotation(object):
        SmartNotation: QTextStream.RealNumberNotation = ...  # 0x0
        FixedNotation: QTextStream.RealNumberNotation = ...  # 0x1
        ScientificNotation: QTextStream.RealNumberNotation = ...  # 0x2

    class Status(object):
        Ok: QTextStream.Status = ...  # 0x0
        ReadPastEnd: QTextStream.Status = ...  # 0x1
        ReadCorruptData: QTextStream.Status = ...  # 0x2
        WriteFailed: QTextStream.Status = ...  # 0x3
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(
        self,
        array: PySide2.QtCore.QByteArray,
        openMode: PySide2.QtCore.QIODevice.OpenMode = ...,
    ): ...
    @typing.overload
    def __init__(self, device: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def __lshift__(
        self, array: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, ch: str) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, ch: int) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, f: float) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, i: int) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, i: int) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(
        self, m: PySide2.QtCore.QTextStreamManipulator
    ) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, s: str) -> PySide2.QtCore.QTextStream: ...
    @typing.overload
    def __lshift__(self, s: str) -> PySide2.QtCore.QTextStream: ...
    def __rshift__(
        self, array: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QTextStream: ...
    def atEnd(self) -> bool: ...
    def autoDetectUnicode(self) -> bool: ...
    def codec(self) -> PySide2.QtCore.QTextCodec: ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def fieldAlignment(self) -> PySide2.QtCore.QTextStream.FieldAlignment: ...
    def fieldWidth(self) -> int: ...
    def flush(self): ...
    def generateByteOrderMark(self) -> bool: ...
    def integerBase(self) -> int: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def numberFlags(self) -> PySide2.QtCore.QTextStream.NumberFlags: ...
    def padChar(self) -> str: ...
    def pos(self) -> int: ...
    def read(self, maxlen: int) -> str: ...
    def readAll(self) -> str: ...
    def readLine(self, maxlen: int = ...) -> str: ...
    def realNumberNotation(self) -> PySide2.QtCore.QTextStream.RealNumberNotation: ...
    def realNumberPrecision(self) -> int: ...
    def reset(self): ...
    def resetStatus(self): ...
    def seek(self, pos: int) -> bool: ...
    def setAutoDetectUnicode(self, enabled: bool): ...
    @typing.overload
    def setCodec(self, codec: PySide2.QtCore.QTextCodec): ...
    @typing.overload
    def setCodec(self, codecName: bytes): ...
    def setDevice(self, device: PySide2.QtCore.QIODevice): ...
    def setFieldAlignment(
        self, alignment: PySide2.QtCore.QTextStream.FieldAlignment
    ): ...
    def setFieldWidth(self, width: int): ...
    def setGenerateByteOrderMark(self, generate: bool): ...
    def setIntegerBase(self, base: int): ...
    def setLocale(self, locale: PySide2.QtCore.QLocale): ...
    def setNumberFlags(self, flags: PySide2.QtCore.QTextStream.NumberFlags): ...
    def setPadChar(self, ch: str): ...
    def setRealNumberNotation(
        self, notation: PySide2.QtCore.QTextStream.RealNumberNotation
    ): ...
    def setRealNumberPrecision(self, precision: int): ...
    def setStatus(self, status: PySide2.QtCore.QTextStream.Status): ...
    def skipWhiteSpace(self): ...
    def status(self) -> PySide2.QtCore.QTextStream.Status: ...
    def string(self) -> typing.List: ...

class QTextStreamManipulator(Shiboken.Object):
    def __copy__(self): ...
    def exec_(self, s: PySide2.QtCore.QTextStream): ...

class QThread(PySide2.QtCore.QObject):
    IdlePriority: QThread = ...  # 0x0
    LowestPriority: QThread = ...  # 0x1
    LowPriority: QThread = ...  # 0x2
    NormalPriority: QThread = ...  # 0x3
    HighPriority: QThread = ...  # 0x4
    HighestPriority: QThread = ...  # 0x5
    TimeCriticalPriority: QThread = ...  # 0x6
    InheritPriority: QThread = ...  # 0x7

    class Priority(object):
        IdlePriority: QThread.Priority = ...  # 0x0
        LowestPriority: QThread.Priority = ...  # 0x1
        LowPriority: QThread.Priority = ...  # 0x2
        NormalPriority: QThread.Priority = ...  # 0x3
        HighPriority: QThread.Priority = ...  # 0x4
        HighestPriority: QThread.Priority = ...  # 0x5
        TimeCriticalPriority: QThread.Priority = ...  # 0x6
        InheritPriority: QThread.Priority = ...  # 0x7
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    @staticmethod
    def currentThread() -> PySide2.QtCore.QThread: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def eventDispatcher(self) -> PySide2.QtCore.QAbstractEventDispatcher: ...
    def exec_(self) -> int: ...
    def exit(self, retcode: int = ...): ...
    @staticmethod
    def idealThreadCount() -> int: ...
    def isFinished(self) -> bool: ...
    def isInterruptionRequested(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def loopLevel(self) -> int: ...
    @staticmethod
    def msleep(arg__1: int): ...
    def priority(self) -> PySide2.QtCore.QThread.Priority: ...
    def quit(self): ...
    def requestInterruption(self): ...
    def run(self): ...
    def setEventDispatcher(
        self, eventDispatcher: PySide2.QtCore.QAbstractEventDispatcher
    ): ...
    def setPriority(self, priority: PySide2.QtCore.QThread.Priority): ...
    def setStackSize(self, stackSize: int): ...
    @staticmethod
    def setTerminationEnabled(enabled: bool = ...): ...
    @staticmethod
    def sleep(arg__1: int): ...
    def stackSize(self) -> int: ...
    def start(self, priority: PySide2.QtCore.QThread.Priority = ...): ...
    def terminate(self): ...
    @staticmethod
    def usleep(arg__1: int): ...
    @typing.overload
    def wait(self, deadline: PySide2.QtCore.QDeadlineTimer = ...) -> bool: ...
    @typing.overload
    def wait(self, time: int) -> bool: ...
    @staticmethod
    def yieldCurrentThread(): ...

class QThreadPool(PySide2.QtCore.QObject):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def activeThreadCount(self) -> int: ...
    def cancel(self, runnable: PySide2.QtCore.QRunnable): ...
    def clear(self): ...
    def expiryTimeout(self) -> int: ...
    @staticmethod
    def globalInstance() -> PySide2.QtCore.QThreadPool: ...
    def maxThreadCount(self) -> int: ...
    def releaseThread(self): ...
    def reserveThread(self): ...
    def setExpiryTimeout(self, expiryTimeout: int): ...
    def setMaxThreadCount(self, maxThreadCount: int): ...
    def setStackSize(self, stackSize: int): ...
    def stackSize(self) -> int: ...
    def start(self, runnable: PySide2.QtCore.QRunnable, priority: int = ...): ...
    def tryStart(self, runnable: PySide2.QtCore.QRunnable) -> bool: ...
    def tryTake(self, runnable: PySide2.QtCore.QRunnable) -> bool: ...
    def waitForDone(self, msecs: int = ...) -> bool: ...

class QTime(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QTime: PySide2.QtCore.QTime): ...
    @typing.overload
    def __init__(self, h: int, m: int, s: int = ..., ms: int = ...): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def addMSecs(self, ms: int) -> PySide2.QtCore.QTime: ...
    def addSecs(self, secs: int) -> PySide2.QtCore.QTime: ...
    @staticmethod
    def currentTime() -> PySide2.QtCore.QTime: ...
    def elapsed(self) -> int: ...
    @staticmethod
    def fromMSecsSinceStartOfDay(msecs: int) -> PySide2.QtCore.QTime: ...
    @typing.overload
    @staticmethod
    def fromString(
        s: str, f: PySide2.QtCore.Qt.DateFormat = ...
    ) -> PySide2.QtCore.QTime: ...
    @typing.overload
    @staticmethod
    def fromString(s: str, format: str) -> PySide2.QtCore.QTime: ...
    def hour(self) -> int: ...
    def isNull(self) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid() -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(h: int, m: int, s: int, ms: int = ...) -> bool: ...
    def minute(self) -> int: ...
    def msec(self) -> int: ...
    def msecsSinceStartOfDay(self) -> int: ...
    def msecsTo(self, arg__1: PySide2.QtCore.QTime) -> int: ...
    def restart(self) -> int: ...
    def second(self) -> int: ...
    def secsTo(self, arg__1: PySide2.QtCore.QTime) -> int: ...
    def setHMS(self, h: int, m: int, s: int, ms: int = ...) -> bool: ...
    def start(self): ...
    def toPython(self) -> object: ...
    @typing.overload
    def toString(self, f: PySide2.QtCore.Qt.DateFormat = ...) -> str: ...
    @typing.overload
    def toString(self, format: str) -> str: ...

class QTimeLine(PySide2.QtCore.QObject):
    EaseInCurve: QTimeLine = ...  # 0x0
    Forward: QTimeLine = ...  # 0x0
    NotRunning: QTimeLine = ...  # 0x0
    Backward: QTimeLine = ...  # 0x1
    EaseOutCurve: QTimeLine = ...  # 0x1
    Paused: QTimeLine = ...  # 0x1
    EaseInOutCurve: QTimeLine = ...  # 0x2
    Running: QTimeLine = ...  # 0x2
    LinearCurve: QTimeLine = ...  # 0x3
    SineCurve: QTimeLine = ...  # 0x4
    CosineCurve: QTimeLine = ...  # 0x5

    class CurveShape(object):
        EaseInCurve: QTimeLine.CurveShape = ...  # 0x0
        EaseOutCurve: QTimeLine.CurveShape = ...  # 0x1
        EaseInOutCurve: QTimeLine.CurveShape = ...  # 0x2
        LinearCurve: QTimeLine.CurveShape = ...  # 0x3
        SineCurve: QTimeLine.CurveShape = ...  # 0x4
        CosineCurve: QTimeLine.CurveShape = ...  # 0x5

    class Direction(object):
        Forward: QTimeLine.Direction = ...  # 0x0
        Backward: QTimeLine.Direction = ...  # 0x1

    class State(object):
        NotRunning: QTimeLine.State = ...  # 0x0
        Paused: QTimeLine.State = ...  # 0x1
        Running: QTimeLine.State = ...  # 0x2
    def __init__(
        self, duration: int = ..., parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ): ...
    def currentFrame(self) -> int: ...
    def currentTime(self) -> int: ...
    def currentValue(self) -> float: ...
    def curveShape(self) -> PySide2.QtCore.QTimeLine.CurveShape: ...
    def direction(self) -> PySide2.QtCore.QTimeLine.Direction: ...
    def duration(self) -> int: ...
    def easingCurve(self) -> PySide2.QtCore.QEasingCurve: ...
    def endFrame(self) -> int: ...
    def frameForTime(self, msec: int) -> int: ...
    def loopCount(self) -> int: ...
    def resume(self): ...
    def setCurrentTime(self, msec: int): ...
    def setCurveShape(self, shape: PySide2.QtCore.QTimeLine.CurveShape): ...
    def setDirection(self, direction: PySide2.QtCore.QTimeLine.Direction): ...
    def setDuration(self, duration: int): ...
    def setEasingCurve(self, curve: PySide2.QtCore.QEasingCurve): ...
    def setEndFrame(self, frame: int): ...
    def setFrameRange(self, startFrame: int, endFrame: int): ...
    def setLoopCount(self, count: int): ...
    def setPaused(self, paused: bool): ...
    def setStartFrame(self, frame: int): ...
    def setUpdateInterval(self, interval: int): ...
    def start(self): ...
    def startFrame(self) -> int: ...
    def state(self) -> PySide2.QtCore.QTimeLine.State: ...
    def stop(self): ...
    def timerEvent(self, event: PySide2.QtCore.QTimerEvent): ...
    def toggleDirection(self): ...
    def updateInterval(self) -> int: ...
    def valueForTime(self, msec: int) -> float: ...

class QTimeZone(Shiboken.Object):
    DefaultName: QTimeZone = ...  # 0x0
    StandardTime: QTimeZone = ...  # 0x0
    DaylightTime: QTimeZone = ...  # 0x1
    LongName: QTimeZone = ...  # 0x1
    GenericTime: QTimeZone = ...  # 0x2
    ShortName: QTimeZone = ...  # 0x2
    OffsetName: QTimeZone = ...  # 0x3

    class NameType(object):
        DefaultName: QTimeZone.NameType = ...  # 0x0
        LongName: QTimeZone.NameType = ...  # 0x1
        ShortName: QTimeZone.NameType = ...  # 0x2
        OffsetName: QTimeZone.NameType = ...  # 0x3

    class OffsetData(Shiboken.Object):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, OffsetData: PySide2.QtCore.QTimeZone.OffsetData): ...
        def __copy__(self): ...

    class TimeType(object):
        StandardTime: QTimeZone.TimeType = ...  # 0x0
        DaylightTime: QTimeZone.TimeType = ...  # 0x1
        GenericTime: QTimeZone.TimeType = ...  # 0x2
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, ianaId: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, offsetSeconds: int): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QTimeZone): ...
    @typing.overload
    def __init__(
        self,
        zoneId: PySide2.QtCore.QByteArray,
        offsetSeconds: int,
        name: str,
        abbreviation: str,
        country: PySide2.QtCore.QLocale.Country = ...,
        comment: str = ...,
    ): ...
    def __copy__(self): ...
    def abbreviation(self, atDateTime: PySide2.QtCore.QDateTime) -> str: ...
    @typing.overload
    @staticmethod
    def availableTimeZoneIds() -> typing.List: ...
    @typing.overload
    @staticmethod
    def availableTimeZoneIds(
        country: PySide2.QtCore.QLocale.Country,
    ) -> typing.List: ...
    @typing.overload
    @staticmethod
    def availableTimeZoneIds(offsetSeconds: int) -> typing.List: ...
    def comment(self) -> str: ...
    def country(self) -> PySide2.QtCore.QLocale.Country: ...
    def daylightTimeOffset(self, atDateTime: PySide2.QtCore.QDateTime) -> int: ...
    @typing.overload
    def displayName(
        self,
        atDateTime: PySide2.QtCore.QDateTime,
        nameType: PySide2.QtCore.QTimeZone.NameType = ...,
        locale: PySide2.QtCore.QLocale = ...,
    ) -> str: ...
    @typing.overload
    def displayName(
        self,
        timeType: PySide2.QtCore.QTimeZone.TimeType,
        nameType: PySide2.QtCore.QTimeZone.NameType = ...,
        locale: PySide2.QtCore.QLocale = ...,
    ) -> str: ...
    def hasDaylightTime(self) -> bool: ...
    def hasTransitions(self) -> bool: ...
    @staticmethod
    def ianaIdToWindowsId(
        ianaId: PySide2.QtCore.QByteArray,
    ) -> PySide2.QtCore.QByteArray: ...
    def id(self) -> PySide2.QtCore.QByteArray: ...
    def isDaylightTime(self, atDateTime: PySide2.QtCore.QDateTime) -> bool: ...
    @staticmethod
    def isTimeZoneIdAvailable(ianaId: PySide2.QtCore.QByteArray) -> bool: ...
    def isValid(self) -> bool: ...
    def nextTransition(
        self, afterDateTime: PySide2.QtCore.QDateTime
    ) -> PySide2.QtCore.QTimeZone.OffsetData: ...
    def offsetData(
        self, forDateTime: PySide2.QtCore.QDateTime
    ) -> PySide2.QtCore.QTimeZone.OffsetData: ...
    def offsetFromUtc(self, atDateTime: PySide2.QtCore.QDateTime) -> int: ...
    def previousTransition(
        self, beforeDateTime: PySide2.QtCore.QDateTime
    ) -> PySide2.QtCore.QTimeZone.OffsetData: ...
    def standardTimeOffset(self, atDateTime: PySide2.QtCore.QDateTime) -> int: ...
    def swap(self, other: PySide2.QtCore.QTimeZone): ...
    @staticmethod
    def systemTimeZone() -> PySide2.QtCore.QTimeZone: ...
    @staticmethod
    def systemTimeZoneId() -> PySide2.QtCore.QByteArray: ...
    def transitions(
        self,
        fromDateTime: PySide2.QtCore.QDateTime,
        toDateTime: PySide2.QtCore.QDateTime,
    ) -> typing.List: ...
    @staticmethod
    def utc() -> PySide2.QtCore.QTimeZone: ...
    @typing.overload
    @staticmethod
    def windowsIdToDefaultIanaId(
        windowsId: PySide2.QtCore.QByteArray,
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def windowsIdToDefaultIanaId(
        windowsId: PySide2.QtCore.QByteArray, country: PySide2.QtCore.QLocale.Country
    ) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def windowsIdToIanaIds(windowsId: PySide2.QtCore.QByteArray) -> typing.List: ...
    @typing.overload
    @staticmethod
    def windowsIdToIanaIds(
        windowsId: PySide2.QtCore.QByteArray, country: PySide2.QtCore.QLocale.Country
    ) -> typing.List: ...

class QTimer(PySide2.QtCore.QObject):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def interval(self) -> int: ...
    def isActive(self) -> bool: ...
    def isSingleShot(self) -> bool: ...
    def killTimer(self, arg__1: int): ...
    def remainingTime(self) -> int: ...
    def setInterval(self, msec: int): ...
    def setSingleShot(self, singleShot: bool): ...
    def setTimerType(self, atype: PySide2.QtCore.Qt.TimerType): ...
    @typing.overload
    @staticmethod
    def singleShot(arg__1: int, arg__2: typing.Callable): ...
    @typing.overload
    @staticmethod
    def singleShot(msec: int, receiver: PySide2.QtCore.QObject, member: bytes): ...
    @typing.overload
    @staticmethod
    def singleShot(
        msec: int,
        timerType: PySide2.QtCore.Qt.TimerType,
        receiver: PySide2.QtCore.QObject,
        member: bytes,
    ): ...
    @typing.overload
    def start(self): ...
    @typing.overload
    def start(self, msec: int): ...
    def stop(self): ...
    def timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent): ...
    def timerId(self) -> int: ...
    def timerType(self) -> PySide2.QtCore.Qt.TimerType: ...

class QTimerEvent(PySide2.QtCore.QEvent):
    def __init__(self, timerId: int): ...
    def timerId(self) -> int: ...

class QTranslator(PySide2.QtCore.QObject):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def filePath(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def language(self) -> str: ...
    @typing.overload
    def load(self, data: bytes, len: int, directory: str = ...) -> bool: ...
    @typing.overload
    def load(
        self,
        filename: str,
        directory: str = ...,
        search_delimiters: str = ...,
        suffix: str = ...,
    ) -> bool: ...
    @typing.overload
    def load(
        self,
        locale: PySide2.QtCore.QLocale,
        filename: str,
        prefix: str = ...,
        directory: str = ...,
        suffix: str = ...,
    ) -> bool: ...
    def translate(
        self,
        context: bytes,
        sourceText: bytes,
        disambiguation: typing.Optional[bytes] = ...,
        n: int = ...,
    ) -> str: ...

class QTransposeProxyModel(PySide2.QtCore.QAbstractProxyModel):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...
    ) -> typing.Any: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    def insertColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def insertRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def itemData(self, index: PySide2.QtCore.QModelIndex) -> typing.Dict: ...
    def mapFromSource(
        self, sourceIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def mapToSource(
        self, proxyIndex: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def moveColumns(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceColumn: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    def moveRows(
        self,
        sourceParent: PySide2.QtCore.QModelIndex,
        sourceRow: int,
        count: int,
        destinationParent: PySide2.QtCore.QModelIndex,
        destinationChild: int,
    ) -> bool: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def removeColumns(
        self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def removeRows(
        self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> bool: ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def setHeaderData(
        self,
        section: int,
        orientation: PySide2.QtCore.Qt.Orientation,
        value: typing.Any,
        role: int = ...,
    ) -> bool: ...
    def setItemData(
        self, index: PySide2.QtCore.QModelIndex, roles: typing.Dict
    ) -> bool: ...
    def setSourceModel(self, newSourceModel: PySide2.QtCore.QAbstractItemModel): ...
    def sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder = ...): ...
    def span(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QSize: ...

class QUrl(Shiboken.Object):
    DefaultResolution: QUrl = ...  # 0x0
    None_: QUrl = ...  # 0x0
    PrettyDecoded: QUrl = ...  # 0x0
    TolerantMode: QUrl = ...  # 0x0
    AssumeLocalFile: QUrl = ...  # 0x1
    RemoveScheme: QUrl = ...  # 0x1
    StrictMode: QUrl = ...  # 0x1
    DecodedMode: QUrl = ...  # 0x2
    RemovePassword: QUrl = ...  # 0x2
    RemoveUserInfo: QUrl = ...  # 0x6
    RemovePort: QUrl = ...  # 0x8
    RemoveAuthority: QUrl = ...  # 0x1e
    RemovePath: QUrl = ...  # 0x20
    RemoveQuery: QUrl = ...  # 0x40
    RemoveFragment: QUrl = ...  # 0x80
    PreferLocalFile: QUrl = ...  # 0x200
    StripTrailingSlash: QUrl = ...  # 0x400
    RemoveFilename: QUrl = ...  # 0x800
    NormalizePathSegments: QUrl = ...  # 0x1000
    EncodeSpaces: QUrl = ...  # 0x100000
    EncodeUnicode: QUrl = ...  # 0x200000
    EncodeDelimiters: QUrl = ...  # 0xc00000
    EncodeReserved: QUrl = ...  # 0x1000000
    FullyEncoded: QUrl = ...  # 0x1f00000
    DecodeReserved: QUrl = ...  # 0x2000000
    FullyDecoded: QUrl = ...  # 0x7f00000

    class ComponentFormattingOption(object):
        PrettyDecoded: QUrl.ComponentFormattingOption = ...  # 0x0
        EncodeSpaces: QUrl.ComponentFormattingOption = ...  # 0x100000
        EncodeUnicode: QUrl.ComponentFormattingOption = ...  # 0x200000
        EncodeDelimiters: QUrl.ComponentFormattingOption = ...  # 0xc00000
        EncodeReserved: QUrl.ComponentFormattingOption = ...  # 0x1000000
        FullyEncoded: QUrl.ComponentFormattingOption = ...  # 0x1f00000
        DecodeReserved: QUrl.ComponentFormattingOption = ...  # 0x2000000
        FullyDecoded: QUrl.ComponentFormattingOption = ...  # 0x7f00000

    class FormattingOptions(object): ...

    class ParsingMode(object):
        TolerantMode: QUrl.ParsingMode = ...  # 0x0
        StrictMode: QUrl.ParsingMode = ...  # 0x1
        DecodedMode: QUrl.ParsingMode = ...  # 0x2

    class UrlFormattingOption(object):
        None_: QUrl.UrlFormattingOption = ...  # 0x0
        RemoveScheme: QUrl.UrlFormattingOption = ...  # 0x1
        RemovePassword: QUrl.UrlFormattingOption = ...  # 0x2
        RemoveUserInfo: QUrl.UrlFormattingOption = ...  # 0x6
        RemovePort: QUrl.UrlFormattingOption = ...  # 0x8
        RemoveAuthority: QUrl.UrlFormattingOption = ...  # 0x1e
        RemovePath: QUrl.UrlFormattingOption = ...  # 0x20
        RemoveQuery: QUrl.UrlFormattingOption = ...  # 0x40
        RemoveFragment: QUrl.UrlFormattingOption = ...  # 0x80
        PreferLocalFile: QUrl.UrlFormattingOption = ...  # 0x200
        StripTrailingSlash: QUrl.UrlFormattingOption = ...  # 0x400
        RemoveFilename: QUrl.UrlFormattingOption = ...  # 0x800
        NormalizePathSegments: QUrl.UrlFormattingOption = ...  # 0x1000

    class UserInputResolutionOption(object):
        DefaultResolution: QUrl.UserInputResolutionOption = ...  # 0x0
        AssumeLocalFile: QUrl.UserInputResolutionOption = ...  # 0x1

    class UserInputResolutionOptions(object): ...

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, copy: PySide2.QtCore.QUrl): ...
    @typing.overload
    def __init__(self, url: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    def adjusted(
        self, options: PySide2.QtCore.QUrl.FormattingOptions
    ) -> PySide2.QtCore.QUrl: ...
    def authority(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def clear(self): ...
    def errorString(self) -> str: ...
    def fileName(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def fragment(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    @staticmethod
    def fromAce(arg__1: PySide2.QtCore.QByteArray) -> str: ...
    @staticmethod
    def fromEncoded(
        url: PySide2.QtCore.QByteArray, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ) -> PySide2.QtCore.QUrl: ...
    @staticmethod
    def fromLocalFile(localfile: str) -> PySide2.QtCore.QUrl: ...
    @staticmethod
    def fromPercentEncoding(arg__1: PySide2.QtCore.QByteArray) -> str: ...
    @staticmethod
    def fromStringList(
        uris: typing.Sequence, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ) -> typing.List: ...
    @typing.overload
    @staticmethod
    def fromUserInput(userInput: str) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    @staticmethod
    def fromUserInput(
        userInput: str,
        workingDirectory: str,
        options: PySide2.QtCore.QUrl.UserInputResolutionOptions = ...,
    ) -> PySide2.QtCore.QUrl: ...
    def hasFragment(self) -> bool: ...
    def hasQuery(self) -> bool: ...
    def host(
        self, arg__1: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    @staticmethod
    def idnWhitelist() -> typing.List: ...
    def isEmpty(self) -> bool: ...
    def isLocalFile(self) -> bool: ...
    def isParentOf(self, url: PySide2.QtCore.QUrl) -> bool: ...
    def isRelative(self) -> bool: ...
    def isValid(self) -> bool: ...
    def matches(
        self, url: PySide2.QtCore.QUrl, options: PySide2.QtCore.QUrl.FormattingOptions
    ) -> bool: ...
    def password(
        self, arg__1: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def path(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def port(self, defaultPort: int = ...) -> int: ...
    def query(
        self, arg__1: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def resolved(self, relative: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl: ...
    def scheme(self) -> str: ...
    def setAuthority(
        self, authority: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ): ...
    def setFragment(
        self, fragment: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ): ...
    def setHost(self, host: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...): ...
    @staticmethod
    def setIdnWhitelist(arg__1: typing.Sequence): ...
    def setPassword(
        self, password: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ): ...
    def setPath(self, path: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...): ...
    def setPort(self, port: int): ...
    @typing.overload
    def setQuery(self, query: PySide2.QtCore.QUrlQuery): ...
    @typing.overload
    def setQuery(self, query: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...): ...
    def setScheme(self, scheme: str): ...
    def setUrl(self, url: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...): ...
    def setUserInfo(
        self, userInfo: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ): ...
    def setUserName(
        self, userName: str, mode: PySide2.QtCore.QUrl.ParsingMode = ...
    ): ...
    def swap(self, other: PySide2.QtCore.QUrl): ...
    @staticmethod
    def toAce(arg__1: str) -> PySide2.QtCore.QByteArray: ...
    def toDisplayString(
        self, options: PySide2.QtCore.QUrl.FormattingOptions = ...
    ) -> str: ...
    def toEncoded(
        self, options: PySide2.QtCore.QUrl.FormattingOptions = ...
    ) -> PySide2.QtCore.QByteArray: ...
    def toLocalFile(self) -> str: ...
    @staticmethod
    def toPercentEncoding(
        arg__1: str,
        exclude: PySide2.QtCore.QByteArray = ...,
        include: PySide2.QtCore.QByteArray = ...,
    ) -> PySide2.QtCore.QByteArray: ...
    def toString(self, options: PySide2.QtCore.QUrl.FormattingOptions = ...) -> str: ...
    @staticmethod
    def toStringList(
        uris: typing.Sequence, options: PySide2.QtCore.QUrl.FormattingOptions = ...
    ) -> typing.List: ...
    def topLevelDomain(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def url(self, options: PySide2.QtCore.QUrl.FormattingOptions = ...) -> str: ...
    def userInfo(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def userName(
        self, options: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...

class QUrlQuery(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtCore.QUrlQuery): ...
    @typing.overload
    def __init__(self, queryString: str): ...
    @typing.overload
    def __init__(self, url: PySide2.QtCore.QUrl): ...
    def __copy__(self): ...
    def addQueryItem(self, key: str, value: str): ...
    def allQueryItemValues(
        self, key: str, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> typing.List: ...
    def clear(self): ...
    @staticmethod
    def defaultQueryPairDelimiter() -> str: ...
    @staticmethod
    def defaultQueryValueDelimiter() -> str: ...
    def hasQueryItem(self, key: str) -> bool: ...
    def isEmpty(self) -> bool: ...
    def query(
        self, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def queryItemValue(
        self, key: str, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...
    def queryItems(
        self, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> typing.List: ...
    def queryPairDelimiter(self) -> str: ...
    def queryValueDelimiter(self) -> str: ...
    def removeAllQueryItems(self, key: str): ...
    def removeQueryItem(self, key: str): ...
    def setQuery(self, queryString: str): ...
    def setQueryDelimiters(self, valueDelimiter: str, pairDelimiter: str): ...
    def setQueryItems(self, query: typing.Sequence): ...
    def swap(self, other: PySide2.QtCore.QUrlQuery): ...
    def toString(
        self, encoding: PySide2.QtCore.QUrl.ComponentFormattingOption = ...
    ) -> str: ...

class QUuid(Shiboken.Object):
    VarUnknown: QUuid = ...  # -0x1
    VerUnknown: QUuid = ...  # -0x1
    NCS: QUuid = ...  # 0x0
    WithBraces: QUuid = ...  # 0x0
    Time: QUuid = ...  # 0x1
    WithoutBraces: QUuid = ...  # 0x1
    DCE: QUuid = ...  # 0x2
    EmbeddedPOSIX: QUuid = ...  # 0x2
    Id128: QUuid = ...  # 0x3
    Md5: QUuid = ...  # 0x3
    Name: QUuid = ...  # 0x3
    Random: QUuid = ...  # 0x4
    Sha1: QUuid = ...  # 0x5
    Microsoft: QUuid = ...  # 0x6
    Reserved: QUuid = ...  # 0x7

    class StringFormat(object):
        WithBraces: QUuid.StringFormat = ...  # 0x0
        WithoutBraces: QUuid.StringFormat = ...  # 0x1
        Id128: QUuid.StringFormat = ...  # 0x3

    class Variant(object):
        VarUnknown: QUuid.Variant = ...  # -0x1
        NCS: QUuid.Variant = ...  # 0x0
        DCE: QUuid.Variant = ...  # 0x2
        Microsoft: QUuid.Variant = ...  # 0x6
        Reserved: QUuid.Variant = ...  # 0x7

    class Version(object):
        VerUnknown: QUuid.Version = ...  # -0x1
        Time: QUuid.Version = ...  # 0x1
        EmbeddedPOSIX: QUuid.Version = ...  # 0x2
        Md5: QUuid.Version = ...  # 0x3
        Name: QUuid.Version = ...  # 0x3
        Random: QUuid.Version = ...  # 0x4
        Sha1: QUuid.Version = ...  # 0x5
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, arg__1: str): ...
    @typing.overload
    def __init__(self, arg__1: bytes): ...
    @typing.overload
    def __init__(
        self,
        l: int,
        w1: int,
        w2: int,
        b1: int,
        b2: int,
        b3: int,
        b4: int,
        b5: int,
        b6: int,
        b7: int,
        b8: int,
    ): ...
    def __copy__(self): ...
    def __reduce__(self) -> object: ...
    def __repr__(self) -> object: ...
    @staticmethod
    def createUuid() -> PySide2.QtCore.QUuid: ...
    @typing.overload
    @staticmethod
    def createUuidV3(
        ns: PySide2.QtCore.QUuid, baseData: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QUuid: ...
    @typing.overload
    @staticmethod
    def createUuidV3(
        ns: PySide2.QtCore.QUuid, baseData: str
    ) -> PySide2.QtCore.QUuid: ...
    @typing.overload
    @staticmethod
    def createUuidV5(
        ns: PySide2.QtCore.QUuid, baseData: PySide2.QtCore.QByteArray
    ) -> PySide2.QtCore.QUuid: ...
    @typing.overload
    @staticmethod
    def createUuidV5(
        ns: PySide2.QtCore.QUuid, baseData: str
    ) -> PySide2.QtCore.QUuid: ...
    @staticmethod
    def fromRfc4122(arg__1: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QUuid: ...
    def isNull(self) -> bool: ...
    @typing.overload
    def toByteArray(self) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toByteArray(
        self, mode: PySide2.QtCore.QUuid.StringFormat
    ) -> PySide2.QtCore.QByteArray: ...
    def toRfc4122(self) -> PySide2.QtCore.QByteArray: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, mode: PySide2.QtCore.QUuid.StringFormat) -> str: ...
    def variant(self) -> PySide2.QtCore.QUuid.Variant: ...
    def version(self) -> PySide2.QtCore.QUuid.Version: ...

class QVariantAnimation(PySide2.QtCore.QAbstractAnimation):
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def currentValue(self) -> typing.Any: ...
    def duration(self) -> int: ...
    def easingCurve(self) -> PySide2.QtCore.QEasingCurve: ...
    def endValue(self) -> typing.Any: ...
    def event(self, event: PySide2.QtCore.QEvent) -> bool: ...
    def interpolated(
        self, from_: typing.Any, to: typing.Any, progress: float
    ) -> typing.Any: ...
    def keyValueAt(self, step: float) -> typing.Any: ...
    def keyValues(self) -> typing.List: ...
    def setDuration(self, msecs: int): ...
    def setEasingCurve(self, easing: PySide2.QtCore.QEasingCurve): ...
    def setEndValue(self, value: typing.Any): ...
    def setKeyValueAt(self, step: float, value: typing.Any): ...
    def setKeyValues(self, values: typing.List): ...
    def setStartValue(self, value: typing.Any): ...
    def startValue(self) -> typing.Any: ...
    def updateCurrentTime(self, arg__1: int): ...
    def updateCurrentValue(self, value: typing.Any): ...
    def updateState(
        self,
        newState: PySide2.QtCore.QAbstractAnimation.State,
        oldState: PySide2.QtCore.QAbstractAnimation.State,
    ): ...

class QVersionNumber(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, maj: int): ...
    @typing.overload
    def __init__(self, maj: int, min: int): ...
    @typing.overload
    def __init__(self, maj: int, min: int, mic: int): ...
    @typing.overload
    def __init__(self, seg: typing.List): ...
    def __copy__(self): ...
    @staticmethod
    def commonPrefix(
        v1: PySide2.QtCore.QVersionNumber, v2: PySide2.QtCore.QVersionNumber
    ) -> PySide2.QtCore.QVersionNumber: ...
    @staticmethod
    def compare(
        v1: PySide2.QtCore.QVersionNumber, v2: PySide2.QtCore.QVersionNumber
    ) -> int: ...
    @staticmethod
    def fromString(string: str) -> typing.Tuple: ...
    def isNormalized(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isPrefixOf(self, other: PySide2.QtCore.QVersionNumber) -> bool: ...
    def majorVersion(self) -> int: ...
    def microVersion(self) -> int: ...
    def minorVersion(self) -> int: ...
    def normalized(self) -> PySide2.QtCore.QVersionNumber: ...
    def segmentAt(self, index: int) -> int: ...
    def segmentCount(self) -> int: ...
    def segments(self) -> typing.List: ...
    def toString(self) -> str: ...

class QWaitCondition(Shiboken.Object):
    def __init__(self): ...
    def notify_all(self): ...
    def notify_one(self): ...
    @typing.overload
    def wait(
        self,
        lockedMutex: PySide2.QtCore.QMutex,
        deadline: PySide2.QtCore.QDeadlineTimer = ...,
    ) -> bool: ...
    @typing.overload
    def wait(self, lockedMutex: PySide2.QtCore.QMutex, time: int) -> bool: ...
    @typing.overload
    def wait(
        self,
        lockedReadWriteLock: PySide2.QtCore.QReadWriteLock,
        deadline: PySide2.QtCore.QDeadlineTimer = ...,
    ) -> bool: ...
    @typing.overload
    def wait(
        self, lockedReadWriteLock: PySide2.QtCore.QReadWriteLock, time: int
    ) -> bool: ...
    def wakeAll(self): ...
    def wakeOne(self): ...

class QWinEventNotifier(PySide2.QtCore.QObject):
    @typing.overload
    def __init__(
        self, hEvent: int, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ): ...
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
    def event(self, e: PySide2.QtCore.QEvent) -> bool: ...
    def handle(self) -> int: ...
    def isEnabled(self) -> bool: ...
    def setEnabled(self, enable: bool): ...
    def setHandle(self, hEvent: int): ...

class QWriteLocker(Shiboken.Object):
    def __init__(self, readWriteLock: PySide2.QtCore.QReadWriteLock): ...
    def __enter__(self): ...
    def __exit__(self, arg__1: object, arg__2: object, arg__3: object): ...
    def readWriteLock(self) -> PySide2.QtCore.QReadWriteLock: ...
    def relock(self): ...
    def unlock(self): ...

class QXmlStreamAttribute(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QXmlStreamAttribute): ...
    @typing.overload
    def __init__(self, namespaceUri: str, name: str, value: str): ...
    @typing.overload
    def __init__(self, qualifiedName: str, value: str): ...
    def __copy__(self): ...
    def isDefault(self) -> bool: ...
    def name(self) -> str: ...
    def namespaceUri(self) -> str: ...
    def prefix(self) -> str: ...
    def qualifiedName(self) -> str: ...
    def value(self) -> str: ...

class QXmlStreamAttributes(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, QXmlStreamAttributes: PySide2.QtCore.QXmlStreamAttributes): ...
    def __add__(self, l: typing.List) -> typing.List: ...
    def __copy__(self): ...
    def __iadd__(self, t: PySide2.QtCore.QXmlStreamAttribute) -> typing.List: ...
    @typing.overload
    def __lshift__(self, l: typing.List) -> typing.List: ...
    @typing.overload
    def __lshift__(self, t: PySide2.QtCore.QXmlStreamAttribute) -> typing.List: ...
    @typing.overload
    def append(self, namespaceUri: str, name: str, value: str): ...
    @typing.overload
    def append(self, qualifiedName: str, value: str): ...
    def at(self, i: int) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def back(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def capacity(self) -> int: ...
    def clear(self): ...
    def constData(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def constFirst(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def constLast(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def contains(self, t: PySide2.QtCore.QXmlStreamAttribute) -> bool: ...
    @typing.overload
    def count(self) -> int: ...
    @typing.overload
    def count(self, t: PySide2.QtCore.QXmlStreamAttribute) -> int: ...
    def data(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def empty(self) -> bool: ...
    def endsWith(self, t: PySide2.QtCore.QXmlStreamAttribute) -> bool: ...
    def fill(
        self, t: PySide2.QtCore.QXmlStreamAttribute, size: int = ...
    ) -> typing.List: ...
    def first(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def front(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    @typing.overload
    def hasAttribute(self, namespaceUri: str, name: str) -> bool: ...
    @typing.overload
    def hasAttribute(self, qualifiedName: str) -> bool: ...
    def indexOf(
        self, t: PySide2.QtCore.QXmlStreamAttribute, from_: int = ...
    ) -> int: ...
    @typing.overload
    def insert(self, i: int, n: int, t: PySide2.QtCore.QXmlStreamAttribute): ...
    @typing.overload
    def insert(self, i: int, t: PySide2.QtCore.QXmlStreamAttribute): ...
    def isEmpty(self) -> bool: ...
    def isSharedWith(self, other: typing.List) -> bool: ...
    def last(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def lastIndexOf(
        self, t: PySide2.QtCore.QXmlStreamAttribute, from_: int = ...
    ) -> int: ...
    def length(self) -> int: ...
    def mid(self, pos: int, len: int = ...) -> typing.List: ...
    def move(self, from_: int, to: int): ...
    def prepend(self, t: PySide2.QtCore.QXmlStreamAttribute): ...
    @typing.overload
    def remove(self, i: int): ...
    @typing.overload
    def remove(self, i: int, n: int): ...
    def removeAll(self, t: PySide2.QtCore.QXmlStreamAttribute) -> int: ...
    def removeAt(self, i: int): ...
    def removeFirst(self): ...
    def removeLast(self): ...
    def removeOne(self, t: PySide2.QtCore.QXmlStreamAttribute) -> bool: ...
    def replace(self, i: int, t: PySide2.QtCore.QXmlStreamAttribute): ...
    def reserve(self, size: int): ...
    def resize(self, size: int): ...
    def setSharable(self, sharable: bool): ...
    def shrink_to_fit(self): ...
    def size(self) -> int: ...
    def squeeze(self): ...
    def startsWith(self, t: PySide2.QtCore.QXmlStreamAttribute) -> bool: ...
    def swap(self, other: typing.List): ...
    def swapItemsAt(self, i: int, j: int): ...
    def takeAt(self, i: int) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def takeFirst(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    def takeLast(self) -> PySide2.QtCore.QXmlStreamAttribute: ...
    @typing.overload
    def value(self, namespaceUri: str, name: str) -> str: ...
    @typing.overload
    def value(self, qualifiedName: str) -> str: ...

class QXmlStreamEntityDeclaration(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QXmlStreamEntityDeclaration): ...
    def __copy__(self): ...
    def name(self) -> str: ...
    def notationName(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...
    def value(self) -> str: ...

class QXmlStreamEntityResolver(Shiboken.Object):
    def __init__(self): ...
    def resolveEntity(self, publicId: str, systemId: str) -> str: ...
    def resolveUndeclaredEntity(self, name: str) -> str: ...

class QXmlStreamNamespaceDeclaration(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QXmlStreamNamespaceDeclaration): ...
    @typing.overload
    def __init__(self, prefix: str, namespaceUri: str): ...
    def __copy__(self): ...
    def namespaceUri(self) -> str: ...
    def prefix(self) -> str: ...

class QXmlStreamNotationDeclaration(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, arg__1: PySide2.QtCore.QXmlStreamNotationDeclaration): ...
    def __copy__(self): ...
    def name(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...

class QXmlStreamReader(Shiboken.Object):
    ErrorOnUnexpectedElement: QXmlStreamReader = ...  # 0x0
    NoError: QXmlStreamReader = ...  # 0x0
    NoToken: QXmlStreamReader = ...  # 0x0
    IncludeChildElements: QXmlStreamReader = ...  # 0x1
    Invalid: QXmlStreamReader = ...  # 0x1
    UnexpectedElementError: QXmlStreamReader = ...  # 0x1
    CustomError: QXmlStreamReader = ...  # 0x2
    SkipChildElements: QXmlStreamReader = ...  # 0x2
    StartDocument: QXmlStreamReader = ...  # 0x2
    EndDocument: QXmlStreamReader = ...  # 0x3
    NotWellFormedError: QXmlStreamReader = ...  # 0x3
    PrematureEndOfDocumentError: QXmlStreamReader = ...  # 0x4
    StartElement: QXmlStreamReader = ...  # 0x4
    EndElement: QXmlStreamReader = ...  # 0x5
    Characters: QXmlStreamReader = ...  # 0x6
    Comment: QXmlStreamReader = ...  # 0x7
    DTD: QXmlStreamReader = ...  # 0x8
    EntityReference: QXmlStreamReader = ...  # 0x9
    ProcessingInstruction: QXmlStreamReader = ...  # 0xa

    class Error(object):
        NoError: QXmlStreamReader.Error = ...  # 0x0
        UnexpectedElementError: QXmlStreamReader.Error = ...  # 0x1
        CustomError: QXmlStreamReader.Error = ...  # 0x2
        NotWellFormedError: QXmlStreamReader.Error = ...  # 0x3
        PrematureEndOfDocumentError: QXmlStreamReader.Error = ...  # 0x4

    class ReadElementTextBehaviour(object):
        ErrorOnUnexpectedElement: QXmlStreamReader.ReadElementTextBehaviour = ...  # 0x0
        IncludeChildElements: QXmlStreamReader.ReadElementTextBehaviour = ...  # 0x1
        SkipChildElements: QXmlStreamReader.ReadElementTextBehaviour = ...  # 0x2

    class TokenType(object):
        NoToken: QXmlStreamReader.TokenType = ...  # 0x0
        Invalid: QXmlStreamReader.TokenType = ...  # 0x1
        StartDocument: QXmlStreamReader.TokenType = ...  # 0x2
        EndDocument: QXmlStreamReader.TokenType = ...  # 0x3
        StartElement: QXmlStreamReader.TokenType = ...  # 0x4
        EndElement: QXmlStreamReader.TokenType = ...  # 0x5
        Characters: QXmlStreamReader.TokenType = ...  # 0x6
        Comment: QXmlStreamReader.TokenType = ...  # 0x7
        DTD: QXmlStreamReader.TokenType = ...  # 0x8
        EntityReference: QXmlStreamReader.TokenType = ...  # 0x9
        ProcessingInstruction: QXmlStreamReader.TokenType = ...  # 0xa
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, data: str): ...
    @typing.overload
    def __init__(self, data: bytes): ...
    @typing.overload
    def __init__(self, device: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def addData(self, data: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def addData(self, data: str): ...
    @typing.overload
    def addData(self, data: bytes): ...
    def addExtraNamespaceDeclaration(
        self, extraNamespaceDeclaraction: PySide2.QtCore.QXmlStreamNamespaceDeclaration
    ): ...
    def addExtraNamespaceDeclarations(
        self, extraNamespaceDeclaractions: typing.List
    ): ...
    def atEnd(self) -> bool: ...
    def attributes(self) -> PySide2.QtCore.QXmlStreamAttributes: ...
    def characterOffset(self) -> int: ...
    def clear(self): ...
    def columnNumber(self) -> int: ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def documentEncoding(self) -> str: ...
    def documentVersion(self) -> str: ...
    def dtdName(self) -> str: ...
    def dtdPublicId(self) -> str: ...
    def dtdSystemId(self) -> str: ...
    def entityDeclarations(self) -> typing.List: ...
    def entityExpansionLimit(self) -> int: ...
    def entityResolver(self) -> PySide2.QtCore.QXmlStreamEntityResolver: ...
    def error(self) -> PySide2.QtCore.QXmlStreamReader.Error: ...
    def errorString(self) -> str: ...
    def hasError(self) -> bool: ...
    def isCDATA(self) -> bool: ...
    def isCharacters(self) -> bool: ...
    def isComment(self) -> bool: ...
    def isDTD(self) -> bool: ...
    def isEndDocument(self) -> bool: ...
    def isEndElement(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isStandaloneDocument(self) -> bool: ...
    def isStartDocument(self) -> bool: ...
    def isStartElement(self) -> bool: ...
    def isWhitespace(self) -> bool: ...
    def lineNumber(self) -> int: ...
    def name(self) -> str: ...
    def namespaceDeclarations(self) -> typing.List: ...
    def namespaceProcessing(self) -> bool: ...
    def namespaceUri(self) -> str: ...
    def notationDeclarations(self) -> typing.List: ...
    def prefix(self) -> str: ...
    def processingInstructionData(self) -> str: ...
    def processingInstructionTarget(self) -> str: ...
    def qualifiedName(self) -> str: ...
    def raiseError(self, message: str = ...): ...
    def readElementText(
        self, behaviour: PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour = ...
    ) -> str: ...
    def readNext(self) -> PySide2.QtCore.QXmlStreamReader.TokenType: ...
    def readNextStartElement(self) -> bool: ...
    def setDevice(self, device: PySide2.QtCore.QIODevice): ...
    def setEntityExpansionLimit(self, limit: int): ...
    def setEntityResolver(self, resolver: PySide2.QtCore.QXmlStreamEntityResolver): ...
    def setNamespaceProcessing(self, arg__1: bool): ...
    def skipCurrentElement(self): ...
    def text(self) -> str: ...
    def tokenString(self) -> str: ...
    def tokenType(self) -> PySide2.QtCore.QXmlStreamReader.TokenType: ...

class QXmlStreamWriter(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, array: PySide2.QtCore.QByteArray): ...
    @typing.overload
    def __init__(self, device: PySide2.QtCore.QIODevice): ...
    def autoFormatting(self) -> bool: ...
    def autoFormattingIndent(self) -> int: ...
    def codec(self) -> PySide2.QtCore.QTextCodec: ...
    def device(self) -> PySide2.QtCore.QIODevice: ...
    def hasError(self) -> bool: ...
    def setAutoFormatting(self, arg__1: bool): ...
    def setAutoFormattingIndent(self, spacesOrTabs: int): ...
    @typing.overload
    def setCodec(self, codec: PySide2.QtCore.QTextCodec): ...
    @typing.overload
    def setCodec(self, codecName: bytes): ...
    def setDevice(self, device: PySide2.QtCore.QIODevice): ...
    @typing.overload
    def writeAttribute(self, attribute: PySide2.QtCore.QXmlStreamAttribute): ...
    @typing.overload
    def writeAttribute(self, namespaceUri: str, name: str, value: str): ...
    @typing.overload
    def writeAttribute(self, qualifiedName: str, value: str): ...
    def writeAttributes(self, attributes: PySide2.QtCore.QXmlStreamAttributes): ...
    def writeCDATA(self, text: str): ...
    def writeCharacters(self, text: str): ...
    def writeComment(self, text: str): ...
    def writeCurrentToken(self, reader: PySide2.QtCore.QXmlStreamReader): ...
    def writeDTD(self, dtd: str): ...
    def writeDefaultNamespace(self, namespaceUri: str): ...
    @typing.overload
    def writeEmptyElement(self, namespaceUri: str, name: str): ...
    @typing.overload
    def writeEmptyElement(self, qualifiedName: str): ...
    def writeEndDocument(self): ...
    def writeEndElement(self): ...
    def writeEntityReference(self, name: str): ...
    def writeNamespace(self, namespaceUri: str, prefix: str = ...): ...
    def writeProcessingInstruction(self, target: str, data: str = ...): ...
    @typing.overload
    def writeStartDocument(self): ...
    @typing.overload
    def writeStartDocument(self, version: str): ...
    @typing.overload
    def writeStartDocument(self, version: str, standalone: bool): ...
    @typing.overload
    def writeStartElement(self, namespaceUri: str, name: str): ...
    @typing.overload
    def writeStartElement(self, qualifiedName: str): ...
    @typing.overload
    def writeTextElement(self, namespaceUri: str, name: str, text: str): ...
    @typing.overload
    def writeTextElement(self, qualifiedName: str, text: str): ...

class Qt(Shiboken.Object):
    ImPlatformData: Qt = ...  # -0x80000000
    WindowFullscreenButtonHint: Qt = ...  # -0x80000000
    KeyboardModifierMask: Qt = ...  # -0x2000000
    MODIFIER_MASK: Qt = ...  # -0x2000000
    ImhExclusiveInputMask: Qt = ...  # -0x10000
    ImQueryAll: Qt = ...  # -0x1
    LastGestureType: Qt = ...  # -0x1
    LowEventPriority: Qt = ...  # -0x1
    MouseButtonMask: Qt = ...  # -0x1
    WhiteSpaceModeUndefined: Qt = ...  # -0x1
    AA_ImmediateWidgetCreation: Qt = ...  # 0x0
    AbsoluteSize: Qt = ...  # 0x0
    AnchorLeft: Qt = ...  # 0x0
    ApplicationSuspended: Qt = ...  # 0x0
    ArrowCursor: Qt = ...  # 0x0
    AscendingOrder: Qt = ...  # 0x0
    AutoColor: Qt = ...  # 0x0
    AutoConnection: Qt = ...  # 0x0
    AutoDither: Qt = ...  # 0x0
    BeginNativeGesture: Qt = ...  # 0x0
    CaseInsensitive: Qt = ...  # 0x0
    ChecksumIso3309: Qt = ...  # 0x0
    ContainsItemShape: Qt = ...  # 0x0
    DeviceCoordinates: Qt = ...  # 0x0
    DiffuseDither: Qt = ...  # 0x0
    DisplayRole: Qt = ...  # 0x0
    ElideLeft: Qt = ...  # 0x0
    EnterKeyDefault: Qt = ...  # 0x0
    ExactHit: Qt = ...  # 0x0
    FastTransformation: Qt = ...  # 0x0
    FindDirectChildrenOnly: Qt = ...  # 0x0
    FlatCap: Qt = ...  # 0x0
    IgnoreAction: Qt = ...  # 0x0
    IgnoreAspectRatio: Qt = ...  # 0x0
    ImhNone: Qt = ...  # 0x0
    KeepEmptyParts: Qt = ...  # 0x0
    LeftToRight: Qt = ...  # 0x0
    LocalTime: Qt = ...  # 0x0
    LogicalMoveStyle: Qt = ...  # 0x0
    MaskInColor: Qt = ...  # 0x0
    MatchExactly: Qt = ...  # 0x0
    MinimumSize: Qt = ...  # 0x0
    MiterJoin: Qt = ...  # 0x0
    MouseEventNotSynthesized: Qt = ...  # 0x0
    MouseFocusReason: Qt = ...  # 0x0
    NavigationModeNone: Qt = ...  # 0x0
    NoArrow: Qt = ...  # 0x0
    NoBrush: Qt = ...  # 0x0
    NoButton: Qt = ...  # 0x0
    NoClip: Qt = ...  # 0x0
    NoContextMenu: Qt = ...  # 0x0
    NoDockWidgetArea: Qt = ...  # 0x0
    NoFocus: Qt = ...  # 0x0
    NoGesture: Qt = ...  # 0x0
    NoItemFlags: Qt = ...  # 0x0
    NoModifier: Qt = ...  # 0x0
    NoPen: Qt = ...  # 0x0
    NoScrollPhase: Qt = ...  # 0x0
    NoSection: Qt = ...  # 0x0
    NoTabFocus: Qt = ...  # 0x0
    NoTextInteraction: Qt = ...  # 0x0
    NoToolBarArea: Qt = ...  # 0x0
    NonModal: Qt = ...  # 0x0
    NormalEventPriority: Qt = ...  # 0x0
    OddEvenFill: Qt = ...  # 0x0
    PlainText: Qt = ...  # 0x0
    PreciseTimer: Qt = ...  # 0x0
    PrimaryOrientation: Qt = ...  # 0x0
    ReplaceSelection: Qt = ...  # 0x0
    ScrollBarAsNeeded: Qt = ...  # 0x0
    StretchTile: Qt = ...  # 0x0
    TextDate: Qt = ...  # 0x0
    ThresholdAlphaDither: Qt = ...  # 0x0
    ToolButtonIconOnly: Qt = ...  # 0x0
    TopLeftCorner: Qt = ...  # 0x0
    TransparentMode: Qt = ...  # 0x0
    UI_General: Qt = ...  # 0x0
    UNICODE_ACCEL: Qt = ...  # 0x0
    Unchecked: Qt = ...  # 0x0
    WA_Disabled: Qt = ...  # 0x0
    WhiteSpaceNormal: Qt = ...  # 0x0
    Widget: Qt = ...  # 0x0
    WidgetShortcut: Qt = ...  # 0x0
    WindowNoState: Qt = ...  # 0x0
    XAxis: Qt = ...  # 0x0
    color0: Qt = ...  # 0x0
    AA_MSWindowsUseDirect3DByDefault: Qt = ...  # 0x1
    AddToSelection: Qt = ...  # 0x1
    AlignLeading: Qt = ...  # 0x1
    AlignLeft: Qt = ...  # 0x1
    AnchorHorizontalCenter: Qt = ...  # 0x1
    ApplicationHidden: Qt = ...  # 0x1
    CaseSensitive: Qt = ...  # 0x1
    ChecksumItuV41: Qt = ...  # 0x1
    CoarseTimer: Qt = ...  # 0x1
    CopyAction: Qt = ...  # 0x1
    DecorationRole: Qt = ...  # 0x1
    DefaultContextMenu: Qt = ...  # 0x1
    DescendingOrder: Qt = ...  # 0x1
    DirectConnection: Qt = ...  # 0x1
    DontStartGestureOnChildren: Qt = ...  # 0x1
    ElideRight: Qt = ...  # 0x1
    EndNativeGesture: Qt = ...  # 0x1
    EnterKeyReturn: Qt = ...  # 0x1
    FindChildrenRecursively: Qt = ...  # 0x1
    FuzzyHit: Qt = ...  # 0x1
    GestureStarted: Qt = ...  # 0x1
    HighEventPriority: Qt = ...  # 0x1
    Horizontal: Qt = ...  # 0x1
    ISODate: Qt = ...  # 0x1
    ImEnabled: Qt = ...  # 0x1
    ImhHiddenText: Qt = ...  # 0x1
    IntersectsItemShape: Qt = ...  # 0x1
    ItemIsSelectable: Qt = ...  # 0x1
    KeepAspectRatio: Qt = ...  # 0x1
    LeftButton: Qt = ...  # 0x1
    LeftDockWidgetArea: Qt = ...  # 0x1
    LeftSection: Qt = ...  # 0x1
    LeftToolBarArea: Qt = ...  # 0x1
    LogicalCoordinates: Qt = ...  # 0x1
    MaskOutColor: Qt = ...  # 0x1
    MatchContains: Qt = ...  # 0x1
    Monday: Qt = ...  # 0x1
    MouseEventCreatedDoubleClick: Qt = ...  # 0x1
    MouseEventSynthesizedBySystem: Qt = ...  # 0x1
    NavigationModeKeypadTabOrder: Qt = ...  # 0x1
    OpaqueMode: Qt = ...  # 0x1
    PartiallyChecked: Qt = ...  # 0x1
    PortraitOrientation: Qt = ...  # 0x1
    PreferredSize: Qt = ...  # 0x1
    RelativeSize: Qt = ...  # 0x1
    RepeatTile: Qt = ...  # 0x1
    ReplaceClip: Qt = ...  # 0x1
    RichText: Qt = ...  # 0x1
    RightToLeft: Qt = ...  # 0x1
    ScrollBarAlwaysOff: Qt = ...  # 0x1
    ScrollBegin: Qt = ...  # 0x1
    SkipEmptyParts: Qt = ...  # 0x1
    SmoothTransformation: Qt = ...  # 0x1
    SolidLine: Qt = ...  # 0x1
    SolidPattern: Qt = ...  # 0x1
    TabFocus: Qt = ...  # 0x1
    TabFocusReason: Qt = ...  # 0x1
    TabFocusTextControls: Qt = ...  # 0x1
    TapGesture: Qt = ...  # 0x1
    TextSelectableByMouse: Qt = ...  # 0x1
    ToolButtonTextOnly: Qt = ...  # 0x1
    TopEdge: Qt = ...  # 0x1
    TopRightCorner: Qt = ...  # 0x1
    TouchPointPressed: Qt = ...  # 0x1
    UI_AnimateMenu: Qt = ...  # 0x1
    UTC: Qt = ...  # 0x1
    UpArrow: Qt = ...  # 0x1
    UpArrowCursor: Qt = ...  # 0x1
    VisualMoveStyle: Qt = ...  # 0x1
    WA_UnderMouse: Qt = ...  # 0x1
    WhiteSpacePre: Qt = ...  # 0x1
    WindingFill: Qt = ...  # 0x1
    Window: Qt = ...  # 0x1
    WindowMinimized: Qt = ...  # 0x1
    WindowModal: Qt = ...  # 0x1
    WindowShortcut: Qt = ...  # 0x1
    YAxis: Qt = ...  # 0x1
    color1: Qt = ...  # 0x1
    AA_DontShowIconsInMenus: Qt = ...  # 0x2
    ActionsContextMenu: Qt = ...  # 0x2
    AlignRight: Qt = ...  # 0x2
    AlignTrailing: Qt = ...  # 0x2
    AnchorRight: Qt = ...  # 0x2
    ApplicationInactive: Qt = ...  # 0x2
    ApplicationModal: Qt = ...  # 0x2
    ApplicationShortcut: Qt = ...  # 0x2
    AutoText: Qt = ...  # 0x2
    BacktabFocusReason: Qt = ...  # 0x2
    BottomLeftCorner: Qt = ...  # 0x2
    Checked: Qt = ...  # 0x2
    ClickFocus: Qt = ...  # 0x2
    ContainsItemBoundingRect: Qt = ...  # 0x2
    CrossCursor: Qt = ...  # 0x2
    DashLine: Qt = ...  # 0x2
    Dense1Pattern: Qt = ...  # 0x2
    DownArrow: Qt = ...  # 0x2
    EditRole: Qt = ...  # 0x2
    ElideMiddle: Qt = ...  # 0x2
    EnterKeyDone: Qt = ...  # 0x2
    GestureUpdated: Qt = ...  # 0x2
    ImCursorRectangle: Qt = ...  # 0x2
    ImMicroFocus: Qt = ...  # 0x2
    ImhSensitiveData: Qt = ...  # 0x2
    IntersectClip: Qt = ...  # 0x2
    ItemIsEditable: Qt = ...  # 0x2
    KeepAspectRatioByExpanding: Qt = ...  # 0x2
    LandscapeOrientation: Qt = ...  # 0x2
    LayoutDirectionAuto: Qt = ...  # 0x2
    LeftEdge: Qt = ...  # 0x2
    LocalDate: Qt = ...  # 0x2
    MatchStartsWith: Qt = ...  # 0x2
    MaximumSize: Qt = ...  # 0x2
    MonoOnly: Qt = ...  # 0x2
    MouseEventSynthesizedByQt: Qt = ...  # 0x2
    MoveAction: Qt = ...  # 0x2
    NavigationModeKeypadDirectional: Qt = ...  # 0x2
    OffsetFromUTC: Qt = ...  # 0x2
    PanNativeGesture: Qt = ...  # 0x2
    QueuedConnection: Qt = ...  # 0x2
    ReceivePartialGestures: Qt = ...  # 0x2
    RightButton: Qt = ...  # 0x2
    RightDockWidgetArea: Qt = ...  # 0x2
    RightToolBarArea: Qt = ...  # 0x2
    RoundTile: Qt = ...  # 0x2
    ScrollBarAlwaysOn: Qt = ...  # 0x2
    ScrollUpdate: Qt = ...  # 0x2
    SystemLocaleDate: Qt = ...  # 0x2
    TabFocusListControls: Qt = ...  # 0x2
    TapAndHoldGesture: Qt = ...  # 0x2
    TextSelectableByKeyboard: Qt = ...  # 0x2
    ToolButtonTextBesideIcon: Qt = ...  # 0x2
    TopLeftSection: Qt = ...  # 0x2
    TouchPointMoved: Qt = ...  # 0x2
    Tuesday: Qt = ...  # 0x2
    UI_FadeMenu: Qt = ...  # 0x2
    Vertical: Qt = ...  # 0x2
    VeryCoarseTimer: Qt = ...  # 0x2
    WA_MouseTracking: Qt = ...  # 0x2
    WhiteSpaceNoWrap: Qt = ...  # 0x2
    WindowMaximized: Qt = ...  # 0x2
    ZAxis: Qt = ...  # 0x2
    black: Qt = ...  # 0x2
    AA_NativeWindows: Qt = ...  # 0x3
    ActiveWindowFocusReason: Qt = ...  # 0x3
    AnchorTop: Qt = ...  # 0x3
    BlockingQueuedConnection: Qt = ...  # 0x3
    BottomRightCorner: Qt = ...  # 0x3
    ColorMode_Mask: Qt = ...  # 0x3
    ColorOnly: Qt = ...  # 0x3
    CustomContextMenu: Qt = ...  # 0x3
    Dense2Pattern: Qt = ...  # 0x3
    Dialog: Qt = ...  # 0x3
    DotLine: Qt = ...  # 0x3
    ElideNone: Qt = ...  # 0x3
    EnterKeyGo: Qt = ...  # 0x3
    GestureFinished: Qt = ...  # 0x3
    IntersectsItemBoundingRect: Qt = ...  # 0x3
    LeftArrow: Qt = ...  # 0x3
    LocaleDate: Qt = ...  # 0x3
    MarkdownText: Qt = ...  # 0x3
    MatchEndsWith: Qt = ...  # 0x3
    MinimumDescent: Qt = ...  # 0x3
    MouseEventSynthesizedByApplication: Qt = ...  # 0x3
    NavigationModeCursorAuto: Qt = ...  # 0x3
    PanGesture: Qt = ...  # 0x3
    ScrollEnd: Qt = ...  # 0x3
    TimeZone: Qt = ...  # 0x3
    ToolButtonTextUnderIcon: Qt = ...  # 0x3
    ToolTipRole: Qt = ...  # 0x3
    TopSection: Qt = ...  # 0x3
    UI_AnimateCombo: Qt = ...  # 0x3
    WA_ContentsPropagated: Qt = ...  # 0x3
    WaitCursor: Qt = ...  # 0x3
    Wednesday: Qt = ...  # 0x3
    WidgetWithChildrenShortcut: Qt = ...  # 0x3
    ZoomNativeGesture: Qt = ...  # 0x3
    white: Qt = ...  # 0x3
    AA_DontCreateNativeWidgetSiblings: Qt = ...  # 0x4
    AlignHCenter: Qt = ...  # 0x4
    AnchorVerticalCenter: Qt = ...  # 0x4
    ApplicationActive: Qt = ...  # 0x4
    DashDotLine: Qt = ...  # 0x4
    Dense3Pattern: Qt = ...  # 0x4
    EnterKeySend: Qt = ...  # 0x4
    GestureCanceled: Qt = ...  # 0x4
    IBeamCursor: Qt = ...  # 0x4
    IgnoredGesturesPropagateToParent: Qt = ...  # 0x4
    ImFont: Qt = ...  # 0x4
    ImhNoAutoUppercase: Qt = ...  # 0x4
    InvertedPortraitOrientation: Qt = ...  # 0x4
    ItemIsDragEnabled: Qt = ...  # 0x4
    LinkAction: Qt = ...  # 0x4
    LinksAccessibleByMouse: Qt = ...  # 0x4
    MatchRegExp: Qt = ...  # 0x4
    MidButton: Qt = ...  # 0x4
    MiddleButton: Qt = ...  # 0x4
    NDockWidgetAreas: Qt = ...  # 0x4
    NSizeHints: Qt = ...  # 0x4
    NToolBarAreas: Qt = ...  # 0x4
    NavigationModeCursorForceVisible: Qt = ...  # 0x4
    OrderedAlphaDither: Qt = ...  # 0x4
    PinchGesture: Qt = ...  # 0x4
    PopupFocusReason: Qt = ...  # 0x4
    PreventContextMenu: Qt = ...  # 0x4
    RightArrow: Qt = ...  # 0x4
    RightEdge: Qt = ...  # 0x4
    ScrollMomentum: Qt = ...  # 0x4
    SmartZoomNativeGesture: Qt = ...  # 0x4
    StatusTipRole: Qt = ...  # 0x4
    SystemLocaleShortDate: Qt = ...  # 0x4
    Thursday: Qt = ...  # 0x4
    ToolButtonFollowStyle: Qt = ...  # 0x4
    TopDockWidgetArea: Qt = ...  # 0x4
    TopRightSection: Qt = ...  # 0x4
    TopToolBarArea: Qt = ...  # 0x4
    TouchPointStationary: Qt = ...  # 0x4
    UI_AnimateTooltip: Qt = ...  # 0x4
    WA_NoBackground: Qt = ...  # 0x4
    WA_OpaquePaintEvent: Qt = ...  # 0x4
    WindowFullScreen: Qt = ...  # 0x4
    darkGray: Qt = ...  # 0x4
    AA_MacPluginApplication: Qt = ...  # 0x5
    AA_PluginApplication: Qt = ...  # 0x5
    AnchorBottom: Qt = ...  # 0x5
    DashDotDotLine: Qt = ...  # 0x5
    Dense4Pattern: Qt = ...  # 0x5
    EnterKeySearch: Qt = ...  # 0x5
    Friday: Qt = ...  # 0x5
    MatchWildcard: Qt = ...  # 0x5
    RightSection: Qt = ...  # 0x5
    RotateNativeGesture: Qt = ...  # 0x5
    Sheet: Qt = ...  # 0x5
    ShortcutFocusReason: Qt = ...  # 0x5
    SizeVerCursor: Qt = ...  # 0x5
    SwipeGesture: Qt = ...  # 0x5
    SystemLocaleLongDate: Qt = ...  # 0x5
    UI_FadeTooltip: Qt = ...  # 0x5
    WA_StaticContents: Qt = ...  # 0x5
    WhatsThisRole: Qt = ...  # 0x5
    gray: Qt = ...  # 0x5
    AA_DontUseNativeMenuBar: Qt = ...  # 0x6
    BottomRightSection: Qt = ...  # 0x6
    CustomDashLine: Qt = ...  # 0x6
    DefaultLocaleShortDate: Qt = ...  # 0x6
    Dense5Pattern: Qt = ...  # 0x6
    EnterKeyNext: Qt = ...  # 0x6
    FontRole: Qt = ...  # 0x6
    MenuBarFocusReason: Qt = ...  # 0x6
    Saturday: Qt = ...  # 0x6
    SizeHorCursor: Qt = ...  # 0x6
    SwipeNativeGesture: Qt = ...  # 0x6
    UI_AnimateToolBox: Qt = ...  # 0x6
    lightGray: Qt = ...  # 0x6
    AA_MacDontSwapCtrlAndMeta: Qt = ...  # 0x7
    BottomSection: Qt = ...  # 0x7
    DefaultLocaleLongDate: Qt = ...  # 0x7
    Dense6Pattern: Qt = ...  # 0x7
    Drawer: Qt = ...  # 0x7
    EnterKeyPrevious: Qt = ...  # 0x7
    OtherFocusReason: Qt = ...  # 0x7
    SizeBDiagCursor: Qt = ...  # 0x7
    Sunday: Qt = ...  # 0x7
    TextAlignmentRole: Qt = ...  # 0x7
    WA_LaidOut: Qt = ...  # 0x7
    red: Qt = ...  # 0x7
    AA_Use96Dpi: Qt = ...  # 0x8
    AlignJustify: Qt = ...  # 0x8
    BackButton: Qt = ...  # 0x8
    BackgroundColorRole: Qt = ...  # 0x8
    BackgroundRole: Qt = ...  # 0x8
    BottomDockWidgetArea: Qt = ...  # 0x8
    BottomEdge: Qt = ...  # 0x8
    BottomLeftSection: Qt = ...  # 0x8
    BottomToolBarArea: Qt = ...  # 0x8
    Dense7Pattern: Qt = ...  # 0x8
    DiffuseAlphaDither: Qt = ...  # 0x8
    ExtraButton1: Qt = ...  # 0x8
    ImCursorPosition: Qt = ...  # 0x8
    ImhPreferNumbers: Qt = ...  # 0x8
    InvertedLandscapeOrientation: Qt = ...  # 0x8
    ItemIsDropEnabled: Qt = ...  # 0x8
    LinksAccessibleByKeyboard: Qt = ...  # 0x8
    MatchFixedString: Qt = ...  # 0x8
    NoFocusReason: Qt = ...  # 0x8
    RFC2822Date: Qt = ...  # 0x8
    SizeFDiagCursor: Qt = ...  # 0x8
    TouchPointReleased: Qt = ...  # 0x8
    WA_PaintOnScreen: Qt = ...  # 0x8
    WindowActive: Qt = ...  # 0x8
    XButton1: Qt = ...  # 0x8
    green: Qt = ...  # 0x8
    AA_DisableNativeVirtualKeyboard: Qt = ...  # 0x9
    ForegroundRole: Qt = ...  # 0x9
    HorPattern: Qt = ...  # 0x9
    ISODateWithMs: Qt = ...  # 0x9
    MatchRegularExpression: Qt = ...  # 0x9
    Popup: Qt = ...  # 0x9
    SizeAllCursor: Qt = ...  # 0x9
    TextColorRole: Qt = ...  # 0x9
    TitleBarArea: Qt = ...  # 0x9
    WA_NoSystemBackground: Qt = ...  # 0x9
    blue: Qt = ...  # 0x9
    AA_X11InitThreads: Qt = ...  # 0xa
    BlankCursor: Qt = ...  # 0xa
    CheckStateRole: Qt = ...  # 0xa
    VerPattern: Qt = ...  # 0xa
    WA_UpdatesDisabled: Qt = ...  # 0xa
    cyan: Qt = ...  # 0xa
    AA_SynthesizeTouchForUnhandledMouseEvents: Qt = ...  # 0xb
    AccessibleTextRole: Qt = ...  # 0xb
    CrossPattern: Qt = ...  # 0xb
    SplitVCursor: Qt = ...  # 0xb
    StrongFocus: Qt = ...  # 0xb
    Tool: Qt = ...  # 0xb
    WA_Mapped: Qt = ...  # 0xb
    magenta: Qt = ...  # 0xb
    AA_SynthesizeMouseForUnhandledTouchEvents: Qt = ...  # 0xc
    AccessibleDescriptionRole: Qt = ...  # 0xc
    AlphaDither_Mask: Qt = ...  # 0xc
    BDiagPattern: Qt = ...  # 0xc
    NoAlpha: Qt = ...  # 0xc
    SplitHCursor: Qt = ...  # 0xc
    WA_MacNoClickThrough: Qt = ...  # 0xc
    yellow: Qt = ...  # 0xc
    AA_UseHighDpiPixmaps: Qt = ...  # 0xd
    FDiagPattern: Qt = ...  # 0xd
    PointingHandCursor: Qt = ...  # 0xd
    SizeHintRole: Qt = ...  # 0xd
    TextBrowserInteraction: Qt = ...  # 0xd
    ToolTip: Qt = ...  # 0xd
    darkRed: Qt = ...  # 0xd
    AA_ForceRasterWidgets: Qt = ...  # 0xe
    DiagCrossPattern: Qt = ...  # 0xe
    ForbiddenCursor: Qt = ...  # 0xe
    InitialSortOrderRole: Qt = ...  # 0xe
    WA_InputMethodEnabled: Qt = ...  # 0xe
    darkGreen: Qt = ...  # 0xe
    AA_UseDesktopOpenGL: Qt = ...  # 0xf
    AllDockWidgetAreas: Qt = ...  # 0xf
    AllToolBarAreas: Qt = ...  # 0xf
    DockWidgetArea_Mask: Qt = ...  # 0xf
    LinearGradientPattern: Qt = ...  # 0xf
    MPenStyle: Qt = ...  # 0xf
    SplashScreen: Qt = ...  # 0xf
    ToolBarArea_Mask: Qt = ...  # 0xf
    WA_WState_Visible: Qt = ...  # 0xf
    WhatsThisCursor: Qt = ...  # 0xf
    WheelFocus: Qt = ...  # 0xf
    darkBlue: Qt = ...  # 0xf
    AA_UseOpenGLES: Qt = ...  # 0x10
    AlignAbsolute: Qt = ...  # 0x10
    BusyCursor: Qt = ...  # 0x10
    ExtraButton2: Qt = ...  # 0x10
    ForwardButton: Qt = ...  # 0x10
    ImSurroundingText: Qt = ...  # 0x10
    ImhPreferUppercase: Qt = ...  # 0x10
    ItemIsUserCheckable: Qt = ...  # 0x10
    MatchCaseSensitive: Qt = ...  # 0x10
    OrderedDither: Qt = ...  # 0x10
    RadialGradientPattern: Qt = ...  # 0x10
    SquareCap: Qt = ...  # 0x10
    TextEditable: Qt = ...  # 0x10
    WA_WState_Hidden: Qt = ...  # 0x10
    XButton2: Qt = ...  # 0x10
    darkCyan: Qt = ...  # 0x10
    AA_UseSoftwareOpenGL: Qt = ...  # 0x11
    ConicalGradientPattern: Qt = ...  # 0x11
    Desktop: Qt = ...  # 0x11
    OpenHandCursor: Qt = ...  # 0x11
    darkMagenta: Qt = ...  # 0x11
    AA_ShareOpenGLContexts: Qt = ...  # 0x12
    ClosedHandCursor: Qt = ...  # 0x12
    SubWindow: Qt = ...  # 0x12
    darkYellow: Qt = ...  # 0x12
    AA_SetPalette: Qt = ...  # 0x13
    DragCopyCursor: Qt = ...  # 0x13
    TextEditorInteraction: Qt = ...  # 0x13
    transparent: Qt = ...  # 0x13
    AA_EnableHighDpiScaling: Qt = ...  # 0x14
    DragMoveCursor: Qt = ...  # 0x14
    AA_DisableHighDpiScaling: Qt = ...  # 0x15
    DragLinkCursor: Qt = ...  # 0x15
    LastCursor: Qt = ...  # 0x15
    AA_UseStyleSheetPropagationInWidgetStyles: Qt = ...  # 0x16
    AA_DontUseNativeDialogs: Qt = ...  # 0x17
    AA_SynthesizeMouseForUnhandledTabletEvents: Qt = ...  # 0x18
    BitmapCursor: Qt = ...  # 0x18
    TexturePattern: Qt = ...  # 0x18
    AA_CompressHighFrequencyEvents: Qt = ...  # 0x19
    CustomCursor: Qt = ...  # 0x19
    AA_DontCheckOpenGLContextThreadAffinity: Qt = ...  # 0x1a
    AA_DisableShaderDiskCache: Qt = ...  # 0x1b
    DisplayPropertyRole: Qt = ...  # 0x1b
    AA_DontShowShortcutsInContextMenus: Qt = ...  # 0x1c
    DecorationPropertyRole: Qt = ...  # 0x1c
    AA_CompressTabletEvents: Qt = ...  # 0x1d
    ToolTipPropertyRole: Qt = ...  # 0x1d
    AA_DisableWindowContextHelpButton: Qt = ...  # 0x1e
    StatusTipPropertyRole: Qt = ...  # 0x1e
    AA_DisableSessionManager: Qt = ...  # 0x1f
    AlignHorizontal_Mask: Qt = ...  # 0x1f
    WhatsThisPropertyRole: Qt = ...  # 0x1f
    AA_AttributeCount: Qt = ...  # 0x20
    AlignTop: Qt = ...  # 0x20
    ExtraButton3: Qt = ...  # 0x20
    ImCurrentSelection: Qt = ...  # 0x20
    ImhPreferLowercase: Qt = ...  # 0x20
    ItemIsEnabled: Qt = ...  # 0x20
    Key_Any: Qt = ...  # 0x20
    Key_Space: Qt = ...  # 0x20
    MatchWrap: Qt = ...  # 0x20
    RoundCap: Qt = ...  # 0x20
    TaskButton: Qt = ...  # 0x20
    ThresholdDither: Qt = ...  # 0x20
    WA_ForceDisabled: Qt = ...  # 0x20
    ForeignWindow: Qt = ...  # 0x21
    Key_Exclam: Qt = ...  # 0x21
    WA_KeyCompression: Qt = ...  # 0x21
    Key_QuoteDbl: Qt = ...  # 0x22
    WA_PendingMoveEvent: Qt = ...  # 0x22
    Key_NumberSign: Qt = ...  # 0x23
    WA_PendingResizeEvent: Qt = ...  # 0x23
    Key_Dollar: Qt = ...  # 0x24
    WA_SetPalette: Qt = ...  # 0x24
    Key_Percent: Qt = ...  # 0x25
    WA_SetFont: Qt = ...  # 0x25
    Key_Ampersand: Qt = ...  # 0x26
    WA_SetCursor: Qt = ...  # 0x26
    Key_Apostrophe: Qt = ...  # 0x27
    WA_NoChildEventsFromChildren: Qt = ...  # 0x27
    Key_ParenLeft: Qt = ...  # 0x28
    Key_ParenRight: Qt = ...  # 0x29
    WA_WindowModified: Qt = ...  # 0x29
    Key_Asterisk: Qt = ...  # 0x2a
    WA_Resized: Qt = ...  # 0x2a
    Key_Plus: Qt = ...  # 0x2b
    WA_Moved: Qt = ...  # 0x2b
    Key_Comma: Qt = ...  # 0x2c
    WA_PendingUpdate: Qt = ...  # 0x2c
    Key_Minus: Qt = ...  # 0x2d
    WA_InvalidSize: Qt = ...  # 0x2d
    Key_Period: Qt = ...  # 0x2e
    WA_MacBrushedMetal: Qt = ...  # 0x2e
    WA_MacMetalStyle: Qt = ...  # 0x2e
    Key_Slash: Qt = ...  # 0x2f
    WA_CustomWhatsThis: Qt = ...  # 0x2f
    Dither_Mask: Qt = ...  # 0x30
    Key_0: Qt = ...  # 0x30
    MPenCapStyle: Qt = ...  # 0x30
    WA_LayoutOnEntireRect: Qt = ...  # 0x30
    Key_1: Qt = ...  # 0x31
    WA_OutsideWSRange: Qt = ...  # 0x31
    Key_2: Qt = ...  # 0x32
    WA_GrabbedShortcut: Qt = ...  # 0x32
    Key_3: Qt = ...  # 0x33
    WA_TransparentForMouseEvents: Qt = ...  # 0x33
    Key_4: Qt = ...  # 0x34
    WA_PaintUnclipped: Qt = ...  # 0x34
    Key_5: Qt = ...  # 0x35
    WA_SetWindowIcon: Qt = ...  # 0x35
    Key_6: Qt = ...  # 0x36
    WA_NoMouseReplay: Qt = ...  # 0x36
    Key_7: Qt = ...  # 0x37
    WA_DeleteOnClose: Qt = ...  # 0x37
    Key_8: Qt = ...  # 0x38
    WA_RightToLeft: Qt = ...  # 0x38
    Key_9: Qt = ...  # 0x39
    WA_SetLayoutDirection: Qt = ...  # 0x39
    Key_Colon: Qt = ...  # 0x3a
    WA_NoChildEventsForParent: Qt = ...  # 0x3a
    Key_Semicolon: Qt = ...  # 0x3b
    WA_ForceUpdatesDisabled: Qt = ...  # 0x3b
    Key_Less: Qt = ...  # 0x3c
    WA_WState_Created: Qt = ...  # 0x3c
    Key_Equal: Qt = ...  # 0x3d
    WA_WState_CompressKeys: Qt = ...  # 0x3d
    Key_Greater: Qt = ...  # 0x3e
    WA_WState_InPaintEvent: Qt = ...  # 0x3e
    Key_Question: Qt = ...  # 0x3f
    WA_WState_Reparented: Qt = ...  # 0x3f
    AlignBottom: Qt = ...  # 0x40
    BevelJoin: Qt = ...  # 0x40
    ExtraButton4: Qt = ...  # 0x40
    ImMaximumTextLength: Qt = ...  # 0x40
    ImhNoPredictiveText: Qt = ...  # 0x40
    ItemIsAutoTristate: Qt = ...  # 0x40
    ItemIsTristate: Qt = ...  # 0x40
    Key_At: Qt = ...  # 0x40
    MatchRecursive: Qt = ...  # 0x40
    PreferDither: Qt = ...  # 0x40
    WA_WState_ConfigPending: Qt = ...  # 0x40
    CoverWindow: Qt = ...  # 0x41
    Key_A: Qt = ...  # 0x41
    Key_B: Qt = ...  # 0x42
    WA_WState_Polished: Qt = ...  # 0x42
    Key_C: Qt = ...  # 0x43
    WA_WState_DND: Qt = ...  # 0x43
    Key_D: Qt = ...  # 0x44
    WA_WState_OwnSizePolicy: Qt = ...  # 0x44
    Key_E: Qt = ...  # 0x45
    WA_WState_ExplicitShowHide: Qt = ...  # 0x45
    Key_F: Qt = ...  # 0x46
    WA_ShowModal: Qt = ...  # 0x46
    Key_G: Qt = ...  # 0x47
    WA_MouseNoMask: Qt = ...  # 0x47
    Key_H: Qt = ...  # 0x48
    WA_GroupLeader: Qt = ...  # 0x48
    Key_I: Qt = ...  # 0x49
    WA_NoMousePropagation: Qt = ...  # 0x49
    Key_J: Qt = ...  # 0x4a
    WA_Hover: Qt = ...  # 0x4a
    Key_K: Qt = ...  # 0x4b
    WA_InputMethodTransparent: Qt = ...  # 0x4b
    Key_L: Qt = ...  # 0x4c
    WA_QuitOnClose: Qt = ...  # 0x4c
    Key_M: Qt = ...  # 0x4d
    WA_KeyboardFocusChange: Qt = ...  # 0x4d
    Key_N: Qt = ...  # 0x4e
    WA_AcceptDrops: Qt = ...  # 0x4e
    Key_O: Qt = ...  # 0x4f
    WA_DropSiteRegistered: Qt = ...  # 0x4f
    WA_ForceAcceptDrops: Qt = ...  # 0x4f
    Key_P: Qt = ...  # 0x50
    WA_WindowPropagation: Qt = ...  # 0x50
    Key_Q: Qt = ...  # 0x51
    WA_NoX11EventCompression: Qt = ...  # 0x51
    Key_R: Qt = ...  # 0x52
    WA_TintedBackground: Qt = ...  # 0x52
    Key_S: Qt = ...  # 0x53
    WA_X11OpenGLOverlay: Qt = ...  # 0x53
    Key_T: Qt = ...  # 0x54
    WA_AlwaysShowToolTips: Qt = ...  # 0x54
    Key_U: Qt = ...  # 0x55
    WA_MacOpaqueSizeGrip: Qt = ...  # 0x55
    Key_V: Qt = ...  # 0x56
    WA_SetStyle: Qt = ...  # 0x56
    Key_W: Qt = ...  # 0x57
    WA_SetLocale: Qt = ...  # 0x57
    Key_X: Qt = ...  # 0x58
    WA_MacShowFocusRect: Qt = ...  # 0x58
    Key_Y: Qt = ...  # 0x59
    WA_MacNormalSize: Qt = ...  # 0x59
    Key_Z: Qt = ...  # 0x5a
    WA_MacSmallSize: Qt = ...  # 0x5a
    Key_BracketLeft: Qt = ...  # 0x5b
    WA_MacMiniSize: Qt = ...  # 0x5b
    Key_Backslash: Qt = ...  # 0x5c
    WA_LayoutUsesWidgetRect: Qt = ...  # 0x5c
    Key_BracketRight: Qt = ...  # 0x5d
    WA_StyledBackground: Qt = ...  # 0x5d
    Key_AsciiCircum: Qt = ...  # 0x5e
    WA_MSWindowsUseDirect3D: Qt = ...  # 0x5e
    Key_Underscore: Qt = ...  # 0x5f
    WA_CanHostQMdiSubWindowTitleBar: Qt = ...  # 0x5f
    Key_QuoteLeft: Qt = ...  # 0x60
    WA_MacAlwaysShowToolWindow: Qt = ...  # 0x60
    WA_StyleSheet: Qt = ...  # 0x61
    WA_ShowWithoutActivating: Qt = ...  # 0x62
    WA_X11BypassTransientForHint: Qt = ...  # 0x63
    WA_NativeWindow: Qt = ...  # 0x64
    WA_DontCreateNativeAncestors: Qt = ...  # 0x65
    WA_MacVariableSize: Qt = ...  # 0x66
    WA_DontShowOnScreen: Qt = ...  # 0x67
    WA_X11NetWmWindowTypeDesktop: Qt = ...  # 0x68
    WA_X11NetWmWindowTypeDock: Qt = ...  # 0x69
    WA_X11NetWmWindowTypeToolBar: Qt = ...  # 0x6a
    WA_X11NetWmWindowTypeMenu: Qt = ...  # 0x6b
    WA_X11NetWmWindowTypeUtility: Qt = ...  # 0x6c
    WA_X11NetWmWindowTypeSplash: Qt = ...  # 0x6d
    WA_X11NetWmWindowTypeDialog: Qt = ...  # 0x6e
    WA_X11NetWmWindowTypeDropDownMenu: Qt = ...  # 0x6f
    WA_X11NetWmWindowTypePopupMenu: Qt = ...  # 0x70
    WA_X11NetWmWindowTypeToolTip: Qt = ...  # 0x71
    WA_X11NetWmWindowTypeNotification: Qt = ...  # 0x72
    WA_X11NetWmWindowTypeCombo: Qt = ...  # 0x73
    WA_X11NetWmWindowTypeDND: Qt = ...  # 0x74
    WA_MacFrameworkScaled: Qt = ...  # 0x75
    WA_SetWindowModality: Qt = ...  # 0x76
    WA_WState_WindowOpacitySet: Qt = ...  # 0x77
    WA_TranslucentBackground: Qt = ...  # 0x78
    WA_AcceptTouchEvents: Qt = ...  # 0x79
    WA_WState_AcceptedTouchBeginEvent: Qt = ...  # 0x7a
    Key_BraceLeft: Qt = ...  # 0x7b
    WA_TouchPadAcceptSingleTouchEvents: Qt = ...  # 0x7b
    Key_Bar: Qt = ...  # 0x7c
    Key_BraceRight: Qt = ...  # 0x7d
    Key_AsciiTilde: Qt = ...  # 0x7e
    WA_X11DoNotAcceptFocus: Qt = ...  # 0x7e
    WA_MacNoShadow: Qt = ...  # 0x7f
    AlignVCenter: Qt = ...  # 0x80
    AvoidDither: Qt = ...  # 0x80
    ExtraButton5: Qt = ...  # 0x80
    ImAnchorPosition: Qt = ...  # 0x80
    ImhDate: Qt = ...  # 0x80
    ItemNeverHasChildren: Qt = ...  # 0x80
    RoundJoin: Qt = ...  # 0x80
    UniqueConnection: Qt = ...  # 0x80
    WA_AlwaysStackOnTop: Qt = ...  # 0x80
    WA_TabletTracking: Qt = ...  # 0x81
    WA_ContentsMarginsRespectsSafeArea: Qt = ...  # 0x82
    WA_StyleSheetTarget: Qt = ...  # 0x83
    AlignCenter: Qt = ...  # 0x84
    WA_AttributeCount: Qt = ...  # 0x84
    Key_nobreakspace: Qt = ...  # 0xa0
    Key_exclamdown: Qt = ...  # 0xa1
    Key_cent: Qt = ...  # 0xa2
    Key_sterling: Qt = ...  # 0xa3
    Key_currency: Qt = ...  # 0xa4
    Key_yen: Qt = ...  # 0xa5
    Key_brokenbar: Qt = ...  # 0xa6
    Key_section: Qt = ...  # 0xa7
    Key_diaeresis: Qt = ...  # 0xa8
    Key_copyright: Qt = ...  # 0xa9
    Key_ordfeminine: Qt = ...  # 0xaa
    Key_guillemotleft: Qt = ...  # 0xab
    Key_notsign: Qt = ...  # 0xac
    Key_hyphen: Qt = ...  # 0xad
    Key_registered: Qt = ...  # 0xae
    Key_macron: Qt = ...  # 0xaf
    Key_degree: Qt = ...  # 0xb0
    Key_plusminus: Qt = ...  # 0xb1
    Key_twosuperior: Qt = ...  # 0xb2
    Key_threesuperior: Qt = ...  # 0xb3
    Key_acute: Qt = ...  # 0xb4
    Key_mu: Qt = ...  # 0xb5
    Key_paragraph: Qt = ...  # 0xb6
    Key_periodcentered: Qt = ...  # 0xb7
    Key_cedilla: Qt = ...  # 0xb8
    Key_onesuperior: Qt = ...  # 0xb9
    Key_masculine: Qt = ...  # 0xba
    Key_guillemotright: Qt = ...  # 0xbb
    Key_onequarter: Qt = ...  # 0xbc
    Key_onehalf: Qt = ...  # 0xbd
    Key_threequarters: Qt = ...  # 0xbe
    Key_questiondown: Qt = ...  # 0xbf
    DitherMode_Mask: Qt = ...  # 0xc0
    Key_Agrave: Qt = ...  # 0xc0
    Key_Aacute: Qt = ...  # 0xc1
    Key_Acircumflex: Qt = ...  # 0xc2
    Key_Atilde: Qt = ...  # 0xc3
    Key_Adiaeresis: Qt = ...  # 0xc4
    Key_Aring: Qt = ...  # 0xc5
    Key_AE: Qt = ...  # 0xc6
    Key_Ccedilla: Qt = ...  # 0xc7
    Key_Egrave: Qt = ...  # 0xc8
    Key_Eacute: Qt = ...  # 0xc9
    Key_Ecircumflex: Qt = ...  # 0xca
    Key_Ediaeresis: Qt = ...  # 0xcb
    Key_Igrave: Qt = ...  # 0xcc
    Key_Iacute: Qt = ...  # 0xcd
    Key_Icircumflex: Qt = ...  # 0xce
    Key_Idiaeresis: Qt = ...  # 0xcf
    Key_ETH: Qt = ...  # 0xd0
    Key_Ntilde: Qt = ...  # 0xd1
    Key_Ograve: Qt = ...  # 0xd2
    Key_Oacute: Qt = ...  # 0xd3
    Key_Ocircumflex: Qt = ...  # 0xd4
    Key_Otilde: Qt = ...  # 0xd5
    Key_Odiaeresis: Qt = ...  # 0xd6
    Key_multiply: Qt = ...  # 0xd7
    Key_Ooblique: Qt = ...  # 0xd8
    Key_Ugrave: Qt = ...  # 0xd9
    Key_Uacute: Qt = ...  # 0xda
    Key_Ucircumflex: Qt = ...  # 0xdb
    Key_Udiaeresis: Qt = ...  # 0xdc
    Key_Yacute: Qt = ...  # 0xdd
    Key_THORN: Qt = ...  # 0xde
    Key_ssharp: Qt = ...  # 0xdf
    Key_division: Qt = ...  # 0xf7
    ActionMask: Qt = ...  # 0xff
    Key_ydiaeresis: Qt = ...  # 0xff
    MouseEventFlagMask: Qt = ...  # 0xff
    TabFocusAllControls: Qt = ...  # 0xff
    WindowType_Mask: Qt = ...  # 0xff
    AlignBaseline: Qt = ...  # 0x100
    CustomGesture: Qt = ...  # 0x100
    ExtraButton6: Qt = ...  # 0x100
    ImHints: Qt = ...  # 0x100
    ImhTime: Qt = ...  # 0x100
    ItemIsUserTristate: Qt = ...  # 0x100
    MSWindowsFixedSizeDialogHint: Qt = ...  # 0x100
    NoOpaqueDetection: Qt = ...  # 0x100
    SvgMiterJoin: Qt = ...  # 0x100
    TextSingleLine: Qt = ...  # 0x100
    UserRole: Qt = ...  # 0x100
    MPenJoinStyle: Qt = ...  # 0x1c0
    AlignVertical_Mask: Qt = ...  # 0x1e0
    ExtraButton7: Qt = ...  # 0x200
    ImPreferredLanguage: Qt = ...  # 0x200
    ImhPreferLatin: Qt = ...  # 0x200
    MSWindowsOwnDC: Qt = ...  # 0x200
    NoFormatConversion: Qt = ...  # 0x200
    TextDontClip: Qt = ...  # 0x200
    BypassWindowManagerHint: Qt = ...  # 0x400
    ExtraButton8: Qt = ...  # 0x400
    ImAbsolutePosition: Qt = ...  # 0x400
    ImhMultiLine: Qt = ...  # 0x400
    TextExpandTabs: Qt = ...  # 0x400
    X11BypassWindowManagerHint: Qt = ...  # 0x400
    ExtraButton9: Qt = ...  # 0x800
    FramelessWindowHint: Qt = ...  # 0x800
    ImTextBeforeCursor: Qt = ...  # 0x800
    ImhNoEditMenu: Qt = ...  # 0x800
    TextShowMnemonic: Qt = ...  # 0x800
    ExtraButton10: Qt = ...  # 0x1000
    ImTextAfterCursor: Qt = ...  # 0x1000
    ImhNoTextHandles: Qt = ...  # 0x1000
    TextWordWrap: Qt = ...  # 0x1000
    WindowTitleHint: Qt = ...  # 0x1000
    ExtraButton11: Qt = ...  # 0x2000
    ImEnterKeyType: Qt = ...  # 0x2000
    TextWrapAnywhere: Qt = ...  # 0x2000
    WindowSystemMenuHint: Qt = ...  # 0x2000
    ExtraButton12: Qt = ...  # 0x4000
    ImAnchorRectangle: Qt = ...  # 0x4000
    TextDontPrint: Qt = ...  # 0x4000
    WindowMinimizeButtonHint: Qt = ...  # 0x4000
    ImQueryInput: Qt = ...  # 0x40ba
    ExtraButton13: Qt = ...  # 0x8000
    ImInputItemClipRectangle: Qt = ...  # 0x8000
    TextHideMnemonic: Qt = ...  # 0x8000
    WindowMaximizeButtonHint: Qt = ...  # 0x8000
    TargetMoveAction: Qt = ...  # 0x8002
    WindowMinMaxButtonsHint: Qt = ...  # 0xc000
    ExtraButton14: Qt = ...  # 0x10000
    ImhDigitsOnly: Qt = ...  # 0x10000
    TextJustificationForced: Qt = ...  # 0x10000
    WindowContextHelpButtonHint: Qt = ...  # 0x10000
    ExtraButton15: Qt = ...  # 0x20000
    ImhFormattedNumbersOnly: Qt = ...  # 0x20000
    TextForceLeftToRight: Qt = ...  # 0x20000
    WindowShadeButtonHint: Qt = ...  # 0x20000
    ExtraButton16: Qt = ...  # 0x40000
    ImhUppercaseOnly: Qt = ...  # 0x40000
    TextForceRightToLeft: Qt = ...  # 0x40000
    WindowStaysOnTopHint: Qt = ...  # 0x40000
    ExtraButton17: Qt = ...  # 0x80000
    ImhLowercaseOnly: Qt = ...  # 0x80000
    TextLongestVariant: Qt = ...  # 0x80000
    WindowTransparentForInput: Qt = ...  # 0x80000
    ExtraButton18: Qt = ...  # 0x100000
    ImhDialableCharactersOnly: Qt = ...  # 0x100000
    TextBypassShaping: Qt = ...  # 0x100000
    WindowOverridesSystemGestures: Qt = ...  # 0x100000
    ExtraButton19: Qt = ...  # 0x200000
    ImhEmailCharactersOnly: Qt = ...  # 0x200000
    WindowDoesNotAcceptFocus: Qt = ...  # 0x200000
    ExtraButton20: Qt = ...  # 0x400000
    ImhUrlCharactersOnly: Qt = ...  # 0x400000
    MaximizeUsingFullscreenGeometryHint: Qt = ...  # 0x400000
    ExtraButton21: Qt = ...  # 0x800000
    ImhLatinOnly: Qt = ...  # 0x800000
    ExtraButton22: Qt = ...  # 0x1000000
    Key_Escape: Qt = ...  # 0x1000000
    Key_Tab: Qt = ...  # 0x1000001
    Key_Backtab: Qt = ...  # 0x1000002
    Key_Backspace: Qt = ...  # 0x1000003
    Key_Return: Qt = ...  # 0x1000004
    Key_Enter: Qt = ...  # 0x1000005
    Key_Insert: Qt = ...  # 0x1000006
    Key_Delete: Qt = ...  # 0x1000007
    Key_Pause: Qt = ...  # 0x1000008
    Key_Print: Qt = ...  # 0x1000009
    Key_SysReq: Qt = ...  # 0x100000a
    Key_Clear: Qt = ...  # 0x100000b
    Key_Home: Qt = ...  # 0x1000010
    Key_End: Qt = ...  # 0x1000011
    Key_Left: Qt = ...  # 0x1000012
    Key_Up: Qt = ...  # 0x1000013
    Key_Right: Qt = ...  # 0x1000014
    Key_Down: Qt = ...  # 0x1000015
    Key_PageUp: Qt = ...  # 0x1000016
    Key_PageDown: Qt = ...  # 0x1000017
    Key_Shift: Qt = ...  # 0x1000020
    Key_Control: Qt = ...  # 0x1000021
    Key_Meta: Qt = ...  # 0x1000022
    Key_Alt: Qt = ...  # 0x1000023
    Key_CapsLock: Qt = ...  # 0x1000024
    Key_NumLock: Qt = ...  # 0x1000025
    Key_ScrollLock: Qt = ...  # 0x1000026
    Key_F1: Qt = ...  # 0x1000030
    Key_F2: Qt = ...  # 0x1000031
    Key_F3: Qt = ...  # 0x1000032
    Key_F4: Qt = ...  # 0x1000033
    Key_F5: Qt = ...  # 0x1000034
    Key_F6: Qt = ...  # 0x1000035
    Key_F7: Qt = ...  # 0x1000036
    Key_F8: Qt = ...  # 0x1000037
    Key_F9: Qt = ...  # 0x1000038
    Key_F10: Qt = ...  # 0x1000039
    Key_F11: Qt = ...  # 0x100003a
    Key_F12: Qt = ...  # 0x100003b
    Key_F13: Qt = ...  # 0x100003c
    Key_F14: Qt = ...  # 0x100003d
    Key_F15: Qt = ...  # 0x100003e
    Key_F16: Qt = ...  # 0x100003f
    Key_F17: Qt = ...  # 0x1000040
    Key_F18: Qt = ...  # 0x1000041
    Key_F19: Qt = ...  # 0x1000042
    Key_F20: Qt = ...  # 0x1000043
    Key_F21: Qt = ...  # 0x1000044
    Key_F22: Qt = ...  # 0x1000045
    Key_F23: Qt = ...  # 0x1000046
    Key_F24: Qt = ...  # 0x1000047
    Key_F25: Qt = ...  # 0x1000048
    Key_F26: Qt = ...  # 0x1000049
    Key_F27: Qt = ...  # 0x100004a
    Key_F28: Qt = ...  # 0x100004b
    Key_F29: Qt = ...  # 0x100004c
    Key_F30: Qt = ...  # 0x100004d
    Key_F31: Qt = ...  # 0x100004e
    Key_F32: Qt = ...  # 0x100004f
    Key_F33: Qt = ...  # 0x1000050
    Key_F34: Qt = ...  # 0x1000051
    Key_F35: Qt = ...  # 0x1000052
    Key_Super_L: Qt = ...  # 0x1000053
    Key_Super_R: Qt = ...  # 0x1000054
    Key_Menu: Qt = ...  # 0x1000055
    Key_Hyper_L: Qt = ...  # 0x1000056
    Key_Hyper_R: Qt = ...  # 0x1000057
    Key_Help: Qt = ...  # 0x1000058
    Key_Direction_L: Qt = ...  # 0x1000059
    Key_Direction_R: Qt = ...  # 0x1000060
    Key_Back: Qt = ...  # 0x1000061
    Key_Forward: Qt = ...  # 0x1000062
    Key_Stop: Qt = ...  # 0x1000063
    Key_Refresh: Qt = ...  # 0x1000064
    Key_VolumeDown: Qt = ...  # 0x1000070
    Key_VolumeMute: Qt = ...  # 0x1000071
    Key_VolumeUp: Qt = ...  # 0x1000072
    Key_BassBoost: Qt = ...  # 0x1000073
    Key_BassUp: Qt = ...  # 0x1000074
    Key_BassDown: Qt = ...  # 0x1000075
    Key_TrebleUp: Qt = ...  # 0x1000076
    Key_TrebleDown: Qt = ...  # 0x1000077
    Key_MediaPlay: Qt = ...  # 0x1000080
    Key_MediaStop: Qt = ...  # 0x1000081
    Key_MediaPrevious: Qt = ...  # 0x1000082
    Key_MediaNext: Qt = ...  # 0x1000083
    Key_MediaRecord: Qt = ...  # 0x1000084
    Key_MediaPause: Qt = ...  # 0x1000085
    Key_MediaTogglePlayPause: Qt = ...  # 0x1000086
    Key_HomePage: Qt = ...  # 0x1000090
    Key_Favorites: Qt = ...  # 0x1000091
    Key_Search: Qt = ...  # 0x1000092
    Key_Standby: Qt = ...  # 0x1000093
    Key_OpenUrl: Qt = ...  # 0x1000094
    Key_LaunchMail: Qt = ...  # 0x10000a0
    Key_LaunchMedia: Qt = ...  # 0x10000a1
    Key_Launch0: Qt = ...  # 0x10000a2
    Key_Launch1: Qt = ...  # 0x10000a3
    Key_Launch2: Qt = ...  # 0x10000a4
    Key_Launch3: Qt = ...  # 0x10000a5
    Key_Launch4: Qt = ...  # 0x10000a6
    Key_Launch5: Qt = ...  # 0x10000a7
    Key_Launch6: Qt = ...  # 0x10000a8
    Key_Launch7: Qt = ...  # 0x10000a9
    Key_Launch8: Qt = ...  # 0x10000aa
    Key_Launch9: Qt = ...  # 0x10000ab
    Key_LaunchA: Qt = ...  # 0x10000ac
    Key_LaunchB: Qt = ...  # 0x10000ad
    Key_LaunchC: Qt = ...  # 0x10000ae
    Key_LaunchD: Qt = ...  # 0x10000af
    Key_LaunchE: Qt = ...  # 0x10000b0
    Key_LaunchF: Qt = ...  # 0x10000b1
    Key_MonBrightnessUp: Qt = ...  # 0x10000b2
    Key_MonBrightnessDown: Qt = ...  # 0x10000b3
    Key_KeyboardLightOnOff: Qt = ...  # 0x10000b4
    Key_KeyboardBrightnessUp: Qt = ...  # 0x10000b5
    Key_KeyboardBrightnessDown: Qt = ...  # 0x10000b6
    Key_PowerOff: Qt = ...  # 0x10000b7
    Key_WakeUp: Qt = ...  # 0x10000b8
    Key_Eject: Qt = ...  # 0x10000b9
    Key_ScreenSaver: Qt = ...  # 0x10000ba
    Key_WWW: Qt = ...  # 0x10000bb
    Key_Memo: Qt = ...  # 0x10000bc
    Key_LightBulb: Qt = ...  # 0x10000bd
    Key_Shop: Qt = ...  # 0x10000be
    Key_History: Qt = ...  # 0x10000bf
    Key_AddFavorite: Qt = ...  # 0x10000c0
    Key_HotLinks: Qt = ...  # 0x10000c1
    Key_BrightnessAdjust: Qt = ...  # 0x10000c2
    Key_Finance: Qt = ...  # 0x10000c3
    Key_Community: Qt = ...  # 0x10000c4
    Key_AudioRewind: Qt = ...  # 0x10000c5
    Key_BackForward: Qt = ...  # 0x10000c6
    Key_ApplicationLeft: Qt = ...  # 0x10000c7
    Key_ApplicationRight: Qt = ...  # 0x10000c8
    Key_Book: Qt = ...  # 0x10000c9
    Key_CD: Qt = ...  # 0x10000ca
    Key_Calculator: Qt = ...  # 0x10000cb
    Key_ToDoList: Qt = ...  # 0x10000cc
    Key_ClearGrab: Qt = ...  # 0x10000cd
    Key_Close: Qt = ...  # 0x10000ce
    Key_Copy: Qt = ...  # 0x10000cf
    Key_Cut: Qt = ...  # 0x10000d0
    Key_Display: Qt = ...  # 0x10000d1
    Key_DOS: Qt = ...  # 0x10000d2
    Key_Documents: Qt = ...  # 0x10000d3
    Key_Excel: Qt = ...  # 0x10000d4
    Key_Explorer: Qt = ...  # 0x10000d5
    Key_Game: Qt = ...  # 0x10000d6
    Key_Go: Qt = ...  # 0x10000d7
    Key_iTouch: Qt = ...  # 0x10000d8
    Key_LogOff: Qt = ...  # 0x10000d9
    Key_Market: Qt = ...  # 0x10000da
    Key_Meeting: Qt = ...  # 0x10000db
    Key_MenuKB: Qt = ...  # 0x10000dc
    Key_MenuPB: Qt = ...  # 0x10000dd
    Key_MySites: Qt = ...  # 0x10000de
    Key_News: Qt = ...  # 0x10000df
    Key_OfficeHome: Qt = ...  # 0x10000e0
    Key_Option: Qt = ...  # 0x10000e1
    Key_Paste: Qt = ...  # 0x10000e2
    Key_Phone: Qt = ...  # 0x10000e3
    Key_Calendar: Qt = ...  # 0x10000e4
    Key_Reply: Qt = ...  # 0x10000e5
    Key_Reload: Qt = ...  # 0x10000e6
    Key_RotateWindows: Qt = ...  # 0x10000e7
    Key_RotationPB: Qt = ...  # 0x10000e8
    Key_RotationKB: Qt = ...  # 0x10000e9
    Key_Save: Qt = ...  # 0x10000ea
    Key_Send: Qt = ...  # 0x10000eb
    Key_Spell: Qt = ...  # 0x10000ec
    Key_SplitScreen: Qt = ...  # 0x10000ed
    Key_Support: Qt = ...  # 0x10000ee
    Key_TaskPane: Qt = ...  # 0x10000ef
    Key_Terminal: Qt = ...  # 0x10000f0
    Key_Tools: Qt = ...  # 0x10000f1
    Key_Travel: Qt = ...  # 0x10000f2
    Key_Video: Qt = ...  # 0x10000f3
    Key_Word: Qt = ...  # 0x10000f4
    Key_Xfer: Qt = ...  # 0x10000f5
    Key_ZoomIn: Qt = ...  # 0x10000f6
    Key_ZoomOut: Qt = ...  # 0x10000f7
    Key_Away: Qt = ...  # 0x10000f8
    Key_Messenger: Qt = ...  # 0x10000f9
    Key_WebCam: Qt = ...  # 0x10000fa
    Key_MailForward: Qt = ...  # 0x10000fb
    Key_Pictures: Qt = ...  # 0x10000fc
    Key_Music: Qt = ...  # 0x10000fd
    Key_Battery: Qt = ...  # 0x10000fe
    Key_Bluetooth: Qt = ...  # 0x10000ff
    Key_WLAN: Qt = ...  # 0x1000100
    Key_UWB: Qt = ...  # 0x1000101
    Key_AudioForward: Qt = ...  # 0x1000102
    Key_AudioRepeat: Qt = ...  # 0x1000103
    Key_AudioRandomPlay: Qt = ...  # 0x1000104
    Key_Subtitle: Qt = ...  # 0x1000105
    Key_AudioCycleTrack: Qt = ...  # 0x1000106
    Key_Time: Qt = ...  # 0x1000107
    Key_Hibernate: Qt = ...  # 0x1000108
    Key_View: Qt = ...  # 0x1000109
    Key_TopMenu: Qt = ...  # 0x100010a
    Key_PowerDown: Qt = ...  # 0x100010b
    Key_Suspend: Qt = ...  # 0x100010c
    Key_ContrastAdjust: Qt = ...  # 0x100010d
    Key_LaunchG: Qt = ...  # 0x100010e
    Key_LaunchH: Qt = ...  # 0x100010f
    Key_TouchpadToggle: Qt = ...  # 0x1000110
    Key_TouchpadOn: Qt = ...  # 0x1000111
    Key_TouchpadOff: Qt = ...  # 0x1000112
    Key_MicMute: Qt = ...  # 0x1000113
    Key_Red: Qt = ...  # 0x1000114
    Key_Green: Qt = ...  # 0x1000115
    Key_Yellow: Qt = ...  # 0x1000116
    Key_Blue: Qt = ...  # 0x1000117
    Key_ChannelUp: Qt = ...  # 0x1000118
    Key_ChannelDown: Qt = ...  # 0x1000119
    Key_Guide: Qt = ...  # 0x100011a
    Key_Info: Qt = ...  # 0x100011b
    Key_Settings: Qt = ...  # 0x100011c
    Key_MicVolumeUp: Qt = ...  # 0x100011d
    Key_MicVolumeDown: Qt = ...  # 0x100011e
    Key_New: Qt = ...  # 0x1000120
    Key_Open: Qt = ...  # 0x1000121
    Key_Find: Qt = ...  # 0x1000122
    Key_Undo: Qt = ...  # 0x1000123
    Key_Redo: Qt = ...  # 0x1000124
    Key_AltGr: Qt = ...  # 0x1001103
    Key_Multi_key: Qt = ...  # 0x1001120
    Key_Kanji: Qt = ...  # 0x1001121
    Key_Muhenkan: Qt = ...  # 0x1001122
    Key_Henkan: Qt = ...  # 0x1001123
    Key_Romaji: Qt = ...  # 0x1001124
    Key_Hiragana: Qt = ...  # 0x1001125
    Key_Katakana: Qt = ...  # 0x1001126
    Key_Hiragana_Katakana: Qt = ...  # 0x1001127
    Key_Zenkaku: Qt = ...  # 0x1001128
    Key_Hankaku: Qt = ...  # 0x1001129
    Key_Zenkaku_Hankaku: Qt = ...  # 0x100112a
    Key_Touroku: Qt = ...  # 0x100112b
    Key_Massyo: Qt = ...  # 0x100112c
    Key_Kana_Lock: Qt = ...  # 0x100112d
    Key_Kana_Shift: Qt = ...  # 0x100112e
    Key_Eisu_Shift: Qt = ...  # 0x100112f
    Key_Eisu_toggle: Qt = ...  # 0x1001130
    Key_Hangul: Qt = ...  # 0x1001131
    Key_Hangul_Start: Qt = ...  # 0x1001132
    Key_Hangul_End: Qt = ...  # 0x1001133
    Key_Hangul_Hanja: Qt = ...  # 0x1001134
    Key_Hangul_Jamo: Qt = ...  # 0x1001135
    Key_Hangul_Romaja: Qt = ...  # 0x1001136
    Key_Codeinput: Qt = ...  # 0x1001137
    Key_Hangul_Jeonja: Qt = ...  # 0x1001138
    Key_Hangul_Banja: Qt = ...  # 0x1001139
    Key_Hangul_PreHanja: Qt = ...  # 0x100113a
    Key_Hangul_PostHanja: Qt = ...  # 0x100113b
    Key_SingleCandidate: Qt = ...  # 0x100113c
    Key_MultipleCandidate: Qt = ...  # 0x100113d
    Key_PreviousCandidate: Qt = ...  # 0x100113e
    Key_Hangul_Special: Qt = ...  # 0x100113f
    Key_Mode_switch: Qt = ...  # 0x100117e
    Key_Dead_Grave: Qt = ...  # 0x1001250
    Key_Dead_Acute: Qt = ...  # 0x1001251
    Key_Dead_Circumflex: Qt = ...  # 0x1001252
    Key_Dead_Tilde: Qt = ...  # 0x1001253
    Key_Dead_Macron: Qt = ...  # 0x1001254
    Key_Dead_Breve: Qt = ...  # 0x1001255
    Key_Dead_Abovedot: Qt = ...  # 0x1001256
    Key_Dead_Diaeresis: Qt = ...  # 0x1001257
    Key_Dead_Abovering: Qt = ...  # 0x1001258
    Key_Dead_Doubleacute: Qt = ...  # 0x1001259
    Key_Dead_Caron: Qt = ...  # 0x100125a
    Key_Dead_Cedilla: Qt = ...  # 0x100125b
    Key_Dead_Ogonek: Qt = ...  # 0x100125c
    Key_Dead_Iota: Qt = ...  # 0x100125d
    Key_Dead_Voiced_Sound: Qt = ...  # 0x100125e
    Key_Dead_Semivoiced_Sound: Qt = ...  # 0x100125f
    Key_Dead_Belowdot: Qt = ...  # 0x1001260
    Key_Dead_Hook: Qt = ...  # 0x1001261
    Key_Dead_Horn: Qt = ...  # 0x1001262
    Key_Dead_Stroke: Qt = ...  # 0x1001263
    Key_Dead_Abovecomma: Qt = ...  # 0x1001264
    Key_Dead_Abovereversedcomma: Qt = ...  # 0x1001265
    Key_Dead_Doublegrave: Qt = ...  # 0x1001266
    Key_Dead_Belowring: Qt = ...  # 0x1001267
    Key_Dead_Belowmacron: Qt = ...  # 0x1001268
    Key_Dead_Belowcircumflex: Qt = ...  # 0x1001269
    Key_Dead_Belowtilde: Qt = ...  # 0x100126a
    Key_Dead_Belowbreve: Qt = ...  # 0x100126b
    Key_Dead_Belowdiaeresis: Qt = ...  # 0x100126c
    Key_Dead_Invertedbreve: Qt = ...  # 0x100126d
    Key_Dead_Belowcomma: Qt = ...  # 0x100126e
    Key_Dead_Currency: Qt = ...  # 0x100126f
    Key_Dead_a: Qt = ...  # 0x1001280
    Key_Dead_A: Qt = ...  # 0x1001281
    Key_Dead_e: Qt = ...  # 0x1001282
    Key_Dead_E: Qt = ...  # 0x1001283
    Key_Dead_i: Qt = ...  # 0x1001284
    Key_Dead_I: Qt = ...  # 0x1001285
    Key_Dead_o: Qt = ...  # 0x1001286
    Key_Dead_O: Qt = ...  # 0x1001287
    Key_Dead_u: Qt = ...  # 0x1001288
    Key_Dead_U: Qt = ...  # 0x1001289
    Key_Dead_Small_Schwa: Qt = ...  # 0x100128a
    Key_Dead_Capital_Schwa: Qt = ...  # 0x100128b
    Key_Dead_Greek: Qt = ...  # 0x100128c
    Key_Dead_Lowline: Qt = ...  # 0x1001290
    Key_Dead_Aboveverticalline: Qt = ...  # 0x1001291
    Key_Dead_Belowverticalline: Qt = ...  # 0x1001292
    Key_Dead_Longsolidusoverlay: Qt = ...  # 0x1001293
    Key_MediaLast: Qt = ...  # 0x100ffff
    Key_Select: Qt = ...  # 0x1010000
    Key_Yes: Qt = ...  # 0x1010001
    Key_No: Qt = ...  # 0x1010002
    Key_Cancel: Qt = ...  # 0x1020001
    Key_Printer: Qt = ...  # 0x1020002
    Key_Execute: Qt = ...  # 0x1020003
    Key_Sleep: Qt = ...  # 0x1020004
    Key_Play: Qt = ...  # 0x1020005
    Key_Zoom: Qt = ...  # 0x1020006
    Key_Exit: Qt = ...  # 0x102000a
    Key_Context1: Qt = ...  # 0x1100000
    Key_Context2: Qt = ...  # 0x1100001
    Key_Context3: Qt = ...  # 0x1100002
    Key_Context4: Qt = ...  # 0x1100003
    Key_Call: Qt = ...  # 0x1100004
    Key_Hangup: Qt = ...  # 0x1100005
    Key_Flip: Qt = ...  # 0x1100006
    Key_ToggleCallHangup: Qt = ...  # 0x1100007
    Key_VoiceDial: Qt = ...  # 0x1100008
    Key_LastNumberRedial: Qt = ...  # 0x1100009
    Key_Camera: Qt = ...  # 0x1100020
    Key_CameraFocus: Qt = ...  # 0x1100021
    Key_unknown: Qt = ...  # 0x1ffffff
    CustomizeWindowHint: Qt = ...  # 0x2000000
    ExtraButton23: Qt = ...  # 0x2000000
    SHIFT: Qt = ...  # 0x2000000
    ShiftModifier: Qt = ...  # 0x2000000
    CTRL: Qt = ...  # 0x4000000
    ControlModifier: Qt = ...  # 0x4000000
    ExtraButton24: Qt = ...  # 0x4000000
    MaxMouseButton: Qt = ...  # 0x4000000
    WindowStaysOnBottomHint: Qt = ...  # 0x4000000
    AllButtons: Qt = ...  # 0x7ffffff
    ALT: Qt = ...  # 0x8000000
    AltModifier: Qt = ...  # 0x8000000
    TextIncludeTrailingSpaces: Qt = ...  # 0x8000000
    WindowCloseButtonHint: Qt = ...  # 0x8000000
    META: Qt = ...  # 0x10000000
    MacWindowToolBarButtonHint: Qt = ...  # 0x10000000
    MetaModifier: Qt = ...  # 0x10000000
    BypassGraphicsProxyWidget: Qt = ...  # 0x20000000
    KeypadModifier: Qt = ...  # 0x20000000
    GroupSwitchModifier: Qt = ...  # 0x40000000
    NoDropShadowWindowHint: Qt = ...  # 0x40000000

    class Alignment(object): ...

    class AlignmentFlag(object):
        AlignLeading: Qt.AlignmentFlag = ...  # 0x1
        AlignLeft: Qt.AlignmentFlag = ...  # 0x1
        AlignRight: Qt.AlignmentFlag = ...  # 0x2
        AlignTrailing: Qt.AlignmentFlag = ...  # 0x2
        AlignHCenter: Qt.AlignmentFlag = ...  # 0x4
        AlignJustify: Qt.AlignmentFlag = ...  # 0x8
        AlignAbsolute: Qt.AlignmentFlag = ...  # 0x10
        AlignHorizontal_Mask: Qt.AlignmentFlag = ...  # 0x1f
        AlignTop: Qt.AlignmentFlag = ...  # 0x20
        AlignBottom: Qt.AlignmentFlag = ...  # 0x40
        AlignVCenter: Qt.AlignmentFlag = ...  # 0x80
        AlignCenter: Qt.AlignmentFlag = ...  # 0x84
        AlignBaseline: Qt.AlignmentFlag = ...  # 0x100
        AlignVertical_Mask: Qt.AlignmentFlag = ...  # 0x1e0

    class AnchorPoint(object):
        AnchorLeft: Qt.AnchorPoint = ...  # 0x0
        AnchorHorizontalCenter: Qt.AnchorPoint = ...  # 0x1
        AnchorRight: Qt.AnchorPoint = ...  # 0x2
        AnchorTop: Qt.AnchorPoint = ...  # 0x3
        AnchorVerticalCenter: Qt.AnchorPoint = ...  # 0x4
        AnchorBottom: Qt.AnchorPoint = ...  # 0x5

    class ApplicationAttribute(object):
        AA_ImmediateWidgetCreation: Qt.ApplicationAttribute = ...  # 0x0
        AA_MSWindowsUseDirect3DByDefault: Qt.ApplicationAttribute = ...  # 0x1
        AA_DontShowIconsInMenus: Qt.ApplicationAttribute = ...  # 0x2
        AA_NativeWindows: Qt.ApplicationAttribute = ...  # 0x3
        AA_DontCreateNativeWidgetSiblings: Qt.ApplicationAttribute = ...  # 0x4
        AA_MacPluginApplication: Qt.ApplicationAttribute = ...  # 0x5
        AA_PluginApplication: Qt.ApplicationAttribute = ...  # 0x5
        AA_DontUseNativeMenuBar: Qt.ApplicationAttribute = ...  # 0x6
        AA_MacDontSwapCtrlAndMeta: Qt.ApplicationAttribute = ...  # 0x7
        AA_Use96Dpi: Qt.ApplicationAttribute = ...  # 0x8
        AA_DisableNativeVirtualKeyboard: Qt.ApplicationAttribute = ...  # 0x9
        AA_X11InitThreads: Qt.ApplicationAttribute = ...  # 0xa
        AA_SynthesizeTouchForUnhandledMouseEvents: Qt.ApplicationAttribute = ...  # 0xb
        AA_SynthesizeMouseForUnhandledTouchEvents: Qt.ApplicationAttribute = ...  # 0xc
        AA_UseHighDpiPixmaps: Qt.ApplicationAttribute = ...  # 0xd
        AA_ForceRasterWidgets: Qt.ApplicationAttribute = ...  # 0xe
        AA_UseDesktopOpenGL: Qt.ApplicationAttribute = ...  # 0xf
        AA_UseOpenGLES: Qt.ApplicationAttribute = ...  # 0x10
        AA_UseSoftwareOpenGL: Qt.ApplicationAttribute = ...  # 0x11
        AA_ShareOpenGLContexts: Qt.ApplicationAttribute = ...  # 0x12
        AA_SetPalette: Qt.ApplicationAttribute = ...  # 0x13
        AA_EnableHighDpiScaling: Qt.ApplicationAttribute = ...  # 0x14
        AA_DisableHighDpiScaling: Qt.ApplicationAttribute = ...  # 0x15
        AA_UseStyleSheetPropagationInWidgetStyles: Qt.ApplicationAttribute = ...  # 0x16
        AA_DontUseNativeDialogs: Qt.ApplicationAttribute = ...  # 0x17
        AA_SynthesizeMouseForUnhandledTabletEvents: Qt.ApplicationAttribute = (
            ...
        )  # 0x18
        AA_CompressHighFrequencyEvents: Qt.ApplicationAttribute = ...  # 0x19
        AA_DontCheckOpenGLContextThreadAffinity: Qt.ApplicationAttribute = ...  # 0x1a
        AA_DisableShaderDiskCache: Qt.ApplicationAttribute = ...  # 0x1b
        AA_DontShowShortcutsInContextMenus: Qt.ApplicationAttribute = ...  # 0x1c
        AA_CompressTabletEvents: Qt.ApplicationAttribute = ...  # 0x1d
        AA_DisableWindowContextHelpButton: Qt.ApplicationAttribute = ...  # 0x1e
        AA_DisableSessionManager: Qt.ApplicationAttribute = ...  # 0x1f
        AA_AttributeCount: Qt.ApplicationAttribute = ...  # 0x20

    class ApplicationState(object):
        ApplicationSuspended: Qt.ApplicationState = ...  # 0x0
        ApplicationHidden: Qt.ApplicationState = ...  # 0x1
        ApplicationInactive: Qt.ApplicationState = ...  # 0x2
        ApplicationActive: Qt.ApplicationState = ...  # 0x4

    class ApplicationStates(object): ...

    class ArrowType(object):
        NoArrow: Qt.ArrowType = ...  # 0x0
        UpArrow: Qt.ArrowType = ...  # 0x1
        DownArrow: Qt.ArrowType = ...  # 0x2
        LeftArrow: Qt.ArrowType = ...  # 0x3
        RightArrow: Qt.ArrowType = ...  # 0x4

    class AspectRatioMode(object):
        IgnoreAspectRatio: Qt.AspectRatioMode = ...  # 0x0
        KeepAspectRatio: Qt.AspectRatioMode = ...  # 0x1
        KeepAspectRatioByExpanding: Qt.AspectRatioMode = ...  # 0x2

    class Axis(object):
        XAxis: Qt.Axis = ...  # 0x0
        YAxis: Qt.Axis = ...  # 0x1
        ZAxis: Qt.Axis = ...  # 0x2

    class BGMode(object):
        TransparentMode: Qt.BGMode = ...  # 0x0
        OpaqueMode: Qt.BGMode = ...  # 0x1

    class BrushStyle(object):
        NoBrush: Qt.BrushStyle = ...  # 0x0
        SolidPattern: Qt.BrushStyle = ...  # 0x1
        Dense1Pattern: Qt.BrushStyle = ...  # 0x2
        Dense2Pattern: Qt.BrushStyle = ...  # 0x3
        Dense3Pattern: Qt.BrushStyle = ...  # 0x4
        Dense4Pattern: Qt.BrushStyle = ...  # 0x5
        Dense5Pattern: Qt.BrushStyle = ...  # 0x6
        Dense6Pattern: Qt.BrushStyle = ...  # 0x7
        Dense7Pattern: Qt.BrushStyle = ...  # 0x8
        HorPattern: Qt.BrushStyle = ...  # 0x9
        VerPattern: Qt.BrushStyle = ...  # 0xa
        CrossPattern: Qt.BrushStyle = ...  # 0xb
        BDiagPattern: Qt.BrushStyle = ...  # 0xc
        FDiagPattern: Qt.BrushStyle = ...  # 0xd
        DiagCrossPattern: Qt.BrushStyle = ...  # 0xe
        LinearGradientPattern: Qt.BrushStyle = ...  # 0xf
        RadialGradientPattern: Qt.BrushStyle = ...  # 0x10
        ConicalGradientPattern: Qt.BrushStyle = ...  # 0x11
        TexturePattern: Qt.BrushStyle = ...  # 0x18

    class CaseSensitivity(object):
        CaseInsensitive: Qt.CaseSensitivity = ...  # 0x0
        CaseSensitive: Qt.CaseSensitivity = ...  # 0x1

    class CheckState(object):
        Unchecked: Qt.CheckState = ...  # 0x0
        PartiallyChecked: Qt.CheckState = ...  # 0x1
        Checked: Qt.CheckState = ...  # 0x2

    class ChecksumType(object):
        ChecksumIso3309: Qt.ChecksumType = ...  # 0x0
        ChecksumItuV41: Qt.ChecksumType = ...  # 0x1

    class ClipOperation(object):
        NoClip: Qt.ClipOperation = ...  # 0x0
        ReplaceClip: Qt.ClipOperation = ...  # 0x1
        IntersectClip: Qt.ClipOperation = ...  # 0x2

    class ConnectionType(object):
        AutoConnection: Qt.ConnectionType = ...  # 0x0
        DirectConnection: Qt.ConnectionType = ...  # 0x1
        QueuedConnection: Qt.ConnectionType = ...  # 0x2
        BlockingQueuedConnection: Qt.ConnectionType = ...  # 0x3
        UniqueConnection: Qt.ConnectionType = ...  # 0x80

    class ContextMenuPolicy(object):
        NoContextMenu: Qt.ContextMenuPolicy = ...  # 0x0
        DefaultContextMenu: Qt.ContextMenuPolicy = ...  # 0x1
        ActionsContextMenu: Qt.ContextMenuPolicy = ...  # 0x2
        CustomContextMenu: Qt.ContextMenuPolicy = ...  # 0x3
        PreventContextMenu: Qt.ContextMenuPolicy = ...  # 0x4

    class CoordinateSystem(object):
        DeviceCoordinates: Qt.CoordinateSystem = ...  # 0x0
        LogicalCoordinates: Qt.CoordinateSystem = ...  # 0x1

    class Corner(object):
        TopLeftCorner: Qt.Corner = ...  # 0x0
        TopRightCorner: Qt.Corner = ...  # 0x1
        BottomLeftCorner: Qt.Corner = ...  # 0x2
        BottomRightCorner: Qt.Corner = ...  # 0x3

    class CursorMoveStyle(object):
        LogicalMoveStyle: Qt.CursorMoveStyle = ...  # 0x0
        VisualMoveStyle: Qt.CursorMoveStyle = ...  # 0x1

    class CursorShape(object):
        ArrowCursor: Qt.CursorShape = ...  # 0x0
        UpArrowCursor: Qt.CursorShape = ...  # 0x1
        CrossCursor: Qt.CursorShape = ...  # 0x2
        WaitCursor: Qt.CursorShape = ...  # 0x3
        IBeamCursor: Qt.CursorShape = ...  # 0x4
        SizeVerCursor: Qt.CursorShape = ...  # 0x5
        SizeHorCursor: Qt.CursorShape = ...  # 0x6
        SizeBDiagCursor: Qt.CursorShape = ...  # 0x7
        SizeFDiagCursor: Qt.CursorShape = ...  # 0x8
        SizeAllCursor: Qt.CursorShape = ...  # 0x9
        BlankCursor: Qt.CursorShape = ...  # 0xa
        SplitVCursor: Qt.CursorShape = ...  # 0xb
        SplitHCursor: Qt.CursorShape = ...  # 0xc
        PointingHandCursor: Qt.CursorShape = ...  # 0xd
        ForbiddenCursor: Qt.CursorShape = ...  # 0xe
        WhatsThisCursor: Qt.CursorShape = ...  # 0xf
        BusyCursor: Qt.CursorShape = ...  # 0x10
        OpenHandCursor: Qt.CursorShape = ...  # 0x11
        ClosedHandCursor: Qt.CursorShape = ...  # 0x12
        DragCopyCursor: Qt.CursorShape = ...  # 0x13
        DragMoveCursor: Qt.CursorShape = ...  # 0x14
        DragLinkCursor: Qt.CursorShape = ...  # 0x15
        LastCursor: Qt.CursorShape = ...  # 0x15
        BitmapCursor: Qt.CursorShape = ...  # 0x18
        CustomCursor: Qt.CursorShape = ...  # 0x19

    class DateFormat(object):
        TextDate: Qt.DateFormat = ...  # 0x0
        ISODate: Qt.DateFormat = ...  # 0x1
        LocalDate: Qt.DateFormat = ...  # 0x2
        SystemLocaleDate: Qt.DateFormat = ...  # 0x2
        LocaleDate: Qt.DateFormat = ...  # 0x3
        SystemLocaleShortDate: Qt.DateFormat = ...  # 0x4
        SystemLocaleLongDate: Qt.DateFormat = ...  # 0x5
        DefaultLocaleShortDate: Qt.DateFormat = ...  # 0x6
        DefaultLocaleLongDate: Qt.DateFormat = ...  # 0x7
        RFC2822Date: Qt.DateFormat = ...  # 0x8
        ISODateWithMs: Qt.DateFormat = ...  # 0x9

    class DayOfWeek(object):
        Monday: Qt.DayOfWeek = ...  # 0x1
        Tuesday: Qt.DayOfWeek = ...  # 0x2
        Wednesday: Qt.DayOfWeek = ...  # 0x3
        Thursday: Qt.DayOfWeek = ...  # 0x4
        Friday: Qt.DayOfWeek = ...  # 0x5
        Saturday: Qt.DayOfWeek = ...  # 0x6
        Sunday: Qt.DayOfWeek = ...  # 0x7

    class DockWidgetArea(object):
        NoDockWidgetArea: Qt.DockWidgetArea = ...  # 0x0
        LeftDockWidgetArea: Qt.DockWidgetArea = ...  # 0x1
        RightDockWidgetArea: Qt.DockWidgetArea = ...  # 0x2
        TopDockWidgetArea: Qt.DockWidgetArea = ...  # 0x4
        BottomDockWidgetArea: Qt.DockWidgetArea = ...  # 0x8
        AllDockWidgetAreas: Qt.DockWidgetArea = ...  # 0xf
        DockWidgetArea_Mask: Qt.DockWidgetArea = ...  # 0xf

    class DockWidgetAreaSizes(object):
        NDockWidgetAreas: Qt.DockWidgetAreaSizes = ...  # 0x4

    class DockWidgetAreas(object): ...

    class DropAction(object):
        IgnoreAction: Qt.DropAction = ...  # 0x0
        CopyAction: Qt.DropAction = ...  # 0x1
        MoveAction: Qt.DropAction = ...  # 0x2
        LinkAction: Qt.DropAction = ...  # 0x4
        ActionMask: Qt.DropAction = ...  # 0xff
        TargetMoveAction: Qt.DropAction = ...  # 0x8002

    class DropActions(object): ...

    class Edge(object):
        TopEdge: Qt.Edge = ...  # 0x1
        LeftEdge: Qt.Edge = ...  # 0x2
        RightEdge: Qt.Edge = ...  # 0x4
        BottomEdge: Qt.Edge = ...  # 0x8

    class Edges(object): ...

    class EnterKeyType(object):
        EnterKeyDefault: Qt.EnterKeyType = ...  # 0x0
        EnterKeyReturn: Qt.EnterKeyType = ...  # 0x1
        EnterKeyDone: Qt.EnterKeyType = ...  # 0x2
        EnterKeyGo: Qt.EnterKeyType = ...  # 0x3
        EnterKeySend: Qt.EnterKeyType = ...  # 0x4
        EnterKeySearch: Qt.EnterKeyType = ...  # 0x5
        EnterKeyNext: Qt.EnterKeyType = ...  # 0x6
        EnterKeyPrevious: Qt.EnterKeyType = ...  # 0x7

    class EventPriority(object):
        LowEventPriority: Qt.EventPriority = ...  # -0x1
        NormalEventPriority: Qt.EventPriority = ...  # 0x0
        HighEventPriority: Qt.EventPriority = ...  # 0x1

    class FillRule(object):
        OddEvenFill: Qt.FillRule = ...  # 0x0
        WindingFill: Qt.FillRule = ...  # 0x1

    class FindChildOption(object):
        FindDirectChildrenOnly: Qt.FindChildOption = ...  # 0x0
        FindChildrenRecursively: Qt.FindChildOption = ...  # 0x1

    class FindChildOptions(object): ...

    class FocusPolicy(object):
        NoFocus: Qt.FocusPolicy = ...  # 0x0
        TabFocus: Qt.FocusPolicy = ...  # 0x1
        ClickFocus: Qt.FocusPolicy = ...  # 0x2
        StrongFocus: Qt.FocusPolicy = ...  # 0xb
        WheelFocus: Qt.FocusPolicy = ...  # 0xf

    class FocusReason(object):
        MouseFocusReason: Qt.FocusReason = ...  # 0x0
        TabFocusReason: Qt.FocusReason = ...  # 0x1
        BacktabFocusReason: Qt.FocusReason = ...  # 0x2
        ActiveWindowFocusReason: Qt.FocusReason = ...  # 0x3
        PopupFocusReason: Qt.FocusReason = ...  # 0x4
        ShortcutFocusReason: Qt.FocusReason = ...  # 0x5
        MenuBarFocusReason: Qt.FocusReason = ...  # 0x6
        OtherFocusReason: Qt.FocusReason = ...  # 0x7
        NoFocusReason: Qt.FocusReason = ...  # 0x8

    class GestureFlag(object):
        DontStartGestureOnChildren: Qt.GestureFlag = ...  # 0x1
        ReceivePartialGestures: Qt.GestureFlag = ...  # 0x2
        IgnoredGesturesPropagateToParent: Qt.GestureFlag = ...  # 0x4

    class GestureFlags(object): ...

    class GestureState(object):
        NoGesture: Qt.GestureState = ...  # 0x0
        GestureStarted: Qt.GestureState = ...  # 0x1
        GestureUpdated: Qt.GestureState = ...  # 0x2
        GestureFinished: Qt.GestureState = ...  # 0x3
        GestureCanceled: Qt.GestureState = ...  # 0x4

    class GestureType(object):
        LastGestureType: Qt.GestureType = ...  # -0x1
        TapGesture: Qt.GestureType = ...  # 0x1
        TapAndHoldGesture: Qt.GestureType = ...  # 0x2
        PanGesture: Qt.GestureType = ...  # 0x3
        PinchGesture: Qt.GestureType = ...  # 0x4
        SwipeGesture: Qt.GestureType = ...  # 0x5
        CustomGesture: Qt.GestureType = ...  # 0x100

    class GlobalColor(object):
        color0: Qt.GlobalColor = ...  # 0x0
        color1: Qt.GlobalColor = ...  # 0x1
        black: Qt.GlobalColor = ...  # 0x2
        white: Qt.GlobalColor = ...  # 0x3
        darkGray: Qt.GlobalColor = ...  # 0x4
        gray: Qt.GlobalColor = ...  # 0x5
        lightGray: Qt.GlobalColor = ...  # 0x6
        red: Qt.GlobalColor = ...  # 0x7
        green: Qt.GlobalColor = ...  # 0x8
        blue: Qt.GlobalColor = ...  # 0x9
        cyan: Qt.GlobalColor = ...  # 0xa
        magenta: Qt.GlobalColor = ...  # 0xb
        yellow: Qt.GlobalColor = ...  # 0xc
        darkRed: Qt.GlobalColor = ...  # 0xd
        darkGreen: Qt.GlobalColor = ...  # 0xe
        darkBlue: Qt.GlobalColor = ...  # 0xf
        darkCyan: Qt.GlobalColor = ...  # 0x10
        darkMagenta: Qt.GlobalColor = ...  # 0x11
        darkYellow: Qt.GlobalColor = ...  # 0x12
        transparent: Qt.GlobalColor = ...  # 0x13

    class HighDpiScaleFactorRoundingPolicy(object):
        Unset: Qt.HighDpiScaleFactorRoundingPolicy = ...  # 0x0
        Round: Qt.HighDpiScaleFactorRoundingPolicy = ...  # 0x1
        Ceil: Qt.HighDpiScaleFactorRoundingPolicy = ...  # 0x2
        Floor: Qt.HighDpiScaleFactorRoundingPolicy = ...  # 0x3
        RoundPreferFloor: Qt.HighDpiScaleFactorRoundingPolicy = ...  # 0x4
        PassThrough: Qt.HighDpiScaleFactorRoundingPolicy = ...  # 0x5

    class HitTestAccuracy(object):
        ExactHit: Qt.HitTestAccuracy = ...  # 0x0
        FuzzyHit: Qt.HitTestAccuracy = ...  # 0x1

    class ImageConversionFlag(object):
        AutoColor: Qt.ImageConversionFlag = ...  # 0x0
        AutoDither: Qt.ImageConversionFlag = ...  # 0x0
        DiffuseDither: Qt.ImageConversionFlag = ...  # 0x0
        ThresholdAlphaDither: Qt.ImageConversionFlag = ...  # 0x0
        MonoOnly: Qt.ImageConversionFlag = ...  # 0x2
        ColorMode_Mask: Qt.ImageConversionFlag = ...  # 0x3
        ColorOnly: Qt.ImageConversionFlag = ...  # 0x3
        OrderedAlphaDither: Qt.ImageConversionFlag = ...  # 0x4
        DiffuseAlphaDither: Qt.ImageConversionFlag = ...  # 0x8
        AlphaDither_Mask: Qt.ImageConversionFlag = ...  # 0xc
        NoAlpha: Qt.ImageConversionFlag = ...  # 0xc
        OrderedDither: Qt.ImageConversionFlag = ...  # 0x10
        ThresholdDither: Qt.ImageConversionFlag = ...  # 0x20
        Dither_Mask: Qt.ImageConversionFlag = ...  # 0x30
        PreferDither: Qt.ImageConversionFlag = ...  # 0x40
        AvoidDither: Qt.ImageConversionFlag = ...  # 0x80
        DitherMode_Mask: Qt.ImageConversionFlag = ...  # 0xc0
        NoOpaqueDetection: Qt.ImageConversionFlag = ...  # 0x100
        NoFormatConversion: Qt.ImageConversionFlag = ...  # 0x200

    class ImageConversionFlags(object): ...

    class InputMethodHint(object):
        ImhExclusiveInputMask: Qt.InputMethodHint = ...  # -0x10000
        ImhNone: Qt.InputMethodHint = ...  # 0x0
        ImhHiddenText: Qt.InputMethodHint = ...  # 0x1
        ImhSensitiveData: Qt.InputMethodHint = ...  # 0x2
        ImhNoAutoUppercase: Qt.InputMethodHint = ...  # 0x4
        ImhPreferNumbers: Qt.InputMethodHint = ...  # 0x8
        ImhPreferUppercase: Qt.InputMethodHint = ...  # 0x10
        ImhPreferLowercase: Qt.InputMethodHint = ...  # 0x20
        ImhNoPredictiveText: Qt.InputMethodHint = ...  # 0x40
        ImhDate: Qt.InputMethodHint = ...  # 0x80
        ImhTime: Qt.InputMethodHint = ...  # 0x100
        ImhPreferLatin: Qt.InputMethodHint = ...  # 0x200
        ImhMultiLine: Qt.InputMethodHint = ...  # 0x400
        ImhNoEditMenu: Qt.InputMethodHint = ...  # 0x800
        ImhNoTextHandles: Qt.InputMethodHint = ...  # 0x1000
        ImhDigitsOnly: Qt.InputMethodHint = ...  # 0x10000
        ImhFormattedNumbersOnly: Qt.InputMethodHint = ...  # 0x20000
        ImhUppercaseOnly: Qt.InputMethodHint = ...  # 0x40000
        ImhLowercaseOnly: Qt.InputMethodHint = ...  # 0x80000
        ImhDialableCharactersOnly: Qt.InputMethodHint = ...  # 0x100000
        ImhEmailCharactersOnly: Qt.InputMethodHint = ...  # 0x200000
        ImhUrlCharactersOnly: Qt.InputMethodHint = ...  # 0x400000
        ImhLatinOnly: Qt.InputMethodHint = ...  # 0x800000

    class InputMethodHints(object): ...
    class InputMethodQueries(object): ...

    class InputMethodQuery(object):
        ImPlatformData: Qt.InputMethodQuery = ...  # -0x80000000
        ImQueryAll: Qt.InputMethodQuery = ...  # -0x1
        ImEnabled: Qt.InputMethodQuery = ...  # 0x1
        ImCursorRectangle: Qt.InputMethodQuery = ...  # 0x2
        ImMicroFocus: Qt.InputMethodQuery = ...  # 0x2
        ImFont: Qt.InputMethodQuery = ...  # 0x4
        ImCursorPosition: Qt.InputMethodQuery = ...  # 0x8
        ImSurroundingText: Qt.InputMethodQuery = ...  # 0x10
        ImCurrentSelection: Qt.InputMethodQuery = ...  # 0x20
        ImMaximumTextLength: Qt.InputMethodQuery = ...  # 0x40
        ImAnchorPosition: Qt.InputMethodQuery = ...  # 0x80
        ImHints: Qt.InputMethodQuery = ...  # 0x100
        ImPreferredLanguage: Qt.InputMethodQuery = ...  # 0x200
        ImAbsolutePosition: Qt.InputMethodQuery = ...  # 0x400
        ImTextBeforeCursor: Qt.InputMethodQuery = ...  # 0x800
        ImTextAfterCursor: Qt.InputMethodQuery = ...  # 0x1000
        ImEnterKeyType: Qt.InputMethodQuery = ...  # 0x2000
        ImAnchorRectangle: Qt.InputMethodQuery = ...  # 0x4000
        ImQueryInput: Qt.InputMethodQuery = ...  # 0x40ba
        ImInputItemClipRectangle: Qt.InputMethodQuery = ...  # 0x8000

    class ItemDataRole(object):
        DisplayRole: Qt.ItemDataRole = ...  # 0x0
        DecorationRole: Qt.ItemDataRole = ...  # 0x1
        EditRole: Qt.ItemDataRole = ...  # 0x2
        ToolTipRole: Qt.ItemDataRole = ...  # 0x3
        StatusTipRole: Qt.ItemDataRole = ...  # 0x4
        WhatsThisRole: Qt.ItemDataRole = ...  # 0x5
        FontRole: Qt.ItemDataRole = ...  # 0x6
        TextAlignmentRole: Qt.ItemDataRole = ...  # 0x7
        BackgroundColorRole: Qt.ItemDataRole = ...  # 0x8
        BackgroundRole: Qt.ItemDataRole = ...  # 0x8
        ForegroundRole: Qt.ItemDataRole = ...  # 0x9
        TextColorRole: Qt.ItemDataRole = ...  # 0x9
        CheckStateRole: Qt.ItemDataRole = ...  # 0xa
        AccessibleTextRole: Qt.ItemDataRole = ...  # 0xb
        AccessibleDescriptionRole: Qt.ItemDataRole = ...  # 0xc
        SizeHintRole: Qt.ItemDataRole = ...  # 0xd
        InitialSortOrderRole: Qt.ItemDataRole = ...  # 0xe
        DisplayPropertyRole: Qt.ItemDataRole = ...  # 0x1b
        DecorationPropertyRole: Qt.ItemDataRole = ...  # 0x1c
        ToolTipPropertyRole: Qt.ItemDataRole = ...  # 0x1d
        StatusTipPropertyRole: Qt.ItemDataRole = ...  # 0x1e
        WhatsThisPropertyRole: Qt.ItemDataRole = ...  # 0x1f
        UserRole: Qt.ItemDataRole = ...  # 0x100

    class ItemFlag(object):
        NoItemFlags: Qt.ItemFlag = ...  # 0x0
        ItemIsSelectable: Qt.ItemFlag = ...  # 0x1
        ItemIsEditable: Qt.ItemFlag = ...  # 0x2
        ItemIsDragEnabled: Qt.ItemFlag = ...  # 0x4
        ItemIsDropEnabled: Qt.ItemFlag = ...  # 0x8
        ItemIsUserCheckable: Qt.ItemFlag = ...  # 0x10
        ItemIsEnabled: Qt.ItemFlag = ...  # 0x20
        ItemIsAutoTristate: Qt.ItemFlag = ...  # 0x40
        ItemIsTristate: Qt.ItemFlag = ...  # 0x40
        ItemNeverHasChildren: Qt.ItemFlag = ...  # 0x80
        ItemIsUserTristate: Qt.ItemFlag = ...  # 0x100

    class ItemFlags(object): ...

    class ItemSelectionMode(object):
        ContainsItemShape: Qt.ItemSelectionMode = ...  # 0x0
        IntersectsItemShape: Qt.ItemSelectionMode = ...  # 0x1
        ContainsItemBoundingRect: Qt.ItemSelectionMode = ...  # 0x2
        IntersectsItemBoundingRect: Qt.ItemSelectionMode = ...  # 0x3

    class ItemSelectionOperation(object):
        ReplaceSelection: Qt.ItemSelectionOperation = ...  # 0x0
        AddToSelection: Qt.ItemSelectionOperation = ...  # 0x1

    class Key(object):
        Key_Any: Qt.Key = ...  # 0x20
        Key_Space: Qt.Key = ...  # 0x20
        Key_Exclam: Qt.Key = ...  # 0x21
        Key_QuoteDbl: Qt.Key = ...  # 0x22
        Key_NumberSign: Qt.Key = ...  # 0x23
        Key_Dollar: Qt.Key = ...  # 0x24
        Key_Percent: Qt.Key = ...  # 0x25
        Key_Ampersand: Qt.Key = ...  # 0x26
        Key_Apostrophe: Qt.Key = ...  # 0x27
        Key_ParenLeft: Qt.Key = ...  # 0x28
        Key_ParenRight: Qt.Key = ...  # 0x29
        Key_Asterisk: Qt.Key = ...  # 0x2a
        Key_Plus: Qt.Key = ...  # 0x2b
        Key_Comma: Qt.Key = ...  # 0x2c
        Key_Minus: Qt.Key = ...  # 0x2d
        Key_Period: Qt.Key = ...  # 0x2e
        Key_Slash: Qt.Key = ...  # 0x2f
        Key_0: Qt.Key = ...  # 0x30
        Key_1: Qt.Key = ...  # 0x31
        Key_2: Qt.Key = ...  # 0x32
        Key_3: Qt.Key = ...  # 0x33
        Key_4: Qt.Key = ...  # 0x34
        Key_5: Qt.Key = ...  # 0x35
        Key_6: Qt.Key = ...  # 0x36
        Key_7: Qt.Key = ...  # 0x37
        Key_8: Qt.Key = ...  # 0x38
        Key_9: Qt.Key = ...  # 0x39
        Key_Colon: Qt.Key = ...  # 0x3a
        Key_Semicolon: Qt.Key = ...  # 0x3b
        Key_Less: Qt.Key = ...  # 0x3c
        Key_Equal: Qt.Key = ...  # 0x3d
        Key_Greater: Qt.Key = ...  # 0x3e
        Key_Question: Qt.Key = ...  # 0x3f
        Key_At: Qt.Key = ...  # 0x40
        Key_A: Qt.Key = ...  # 0x41
        Key_B: Qt.Key = ...  # 0x42
        Key_C: Qt.Key = ...  # 0x43
        Key_D: Qt.Key = ...  # 0x44
        Key_E: Qt.Key = ...  # 0x45
        Key_F: Qt.Key = ...  # 0x46
        Key_G: Qt.Key = ...  # 0x47
        Key_H: Qt.Key = ...  # 0x48
        Key_I: Qt.Key = ...  # 0x49
        Key_J: Qt.Key = ...  # 0x4a
        Key_K: Qt.Key = ...  # 0x4b
        Key_L: Qt.Key = ...  # 0x4c
        Key_M: Qt.Key = ...  # 0x4d
        Key_N: Qt.Key = ...  # 0x4e
        Key_O: Qt.Key = ...  # 0x4f
        Key_P: Qt.Key = ...  # 0x50
        Key_Q: Qt.Key = ...  # 0x51
        Key_R: Qt.Key = ...  # 0x52
        Key_S: Qt.Key = ...  # 0x53
        Key_T: Qt.Key = ...  # 0x54
        Key_U: Qt.Key = ...  # 0x55
        Key_V: Qt.Key = ...  # 0x56
        Key_W: Qt.Key = ...  # 0x57
        Key_X: Qt.Key = ...  # 0x58
        Key_Y: Qt.Key = ...  # 0x59
        Key_Z: Qt.Key = ...  # 0x5a
        Key_BracketLeft: Qt.Key = ...  # 0x5b
        Key_Backslash: Qt.Key = ...  # 0x5c
        Key_BracketRight: Qt.Key = ...  # 0x5d
        Key_AsciiCircum: Qt.Key = ...  # 0x5e
        Key_Underscore: Qt.Key = ...  # 0x5f
        Key_QuoteLeft: Qt.Key = ...  # 0x60
        Key_BraceLeft: Qt.Key = ...  # 0x7b
        Key_Bar: Qt.Key = ...  # 0x7c
        Key_BraceRight: Qt.Key = ...  # 0x7d
        Key_AsciiTilde: Qt.Key = ...  # 0x7e
        Key_nobreakspace: Qt.Key = ...  # 0xa0
        Key_exclamdown: Qt.Key = ...  # 0xa1
        Key_cent: Qt.Key = ...  # 0xa2
        Key_sterling: Qt.Key = ...  # 0xa3
        Key_currency: Qt.Key = ...  # 0xa4
        Key_yen: Qt.Key = ...  # 0xa5
        Key_brokenbar: Qt.Key = ...  # 0xa6
        Key_section: Qt.Key = ...  # 0xa7
        Key_diaeresis: Qt.Key = ...  # 0xa8
        Key_copyright: Qt.Key = ...  # 0xa9
        Key_ordfeminine: Qt.Key = ...  # 0xaa
        Key_guillemotleft: Qt.Key = ...  # 0xab
        Key_notsign: Qt.Key = ...  # 0xac
        Key_hyphen: Qt.Key = ...  # 0xad
        Key_registered: Qt.Key = ...  # 0xae
        Key_macron: Qt.Key = ...  # 0xaf
        Key_degree: Qt.Key = ...  # 0xb0
        Key_plusminus: Qt.Key = ...  # 0xb1
        Key_twosuperior: Qt.Key = ...  # 0xb2
        Key_threesuperior: Qt.Key = ...  # 0xb3
        Key_acute: Qt.Key = ...  # 0xb4
        Key_mu: Qt.Key = ...  # 0xb5
        Key_paragraph: Qt.Key = ...  # 0xb6
        Key_periodcentered: Qt.Key = ...  # 0xb7
        Key_cedilla: Qt.Key = ...  # 0xb8
        Key_onesuperior: Qt.Key = ...  # 0xb9
        Key_masculine: Qt.Key = ...  # 0xba
        Key_guillemotright: Qt.Key = ...  # 0xbb
        Key_onequarter: Qt.Key = ...  # 0xbc
        Key_onehalf: Qt.Key = ...  # 0xbd
        Key_threequarters: Qt.Key = ...  # 0xbe
        Key_questiondown: Qt.Key = ...  # 0xbf
        Key_Agrave: Qt.Key = ...  # 0xc0
        Key_Aacute: Qt.Key = ...  # 0xc1
        Key_Acircumflex: Qt.Key = ...  # 0xc2
        Key_Atilde: Qt.Key = ...  # 0xc3
        Key_Adiaeresis: Qt.Key = ...  # 0xc4
        Key_Aring: Qt.Key = ...  # 0xc5
        Key_AE: Qt.Key = ...  # 0xc6
        Key_Ccedilla: Qt.Key = ...  # 0xc7
        Key_Egrave: Qt.Key = ...  # 0xc8
        Key_Eacute: Qt.Key = ...  # 0xc9
        Key_Ecircumflex: Qt.Key = ...  # 0xca
        Key_Ediaeresis: Qt.Key = ...  # 0xcb
        Key_Igrave: Qt.Key = ...  # 0xcc
        Key_Iacute: Qt.Key = ...  # 0xcd
        Key_Icircumflex: Qt.Key = ...  # 0xce
        Key_Idiaeresis: Qt.Key = ...  # 0xcf
        Key_ETH: Qt.Key = ...  # 0xd0
        Key_Ntilde: Qt.Key = ...  # 0xd1
        Key_Ograve: Qt.Key = ...  # 0xd2
        Key_Oacute: Qt.Key = ...  # 0xd3
        Key_Ocircumflex: Qt.Key = ...  # 0xd4
        Key_Otilde: Qt.Key = ...  # 0xd5
        Key_Odiaeresis: Qt.Key = ...  # 0xd6
        Key_multiply: Qt.Key = ...  # 0xd7
        Key_Ooblique: Qt.Key = ...  # 0xd8
        Key_Ugrave: Qt.Key = ...  # 0xd9
        Key_Uacute: Qt.Key = ...  # 0xda
        Key_Ucircumflex: Qt.Key = ...  # 0xdb
        Key_Udiaeresis: Qt.Key = ...  # 0xdc
        Key_Yacute: Qt.Key = ...  # 0xdd
        Key_THORN: Qt.Key = ...  # 0xde
        Key_ssharp: Qt.Key = ...  # 0xdf
        Key_division: Qt.Key = ...  # 0xf7
        Key_ydiaeresis: Qt.Key = ...  # 0xff
        Key_Escape: Qt.Key = ...  # 0x1000000
        Key_Tab: Qt.Key = ...  # 0x1000001
        Key_Backtab: Qt.Key = ...  # 0x1000002
        Key_Backspace: Qt.Key = ...  # 0x1000003
        Key_Return: Qt.Key = ...  # 0x1000004
        Key_Enter: Qt.Key = ...  # 0x1000005
        Key_Insert: Qt.Key = ...  # 0x1000006
        Key_Delete: Qt.Key = ...  # 0x1000007
        Key_Pause: Qt.Key = ...  # 0x1000008
        Key_Print: Qt.Key = ...  # 0x1000009
        Key_SysReq: Qt.Key = ...  # 0x100000a
        Key_Clear: Qt.Key = ...  # 0x100000b
        Key_Home: Qt.Key = ...  # 0x1000010
        Key_End: Qt.Key = ...  # 0x1000011
        Key_Left: Qt.Key = ...  # 0x1000012
        Key_Up: Qt.Key = ...  # 0x1000013
        Key_Right: Qt.Key = ...  # 0x1000014
        Key_Down: Qt.Key = ...  # 0x1000015
        Key_PageUp: Qt.Key = ...  # 0x1000016
        Key_PageDown: Qt.Key = ...  # 0x1000017
        Key_Shift: Qt.Key = ...  # 0x1000020
        Key_Control: Qt.Key = ...  # 0x1000021
        Key_Meta: Qt.Key = ...  # 0x1000022
        Key_Alt: Qt.Key = ...  # 0x1000023
        Key_CapsLock: Qt.Key = ...  # 0x1000024
        Key_NumLock: Qt.Key = ...  # 0x1000025
        Key_ScrollLock: Qt.Key = ...  # 0x1000026
        Key_F1: Qt.Key = ...  # 0x1000030
        Key_F2: Qt.Key = ...  # 0x1000031
        Key_F3: Qt.Key = ...  # 0x1000032
        Key_F4: Qt.Key = ...  # 0x1000033
        Key_F5: Qt.Key = ...  # 0x1000034
        Key_F6: Qt.Key = ...  # 0x1000035
        Key_F7: Qt.Key = ...  # 0x1000036
        Key_F8: Qt.Key = ...  # 0x1000037
        Key_F9: Qt.Key = ...  # 0x1000038
        Key_F10: Qt.Key = ...  # 0x1000039
        Key_F11: Qt.Key = ...  # 0x100003a
        Key_F12: Qt.Key = ...  # 0x100003b
        Key_F13: Qt.Key = ...  # 0x100003c
        Key_F14: Qt.Key = ...  # 0x100003d
        Key_F15: Qt.Key = ...  # 0x100003e
        Key_F16: Qt.Key = ...  # 0x100003f
        Key_F17: Qt.Key = ...  # 0x1000040
        Key_F18: Qt.Key = ...  # 0x1000041
        Key_F19: Qt.Key = ...  # 0x1000042
        Key_F20: Qt.Key = ...  # 0x1000043
        Key_F21: Qt.Key = ...  # 0x1000044
        Key_F22: Qt.Key = ...  # 0x1000045
        Key_F23: Qt.Key = ...  # 0x1000046
        Key_F24: Qt.Key = ...  # 0x1000047
        Key_F25: Qt.Key = ...  # 0x1000048
        Key_F26: Qt.Key = ...  # 0x1000049
        Key_F27: Qt.Key = ...  # 0x100004a
        Key_F28: Qt.Key = ...  # 0x100004b
        Key_F29: Qt.Key = ...  # 0x100004c
        Key_F30: Qt.Key = ...  # 0x100004d
        Key_F31: Qt.Key = ...  # 0x100004e
        Key_F32: Qt.Key = ...  # 0x100004f
        Key_F33: Qt.Key = ...  # 0x1000050
        Key_F34: Qt.Key = ...  # 0x1000051
        Key_F35: Qt.Key = ...  # 0x1000052
        Key_Super_L: Qt.Key = ...  # 0x1000053
        Key_Super_R: Qt.Key = ...  # 0x1000054
        Key_Menu: Qt.Key = ...  # 0x1000055
        Key_Hyper_L: Qt.Key = ...  # 0x1000056
        Key_Hyper_R: Qt.Key = ...  # 0x1000057
        Key_Help: Qt.Key = ...  # 0x1000058
        Key_Direction_L: Qt.Key = ...  # 0x1000059
        Key_Direction_R: Qt.Key = ...  # 0x1000060
        Key_Back: Qt.Key = ...  # 0x1000061
        Key_Forward: Qt.Key = ...  # 0x1000062
        Key_Stop: Qt.Key = ...  # 0x1000063
        Key_Refresh: Qt.Key = ...  # 0x1000064
        Key_VolumeDown: Qt.Key = ...  # 0x1000070
        Key_VolumeMute: Qt.Key = ...  # 0x1000071
        Key_VolumeUp: Qt.Key = ...  # 0x1000072
        Key_BassBoost: Qt.Key = ...  # 0x1000073
        Key_BassUp: Qt.Key = ...  # 0x1000074
        Key_BassDown: Qt.Key = ...  # 0x1000075
        Key_TrebleUp: Qt.Key = ...  # 0x1000076
        Key_TrebleDown: Qt.Key = ...  # 0x1000077
        Key_MediaPlay: Qt.Key = ...  # 0x1000080
        Key_MediaStop: Qt.Key = ...  # 0x1000081
        Key_MediaPrevious: Qt.Key = ...  # 0x1000082
        Key_MediaNext: Qt.Key = ...  # 0x1000083
        Key_MediaRecord: Qt.Key = ...  # 0x1000084
        Key_MediaPause: Qt.Key = ...  # 0x1000085
        Key_MediaTogglePlayPause: Qt.Key = ...  # 0x1000086
        Key_HomePage: Qt.Key = ...  # 0x1000090
        Key_Favorites: Qt.Key = ...  # 0x1000091
        Key_Search: Qt.Key = ...  # 0x1000092
        Key_Standby: Qt.Key = ...  # 0x1000093
        Key_OpenUrl: Qt.Key = ...  # 0x1000094
        Key_LaunchMail: Qt.Key = ...  # 0x10000a0
        Key_LaunchMedia: Qt.Key = ...  # 0x10000a1
        Key_Launch0: Qt.Key = ...  # 0x10000a2
        Key_Launch1: Qt.Key = ...  # 0x10000a3
        Key_Launch2: Qt.Key = ...  # 0x10000a4
        Key_Launch3: Qt.Key = ...  # 0x10000a5
        Key_Launch4: Qt.Key = ...  # 0x10000a6
        Key_Launch5: Qt.Key = ...  # 0x10000a7
        Key_Launch6: Qt.Key = ...  # 0x10000a8
        Key_Launch7: Qt.Key = ...  # 0x10000a9
        Key_Launch8: Qt.Key = ...  # 0x10000aa
        Key_Launch9: Qt.Key = ...  # 0x10000ab
        Key_LaunchA: Qt.Key = ...  # 0x10000ac
        Key_LaunchB: Qt.Key = ...  # 0x10000ad
        Key_LaunchC: Qt.Key = ...  # 0x10000ae
        Key_LaunchD: Qt.Key = ...  # 0x10000af
        Key_LaunchE: Qt.Key = ...  # 0x10000b0
        Key_LaunchF: Qt.Key = ...  # 0x10000b1
        Key_MonBrightnessUp: Qt.Key = ...  # 0x10000b2
        Key_MonBrightnessDown: Qt.Key = ...  # 0x10000b3
        Key_KeyboardLightOnOff: Qt.Key = ...  # 0x10000b4
        Key_KeyboardBrightnessUp: Qt.Key = ...  # 0x10000b5
        Key_KeyboardBrightnessDown: Qt.Key = ...  # 0x10000b6
        Key_PowerOff: Qt.Key = ...  # 0x10000b7
        Key_WakeUp: Qt.Key = ...  # 0x10000b8
        Key_Eject: Qt.Key = ...  # 0x10000b9
        Key_ScreenSaver: Qt.Key = ...  # 0x10000ba
        Key_WWW: Qt.Key = ...  # 0x10000bb
        Key_Memo: Qt.Key = ...  # 0x10000bc
        Key_LightBulb: Qt.Key = ...  # 0x10000bd
        Key_Shop: Qt.Key = ...  # 0x10000be
        Key_History: Qt.Key = ...  # 0x10000bf
        Key_AddFavorite: Qt.Key = ...  # 0x10000c0
        Key_HotLinks: Qt.Key = ...  # 0x10000c1
        Key_BrightnessAdjust: Qt.Key = ...  # 0x10000c2
        Key_Finance: Qt.Key = ...  # 0x10000c3
        Key_Community: Qt.Key = ...  # 0x10000c4
        Key_AudioRewind: Qt.Key = ...  # 0x10000c5
        Key_BackForward: Qt.Key = ...  # 0x10000c6
        Key_ApplicationLeft: Qt.Key = ...  # 0x10000c7
        Key_ApplicationRight: Qt.Key = ...  # 0x10000c8
        Key_Book: Qt.Key = ...  # 0x10000c9
        Key_CD: Qt.Key = ...  # 0x10000ca
        Key_Calculator: Qt.Key = ...  # 0x10000cb
        Key_ToDoList: Qt.Key = ...  # 0x10000cc
        Key_ClearGrab: Qt.Key = ...  # 0x10000cd
        Key_Close: Qt.Key = ...  # 0x10000ce
        Key_Copy: Qt.Key = ...  # 0x10000cf
        Key_Cut: Qt.Key = ...  # 0x10000d0
        Key_Display: Qt.Key = ...  # 0x10000d1
        Key_DOS: Qt.Key = ...  # 0x10000d2
        Key_Documents: Qt.Key = ...  # 0x10000d3
        Key_Excel: Qt.Key = ...  # 0x10000d4
        Key_Explorer: Qt.Key = ...  # 0x10000d5
        Key_Game: Qt.Key = ...  # 0x10000d6
        Key_Go: Qt.Key = ...  # 0x10000d7
        Key_iTouch: Qt.Key = ...  # 0x10000d8
        Key_LogOff: Qt.Key = ...  # 0x10000d9
        Key_Market: Qt.Key = ...  # 0x10000da
        Key_Meeting: Qt.Key = ...  # 0x10000db
        Key_MenuKB: Qt.Key = ...  # 0x10000dc
        Key_MenuPB: Qt.Key = ...  # 0x10000dd
        Key_MySites: Qt.Key = ...  # 0x10000de
        Key_News: Qt.Key = ...  # 0x10000df
        Key_OfficeHome: Qt.Key = ...  # 0x10000e0
        Key_Option: Qt.Key = ...  # 0x10000e1
        Key_Paste: Qt.Key = ...  # 0x10000e2
        Key_Phone: Qt.Key = ...  # 0x10000e3
        Key_Calendar: Qt.Key = ...  # 0x10000e4
        Key_Reply: Qt.Key = ...  # 0x10000e5
        Key_Reload: Qt.Key = ...  # 0x10000e6
        Key_RotateWindows: Qt.Key = ...  # 0x10000e7
        Key_RotationPB: Qt.Key = ...  # 0x10000e8
        Key_RotationKB: Qt.Key = ...  # 0x10000e9
        Key_Save: Qt.Key = ...  # 0x10000ea
        Key_Send: Qt.Key = ...  # 0x10000eb
        Key_Spell: Qt.Key = ...  # 0x10000ec
        Key_SplitScreen: Qt.Key = ...  # 0x10000ed
        Key_Support: Qt.Key = ...  # 0x10000ee
        Key_TaskPane: Qt.Key = ...  # 0x10000ef
        Key_Terminal: Qt.Key = ...  # 0x10000f0
        Key_Tools: Qt.Key = ...  # 0x10000f1
        Key_Travel: Qt.Key = ...  # 0x10000f2
        Key_Video: Qt.Key = ...  # 0x10000f3
        Key_Word: Qt.Key = ...  # 0x10000f4
        Key_Xfer: Qt.Key = ...  # 0x10000f5
        Key_ZoomIn: Qt.Key = ...  # 0x10000f6
        Key_ZoomOut: Qt.Key = ...  # 0x10000f7
        Key_Away: Qt.Key = ...  # 0x10000f8
        Key_Messenger: Qt.Key = ...  # 0x10000f9
        Key_WebCam: Qt.Key = ...  # 0x10000fa
        Key_MailForward: Qt.Key = ...  # 0x10000fb
        Key_Pictures: Qt.Key = ...  # 0x10000fc
        Key_Music: Qt.Key = ...  # 0x10000fd
        Key_Battery: Qt.Key = ...  # 0x10000fe
        Key_Bluetooth: Qt.Key = ...  # 0x10000ff
        Key_WLAN: Qt.Key = ...  # 0x1000100
        Key_UWB: Qt.Key = ...  # 0x1000101
        Key_AudioForward: Qt.Key = ...  # 0x1000102
        Key_AudioRepeat: Qt.Key = ...  # 0x1000103
        Key_AudioRandomPlay: Qt.Key = ...  # 0x1000104
        Key_Subtitle: Qt.Key = ...  # 0x1000105
        Key_AudioCycleTrack: Qt.Key = ...  # 0x1000106
        Key_Time: Qt.Key = ...  # 0x1000107
        Key_Hibernate: Qt.Key = ...  # 0x1000108
        Key_View: Qt.Key = ...  # 0x1000109
        Key_TopMenu: Qt.Key = ...  # 0x100010a
        Key_PowerDown: Qt.Key = ...  # 0x100010b
        Key_Suspend: Qt.Key = ...  # 0x100010c
        Key_ContrastAdjust: Qt.Key = ...  # 0x100010d
        Key_LaunchG: Qt.Key = ...  # 0x100010e
        Key_LaunchH: Qt.Key = ...  # 0x100010f
        Key_TouchpadToggle: Qt.Key = ...  # 0x1000110
        Key_TouchpadOn: Qt.Key = ...  # 0x1000111
        Key_TouchpadOff: Qt.Key = ...  # 0x1000112
        Key_MicMute: Qt.Key = ...  # 0x1000113
        Key_Red: Qt.Key = ...  # 0x1000114
        Key_Green: Qt.Key = ...  # 0x1000115
        Key_Yellow: Qt.Key = ...  # 0x1000116
        Key_Blue: Qt.Key = ...  # 0x1000117
        Key_ChannelUp: Qt.Key = ...  # 0x1000118
        Key_ChannelDown: Qt.Key = ...  # 0x1000119
        Key_Guide: Qt.Key = ...  # 0x100011a
        Key_Info: Qt.Key = ...  # 0x100011b
        Key_Settings: Qt.Key = ...  # 0x100011c
        Key_MicVolumeUp: Qt.Key = ...  # 0x100011d
        Key_MicVolumeDown: Qt.Key = ...  # 0x100011e
        Key_New: Qt.Key = ...  # 0x1000120
        Key_Open: Qt.Key = ...  # 0x1000121
        Key_Find: Qt.Key = ...  # 0x1000122
        Key_Undo: Qt.Key = ...  # 0x1000123
        Key_Redo: Qt.Key = ...  # 0x1000124
        Key_AltGr: Qt.Key = ...  # 0x1001103
        Key_Multi_key: Qt.Key = ...  # 0x1001120
        Key_Kanji: Qt.Key = ...  # 0x1001121
        Key_Muhenkan: Qt.Key = ...  # 0x1001122
        Key_Henkan: Qt.Key = ...  # 0x1001123
        Key_Romaji: Qt.Key = ...  # 0x1001124
        Key_Hiragana: Qt.Key = ...  # 0x1001125
        Key_Katakana: Qt.Key = ...  # 0x1001126
        Key_Hiragana_Katakana: Qt.Key = ...  # 0x1001127
        Key_Zenkaku: Qt.Key = ...  # 0x1001128
        Key_Hankaku: Qt.Key = ...  # 0x1001129
        Key_Zenkaku_Hankaku: Qt.Key = ...  # 0x100112a
        Key_Touroku: Qt.Key = ...  # 0x100112b
        Key_Massyo: Qt.Key = ...  # 0x100112c
        Key_Kana_Lock: Qt.Key = ...  # 0x100112d
        Key_Kana_Shift: Qt.Key = ...  # 0x100112e
        Key_Eisu_Shift: Qt.Key = ...  # 0x100112f
        Key_Eisu_toggle: Qt.Key = ...  # 0x1001130
        Key_Hangul: Qt.Key = ...  # 0x1001131
        Key_Hangul_Start: Qt.Key = ...  # 0x1001132
        Key_Hangul_End: Qt.Key = ...  # 0x1001133
        Key_Hangul_Hanja: Qt.Key = ...  # 0x1001134
        Key_Hangul_Jamo: Qt.Key = ...  # 0x1001135
        Key_Hangul_Romaja: Qt.Key = ...  # 0x1001136
        Key_Codeinput: Qt.Key = ...  # 0x1001137
        Key_Hangul_Jeonja: Qt.Key = ...  # 0x1001138
        Key_Hangul_Banja: Qt.Key = ...  # 0x1001139
        Key_Hangul_PreHanja: Qt.Key = ...  # 0x100113a
        Key_Hangul_PostHanja: Qt.Key = ...  # 0x100113b
        Key_SingleCandidate: Qt.Key = ...  # 0x100113c
        Key_MultipleCandidate: Qt.Key = ...  # 0x100113d
        Key_PreviousCandidate: Qt.Key = ...  # 0x100113e
        Key_Hangul_Special: Qt.Key = ...  # 0x100113f
        Key_Mode_switch: Qt.Key = ...  # 0x100117e
        Key_Dead_Grave: Qt.Key = ...  # 0x1001250
        Key_Dead_Acute: Qt.Key = ...  # 0x1001251
        Key_Dead_Circumflex: Qt.Key = ...  # 0x1001252
        Key_Dead_Tilde: Qt.Key = ...  # 0x1001253
        Key_Dead_Macron: Qt.Key = ...  # 0x1001254
        Key_Dead_Breve: Qt.Key = ...  # 0x1001255
        Key_Dead_Abovedot: Qt.Key = ...  # 0x1001256
        Key_Dead_Diaeresis: Qt.Key = ...  # 0x1001257
        Key_Dead_Abovering: Qt.Key = ...  # 0x1001258
        Key_Dead_Doubleacute: Qt.Key = ...  # 0x1001259
        Key_Dead_Caron: Qt.Key = ...  # 0x100125a
        Key_Dead_Cedilla: Qt.Key = ...  # 0x100125b
        Key_Dead_Ogonek: Qt.Key = ...  # 0x100125c
        Key_Dead_Iota: Qt.Key = ...  # 0x100125d
        Key_Dead_Voiced_Sound: Qt.Key = ...  # 0x100125e
        Key_Dead_Semivoiced_Sound: Qt.Key = ...  # 0x100125f
        Key_Dead_Belowdot: Qt.Key = ...  # 0x1001260
        Key_Dead_Hook: Qt.Key = ...  # 0x1001261
        Key_Dead_Horn: Qt.Key = ...  # 0x1001262
        Key_Dead_Stroke: Qt.Key = ...  # 0x1001263
        Key_Dead_Abovecomma: Qt.Key = ...  # 0x1001264
        Key_Dead_Abovereversedcomma: Qt.Key = ...  # 0x1001265
        Key_Dead_Doublegrave: Qt.Key = ...  # 0x1001266
        Key_Dead_Belowring: Qt.Key = ...  # 0x1001267
        Key_Dead_Belowmacron: Qt.Key = ...  # 0x1001268
        Key_Dead_Belowcircumflex: Qt.Key = ...  # 0x1001269
        Key_Dead_Belowtilde: Qt.Key = ...  # 0x100126a
        Key_Dead_Belowbreve: Qt.Key = ...  # 0x100126b
        Key_Dead_Belowdiaeresis: Qt.Key = ...  # 0x100126c
        Key_Dead_Invertedbreve: Qt.Key = ...  # 0x100126d
        Key_Dead_Belowcomma: Qt.Key = ...  # 0x100126e
        Key_Dead_Currency: Qt.Key = ...  # 0x100126f
        Key_Dead_a: Qt.Key = ...  # 0x1001280
        Key_Dead_A: Qt.Key = ...  # 0x1001281
        Key_Dead_e: Qt.Key = ...  # 0x1001282
        Key_Dead_E: Qt.Key = ...  # 0x1001283
        Key_Dead_i: Qt.Key = ...  # 0x1001284
        Key_Dead_I: Qt.Key = ...  # 0x1001285
        Key_Dead_o: Qt.Key = ...  # 0x1001286
        Key_Dead_O: Qt.Key = ...  # 0x1001287
        Key_Dead_u: Qt.Key = ...  # 0x1001288
        Key_Dead_U: Qt.Key = ...  # 0x1001289
        Key_Dead_Small_Schwa: Qt.Key = ...  # 0x100128a
        Key_Dead_Capital_Schwa: Qt.Key = ...  # 0x100128b
        Key_Dead_Greek: Qt.Key = ...  # 0x100128c
        Key_Dead_Lowline: Qt.Key = ...  # 0x1001290
        Key_Dead_Aboveverticalline: Qt.Key = ...  # 0x1001291
        Key_Dead_Belowverticalline: Qt.Key = ...  # 0x1001292
        Key_Dead_Longsolidusoverlay: Qt.Key = ...  # 0x1001293
        Key_MediaLast: Qt.Key = ...  # 0x100ffff
        Key_Select: Qt.Key = ...  # 0x1010000
        Key_Yes: Qt.Key = ...  # 0x1010001
        Key_No: Qt.Key = ...  # 0x1010002
        Key_Cancel: Qt.Key = ...  # 0x1020001
        Key_Printer: Qt.Key = ...  # 0x1020002
        Key_Execute: Qt.Key = ...  # 0x1020003
        Key_Sleep: Qt.Key = ...  # 0x1020004
        Key_Play: Qt.Key = ...  # 0x1020005
        Key_Zoom: Qt.Key = ...  # 0x1020006
        Key_Exit: Qt.Key = ...  # 0x102000a
        Key_Context1: Qt.Key = ...  # 0x1100000
        Key_Context2: Qt.Key = ...  # 0x1100001
        Key_Context3: Qt.Key = ...  # 0x1100002
        Key_Context4: Qt.Key = ...  # 0x1100003
        Key_Call: Qt.Key = ...  # 0x1100004
        Key_Hangup: Qt.Key = ...  # 0x1100005
        Key_Flip: Qt.Key = ...  # 0x1100006
        Key_ToggleCallHangup: Qt.Key = ...  # 0x1100007
        Key_VoiceDial: Qt.Key = ...  # 0x1100008
        Key_LastNumberRedial: Qt.Key = ...  # 0x1100009
        Key_Camera: Qt.Key = ...  # 0x1100020
        Key_CameraFocus: Qt.Key = ...  # 0x1100021
        Key_unknown: Qt.Key = ...  # 0x1ffffff

    class KeyboardModifier(object):
        KeyboardModifierMask: Qt.KeyboardModifier = ...  # -0x2000000
        NoModifier: Qt.KeyboardModifier = ...  # 0x0
        ShiftModifier: Qt.KeyboardModifier = ...  # 0x2000000
        ControlModifier: Qt.KeyboardModifier = ...  # 0x4000000
        AltModifier: Qt.KeyboardModifier = ...  # 0x8000000
        MetaModifier: Qt.KeyboardModifier = ...  # 0x10000000
        KeypadModifier: Qt.KeyboardModifier = ...  # 0x20000000
        GroupSwitchModifier: Qt.KeyboardModifier = ...  # 0x40000000

    class KeyboardModifiers(object): ...

    class LayoutDirection(object):
        LeftToRight: Qt.LayoutDirection = ...  # 0x0
        RightToLeft: Qt.LayoutDirection = ...  # 0x1
        LayoutDirectionAuto: Qt.LayoutDirection = ...  # 0x2

    class MaskMode(object):
        MaskInColor: Qt.MaskMode = ...  # 0x0
        MaskOutColor: Qt.MaskMode = ...  # 0x1

    class MatchFlag(object):
        MatchExactly: Qt.MatchFlag = ...  # 0x0
        MatchContains: Qt.MatchFlag = ...  # 0x1
        MatchStartsWith: Qt.MatchFlag = ...  # 0x2
        MatchEndsWith: Qt.MatchFlag = ...  # 0x3
        MatchRegExp: Qt.MatchFlag = ...  # 0x4
        MatchWildcard: Qt.MatchFlag = ...  # 0x5
        MatchFixedString: Qt.MatchFlag = ...  # 0x8
        MatchRegularExpression: Qt.MatchFlag = ...  # 0x9
        MatchCaseSensitive: Qt.MatchFlag = ...  # 0x10
        MatchWrap: Qt.MatchFlag = ...  # 0x20
        MatchRecursive: Qt.MatchFlag = ...  # 0x40

    class MatchFlags(object): ...

    class Modifier(object):
        MODIFIER_MASK: Qt.Modifier = ...  # -0x2000000
        UNICODE_ACCEL: Qt.Modifier = ...  # 0x0
        SHIFT: Qt.Modifier = ...  # 0x2000000
        CTRL: Qt.Modifier = ...  # 0x4000000
        ALT: Qt.Modifier = ...  # 0x8000000
        META: Qt.Modifier = ...  # 0x10000000

    class MouseButton(object):
        MouseButtonMask: Qt.MouseButton = ...  # -0x1
        NoButton: Qt.MouseButton = ...  # 0x0
        LeftButton: Qt.MouseButton = ...  # 0x1
        RightButton: Qt.MouseButton = ...  # 0x2
        MidButton: Qt.MouseButton = ...  # 0x4
        MiddleButton: Qt.MouseButton = ...  # 0x4
        BackButton: Qt.MouseButton = ...  # 0x8
        ExtraButton1: Qt.MouseButton = ...  # 0x8
        XButton1: Qt.MouseButton = ...  # 0x8
        ExtraButton2: Qt.MouseButton = ...  # 0x10
        ForwardButton: Qt.MouseButton = ...  # 0x10
        XButton2: Qt.MouseButton = ...  # 0x10
        ExtraButton3: Qt.MouseButton = ...  # 0x20
        TaskButton: Qt.MouseButton = ...  # 0x20
        ExtraButton4: Qt.MouseButton = ...  # 0x40
        ExtraButton5: Qt.MouseButton = ...  # 0x80
        ExtraButton6: Qt.MouseButton = ...  # 0x100
        ExtraButton7: Qt.MouseButton = ...  # 0x200
        ExtraButton8: Qt.MouseButton = ...  # 0x400
        ExtraButton9: Qt.MouseButton = ...  # 0x800
        ExtraButton10: Qt.MouseButton = ...  # 0x1000
        ExtraButton11: Qt.MouseButton = ...  # 0x2000
        ExtraButton12: Qt.MouseButton = ...  # 0x4000
        ExtraButton13: Qt.MouseButton = ...  # 0x8000
        ExtraButton14: Qt.MouseButton = ...  # 0x10000
        ExtraButton15: Qt.MouseButton = ...  # 0x20000
        ExtraButton16: Qt.MouseButton = ...  # 0x40000
        ExtraButton17: Qt.MouseButton = ...  # 0x80000
        ExtraButton18: Qt.MouseButton = ...  # 0x100000
        ExtraButton19: Qt.MouseButton = ...  # 0x200000
        ExtraButton20: Qt.MouseButton = ...  # 0x400000
        ExtraButton21: Qt.MouseButton = ...  # 0x800000
        ExtraButton22: Qt.MouseButton = ...  # 0x1000000
        ExtraButton23: Qt.MouseButton = ...  # 0x2000000
        ExtraButton24: Qt.MouseButton = ...  # 0x4000000
        MaxMouseButton: Qt.MouseButton = ...  # 0x4000000
        AllButtons: Qt.MouseButton = ...  # 0x7ffffff

    class MouseButtons(object): ...

    class MouseEventFlag(object):
        MouseEventCreatedDoubleClick: Qt.MouseEventFlag = ...  # 0x1
        MouseEventFlagMask: Qt.MouseEventFlag = ...  # 0xff

    class MouseEventFlags(object): ...

    class MouseEventSource(object):
        MouseEventNotSynthesized: Qt.MouseEventSource = ...  # 0x0
        MouseEventSynthesizedBySystem: Qt.MouseEventSource = ...  # 0x1
        MouseEventSynthesizedByQt: Qt.MouseEventSource = ...  # 0x2
        MouseEventSynthesizedByApplication: Qt.MouseEventSource = ...  # 0x3

    class NativeGestureType(object):
        BeginNativeGesture: Qt.NativeGestureType = ...  # 0x0
        EndNativeGesture: Qt.NativeGestureType = ...  # 0x1
        PanNativeGesture: Qt.NativeGestureType = ...  # 0x2
        ZoomNativeGesture: Qt.NativeGestureType = ...  # 0x3
        SmartZoomNativeGesture: Qt.NativeGestureType = ...  # 0x4
        RotateNativeGesture: Qt.NativeGestureType = ...  # 0x5
        SwipeNativeGesture: Qt.NativeGestureType = ...  # 0x6

    class NavigationMode(object):
        NavigationModeNone: Qt.NavigationMode = ...  # 0x0
        NavigationModeKeypadTabOrder: Qt.NavigationMode = ...  # 0x1
        NavigationModeKeypadDirectional: Qt.NavigationMode = ...  # 0x2
        NavigationModeCursorAuto: Qt.NavigationMode = ...  # 0x3
        NavigationModeCursorForceVisible: Qt.NavigationMode = ...  # 0x4

    class Orientation(object):
        Horizontal: Qt.Orientation = ...  # 0x1
        Vertical: Qt.Orientation = ...  # 0x2

    class Orientations(object): ...

    class PenCapStyle(object):
        FlatCap: Qt.PenCapStyle = ...  # 0x0
        SquareCap: Qt.PenCapStyle = ...  # 0x10
        RoundCap: Qt.PenCapStyle = ...  # 0x20
        MPenCapStyle: Qt.PenCapStyle = ...  # 0x30

    class PenJoinStyle(object):
        MiterJoin: Qt.PenJoinStyle = ...  # 0x0
        BevelJoin: Qt.PenJoinStyle = ...  # 0x40
        RoundJoin: Qt.PenJoinStyle = ...  # 0x80
        SvgMiterJoin: Qt.PenJoinStyle = ...  # 0x100
        MPenJoinStyle: Qt.PenJoinStyle = ...  # 0x1c0

    class PenStyle(object):
        NoPen: Qt.PenStyle = ...  # 0x0
        SolidLine: Qt.PenStyle = ...  # 0x1
        DashLine: Qt.PenStyle = ...  # 0x2
        DotLine: Qt.PenStyle = ...  # 0x3
        DashDotLine: Qt.PenStyle = ...  # 0x4
        DashDotDotLine: Qt.PenStyle = ...  # 0x5
        CustomDashLine: Qt.PenStyle = ...  # 0x6
        MPenStyle: Qt.PenStyle = ...  # 0xf

    class ScreenOrientation(object):
        PrimaryOrientation: Qt.ScreenOrientation = ...  # 0x0
        PortraitOrientation: Qt.ScreenOrientation = ...  # 0x1
        LandscapeOrientation: Qt.ScreenOrientation = ...  # 0x2
        InvertedPortraitOrientation: Qt.ScreenOrientation = ...  # 0x4
        InvertedLandscapeOrientation: Qt.ScreenOrientation = ...  # 0x8

    class ScreenOrientations(object): ...

    class ScrollBarPolicy(object):
        ScrollBarAsNeeded: Qt.ScrollBarPolicy = ...  # 0x0
        ScrollBarAlwaysOff: Qt.ScrollBarPolicy = ...  # 0x1
        ScrollBarAlwaysOn: Qt.ScrollBarPolicy = ...  # 0x2

    class ScrollPhase(object):
        NoScrollPhase: Qt.ScrollPhase = ...  # 0x0
        ScrollBegin: Qt.ScrollPhase = ...  # 0x1
        ScrollUpdate: Qt.ScrollPhase = ...  # 0x2
        ScrollEnd: Qt.ScrollPhase = ...  # 0x3
        ScrollMomentum: Qt.ScrollPhase = ...  # 0x4

    class ShortcutContext(object):
        WidgetShortcut: Qt.ShortcutContext = ...  # 0x0
        WindowShortcut: Qt.ShortcutContext = ...  # 0x1
        ApplicationShortcut: Qt.ShortcutContext = ...  # 0x2
        WidgetWithChildrenShortcut: Qt.ShortcutContext = ...  # 0x3

    class SizeHint(object):
        MinimumSize: Qt.SizeHint = ...  # 0x0
        PreferredSize: Qt.SizeHint = ...  # 0x1
        MaximumSize: Qt.SizeHint = ...  # 0x2
        MinimumDescent: Qt.SizeHint = ...  # 0x3
        NSizeHints: Qt.SizeHint = ...  # 0x4

    class SizeMode(object):
        AbsoluteSize: Qt.SizeMode = ...  # 0x0
        RelativeSize: Qt.SizeMode = ...  # 0x1

    class SortOrder(object):
        AscendingOrder: Qt.SortOrder = ...  # 0x0
        DescendingOrder: Qt.SortOrder = ...  # 0x1

    class SplitBehavior(object): ...

    class SplitBehaviorFlags(object):
        KeepEmptyParts: Qt.SplitBehaviorFlags = ...  # 0x0
        SkipEmptyParts: Qt.SplitBehaviorFlags = ...  # 0x1

    class TabFocusBehavior(object):
        NoTabFocus: Qt.TabFocusBehavior = ...  # 0x0
        TabFocusTextControls: Qt.TabFocusBehavior = ...  # 0x1
        TabFocusListControls: Qt.TabFocusBehavior = ...  # 0x2
        TabFocusAllControls: Qt.TabFocusBehavior = ...  # 0xff

    class TextElideMode(object):
        ElideLeft: Qt.TextElideMode = ...  # 0x0
        ElideRight: Qt.TextElideMode = ...  # 0x1
        ElideMiddle: Qt.TextElideMode = ...  # 0x2
        ElideNone: Qt.TextElideMode = ...  # 0x3

    class TextFlag(object):
        TextSingleLine: Qt.TextFlag = ...  # 0x100
        TextDontClip: Qt.TextFlag = ...  # 0x200
        TextExpandTabs: Qt.TextFlag = ...  # 0x400
        TextShowMnemonic: Qt.TextFlag = ...  # 0x800
        TextWordWrap: Qt.TextFlag = ...  # 0x1000
        TextWrapAnywhere: Qt.TextFlag = ...  # 0x2000
        TextDontPrint: Qt.TextFlag = ...  # 0x4000
        TextHideMnemonic: Qt.TextFlag = ...  # 0x8000
        TextJustificationForced: Qt.TextFlag = ...  # 0x10000
        TextForceLeftToRight: Qt.TextFlag = ...  # 0x20000
        TextForceRightToLeft: Qt.TextFlag = ...  # 0x40000
        TextLongestVariant: Qt.TextFlag = ...  # 0x80000
        TextBypassShaping: Qt.TextFlag = ...  # 0x100000
        TextIncludeTrailingSpaces: Qt.TextFlag = ...  # 0x8000000

    class TextFormat(object):
        PlainText: Qt.TextFormat = ...  # 0x0
        RichText: Qt.TextFormat = ...  # 0x1
        AutoText: Qt.TextFormat = ...  # 0x2
        MarkdownText: Qt.TextFormat = ...  # 0x3

    class TextInteractionFlag(object):
        NoTextInteraction: Qt.TextInteractionFlag = ...  # 0x0
        TextSelectableByMouse: Qt.TextInteractionFlag = ...  # 0x1
        TextSelectableByKeyboard: Qt.TextInteractionFlag = ...  # 0x2
        LinksAccessibleByMouse: Qt.TextInteractionFlag = ...  # 0x4
        LinksAccessibleByKeyboard: Qt.TextInteractionFlag = ...  # 0x8
        TextBrowserInteraction: Qt.TextInteractionFlag = ...  # 0xd
        TextEditable: Qt.TextInteractionFlag = ...  # 0x10
        TextEditorInteraction: Qt.TextInteractionFlag = ...  # 0x13

    class TextInteractionFlags(object): ...

    class TileRule(object):
        StretchTile: Qt.TileRule = ...  # 0x0
        RepeatTile: Qt.TileRule = ...  # 0x1
        RoundTile: Qt.TileRule = ...  # 0x2

    class TimeSpec(object):
        LocalTime: Qt.TimeSpec = ...  # 0x0
        UTC: Qt.TimeSpec = ...  # 0x1
        OffsetFromUTC: Qt.TimeSpec = ...  # 0x2
        TimeZone: Qt.TimeSpec = ...  # 0x3

    class TimerType(object):
        PreciseTimer: Qt.TimerType = ...  # 0x0
        CoarseTimer: Qt.TimerType = ...  # 0x1
        VeryCoarseTimer: Qt.TimerType = ...  # 0x2

    class ToolBarArea(object):
        NoToolBarArea: Qt.ToolBarArea = ...  # 0x0
        LeftToolBarArea: Qt.ToolBarArea = ...  # 0x1
        RightToolBarArea: Qt.ToolBarArea = ...  # 0x2
        TopToolBarArea: Qt.ToolBarArea = ...  # 0x4
        BottomToolBarArea: Qt.ToolBarArea = ...  # 0x8
        AllToolBarAreas: Qt.ToolBarArea = ...  # 0xf
        ToolBarArea_Mask: Qt.ToolBarArea = ...  # 0xf

    class ToolBarAreaSizes(object):
        NToolBarAreas: Qt.ToolBarAreaSizes = ...  # 0x4

    class ToolBarAreas(object): ...

    class ToolButtonStyle(object):
        ToolButtonIconOnly: Qt.ToolButtonStyle = ...  # 0x0
        ToolButtonTextOnly: Qt.ToolButtonStyle = ...  # 0x1
        ToolButtonTextBesideIcon: Qt.ToolButtonStyle = ...  # 0x2
        ToolButtonTextUnderIcon: Qt.ToolButtonStyle = ...  # 0x3
        ToolButtonFollowStyle: Qt.ToolButtonStyle = ...  # 0x4

    class TouchPointState(object):
        TouchPointPressed: Qt.TouchPointState = ...  # 0x1
        TouchPointMoved: Qt.TouchPointState = ...  # 0x2
        TouchPointStationary: Qt.TouchPointState = ...  # 0x4
        TouchPointReleased: Qt.TouchPointState = ...  # 0x8

    class TouchPointStates(object): ...

    class TransformationMode(object):
        FastTransformation: Qt.TransformationMode = ...  # 0x0
        SmoothTransformation: Qt.TransformationMode = ...  # 0x1

    class UIEffect(object):
        UI_General: Qt.UIEffect = ...  # 0x0
        UI_AnimateMenu: Qt.UIEffect = ...  # 0x1
        UI_FadeMenu: Qt.UIEffect = ...  # 0x2
        UI_AnimateCombo: Qt.UIEffect = ...  # 0x3
        UI_AnimateTooltip: Qt.UIEffect = ...  # 0x4
        UI_FadeTooltip: Qt.UIEffect = ...  # 0x5
        UI_AnimateToolBox: Qt.UIEffect = ...  # 0x6

    class WhiteSpaceMode(object):
        WhiteSpaceModeUndefined: Qt.WhiteSpaceMode = ...  # -0x1
        WhiteSpaceNormal: Qt.WhiteSpaceMode = ...  # 0x0
        WhiteSpacePre: Qt.WhiteSpaceMode = ...  # 0x1
        WhiteSpaceNoWrap: Qt.WhiteSpaceMode = ...  # 0x2

    class WidgetAttribute(object):
        WA_Disabled: Qt.WidgetAttribute = ...  # 0x0
        WA_UnderMouse: Qt.WidgetAttribute = ...  # 0x1
        WA_MouseTracking: Qt.WidgetAttribute = ...  # 0x2
        WA_ContentsPropagated: Qt.WidgetAttribute = ...  # 0x3
        WA_NoBackground: Qt.WidgetAttribute = ...  # 0x4
        WA_OpaquePaintEvent: Qt.WidgetAttribute = ...  # 0x4
        WA_StaticContents: Qt.WidgetAttribute = ...  # 0x5
        WA_LaidOut: Qt.WidgetAttribute = ...  # 0x7
        WA_PaintOnScreen: Qt.WidgetAttribute = ...  # 0x8
        WA_NoSystemBackground: Qt.WidgetAttribute = ...  # 0x9
        WA_UpdatesDisabled: Qt.WidgetAttribute = ...  # 0xa
        WA_Mapped: Qt.WidgetAttribute = ...  # 0xb
        WA_MacNoClickThrough: Qt.WidgetAttribute = ...  # 0xc
        WA_InputMethodEnabled: Qt.WidgetAttribute = ...  # 0xe
        WA_WState_Visible: Qt.WidgetAttribute = ...  # 0xf
        WA_WState_Hidden: Qt.WidgetAttribute = ...  # 0x10
        WA_ForceDisabled: Qt.WidgetAttribute = ...  # 0x20
        WA_KeyCompression: Qt.WidgetAttribute = ...  # 0x21
        WA_PendingMoveEvent: Qt.WidgetAttribute = ...  # 0x22
        WA_PendingResizeEvent: Qt.WidgetAttribute = ...  # 0x23
        WA_SetPalette: Qt.WidgetAttribute = ...  # 0x24
        WA_SetFont: Qt.WidgetAttribute = ...  # 0x25
        WA_SetCursor: Qt.WidgetAttribute = ...  # 0x26
        WA_NoChildEventsFromChildren: Qt.WidgetAttribute = ...  # 0x27
        WA_WindowModified: Qt.WidgetAttribute = ...  # 0x29
        WA_Resized: Qt.WidgetAttribute = ...  # 0x2a
        WA_Moved: Qt.WidgetAttribute = ...  # 0x2b
        WA_PendingUpdate: Qt.WidgetAttribute = ...  # 0x2c
        WA_InvalidSize: Qt.WidgetAttribute = ...  # 0x2d
        WA_MacBrushedMetal: Qt.WidgetAttribute = ...  # 0x2e
        WA_MacMetalStyle: Qt.WidgetAttribute = ...  # 0x2e
        WA_CustomWhatsThis: Qt.WidgetAttribute = ...  # 0x2f
        WA_LayoutOnEntireRect: Qt.WidgetAttribute = ...  # 0x30
        WA_OutsideWSRange: Qt.WidgetAttribute = ...  # 0x31
        WA_GrabbedShortcut: Qt.WidgetAttribute = ...  # 0x32
        WA_TransparentForMouseEvents: Qt.WidgetAttribute = ...  # 0x33
        WA_PaintUnclipped: Qt.WidgetAttribute = ...  # 0x34
        WA_SetWindowIcon: Qt.WidgetAttribute = ...  # 0x35
        WA_NoMouseReplay: Qt.WidgetAttribute = ...  # 0x36
        WA_DeleteOnClose: Qt.WidgetAttribute = ...  # 0x37
        WA_RightToLeft: Qt.WidgetAttribute = ...  # 0x38
        WA_SetLayoutDirection: Qt.WidgetAttribute = ...  # 0x39
        WA_NoChildEventsForParent: Qt.WidgetAttribute = ...  # 0x3a
        WA_ForceUpdatesDisabled: Qt.WidgetAttribute = ...  # 0x3b
        WA_WState_Created: Qt.WidgetAttribute = ...  # 0x3c
        WA_WState_CompressKeys: Qt.WidgetAttribute = ...  # 0x3d
        WA_WState_InPaintEvent: Qt.WidgetAttribute = ...  # 0x3e
        WA_WState_Reparented: Qt.WidgetAttribute = ...  # 0x3f
        WA_WState_ConfigPending: Qt.WidgetAttribute = ...  # 0x40
        WA_WState_Polished: Qt.WidgetAttribute = ...  # 0x42
        WA_WState_DND: Qt.WidgetAttribute = ...  # 0x43
        WA_WState_OwnSizePolicy: Qt.WidgetAttribute = ...  # 0x44
        WA_WState_ExplicitShowHide: Qt.WidgetAttribute = ...  # 0x45
        WA_ShowModal: Qt.WidgetAttribute = ...  # 0x46
        WA_MouseNoMask: Qt.WidgetAttribute = ...  # 0x47
        WA_GroupLeader: Qt.WidgetAttribute = ...  # 0x48
        WA_NoMousePropagation: Qt.WidgetAttribute = ...  # 0x49
        WA_Hover: Qt.WidgetAttribute = ...  # 0x4a
        WA_InputMethodTransparent: Qt.WidgetAttribute = ...  # 0x4b
        WA_QuitOnClose: Qt.WidgetAttribute = ...  # 0x4c
        WA_KeyboardFocusChange: Qt.WidgetAttribute = ...  # 0x4d
        WA_AcceptDrops: Qt.WidgetAttribute = ...  # 0x4e
        WA_DropSiteRegistered: Qt.WidgetAttribute = ...  # 0x4f
        WA_ForceAcceptDrops: Qt.WidgetAttribute = ...  # 0x4f
        WA_WindowPropagation: Qt.WidgetAttribute = ...  # 0x50
        WA_NoX11EventCompression: Qt.WidgetAttribute = ...  # 0x51
        WA_TintedBackground: Qt.WidgetAttribute = ...  # 0x52
        WA_X11OpenGLOverlay: Qt.WidgetAttribute = ...  # 0x53
        WA_AlwaysShowToolTips: Qt.WidgetAttribute = ...  # 0x54
        WA_MacOpaqueSizeGrip: Qt.WidgetAttribute = ...  # 0x55
        WA_SetStyle: Qt.WidgetAttribute = ...  # 0x56
        WA_SetLocale: Qt.WidgetAttribute = ...  # 0x57
        WA_MacShowFocusRect: Qt.WidgetAttribute = ...  # 0x58
        WA_MacNormalSize: Qt.WidgetAttribute = ...  # 0x59
        WA_MacSmallSize: Qt.WidgetAttribute = ...  # 0x5a
        WA_MacMiniSize: Qt.WidgetAttribute = ...  # 0x5b
        WA_LayoutUsesWidgetRect: Qt.WidgetAttribute = ...  # 0x5c
        WA_StyledBackground: Qt.WidgetAttribute = ...  # 0x5d
        WA_MSWindowsUseDirect3D: Qt.WidgetAttribute = ...  # 0x5e
        WA_CanHostQMdiSubWindowTitleBar: Qt.WidgetAttribute = ...  # 0x5f
        WA_MacAlwaysShowToolWindow: Qt.WidgetAttribute = ...  # 0x60
        WA_StyleSheet: Qt.WidgetAttribute = ...  # 0x61
        WA_ShowWithoutActivating: Qt.WidgetAttribute = ...  # 0x62
        WA_X11BypassTransientForHint: Qt.WidgetAttribute = ...  # 0x63
        WA_NativeWindow: Qt.WidgetAttribute = ...  # 0x64
        WA_DontCreateNativeAncestors: Qt.WidgetAttribute = ...  # 0x65
        WA_MacVariableSize: Qt.WidgetAttribute = ...  # 0x66
        WA_DontShowOnScreen: Qt.WidgetAttribute = ...  # 0x67
        WA_X11NetWmWindowTypeDesktop: Qt.WidgetAttribute = ...  # 0x68
        WA_X11NetWmWindowTypeDock: Qt.WidgetAttribute = ...  # 0x69
        WA_X11NetWmWindowTypeToolBar: Qt.WidgetAttribute = ...  # 0x6a
        WA_X11NetWmWindowTypeMenu: Qt.WidgetAttribute = ...  # 0x6b
        WA_X11NetWmWindowTypeUtility: Qt.WidgetAttribute = ...  # 0x6c
        WA_X11NetWmWindowTypeSplash: Qt.WidgetAttribute = ...  # 0x6d
        WA_X11NetWmWindowTypeDialog: Qt.WidgetAttribute = ...  # 0x6e
        WA_X11NetWmWindowTypeDropDownMenu: Qt.WidgetAttribute = ...  # 0x6f
        WA_X11NetWmWindowTypePopupMenu: Qt.WidgetAttribute = ...  # 0x70
        WA_X11NetWmWindowTypeToolTip: Qt.WidgetAttribute = ...  # 0x71
        WA_X11NetWmWindowTypeNotification: Qt.WidgetAttribute = ...  # 0x72
        WA_X11NetWmWindowTypeCombo: Qt.WidgetAttribute = ...  # 0x73
        WA_X11NetWmWindowTypeDND: Qt.WidgetAttribute = ...  # 0x74
        WA_MacFrameworkScaled: Qt.WidgetAttribute = ...  # 0x75
        WA_SetWindowModality: Qt.WidgetAttribute = ...  # 0x76
        WA_WState_WindowOpacitySet: Qt.WidgetAttribute = ...  # 0x77
        WA_TranslucentBackground: Qt.WidgetAttribute = ...  # 0x78
        WA_AcceptTouchEvents: Qt.WidgetAttribute = ...  # 0x79
        WA_WState_AcceptedTouchBeginEvent: Qt.WidgetAttribute = ...  # 0x7a
        WA_TouchPadAcceptSingleTouchEvents: Qt.WidgetAttribute = ...  # 0x7b
        WA_X11DoNotAcceptFocus: Qt.WidgetAttribute = ...  # 0x7e
        WA_MacNoShadow: Qt.WidgetAttribute = ...  # 0x7f
        WA_AlwaysStackOnTop: Qt.WidgetAttribute = ...  # 0x80
        WA_TabletTracking: Qt.WidgetAttribute = ...  # 0x81
        WA_ContentsMarginsRespectsSafeArea: Qt.WidgetAttribute = ...  # 0x82
        WA_StyleSheetTarget: Qt.WidgetAttribute = ...  # 0x83
        WA_AttributeCount: Qt.WidgetAttribute = ...  # 0x84

    class WindowFlags(object): ...

    class WindowFrameSection(object):
        NoSection: Qt.WindowFrameSection = ...  # 0x0
        LeftSection: Qt.WindowFrameSection = ...  # 0x1
        TopLeftSection: Qt.WindowFrameSection = ...  # 0x2
        TopSection: Qt.WindowFrameSection = ...  # 0x3
        TopRightSection: Qt.WindowFrameSection = ...  # 0x4
        RightSection: Qt.WindowFrameSection = ...  # 0x5
        BottomRightSection: Qt.WindowFrameSection = ...  # 0x6
        BottomSection: Qt.WindowFrameSection = ...  # 0x7
        BottomLeftSection: Qt.WindowFrameSection = ...  # 0x8
        TitleBarArea: Qt.WindowFrameSection = ...  # 0x9

    class WindowModality(object):
        NonModal: Qt.WindowModality = ...  # 0x0
        WindowModal: Qt.WindowModality = ...  # 0x1
        ApplicationModal: Qt.WindowModality = ...  # 0x2

    class WindowState(object):
        WindowNoState: Qt.WindowState = ...  # 0x0
        WindowMinimized: Qt.WindowState = ...  # 0x1
        WindowMaximized: Qt.WindowState = ...  # 0x2
        WindowFullScreen: Qt.WindowState = ...  # 0x4
        WindowActive: Qt.WindowState = ...  # 0x8

    class WindowStates(object): ...

    class WindowType(object):
        WindowFullscreenButtonHint: Qt.WindowType = ...  # -0x80000000
        Widget: Qt.WindowType = ...  # 0x0
        Window: Qt.WindowType = ...  # 0x1
        Dialog: Qt.WindowType = ...  # 0x3
        Sheet: Qt.WindowType = ...  # 0x5
        Drawer: Qt.WindowType = ...  # 0x7
        Popup: Qt.WindowType = ...  # 0x9
        Tool: Qt.WindowType = ...  # 0xb
        ToolTip: Qt.WindowType = ...  # 0xd
        SplashScreen: Qt.WindowType = ...  # 0xf
        Desktop: Qt.WindowType = ...  # 0x11
        SubWindow: Qt.WindowType = ...  # 0x12
        ForeignWindow: Qt.WindowType = ...  # 0x21
        CoverWindow: Qt.WindowType = ...  # 0x41
        WindowType_Mask: Qt.WindowType = ...  # 0xff
        MSWindowsFixedSizeDialogHint: Qt.WindowType = ...  # 0x100
        MSWindowsOwnDC: Qt.WindowType = ...  # 0x200
        BypassWindowManagerHint: Qt.WindowType = ...  # 0x400
        X11BypassWindowManagerHint: Qt.WindowType = ...  # 0x400
        FramelessWindowHint: Qt.WindowType = ...  # 0x800
        WindowTitleHint: Qt.WindowType = ...  # 0x1000
        WindowSystemMenuHint: Qt.WindowType = ...  # 0x2000
        WindowMinimizeButtonHint: Qt.WindowType = ...  # 0x4000
        WindowMaximizeButtonHint: Qt.WindowType = ...  # 0x8000
        WindowMinMaxButtonsHint: Qt.WindowType = ...  # 0xc000
        WindowContextHelpButtonHint: Qt.WindowType = ...  # 0x10000
        WindowShadeButtonHint: Qt.WindowType = ...  # 0x20000
        WindowStaysOnTopHint: Qt.WindowType = ...  # 0x40000
        WindowTransparentForInput: Qt.WindowType = ...  # 0x80000
        WindowOverridesSystemGestures: Qt.WindowType = ...  # 0x100000
        WindowDoesNotAcceptFocus: Qt.WindowType = ...  # 0x200000
        MaximizeUsingFullscreenGeometryHint: Qt.WindowType = ...  # 0x400000
        CustomizeWindowHint: Qt.WindowType = ...  # 0x2000000
        WindowStaysOnBottomHint: Qt.WindowType = ...  # 0x4000000
        WindowCloseButtonHint: Qt.WindowType = ...  # 0x8000000
        MacWindowToolBarButtonHint: Qt.WindowType = ...  # 0x10000000
        BypassGraphicsProxyWidget: Qt.WindowType = ...  # 0x20000000
        NoDropShadowWindowHint: Qt.WindowType = ...  # 0x40000000
    @staticmethod
    def bin(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def bom(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def center(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def dec(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def endl(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def fixed(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def flush(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def forcepoint(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def forcesign(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def hex(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def left(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def lowercasebase(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def lowercasedigits(
        s: PySide2.QtCore.QTextStream,
    ) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def noforcepoint(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def noforcesign(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def noshowbase(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def oct(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def reset(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def right(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def scientific(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def showbase(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def uppercasebase(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def uppercasedigits(
        s: PySide2.QtCore.QTextStream,
    ) -> PySide2.QtCore.QTextStream: ...
    @staticmethod
    def ws(s: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...

class QtMsgType(object):
    QtDebugMsg: QtMsgType = ...  # 0x0
    QtWarningMsg: QtMsgType = ...  # 0x1
    QtCriticalMsg: QtMsgType = ...  # 0x2
    QtSystemMsg: QtMsgType = ...  # 0x2
    QtFatalMsg: QtMsgType = ...  # 0x3
    QtInfoMsg: QtMsgType = ...  # 0x4

class Signal(object):
    def __init__(
        self,
        *types: type,
        name: typing.Optional[str] = ...,
        arguments: typing.Optional[str] = ...
    ): ...

class SignalInstance(object):
    def connect(self, slot: object, type: typing.Optional[type] = ...): ...
    def disconnect(self, slot: object = ...): ...
    def emit(self, *args: typing.Any): ...

class Slot(object):
    def __init__(
        self,
        *types: type,
        name: typing.Optional[str] = ...,
        result: typing.Optional[str] = ...
    ) -> typing.Callable: ...

def QT_TRANSLATE_NOOP(arg__1: object, arg__2: object) -> object: ...
def QT_TRANSLATE_NOOP3(arg__1: object, arg__2: object, arg__3: object) -> object: ...
def QT_TRANSLATE_NOOP_UTF8(arg__1: object) -> object: ...
def QT_TR_NOOP(arg__1: object) -> object: ...
def QT_TR_NOOP_UTF8(arg__1: object) -> object: ...
def SIGNAL(arg__1: bytes) -> str: ...
def SLOT(arg__1: bytes) -> str: ...
def __moduleShutdown(): ...
def qAbs(arg__1: float) -> float: ...
def qAcos(v: float) -> float: ...
def qAddPostRoutine(arg__1: object): ...
def qAsin(v: float) -> float: ...
def qAtan(v: float) -> float: ...
def qAtan2(y: float, x: float) -> float: ...
def qChecksum(s: bytes, len: int) -> int: ...
@typing.overload
def qCompress(
    data: PySide2.QtCore.QByteArray, compressionLevel: int = ...
) -> PySide2.QtCore.QByteArray: ...
@typing.overload
def qCompress(
    data: bytes, nbytes: int, compressionLevel: int = ...
) -> PySide2.QtCore.QByteArray: ...
def qCritical(arg__1: bytes): ...
def qDebug(arg__1: bytes): ...
def qExp(v: float) -> float: ...
def qFabs(v: float) -> float: ...
def qFastCos(x: float) -> float: ...
def qFastSin(x: float) -> float: ...
def qFatal(arg__1: bytes): ...
def qFuzzyCompare(p1: float, p2: float) -> bool: ...
def qFuzzyIsNull(d: float) -> bool: ...
def qInstallMessageHandler(arg__1: object) -> object: ...
def qIsFinite(d: float) -> bool: ...
def qIsInf(d: float) -> bool: ...
def qIsNaN(d: float) -> bool: ...
def qIsNull(d: float) -> bool: ...
def qRegisterResourceData(
    arg__1: int, arg__2: bytes, arg__3: bytes, arg__4: bytes
) -> bool: ...
def qTan(v: float) -> float: ...
@typing.overload
def qUncompress(data: PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
@typing.overload
def qUncompress(data: bytes, nbytes: int) -> PySide2.QtCore.QByteArray: ...
def qUnregisterResourceData(
    arg__1: int, arg__2: bytes, arg__3: bytes, arg__4: bytes
) -> bool: ...
def qVersion() -> bytes: ...
def qWarning(arg__1: bytes): ...
def qrand() -> int: ...
def qsrand(seed: int): ...
def qtTrId(id: bytes, n: int = ...) -> str: ...

# eof
