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


from ClassForForm.ClassforFileHandlerForm import *
from ClassForForm.ClassforAddXlxFileForm import *
from ClassForForm.csvClassforForm import *
from ClassForForm.ClassforAddCSVFileForm import *
from ClassForForm.ClassforAddFileHandlerForm import *
from ui.UpdateXlxFileForm import UpdateXlxFileForm


class ClassforUpdateXlxFileForm(QtWidgets.QMainWindow):
    def __init__(self, idx: int, parent=None):
        super().__init__(parent)
        self.ui = UpdateXlxFileForm()
        self.ui.setupUi(self)
        self.idx=idx
        self.initUI()

    def initUI(self):
        self.setWindowTitle("UpdateXlxFileForm")

        from DataMappers.XlxFileMapper import XlxFile
        self.XlxFileClass = XlxFile().GetById(self.idx)
        self.ui.nameEdit.setText(str(self.XlxFileClass.name))
        self.ui.quantityEdit.setText(str(self.XlxFileClass.quantity))
        self.ui.typeEdit.setText(str(self.XlxFileClass.type))
        self.ui.standartBox.setItemText(2, str(self.XlxFileClass.standart))
        self.ui.designationEdit.setText(str(self.XlxFileClass.designation))
        self.ui.idHandEdit.setText(str(self.XlxFileClass.idhand))

        self.ui.saveButton.clicked.connect(self.save)
        pass

    def save(self):
        self.XlxFileClass.name = self.ui.nameEdit.text()
        self.XlxFileClass.quantity = self.ui.quantityEdit.text()
        self.XlxFileClass.type = self.ui.typeEdit.text()
        self.XlxFileClass.standart = self.ui.standartBox.currentText()
        self.XlxFileClass.designation = self.ui.designationEdit.text()
        self.XlxFileClass.idhand = self.ui.idHandEdit.text()

        try:
            self.XlxFileClass.Update(self.idx)
        except:
            QtWidgets.QMessageBox.about(self, "Title", 'ОШИБКА:  INSERT или UPDATE в таблице "xlx_file" нарушает ограничение внешнего ключа "xlx_file_idhand_fkey"')

        # закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.XlxFile = ClassforXLXForm()
        self.XlxFile.show()



class ClassforXLXForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = XLXForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("XLXForm")
        self.connect()
        self.ui.addButton.clicked.connect(self.openAddForm)
        self.ui.back.clicked.connect(self.back)

    def connect(self):
        from DataMappers.XlxFileMapper import XlxFile
        XlxFileClass = XlxFile()
        rows = XlxFileClass.GetAll()

        self.ui.tableWidget.setRowCount(len(rows))
        tablerow = 0
        for row in rows:
            print(row)
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))

            # добавление кнопок "Удалить"
            self.btn = QtWidgets.QPushButton(self.ui.centralwidget)
            self.btn.setObjectName(f'{row[0]}')
            self.btn.setText("Удалить")
            self.ui.tableWidget.setCellWidget(tablerow, 7, self.btn)
            self.btn.clicked.connect(self.del_row)

            # кнопка изменить
            self.update_btn = QtWidgets.QPushButton(self.ui.centralwidget)
            self.update_btn.setObjectName(f'{row[0]}')
            self.update_btn.setText("Изменить")
            self.ui.tableWidget.setCellWidget(tablerow, 8, self.update_btn)
            self.update_btn.clicked.connect(self.update_row)
            tablerow += 1
            pass
        pass

    def del_row(self):
        clicked_btn = self.sender()
        idx = clicked_btn.objectName()
        print(f"DELETE {idx} button")

        from DataMappers.XlxFileMapper import XlxFile
        XlxFileClass = XlxFile()
        XlxFileClass.Delete(idx)

        # закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.XlxForm = ClassforXLXForm()
        self.XlxForm.show()

        pass

    def openAddForm(self):
        from ClassForForm.ClassforAddXlxFileForm import ClassforAddXlxFileForm
        self.AddFormforXlx = ClassforAddXlxFileForm()
        self.AddFormforXlx.show()

    def update_row(self):
        clicked_btn = self.sender()
        idx = int(clicked_btn.objectName())

        self.UpdateForm = ClassforUpdateXlxFileForm(idx)
        self.UpdateForm.show()
        pass

    def back(self):
        from ClassForForm.MainForm import MainForm
        self.MainForm = MainForm()
        self.MainForm.show()
        self.close()
    pass