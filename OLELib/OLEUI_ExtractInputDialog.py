# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OLEUI_ExtractInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OLEUI_ExtractInputDialog(object):
    def setupUi(self, OLEUI_ExtractInputDialog):
        OLEUI_ExtractInputDialog.setObjectName("OLEUI_ExtractInputDialog")
        OLEUI_ExtractInputDialog.resize(569, 217)
        OLEUI_ExtractInputDialog.setMaximumSize(QtCore.QSize(569, 217))
        self.buttonBox = QtWidgets.QDialogButtonBox(OLEUI_ExtractInputDialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 180, 341, 32))
        self.buttonBox.setMinimumSize(QtCore.QSize(341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.UI_InputTitle = QtWidgets.QLabel(OLEUI_ExtractInputDialog)
        self.UI_InputTitle.setGeometry(QtCore.QRect(130, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.UI_InputTitle.setFont(font)
        self.UI_InputTitle.setObjectName("UI_InputTitle")
        self.UI_InputInfo = QtWidgets.QLabel(OLEUI_ExtractInputDialog)
        self.UI_InputInfo.setGeometry(QtCore.QRect(130, 50, 421, 71))
        self.UI_InputInfo.setWordWrap(True)
        self.UI_InputInfo.setObjectName("UI_InputInfo")
        self.UI_InputIcon = QtWidgets.QLabel(OLEUI_ExtractInputDialog)
        self.UI_InputIcon.setGeometry(QtCore.QRect(20, 50, 91, 91))
        self.UI_InputIcon.setText("")
        self.UI_InputIcon.setPixmap(QtGui.QPixmap("../Resources/StatusIcon.png"))
        self.UI_InputIcon.setObjectName("UI_InputIcon")
        self.UI_Input = QtWidgets.QLineEdit(OLEUI_ExtractInputDialog)
        self.UI_Input.setGeometry(QtCore.QRect(130, 140, 411, 20))
        self.UI_Input.setObjectName("UI_Input")

        self.retranslateUi(OLEUI_ExtractInputDialog)
        self.buttonBox.accepted.connect(OLEUI_ExtractInputDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(OLEUI_ExtractInputDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(OLEUI_ExtractInputDialog)

    def retranslateUi(self, OLEUI_ExtractInputDialog):
        _translate = QtCore.QCoreApplication.translate
        OLEUI_ExtractInputDialog.setWindowTitle(_translate("OLEUI_ExtractInputDialog", "Dialog"))
        self.UI_InputTitle.setText(_translate("OLEUI_ExtractInputDialog", "Unknown File Type"))
        self.UI_InputInfo.setText(_translate("OLEUI_ExtractInputDialog", "OLEHandler was not able to identify the file type. Instead, please input the assumed file type of the file."))
        self.UI_Input.setText(_translate("OLEUI_ExtractInputDialog", ".bin"))
