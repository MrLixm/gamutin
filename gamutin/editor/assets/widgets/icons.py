from Qt import QtWidgets


class BaseDisplayIcon(QtWidgets.QPushButton):
    """
    An icon made to just be displayed with an optional tooltip when hovering on it.
    """

    stylesheet = "QPushButton{border: unset; background: transparent;}"

    def __init__(self):
        super().__init__()
        self.setDown(True)
        self.setStyleSheet(self.stylesheet)
