import os
from pathlib import Path
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from OLELib.OLEUI_ExtractInputDialog import Ui_OLEUI_ExtractInputDialog

BASE_PATH = Path(__file__).resolve().parent.parent


class OLEExtInputWindow(QMainWindow):
    """
    The main Window for the UI Error Dialog.
    """

    def __init__(self, ui=False, debug=False, directory: Path or str=None, file: str = None, data=None, parent=None):
        super().__init__(parent)
        # Test UI with .ui file
        # By default, use pyuic5 to convert
        # loadUi(os.path.join(BASE_PATH, "QtUI", "OLEHandler_TestUI.ui"), self)

        # Run Dialog
        dialog = OLEExtInputDialog(ui=ui, debug=debug, directory=directory, file=file, data=data)

        # Update OLE Text
        dialog.ui.UI_InputIcon.setPixmap(QtGui.QPixmap(os.path.join(BASE_PATH, "Resources", "StatusIcon.png")))
        dialog.exec()


class OLEExtInputDialog(QDialog):
    def __init__(self, ui=False, debug=False, directory: Path or str = None, file: str = None, data=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_OLEUI_ExtractInputDialog()

        self.use_ui = ui
        self.dir = directory
        self.debug = debug
        self.file = file
        self.data = data

        self.ui.setupUi(self)

    def accept(self) -> None:
        user_ext = self.ui.UI_Input.text()

        if user_ext == "":
            user_ext = ".bin"

        self.close()

        parse_attachment(ui=self.use_ui, debug=self.debug, directory=self.dir, file=self.file, filetype=user_ext, data=self.data)

    def reject(self) -> None:
        return self.accept()


def parse_attachment(ui=False, debug=False, directory: Path or str = None, file: Path or str = None, filetype: str = None, data = None):
    try:
        filename = os.path.join(directory, file.split(".")[0] + filetype)

        with open(filename, "wb") as file_final:
            file_final.write(data)

        file_final.close()

    except Exception as e:
        print(e)
