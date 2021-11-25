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
from ClassForForm.csvClassforForm import *
from ClassForForm.ClassforAddCSVFileForm import *


class ClassforAddFileHandlerForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AddFileHandlerForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AddFileHandlerForm")
        self.ui.saveButton.clicked.connect(self.save)

    def save(self):
        name = self.ui.nameDEdit.text()
        code = self.ui.codeEdit.text()
        date = self.ui.dateTimeEdit.text()
        result = self.ui.resultBox.currentText()

        from DataMappers.FileHandlerMapper import FileHandler
        fileHandlerClass = FileHandler()
        fileHandlerClass.named = name
        fileHandlerClass.code = code
        fileHandlerClass.data = date
        fileHandlerClass.result = result

        fileHandlerClass.Create()

        # закрытие всех окон и открытие FileHandler обновленного
        QtWidgets.QMessageBox.about(self, "Предупреждение", "Запись сохранена в БД")
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        from ClassForForm.ClassforFileHandlerForm import ClassforFileHandlerForm
        self.FileHandler = ClassforFileHandlerForm()
        self.FileHandler.show()
        pass
    pass