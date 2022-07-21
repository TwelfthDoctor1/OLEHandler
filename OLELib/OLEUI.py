import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from OLELib.OLEUI_Dialog import Ui_OLEHandlerDialog
from PyQt5.uic import loadUi
from pathlib import Path
from OLELib.FileExtractor import convert_file
from OLEVersioning import __version__
from OLELib.OLEErrorUI import OLEErrorWindow

BASE_PATH = Path(__file__).resolve().parent
DEBUG = False


class OLEWindow(QMainWindow):
    """
    The main Window for the UI Dialog.
    """

    def __init__(self, debug, parent=None):
        super().__init__(parent)
        # Test UI with .ui file
        # By default, use pyuic5 to convert
        # loadUi(os.path.join(BASE_PATH, "QtUI", "OLEHandler_TestUI.ui"), self)

        # Run Dialog
        dialog = OLEDialog(debug)

        # Update OLE Versioning
        dialog.ui.OLEUI_Version.setText(f"OLE UI Version: {__version__}")
        dialog.exec()


class OLEDialog(QDialog):
    """
    Dialog Class for the OLEHandler UI.

    Any custom functions MUST be declared and established in QtDesigner.
    From there, establish the custom function in this class.
    """
    def __init__(self, debug=False, parent=None):
        super().__init__(parent)
        self.console_debug = debug
        self.ui = Ui_OLEHandlerDialog()

        self.ui.setupUi(self)

    def chooseExtractSave(self):
        """
        Chooses the extract location.
        :return:
        """
        options = QFileDialog.Options()
        fileName = QFileDialog.getExistingDirectory(self, "Select Extract Directory", "", options=options)
        if fileName:
            print(fileName)
            self.ui.ExtractSaveDirectory.setText(fileName)

    def chooseExtractFile(self):
        """
        Chooses the file to be extracted.
        :return:
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File to Extract", "", "All Files (*)",
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

        # Reject is FilePaths are invalid
        if os.path.exists(extract_dir) is False or os.path.exists(save_dir) is False:
            if self.console_debug is True:
                print("[ERROR 3]: The specified file (either or both) are not found.")

            err_dialog = OLEErrorWindow(error_message="[ERROR 3]: The specified file(s) (either or both) are not found"
                                                      " \nor does not exist.")
            err_dialog.show()

        else:
            # Close Window
            self.close()

            convert_file(extract_dir, save_dir, ui=True, debug=DEBUG)


def run_gtui(extract_dir, save_dir, ui=True, debug=False):
    global DEBUG
    DEBUG = debug

    if ui is True:
        ole_app = QApplication(sys.argv)
        ole_window = OLEWindow(debug)
        ole_window.show()

    else:
        convert_file(extract_dir, save_dir, debug, ui)
        input("Press [ENTER] to continue...")

