import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from OLELib.OLEUI_Dialog import Ui_OLEHandlerDialog
from PyQt5.uic import loadUi
from pathlib import Path
from OLELib.FileExtractor import convert_file

BASE_PATH = Path(__file__).resolve().parent


class OLEWindow(QMainWindow):
    """
    The main Window for the UI Dialog.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # Test UI with .ui file
        # By default, use pyuic5 to convert
        # loadUi(os.path.join(BASE_PATH, "QtUI", "OLEHandler_TestUI.ui"), self)

        # Run Dialog
        dialog = OLEDialog()
        dialog.exec()


class OLEDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_OLEHandlerDialog()
        self.ui.setupUi(self)

    def chooseExtractSave(self):
        """
        Chooses the extract location.
        :return:
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if fileName:
            print(fileName)
            self.ui.ExtractSaveDirectory.setText(fileName)

    def chooseExtractFile(self):
        """
        Chooses the file to be extracted.
        :return:
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if fileName:
            print(fileName)
            self.ui.FileExtractDirectory.setText(fileName)

    def accept(self) -> None:
        """
        Code to handle on accept.
        :return:
        """
        extract_dir = self.ui.FileExtractDirectory.text()
        save_dir = self.ui.ExtractSaveDirectory.text()

        # Close Window
        self.close()

        print(f"{extract_dir} | {save_dir}")

        # convert_file(extract_dir, save_dir)


def run_ui():
    ole_app = QApplication(sys.argv)
    ole_window = OLEWindow()
    ole_window.show()


run_ui()
