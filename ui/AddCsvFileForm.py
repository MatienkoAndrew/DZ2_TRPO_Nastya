# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCsvFileForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AddCsvFileForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 55, 16))
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(160, 60, 113, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.quantityEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.quantityEdit.setGeometry(QtCore.QRect(160, 100, 113, 22))
        self.quantityEdit.setObjectName("quantityEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(44, 150, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 55, 16))
        self.label_4.setObjectName("label_4")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(110, 230, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.standartBox = QtWidgets.QComboBox(self.centralwidget)
        self.standartBox.setGeometry(QtCore.QRect(160, 190, 111, 22))
        self.standartBox.setObjectName("standartBox")
        self.standartBox.addItem("")
        self.standartBox.addItem("")
        self.designationEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.designationEdit.setGeometry(QtCore.QRect(160, 150, 113, 22))
        self.designationEdit.setObjectName("designationEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Quantity"))
        self.label_3.setText(_translate("MainWindow", "Designation"))
        self.label_4.setText(_translate("MainWindow", "Standart"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.standartBox.setItemText(0, _translate("MainWindow", "True"))
        self.standartBox.setItemText(1, _translate("MainWindow", "False"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())