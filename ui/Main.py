# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 221, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.fileHandler = QtWidgets.QPushButton(self.centralwidget)
        self.fileHandler.setGeometry(QtCore.QRect(90, 100, 251, 71))
        self.fileHandler.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.fileHandler.setObjectName("fileHandler")
        self.csvFile = QtWidgets.QPushButton(self.centralwidget)
        self.csvFile.setGeometry(QtCore.QRect(90, 190, 251, 81))
        self.csvFile.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.csvFile.setObjectName("csvFile")
        self.XlxFile = QtWidgets.QPushButton(self.centralwidget)
        self.XlxFile.setGeometry(QtCore.QRect(90, 290, 251, 81))
        self.XlxFile.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.XlxFile.setObjectName("XlxFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "???????????????? ??????????????"))
        self.fileHandler.setText(_translate("MainWindow", "???????????????????? ????????????"))
        self.csvFile.setText(_translate("MainWindow", "CSV-????????"))
        self.XlxFile.setText(_translate("MainWindow", "XLX-????????"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
