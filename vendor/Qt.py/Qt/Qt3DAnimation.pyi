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
PySide2.Qt3DAnimation, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DAnimation
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
import PySide2.Qt3DCore
import PySide2.Qt3DRender
import PySide2.Qt3DAnimation

class Qt3DAnimation(Shiboken.Object):
    class QAbstractAnimation(PySide2.QtCore.QObject):
        KeyframeAnimation: Qt3DAnimation.QAbstractAnimation = ...  # 0x1
        MorphingAnimation: Qt3DAnimation.QAbstractAnimation = ...  # 0x2
        VertexBlendAnimation: Qt3DAnimation.QAbstractAnimation = ...  # 0x3

        class AnimationType(object):
            KeyframeAnimation: Qt3DAnimation.QAbstractAnimation.AnimationType = (
                ...
            )  # 0x1
            MorphingAnimation: Qt3DAnimation.QAbstractAnimation.AnimationType = (
                ...
            )  # 0x2
            VertexBlendAnimation: Qt3DAnimation.QAbstractAnimation.AnimationType = (
                ...
            )  # 0x3
        def animationName(self) -> str: ...
        def animationType(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation.AnimationType: ...
        def duration(self) -> float: ...
        def position(self) -> float: ...
        def setAnimationName(self, name: str): ...
        def setDuration(self, duration: float): ...
        def setPosition(self, position: float): ...

    class QAbstractAnimationClip(PySide2.Qt3DCore.QNode):
        def duration(self) -> float: ...

    class QAbstractChannelMapping(PySide2.Qt3DCore.QNode): ...

    class QAbstractClipAnimator(PySide2.Qt3DCore.QComponent):
        Infinite: Qt3DAnimation.QAbstractClipAnimator = ...  # -0x1

        class Loops(object):
            Infinite: Qt3DAnimation.QAbstractClipAnimator.Loops = ...  # -0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def clock(self) -> PySide2.Qt3DAnimation.Qt3DAnimation.QClock: ...
        def isRunning(self) -> bool: ...
        def loopCount(self) -> int: ...
        def normalizedTime(self) -> float: ...
        def setClock(self, clock: PySide2.Qt3DAnimation.Qt3DAnimation.QClock): ...
        def setLoopCount(self, loops: int): ...
        def setNormalizedTime(self, timeFraction: float): ...
        def setRunning(self, running: bool): ...
        def start(self): ...
        def stop(self): ...

    class QAbstractClipBlendNode(PySide2.Qt3DCore.QNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...

    class QAdditiveClipBlend(PySide2.Qt3DAnimation.QAbstractClipBlendNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def additiveClip(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def additiveFactor(self) -> float: ...
        def baseClip(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def setAdditiveClip(
            self,
            additiveClip: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode,
        ): ...
        def setAdditiveFactor(self, additiveFactor: float): ...
        def setBaseClip(
            self, baseClip: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode
        ): ...

    class QAnimationAspect(PySide2.Qt3DCore.QAbstractAspect):
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...

    class QAnimationCallback(Shiboken.Object):
        OnOwningThread: Qt3DAnimation.QAnimationCallback = ...  # 0x0
        OnThreadPool: Qt3DAnimation.QAnimationCallback = ...  # 0x1

        class Flag(object):
            OnOwningThread: Qt3DAnimation.QAnimationCallback.Flag = ...  # 0x0
            OnThreadPool: Qt3DAnimation.QAnimationCallback.Flag = ...  # 0x1
        def __init__(self): ...
        def valueChanged(self, value: typing.Any): ...

    class QAnimationClip(PySide2.Qt3DAnimation.QAbstractAnimationClip):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...

    class QAnimationClipLoader(PySide2.Qt3DAnimation.QAbstractAnimationClip):
        NotReady: Qt3DAnimation.QAnimationClipLoader = ...  # 0x0
        Ready: Qt3DAnimation.QAnimationClipLoader = ...  # 0x1
        Error: Qt3DAnimation.QAnimationClipLoader = ...  # 0x2

        class Status(object):
            NotReady: Qt3DAnimation.QAnimationClipLoader.Status = ...  # 0x0
            Ready: Qt3DAnimation.QAnimationClipLoader.Status = ...  # 0x1
            Error: Qt3DAnimation.QAnimationClipLoader.Status = ...  # 0x2
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        @typing.overload
        def __init__(
            self,
            source: PySide2.QtCore.QUrl,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ): ...
        def setSource(self, source: PySide2.QtCore.QUrl): ...
        def source(self) -> PySide2.QtCore.QUrl: ...
        def status(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAnimationClipLoader.Status: ...

    class QAnimationController(PySide2.QtCore.QObject):
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
        def activeAnimationGroup(self) -> int: ...
        def addAnimationGroup(
            self, animationGroups: PySide2.Qt3DAnimation.Qt3DAnimation.QAnimationGroup
        ): ...
        def animationGroupList(self) -> typing.List: ...
        def entity(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def getAnimationIndex(self, name: str) -> int: ...
        def getGroup(
            self, index: int
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAnimationGroup: ...
        def position(self) -> float: ...
        def positionOffset(self) -> float: ...
        def positionScale(self) -> float: ...
        def recursive(self) -> bool: ...
        def removeAnimationGroup(
            self, animationGroups: PySide2.Qt3DAnimation.Qt3DAnimation.QAnimationGroup
        ): ...
        def setActiveAnimationGroup(self, index: int): ...
        def setAnimationGroups(self, animationGroups: typing.List): ...
        def setEntity(self, entity: PySide2.Qt3DCore.Qt3DCore.QEntity): ...
        def setPosition(self, position: float): ...
        def setPositionOffset(self, offset: float): ...
        def setPositionScale(self, scale: float): ...
        def setRecursive(self, recursive: bool): ...

    class QAnimationGroup(PySide2.QtCore.QObject):
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
        def addAnimation(
            self, animation: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation
        ): ...
        def animationList(self) -> typing.List: ...
        def duration(self) -> float: ...
        def name(self) -> str: ...
        def position(self) -> float: ...
        def removeAnimation(
            self, animation: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation
        ): ...
        def setAnimations(self, animations: typing.List): ...
        def setName(self, name: str): ...
        def setPosition(self, position: float): ...

    class QBlendedClipAnimator(PySide2.Qt3DAnimation.QAbstractClipAnimator):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def blendTree(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def setBlendTree(
            self, blendTree: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode
        ): ...

    class QClipAnimator(PySide2.Qt3DAnimation.QAbstractClipAnimator):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def clip(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip: ...
        def setClip(
            self, clip: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip
        ): ...

    class QClock(PySide2.Qt3DCore.QNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def playbackRate(self) -> float: ...
        def setPlaybackRate(self, playbackRate: float): ...

    class QKeyFrame(Shiboken.Object):
        ConstantInterpolation: Qt3DAnimation.QKeyFrame = ...  # 0x0
        LinearInterpolation: Qt3DAnimation.QKeyFrame = ...  # 0x1
        BezierInterpolation: Qt3DAnimation.QKeyFrame = ...  # 0x2

        class InterpolationType(object):
            ConstantInterpolation: Qt3DAnimation.QKeyFrame.InterpolationType = (
                ...
            )  # 0x0
            LinearInterpolation: Qt3DAnimation.QKeyFrame.InterpolationType = ...  # 0x1
            BezierInterpolation: Qt3DAnimation.QKeyFrame.InterpolationType = ...  # 0x2
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, coords: PySide2.QtGui.QVector2D): ...
        @typing.overload
        def __init__(
            self,
            coords: PySide2.QtGui.QVector2D,
            lh: PySide2.QtGui.QVector2D,
            rh: PySide2.QtGui.QVector2D,
        ): ...
        def coordinates(self) -> PySide2.QtGui.QVector2D: ...
        def interpolationType(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QKeyFrame.InterpolationType: ...
        def leftControlPoint(self) -> PySide2.QtGui.QVector2D: ...
        def rightControlPoint(self) -> PySide2.QtGui.QVector2D: ...
        def setCoordinates(self, coords: PySide2.QtGui.QVector2D): ...
        def setInterpolationType(
            self,
            interp: PySide2.Qt3DAnimation.Qt3DAnimation.QKeyFrame.InterpolationType,
        ): ...
        def setLeftControlPoint(self, lh: PySide2.QtGui.QVector2D): ...
        def setRightControlPoint(self, rh: PySide2.QtGui.QVector2D): ...

    class QKeyframeAnimation(PySide2.Qt3DAnimation.QAbstractAnimation):
        None_: Qt3DAnimation.QKeyframeAnimation = ...  # 0x0
        Constant: Qt3DAnimation.QKeyframeAnimation = ...  # 0x1
        Repeat: Qt3DAnimation.QKeyframeAnimation = ...  # 0x2

        class RepeatMode(object):
            None_: Qt3DAnimation.QKeyframeAnimation.RepeatMode = ...  # 0x0
            Constant: Qt3DAnimation.QKeyframeAnimation.RepeatMode = ...  # 0x1
            Repeat: Qt3DAnimation.QKeyframeAnimation.RepeatMode = ...  # 0x2
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
        def addKeyframe(self, keyframe: PySide2.Qt3DCore.Qt3DCore.QTransform): ...
        def easing(self) -> PySide2.QtCore.QEasingCurve: ...
        def endMode(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode: ...
        def framePositions(self) -> typing.List: ...
        def keyframeList(self) -> typing.List: ...
        def removeKeyframe(self, keyframe: PySide2.Qt3DCore.Qt3DCore.QTransform): ...
        def setEasing(self, easing: PySide2.QtCore.QEasingCurve): ...
        def setEndMode(
            self,
            mode: PySide2.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode,
        ): ...
        def setFramePositions(self, positions: typing.List): ...
        def setKeyframes(self, keyframes: typing.List): ...
        def setStartMode(
            self,
            mode: PySide2.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode,
        ): ...
        def setTarget(self, target: PySide2.Qt3DCore.Qt3DCore.QTransform): ...
        def setTargetName(self, name: str): ...
        def startMode(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode: ...
        def target(self) -> PySide2.Qt3DCore.Qt3DCore.QTransform: ...
        def targetName(self) -> str: ...

    class QLerpClipBlend(PySide2.Qt3DAnimation.QAbstractClipBlendNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def blendFactor(self) -> float: ...
        def endClip(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def setBlendFactor(self, blendFactor: float): ...
        def setEndClip(
            self, endClip: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode
        ): ...
        def setStartClip(
            self, startClip: PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode
        ): ...
        def startClip(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...

    class QMorphTarget(PySide2.QtCore.QObject):
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
        def addAttribute(self, attribute: PySide2.Qt3DRender.Qt3DRender.QAttribute): ...
        def attributeList(self) -> typing.List: ...
        def attributeNames(self) -> typing.List: ...
        @staticmethod
        def fromGeometry(
            geometry: PySide2.Qt3DRender.Qt3DRender.QGeometry,
            attributes: typing.Sequence,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QMorphTarget: ...
        def removeAttribute(
            self, attribute: PySide2.Qt3DRender.Qt3DRender.QAttribute
        ): ...
        def setAttributes(self, attributes: typing.List): ...

    class QMorphingAnimation(PySide2.Qt3DAnimation.QAbstractAnimation):
        Normalized: Qt3DAnimation.QMorphingAnimation = ...  # 0x0
        Relative: Qt3DAnimation.QMorphingAnimation = ...  # 0x1

        class Method(object):
            Normalized: Qt3DAnimation.QMorphingAnimation.Method = ...  # 0x0
            Relative: Qt3DAnimation.QMorphingAnimation.Method = ...  # 0x1
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
        def addMorphTarget(
            self, target: PySide2.Qt3DAnimation.Qt3DAnimation.QMorphTarget
        ): ...
        def easing(self) -> PySide2.QtCore.QEasingCurve: ...
        def getWeights(self, positionIndex: int) -> typing.List: ...
        def interpolator(self) -> float: ...
        def method(
            self,
        ) -> PySide2.Qt3DAnimation.Qt3DAnimation.QMorphingAnimation.Method: ...
        def morphTargetList(self) -> typing.List: ...
        def removeMorphTarget(
            self, target: PySide2.Qt3DAnimation.Qt3DAnimation.QMorphTarget
        ): ...
        def setEasing(self, easing: PySide2.QtCore.QEasingCurve): ...
        def setMethod(
            self, method: PySide2.Qt3DAnimation.Qt3DAnimation.QMorphingAnimation.Method
        ): ...
        def setMorphTargets(self, targets: typing.List): ...
        def setTarget(
            self, target: PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer
        ): ...
        def setTargetName(self, name: str): ...
        def setTargetPositions(self, targetPositions: typing.List): ...
        def setWeights(self, positionIndex: int, weights: typing.List): ...
        def target(self) -> PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer: ...
        def targetName(self) -> str: ...
        def targetPositions(self) -> typing.List: ...

    class QSkeletonMapping(PySide2.Qt3DAnimation.QAbstractChannelMapping):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ): ...
        def setSkeleton(
            self, skeleton: PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton
        ): ...
        def skeleton(self) -> PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton: ...

    class QVertexBlendAnimation(PySide2.Qt3DAnimation.QAbstractAnimation):
        def __init__(self, parent: typing.Optional[PySide2.QtCore.QObject] = ...): ...
        def addMorphTarget(
            self, target: PySide2.Qt3DAnimation.Qt3DAnimation.QMorphTarget
        ): ...
        def interpolator(self) -> float: ...
        def morphTargetList(self) -> typing.List: ...
        def removeMorphTarget(
            self, target: PySide2.Qt3DAnimation.Qt3DAnimation.QMorphTarget
        ): ...
        def setMorphTargets(self, targets: typing.List): ...
        def setTarget(
            self, target: PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer
        ): ...
        def setTargetName(self, name: str): ...
        def setTargetPositions(self, targetPositions: typing.List): ...
        def target(self) -> PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer: ...
        def targetName(self) -> str: ...
        def targetPositions(self) -> typing.List: ...

# eof
