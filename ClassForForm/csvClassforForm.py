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


from ClassForForm.ClassforXLXForm import *
from ClassForForm.ClassforFileHandlerForm import *
from ClassForForm.ClassforAddXlxFileForm import *
from ClassForForm.ClassforAddCSVFileForm import *
from ClassForForm.ClassforAddFileHandlerForm import *
from ui.UpdateCsvFileForm import UpdateCsvFileForm


class ClassforUpdateCsvFileForm(QtWidgets.QMainWindow):
    def __init__(self, id: int, parent=None):
        super().__init__(parent)
        self.ui = UpdateCsvFileForm()
        self.ui.setupUi(self)
        self.id=id
        self.initUI()

    def initUI(self):
        self.setWindowTitle("UpdateCsvFileForm")

        from DataMappers.CsvFileMapper import CsvFile
        self.CsvFileClass = CsvFile().GetById(self.id)
        self.ui.nameEdit.setText(str(self.CsvFileClass.name))
        self.ui.quantityEdit.setText(str(self.CsvFileClass.quantity))
        self.ui.designationEdit.setText(self.CsvFileClass.designation)
        self.ui.standartBox.setItemText(2, str(self.CsvFileClass.standart))

        self.ui.saveButton.clicked.connect(self.save)
        pass

    def save(self):
        self.CsvFileClass.name = self.ui.nameEdit.text()
        self.CsvFileClass.quantity = self.ui.quantityEdit.text()
        self.CsvFileClass.designation = self.ui.designationEdit.text()
        self.CsvFileClass.standart = self.ui.standartBox.currentText()

        self.CsvFileClass.Update(self.id)

        # закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.CsvForm = csvClassforForm()
        self.CsvForm.show()



class csvClassforForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = CSVFileForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CSVFileForm")
        self.connect()
        self.ui.addButton.clicked.connect(self.openAddForm)
        self.ui.back.clicked.connect(self.back)
        pass

    def connect(self):
        from DataMappers.CsvFileMapper import CsvFile
        CsvFileClass = CsvFile()
        rows = CsvFileClass.GetAll()

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
        # print(f"DELETE {id} button")

        from DataMappers.CsvFileMapper import CsvFile
        CsvFileClass = CsvFile()
        CsvFileClass.Delete(id)

        ##-- закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.csvFileForm = csvClassforForm()
        self.csvFileForm.show()

        pass

    def openAddForm(self):
        self.AddFormforCSV = ClassforAddCSVFileForm()
        self.AddFormforCSV.show()


    def update_row(self):
        clicked_btn = self.sender()
        id = int(clicked_btn.objectName())
        print(f"UPDATE {id} button")

        self.UpdateForm = ClassforUpdateCsvFileForm(id)
        self.UpdateForm.show()
        pass

    def back(self):
        from ClassForForm.MainForm import MainForm
        self.MainForm = MainForm()
        self.MainForm.show()
        self.close()
    pass
