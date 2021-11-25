from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui
from ui.CSVFileForm import CSVFileForm
from ui.Main import Main
from ui.FileHandlerForm import FileHandlerForm
from ui.XLXForm import XLXForm
from ui.AddFileHandlerForm import AddFileHandlerForm
from ui.AddCsvFileForm import AddCsvFileForm
from ui.AddXlxFileForm import AddXlxFileForm
from contextlib import closing
import psycopg2

from ClassForForm.MainForm import MainForm
from ClassForForm.ClassforXLXForm import *
from ClassForForm.ClassforAddXlxFileForm import *
from ClassForForm.csvClassforForm import *
from ClassForForm.ClassforAddCSVFileForm import *
from ClassForForm.ClassforAddFileHandlerForm import *
from ui.UpdateFileHandlerForm import UpdateFileHandlerForm


class ClassforUpdateFileHandlerForm(QtWidgets.QMainWindow):
    def __init__(self, id: int, parent=None):
        super().__init__(parent)
        self.ui = UpdateFileHandlerForm()
        self.ui.setupUi(self)
        self.id=id
        self.initUI()

    def initUI(self):
        self.setWindowTitle("UpdateFileHandlerForm")

        from DataMappers.FileHandlerMapper import FileHandler
        self.FileHandlerClass = FileHandler()
        self.FileHandlerClass = self.FileHandlerClass.GetById(self.id)
        self.ui.nameDEdit.setText(str(self.FileHandlerClass.named))
        self.ui.codeEdit.setText(str(self.FileHandlerClass.code))
        self.ui.dateTimeEdit.setDateTime(self.FileHandlerClass.data)
        self.ui.resultBox.setItemText(2, str(self.FileHandlerClass.result))

        self.ui.saveButton.clicked.connect(self.save)
        pass

    def save(self):
        self.FileHandlerClass.named = self.ui.nameDEdit.text()
        self.FileHandlerClass.code = self.ui.codeEdit.text()
        self.FileHandlerClass.data = self.ui.dateTimeEdit.text()
        self.FileHandlerClass.result = self.ui.resultBox.currentText()

        self.FileHandlerClass.Update(self.id)

        # закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.FileHandler = ClassforFileHandlerForm()
        self.FileHandler.show()


# Класс для взаимодействия с интерфейсом (окном FileHandler)
class ClassforFileHandlerForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = FileHandlerForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FileHandlerForm")
        self.connect()
        self.ui.addButton.clicked.connect(self.openAddForm)
        self.ui.back.clicked.connect(self.back)
        pass

    def connect(self):
        from DataMappers.FileHandlerMapper import FileHandler
        FileHandlerClass = FileHandler()
        rows = FileHandlerClass.GetAll()

        self.ui.tableWidget.setRowCount(len(rows))
        tablerow = 0
        for row in rows:
            print(row)
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            # кнопка удалить
            self.btn = QtWidgets.QPushButton(self.ui.centralwidget)
            self.btn.setObjectName(f'{row[0]}')
            self.btn.setText("Удалить")
            self.ui.tableWidget.setCellWidget(tablerow, 5, self.btn)
            self.btn.clicked.connect(self.del_row)

            # кнопка изменить
            self.update_btn = QtWidgets.QPushButton(self.ui.centralwidget)
            self.update_btn.setObjectName(f'{row[0]}')
            self.update_btn.setText("Изменить")
            self.ui.tableWidget.setCellWidget(tablerow, 6, self.update_btn)
            self.update_btn.clicked.connect(self.update_row)
            tablerow += 1
            pass
        pass

    def del_row(self):
        clicked_btn = self.sender()
        id = clicked_btn.objectName()
        # print(f"DELETE {click_btn_obj_name} button")

        from DataMappers.FileHandlerMapper import FileHandler
        FileHandlerClass = FileHandler()
        FileHandlerClass.Delete(id)

        # закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.FileHandler = ClassforFileHandlerForm()
        self.FileHandler.show()

        pass

    def openAddForm(self):
        self.AddForm = ClassforAddFileHandlerForm()
        self.AddForm.show()
        pass

    def update_row(self):
        clicked_btn = self.sender()
        id = int(clicked_btn.objectName())
        # print(f"UPDATE {id} button")

        self.UpdateForm = ClassforUpdateFileHandlerForm(id)
        self.UpdateForm.show()
        pass

    def back(self):
        self.MainForm = MainForm()
        self.MainForm.show()
        self.close()
        pass
    pass