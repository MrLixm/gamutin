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
PySide2.QtPrintSupport, except for defaults which are replaced by "...".
"""

# Module PySide2.QtPrintSupport
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
import PySide2.QtPrintSupport

class QAbstractPrintDialog(PySide2.QtWidgets.QDialog):
    AllPages: QAbstractPrintDialog = ...  # 0x0
    None_: QAbstractPrintDialog = ...  # 0x0
    PrintToFile: QAbstractPrintDialog = ...  # 0x1
    Selection: QAbstractPrintDialog = ...  # 0x1
    PageRange: QAbstractPrintDialog = ...  # 0x2
    PrintSelection: QAbstractPrintDialog = ...  # 0x2
    CurrentPage: QAbstractPrintDialog = ...  # 0x3
    PrintPageRange: QAbstractPrintDialog = ...  # 0x4
    PrintShowPageSize: QAbstractPrintDialog = ...  # 0x8
    PrintCollateCopies: QAbstractPrintDialog = ...  # 0x10
    DontUseSheet: QAbstractPrintDialog = ...  # 0x20
    PrintCurrentPage: QAbstractPrintDialog = ...  # 0x40

    class PrintDialogOption(object):
        None_: QAbstractPrintDialog.PrintDialogOption = ...  # 0x0
        PrintToFile: QAbstractPrintDialog.PrintDialogOption = ...  # 0x1
        PrintSelection: QAbstractPrintDialog.PrintDialogOption = ...  # 0x2
        PrintPageRange: QAbstractPrintDialog.PrintDialogOption = ...  # 0x4
        PrintShowPageSize: QAbstractPrintDialog.PrintDialogOption = ...  # 0x8
        PrintCollateCopies: QAbstractPrintDialog.PrintDialogOption = ...  # 0x10
        DontUseSheet: QAbstractPrintDialog.PrintDialogOption = ...  # 0x20
        PrintCurrentPage: QAbstractPrintDialog.PrintDialogOption = ...  # 0x40

    class PrintDialogOptions(object): ...

    class PrintRange(object):
        AllPages: QAbstractPrintDialog.PrintRange = ...  # 0x0
        Selection: QAbstractPrintDialog.PrintRange = ...  # 0x1
        PageRange: QAbstractPrintDialog.PrintRange = ...  # 0x2
        CurrentPage: QAbstractPrintDialog.PrintRange = ...  # 0x3
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ): ...
    def addEnabledOption(
        self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
    ): ...
    def enabledOptions(
        self,
    ) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions: ...
    def fromPage(self) -> int: ...
    def isOptionEnabled(
        self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
    ) -> bool: ...
    def maxPage(self) -> int: ...
    def minPage(self) -> int: ...
    def printRange(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange: ...
    def printer(self) -> PySide2.QtPrintSupport.QPrinter: ...
    def setEnabledOptions(
        self, options: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
    ): ...
    def setFromTo(self, fromPage: int, toPage: int): ...
    def setMinMax(self, min: int, max: int): ...
    def setOptionTabs(self, tabs: typing.Sequence): ...
    def setPrintRange(
        self, range: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange
    ): ...
    def toPage(self) -> int: ...

class QPageSetupDialog(PySide2.QtWidgets.QDialog):
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...): ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ): ...
    def done(self, result: int): ...
    def exec_(self) -> int: ...
    @typing.overload
    def open(self): ...
    @typing.overload
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes): ...
    def printer(self) -> PySide2.QtPrintSupport.QPrinter: ...
    def setVisible(self, visible: bool): ...

class QPrintDialog(PySide2.QtPrintSupport.QAbstractPrintDialog):
    @typing.overload
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...): ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ): ...
    def done(self, result: int): ...
    def exec_(self) -> int: ...
    @typing.overload
    def open(self): ...
    @typing.overload
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes): ...
    def options(
        self,
    ) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions: ...
    def setOption(
        self,
        option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption,
        on: bool = ...,
    ): ...
    def setOptions(
        self, options: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
    ): ...
    def setVisible(self, visible: bool): ...
    def testOption(
        self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
    ) -> bool: ...

class QPrintEngine(Shiboken.Object):
    PPK_CollateCopies: QPrintEngine = ...  # 0x0
    PPK_ColorMode: QPrintEngine = ...  # 0x1
    PPK_Creator: QPrintEngine = ...  # 0x2
    PPK_DocumentName: QPrintEngine = ...  # 0x3
    PPK_FullPage: QPrintEngine = ...  # 0x4
    PPK_NumberOfCopies: QPrintEngine = ...  # 0x5
    PPK_Orientation: QPrintEngine = ...  # 0x6
    PPK_OutputFileName: QPrintEngine = ...  # 0x7
    PPK_PageOrder: QPrintEngine = ...  # 0x8
    PPK_PageRect: QPrintEngine = ...  # 0x9
    PPK_PageSize: QPrintEngine = ...  # 0xa
    PPK_PaperSize: QPrintEngine = ...  # 0xa
    PPK_PaperRect: QPrintEngine = ...  # 0xb
    PPK_PaperSource: QPrintEngine = ...  # 0xc
    PPK_PrinterName: QPrintEngine = ...  # 0xd
    PPK_PrinterProgram: QPrintEngine = ...  # 0xe
    PPK_Resolution: QPrintEngine = ...  # 0xf
    PPK_SelectionOption: QPrintEngine = ...  # 0x10
    PPK_SupportedResolutions: QPrintEngine = ...  # 0x11
    PPK_WindowsPageSize: QPrintEngine = ...  # 0x12
    PPK_FontEmbedding: QPrintEngine = ...  # 0x13
    PPK_Duplex: QPrintEngine = ...  # 0x14
    PPK_PaperSources: QPrintEngine = ...  # 0x15
    PPK_CustomPaperSize: QPrintEngine = ...  # 0x16
    PPK_PageMargins: QPrintEngine = ...  # 0x17
    PPK_CopyCount: QPrintEngine = ...  # 0x18
    PPK_SupportsMultipleCopies: QPrintEngine = ...  # 0x19
    PPK_PaperName: QPrintEngine = ...  # 0x1a
    PPK_QPageSize: QPrintEngine = ...  # 0x1b
    PPK_QPageMargins: QPrintEngine = ...  # 0x1c
    PPK_QPageLayout: QPrintEngine = ...  # 0x1d
    PPK_CustomBase: QPrintEngine = ...  # 0xff00

    class PrintEnginePropertyKey(object):
        PPK_CollateCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x0
        PPK_ColorMode: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1
        PPK_Creator: QPrintEngine.PrintEnginePropertyKey = ...  # 0x2
        PPK_DocumentName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x3
        PPK_FullPage: QPrintEngine.PrintEnginePropertyKey = ...  # 0x4
        PPK_NumberOfCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x5
        PPK_Orientation: QPrintEngine.PrintEnginePropertyKey = ...  # 0x6
        PPK_OutputFileName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x7
        PPK_PageOrder: QPrintEngine.PrintEnginePropertyKey = ...  # 0x8
        PPK_PageRect: QPrintEngine.PrintEnginePropertyKey = ...  # 0x9
        PPK_PageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0xa
        PPK_PaperSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0xa
        PPK_PaperRect: QPrintEngine.PrintEnginePropertyKey = ...  # 0xb
        PPK_PaperSource: QPrintEngine.PrintEnginePropertyKey = ...  # 0xc
        PPK_PrinterName: QPrintEngine.PrintEnginePropertyKey = ...  # 0xd
        PPK_PrinterProgram: QPrintEngine.PrintEnginePropertyKey = ...  # 0xe
        PPK_Resolution: QPrintEngine.PrintEnginePropertyKey = ...  # 0xf
        PPK_SelectionOption: QPrintEngine.PrintEnginePropertyKey = ...  # 0x10
        PPK_SupportedResolutions: QPrintEngine.PrintEnginePropertyKey = ...  # 0x11
        PPK_WindowsPageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x12
        PPK_FontEmbedding: QPrintEngine.PrintEnginePropertyKey = ...  # 0x13
        PPK_Duplex: QPrintEngine.PrintEnginePropertyKey = ...  # 0x14
        PPK_PaperSources: QPrintEngine.PrintEnginePropertyKey = ...  # 0x15
        PPK_CustomPaperSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x16
        PPK_PageMargins: QPrintEngine.PrintEnginePropertyKey = ...  # 0x17
        PPK_CopyCount: QPrintEngine.PrintEnginePropertyKey = ...  # 0x18
        PPK_SupportsMultipleCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x19
        PPK_PaperName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1a
        PPK_QPageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1b
        PPK_QPageMargins: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1c
        PPK_QPageLayout: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1d
        PPK_CustomBase: QPrintEngine.PrintEnginePropertyKey = ...  # 0xff00
    def __init__(self): ...
    def abort(self) -> bool: ...
    def metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def newPage(self) -> bool: ...
    def printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState: ...
    def property(
        self, key: PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey
    ) -> typing.Any: ...
    def setProperty(
        self,
        key: PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey,
        value: typing.Any,
    ): ...

class QPrintPreviewDialog(PySide2.QtWidgets.QDialog):
    @typing.overload
    def __init__(
        self,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ): ...
    def done(self, result: int): ...
    @typing.overload
    def open(self): ...
    @typing.overload
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes): ...
    def printer(self) -> PySide2.QtPrintSupport.QPrinter: ...
    def setVisible(self, visible: bool): ...

class QPrintPreviewWidget(PySide2.QtWidgets.QWidget):
    CustomZoom: QPrintPreviewWidget = ...  # 0x0
    SinglePageView: QPrintPreviewWidget = ...  # 0x0
    FacingPagesView: QPrintPreviewWidget = ...  # 0x1
    FitToWidth: QPrintPreviewWidget = ...  # 0x1
    AllPagesView: QPrintPreviewWidget = ...  # 0x2
    FitInView: QPrintPreviewWidget = ...  # 0x2

    class ViewMode(object):
        SinglePageView: QPrintPreviewWidget.ViewMode = ...  # 0x0
        FacingPagesView: QPrintPreviewWidget.ViewMode = ...  # 0x1
        AllPagesView: QPrintPreviewWidget.ViewMode = ...  # 0x2

    class ZoomMode(object):
        CustomZoom: QPrintPreviewWidget.ZoomMode = ...  # 0x0
        FitToWidth: QPrintPreviewWidget.ZoomMode = ...  # 0x1
        FitInView: QPrintPreviewWidget.ZoomMode = ...  # 0x2
    @typing.overload
    def __init__(
        self,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ): ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ): ...
    def currentPage(self) -> int: ...
    def fitInView(self): ...
    def fitToWidth(self): ...
    def orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation: ...
    def pageCount(self) -> int: ...
    def print_(self): ...
    def setAllPagesViewMode(self): ...
    def setCurrentPage(self, pageNumber: int): ...
    def setFacingPagesViewMode(self): ...
    def setLandscapeOrientation(self): ...
    def setOrientation(
        self, orientation: PySide2.QtPrintSupport.QPrinter.Orientation
    ): ...
    def setPortraitOrientation(self): ...
    def setSinglePageViewMode(self): ...
    def setViewMode(
        self, viewMode: PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode
    ): ...
    def setVisible(self, visible: bool): ...
    def setZoomFactor(self, zoomFactor: float): ...
    def setZoomMode(
        self, zoomMode: PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode
    ): ...
    def updatePreview(self): ...
    def viewMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode: ...
    def zoomFactor(self) -> float: ...
    def zoomIn(self, zoom: float = ...): ...
    def zoomMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode: ...
    def zoomOut(self, zoom: float = ...): ...

class QPrinter(PySide2.QtGui.QPagedPaintDevice):
    AllPages: QPrinter = ...  # 0x0
    DuplexNone: QPrinter = ...  # 0x0
    FirstPageFirst: QPrinter = ...  # 0x0
    GrayScale: QPrinter = ...  # 0x0
    Idle: QPrinter = ...  # 0x0
    Millimeter: QPrinter = ...  # 0x0
    NativeFormat: QPrinter = ...  # 0x0
    OnlyOne: QPrinter = ...  # 0x0
    Portrait: QPrinter = ...  # 0x0
    ScreenResolution: QPrinter = ...  # 0x0
    Upper: QPrinter = ...  # 0x0
    Active: QPrinter = ...  # 0x1
    Color: QPrinter = ...  # 0x1
    DuplexAuto: QPrinter = ...  # 0x1
    Landscape: QPrinter = ...  # 0x1
    LastPageFirst: QPrinter = ...  # 0x1
    Lower: QPrinter = ...  # 0x1
    PdfFormat: QPrinter = ...  # 0x1
    Point: QPrinter = ...  # 0x1
    PrinterResolution: QPrinter = ...  # 0x1
    Selection: QPrinter = ...  # 0x1
    Aborted: QPrinter = ...  # 0x2
    DuplexLongSide: QPrinter = ...  # 0x2
    HighResolution: QPrinter = ...  # 0x2
    Inch: QPrinter = ...  # 0x2
    Middle: QPrinter = ...  # 0x2
    PageRange: QPrinter = ...  # 0x2
    CurrentPage: QPrinter = ...  # 0x3
    DuplexShortSide: QPrinter = ...  # 0x3
    Error: QPrinter = ...  # 0x3
    Manual: QPrinter = ...  # 0x3
    Pica: QPrinter = ...  # 0x3
    Didot: QPrinter = ...  # 0x4
    Envelope: QPrinter = ...  # 0x4
    Cicero: QPrinter = ...  # 0x5
    EnvelopeManual: QPrinter = ...  # 0x5
    Auto: QPrinter = ...  # 0x6
    DevicePixel: QPrinter = ...  # 0x6
    Tractor: QPrinter = ...  # 0x7
    SmallFormat: QPrinter = ...  # 0x8
    LargeFormat: QPrinter = ...  # 0x9
    LargeCapacity: QPrinter = ...  # 0xa
    Cassette: QPrinter = ...  # 0xb
    FormSource: QPrinter = ...  # 0xc
    MaxPageSource: QPrinter = ...  # 0xd
    CustomSource: QPrinter = ...  # 0xe
    LastPaperSource: QPrinter = ...  # 0xe

    class ColorMode(object):
        GrayScale: QPrinter.ColorMode = ...  # 0x0
        Color: QPrinter.ColorMode = ...  # 0x1

    class DuplexMode(object):
        DuplexNone: QPrinter.DuplexMode = ...  # 0x0
        DuplexAuto: QPrinter.DuplexMode = ...  # 0x1
        DuplexLongSide: QPrinter.DuplexMode = ...  # 0x2
        DuplexShortSide: QPrinter.DuplexMode = ...  # 0x3

    class Orientation(object):
        Portrait: QPrinter.Orientation = ...  # 0x0
        Landscape: QPrinter.Orientation = ...  # 0x1

    class OutputFormat(object):
        NativeFormat: QPrinter.OutputFormat = ...  # 0x0
        PdfFormat: QPrinter.OutputFormat = ...  # 0x1

    class PageOrder(object):
        FirstPageFirst: QPrinter.PageOrder = ...  # 0x0
        LastPageFirst: QPrinter.PageOrder = ...  # 0x1

    class PaperSource(object):
        OnlyOne: QPrinter.PaperSource = ...  # 0x0
        Upper: QPrinter.PaperSource = ...  # 0x0
        Lower: QPrinter.PaperSource = ...  # 0x1
        Middle: QPrinter.PaperSource = ...  # 0x2
        Manual: QPrinter.PaperSource = ...  # 0x3
        Envelope: QPrinter.PaperSource = ...  # 0x4
        EnvelopeManual: QPrinter.PaperSource = ...  # 0x5
        Auto: QPrinter.PaperSource = ...  # 0x6
        Tractor: QPrinter.PaperSource = ...  # 0x7
        SmallFormat: QPrinter.PaperSource = ...  # 0x8
        LargeFormat: QPrinter.PaperSource = ...  # 0x9
        LargeCapacity: QPrinter.PaperSource = ...  # 0xa
        Cassette: QPrinter.PaperSource = ...  # 0xb
        FormSource: QPrinter.PaperSource = ...  # 0xc
        MaxPageSource: QPrinter.PaperSource = ...  # 0xd
        CustomSource: QPrinter.PaperSource = ...  # 0xe
        LastPaperSource: QPrinter.PaperSource = ...  # 0xe

    class PrintRange(object):
        AllPages: QPrinter.PrintRange = ...  # 0x0
        Selection: QPrinter.PrintRange = ...  # 0x1
        PageRange: QPrinter.PrintRange = ...  # 0x2
        CurrentPage: QPrinter.PrintRange = ...  # 0x3

    class PrinterMode(object):
        ScreenResolution: QPrinter.PrinterMode = ...  # 0x0
        PrinterResolution: QPrinter.PrinterMode = ...  # 0x1
        HighResolution: QPrinter.PrinterMode = ...  # 0x2

    class PrinterState(object):
        Idle: QPrinter.PrinterState = ...  # 0x0
        Active: QPrinter.PrinterState = ...  # 0x1
        Aborted: QPrinter.PrinterState = ...  # 0x2
        Error: QPrinter.PrinterState = ...  # 0x3

    class Unit(object):
        Millimeter: QPrinter.Unit = ...  # 0x0
        Point: QPrinter.Unit = ...  # 0x1
        Inch: QPrinter.Unit = ...  # 0x2
        Pica: QPrinter.Unit = ...  # 0x3
        Didot: QPrinter.Unit = ...  # 0x4
        Cicero: QPrinter.Unit = ...  # 0x5
        DevicePixel: QPrinter.Unit = ...  # 0x6
    @typing.overload
    def __init__(self, mode: PySide2.QtPrintSupport.QPrinter.PrinterMode = ...): ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinterInfo,
        mode: PySide2.QtPrintSupport.QPrinter.PrinterMode = ...,
    ): ...
    def abort(self) -> bool: ...
    def actualNumCopies(self) -> int: ...
    def collateCopies(self) -> bool: ...
    def colorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode: ...
    def copyCount(self) -> int: ...
    def creator(self) -> str: ...
    def devType(self) -> int: ...
    def docName(self) -> str: ...
    def doubleSidedPrinting(self) -> bool: ...
    def duplex(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode: ...
    def fontEmbeddingEnabled(self) -> bool: ...
    def fromPage(self) -> int: ...
    def fullPage(self) -> bool: ...
    def getPageMargins(
        self, unit: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> typing.Tuple: ...
    def isValid(self) -> bool: ...
    def metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def newPage(self) -> bool: ...
    def numCopies(self) -> int: ...
    def orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation: ...
    def outputFileName(self) -> str: ...
    def outputFormat(self) -> PySide2.QtPrintSupport.QPrinter.OutputFormat: ...
    def pageOrder(self) -> PySide2.QtPrintSupport.QPrinter.PageOrder: ...
    @typing.overload
    def pageRect(self) -> PySide2.QtCore.QRect: ...
    @typing.overload
    def pageRect(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> PySide2.QtCore.QRectF: ...
    def pageSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize: ...
    def paintEngine(self) -> PySide2.QtGui.QPaintEngine: ...
    def paperName(self) -> str: ...
    @typing.overload
    def paperRect(self) -> PySide2.QtCore.QRect: ...
    @typing.overload
    def paperRect(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> PySide2.QtCore.QRectF: ...
    @typing.overload
    def paperSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize: ...
    @typing.overload
    def paperSize(
        self, unit: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> PySide2.QtCore.QSizeF: ...
    def paperSource(self) -> PySide2.QtPrintSupport.QPrinter.PaperSource: ...
    def pdfVersion(self) -> PySide2.QtGui.QPagedPaintDevice.PdfVersion: ...
    def printEngine(self) -> PySide2.QtPrintSupport.QPrintEngine: ...
    def printProgram(self) -> str: ...
    def printRange(self) -> PySide2.QtPrintSupport.QPrinter.PrintRange: ...
    def printerName(self) -> str: ...
    def printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState: ...
    def resolution(self) -> int: ...
    def setCollateCopies(self, collate: bool): ...
    def setColorMode(self, arg__1: PySide2.QtPrintSupport.QPrinter.ColorMode): ...
    def setCopyCount(self, arg__1: int): ...
    def setCreator(self, arg__1: str): ...
    def setDocName(self, arg__1: str): ...
    def setDoubleSidedPrinting(self, enable: bool): ...
    def setDuplex(self, duplex: PySide2.QtPrintSupport.QPrinter.DuplexMode): ...
    def setEngines(
        self,
        printEngine: PySide2.QtPrintSupport.QPrintEngine,
        paintEngine: PySide2.QtGui.QPaintEngine,
    ): ...
    def setFontEmbeddingEnabled(self, enable: bool): ...
    def setFromTo(self, fromPage: int, toPage: int): ...
    def setFullPage(self, arg__1: bool): ...
    def setMargins(self, m: PySide2.QtGui.QPagedPaintDevice.Margins): ...
    def setNumCopies(self, arg__1: int): ...
    def setOrientation(self, arg__1: PySide2.QtPrintSupport.QPrinter.Orientation): ...
    def setOutputFileName(self, arg__1: str): ...
    def setOutputFormat(self, format: PySide2.QtPrintSupport.QPrinter.OutputFormat): ...
    @typing.overload
    def setPageMargins(
        self,
        left: float,
        top: float,
        right: float,
        bottom: float,
        unit: PySide2.QtPrintSupport.QPrinter.Unit,
    ): ...
    @typing.overload
    def setPageMargins(self, margins: PySide2.QtCore.QMarginsF) -> bool: ...
    def setPageOrder(self, arg__1: PySide2.QtPrintSupport.QPrinter.PageOrder): ...
    @typing.overload
    def setPageSize(self, arg__1: PySide2.QtGui.QPageSize) -> bool: ...
    @typing.overload
    def setPageSize(self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize): ...
    def setPageSizeMM(self, size: PySide2.QtCore.QSizeF): ...
    def setPaperName(self, paperName: str): ...
    @typing.overload
    def setPaperSize(self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize): ...
    @typing.overload
    def setPaperSize(
        self,
        paperSize: PySide2.QtCore.QSizeF,
        unit: PySide2.QtPrintSupport.QPrinter.Unit,
    ): ...
    def setPaperSource(self, arg__1: PySide2.QtPrintSupport.QPrinter.PaperSource): ...
    def setPdfVersion(self, version: PySide2.QtGui.QPagedPaintDevice.PdfVersion): ...
    def setPrintProgram(self, arg__1: str): ...
    def setPrintRange(self, range: PySide2.QtPrintSupport.QPrinter.PrintRange): ...
    def setPrinterName(self, arg__1: str): ...
    def setResolution(self, arg__1: int): ...
    def setWinPageSize(self, winPageSize: int): ...
    def supportedPaperSources(self) -> typing.List: ...
    def supportedResolutions(self) -> typing.List: ...
    def supportsMultipleCopies(self) -> bool: ...
    def toPage(self) -> int: ...
    def winPageSize(self) -> int: ...

class QPrinterInfo(Shiboken.Object):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other: PySide2.QtPrintSupport.QPrinterInfo): ...
    @typing.overload
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter): ...
    def __copy__(self): ...
    @staticmethod
    def availablePrinterNames() -> typing.List: ...
    @staticmethod
    def availablePrinters() -> typing.List: ...
    def defaultColorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode: ...
    def defaultDuplexMode(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode: ...
    def defaultPageSize(self) -> PySide2.QtGui.QPageSize: ...
    @staticmethod
    def defaultPrinter() -> PySide2.QtPrintSupport.QPrinterInfo: ...
    @staticmethod
    def defaultPrinterName() -> str: ...
    def description(self) -> str: ...
    def isDefault(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isRemote(self) -> bool: ...
    def location(self) -> str: ...
    def makeAndModel(self) -> str: ...
    def maximumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize: ...
    def minimumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize: ...
    @staticmethod
    def printerInfo(printerName: str) -> PySide2.QtPrintSupport.QPrinterInfo: ...
    def printerName(self) -> str: ...
    def state(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState: ...
    def supportedColorModes(self) -> typing.List: ...
    def supportedDuplexModes(self) -> typing.List: ...
    def supportedPageSizes(self) -> typing.List: ...
    def supportedPaperSizes(self) -> typing.List: ...
    def supportedResolutions(self) -> typing.List: ...
    def supportedSizesWithNames(self) -> typing.List: ...
    def supportsCustomPageSizes(self) -> bool: ...

# eof
