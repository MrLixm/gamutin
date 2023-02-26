import math
import urllib.parse
import webbrowser
from typing import Optional

from Qt import QtWidgets
from Qt import QtCore

import gamutin
from gamutin.editor.assets.widgets import ContextWidget

__all__ = ("IssueDialog",)


class IssueDialog(QtWidgets.QDialog):
    def __init__(self, parent: Optional[QtWidgets.QWidget] = None):
        super().__init__(parent)
        self.setWindowTitle(f"{self.parent().windowTitle()} - Report an Issue")
        self.resize(
            math.floor(self.parent().width() / 2.5),
            math.floor(self.parent().height() / 2),
        )

        self.cookUI()
        self.bakeUI()

    def cookUI(self):
        # 1. Create
        self.lyt = QtWidgets.QVBoxLayout()
        self.lbl_title = QtWidgets.QLabel("Reporting an Issue")
        self.lbl_body = QtWidgets.QLabel(
            "Issue tracking is handled on GitHub. You will need a free GitHub account "
            f"to create a new issue on the {gamutin.c.name} repository.\n\n"
            "When submitting an issue please copy and paste the following information:"
        )
        self.context_widget = ContextWidget(self)
        self.btn_report = QtWidgets.QPushButton("Report a New Issue")

        # 2. Add
        self.setLayout(self.lyt)
        self.lyt.addWidget(self.lbl_title)
        self.lyt.addWidget(self.lbl_body)
        self.lyt.addWidget(self.context_widget)
        self.lyt.addWidget(self.btn_report)

        # 3. Modify
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_body.setWordWrap(True)
        # 4. Connections
        self.btn_report.clicked.connect(self.open_new_issue_url)

        return

    def bakeUI(self):
        self.context_widget.bakeUI()

    def open_new_issue_url(self):
        """
        Open the url to create a new issue on the repo in the user's default webbrowser
        """
        url = f"{gamutin.c.vcs_url}/issues/new"
        context = self.context_widget.getContext()

        issue_description = (
            f"# description\n"
            f"\nwrite a clear description of your issue here\n"
            f"\n# context\n\n```\n{context}\n```\n"
        )
        issue_description_safe = urllib.parse.quote_plus(issue_description)

        url = f"{url}?body={issue_description_safe}"

        webbrowser.open(url)
        return
