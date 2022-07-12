from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5 import QtGui
from OLELib.OLEUI_ErrorDialog import Ui_OLE_UIError
from pathlib import Path
import os

BASE_PATH = Path(__file__).resolve().parent.parent


class OLEErrorWindow(QMainWindow):
    """
    The main Window for the UI Error Dialog.
    """

    def __init__(self, error_message="", parent=None):
        super().__init__(parent)
        # Test UI with .ui file
        # By default, use pyuic5 to convert
        # loadUi(os.path.join(BASE_PATH, "QtUI", "OLEHandler_TestUI.ui"), self)

        # Run Dialog
        dialog = OLEErrorDialog()

        # Update OLE Text
        dialog.ui.UI_Error.setText(error_message)
        dialog.ui.UI_ErrorIcon.setPixmap(QtGui.QPixmap(os.path.join(BASE_PATH, "Resources", "ErrorIcon.png")))
        dialog.exec()


class OLEErrorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_OLE_UIError()

        self.ui.setupUi(self)

    def accept(self) -> None:
        self.close()
