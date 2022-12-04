"""
Top level module to build the UI.
"""
from __future__ import annotations

import logging
import pprint
import sys
import webbrowser
from functools import partial

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

import pgcheck
from . import cfg
from . import compounds

logger = logging.getLogger(__name__)


def getQApp() -> QtWidgets.QApplication | None:
    """
    Returns:
        new QApplication instance or None if it already exists.
    """
    app = None

    if not QtWidgets.QApplication.instance():

        app = QtWidgets.QApplication(sys.argv)
        app.setOrganizationName(pgcheck.c.org)
        app.setApplicationName(pgcheck.c.name)
        app.setApplicationVersion(pgcheck.__version__)
        if not pgcheck.c.plateform.is_mac:
            app.setWindowIcon(QtGui.QIcon(str(cfg.resources.icon_main)))

    # load everything that required a QApp
    cfg.resources.register()

    return app


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        logger.info("[MainWindow] Launched.")

        self.setWindowTitle(f"{pgcheck.c.org.upper()} - {pgcheck.c.name.title()}")
        self.resize(700, 500)

        self.settings = cfg.getAppQSettings()
        self.loadSettings()

        self.dialog_about = compounds.dialogs.AboutDialog(self)
        self.dialog_issue = compounds.dialogs.IssueDialog(self)

        self.cookUI()
        return

    # noinspection PyTypeChecker
    def loadSettings(self):

        # if debug mode is on we avoid loading settings
        if pgcheck.cfg.debug:
            return

        self.settings.beginGroup("MainWindow")
        stg_size: QtCore.QSize | None = self.settings.value("size", None)
        stg_pos: QtCore.QPoint = self.settings.value("position")
        self.settings.endGroup()

        if stg_size:
            self.resize(stg_size)
        if stg_pos:
            self.move(stg_pos)

        logger.debug("[MainWindow][loadSettings] Finished.")
        return

    def saveSettings(self):

        self.settings.beginGroup("MainWindow")
        self.settings.setValue("size", self.size())
        self.settings.setValue("position", self.pos())
        self.settings.endGroup()

        return

    def cookUI(self):

        self.setMenuBar(MainMenuBar(self))

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.saveSettings()
        super().closeEvent(event)


class MainMenuBar(QtWidgets.QMenuBar):
    """
    Menu bar of the application. Always visible.
    """

    def __init__(self, parent: MainWindow):
        super().__init__(parent)
        self.cookUI()
        return

    def cookUI(self):

        # 1. Create
        self.menu_file = self.addMenu("File")
        self.menu_help = self.addMenu("Help")

        self.act_exit = QtWidgets.QAction("Exit")
        self.act_about = QtWidgets.QAction("About")
        self.act_open_doc = QtWidgets.QAction("Open Documentation")
        self.act_report_issue = QtWidgets.QAction("Report an Issue")

        # 2. Add
        self.menu_file.addAction(self.act_exit)
        self.menu_help.addAction(self.act_about)
        self.menu_help.addAction(self.act_open_doc)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.act_report_issue)

        # 3. Modify
        self.act_exit.setShortcut("Ctrl+Q")

        # 4. Connections
        self.act_exit.triggered.connect(QtWidgets.QApplication.quit)
        self.act_about.triggered.connect(self.parent().dialog_about.show)
        self.act_report_issue.triggered.connect(self.parent().dialog_issue.show)
        return

    def parent(self) -> MainWindow:
        # override for type-hints
        return super().parent()
