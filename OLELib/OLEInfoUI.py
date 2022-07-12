import os
from pathlib import Path
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from OLELib.OLEUI_InfoDialog import Ui_OLE_UIInfo

BASE_PATH = Path(__file__).resolve().parent.parent


class OLEInfoWindow(QMainWindow):
    """
    The main Window for the UI Error Dialog.
    """

    def __init__(self, title="", text="", parent=None):
        super().__init__(parent)
        # Test UI with .ui file
        # By default, use pyuic5 to convert
        # loadUi(os.path.join(BASE_PATH, "QtUI", "OLEHandler_TestUI.ui"), self)

        # Run Dialog
        dialog = OLEInfoDialog()

        # Update OLE Text
        dialog.ui.UI_StatusTitle.setText(title)
        dialog.ui.UI_Status.setText(text)
        dialog.ui.UI_StatusIcon.setPixmap(QtGui.QPixmap(os.path.join(BASE_PATH, "Resources", "StatusIcon.png")))
        dialog.exec()


class OLEInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_OLE_UIInfo()

        self.ui.setupUi(self)

    def accept(self) -> None:
        self.close()
