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
from ClassForForm.ClassforAddFileHandlerForm import *


from ClassForForm.ClassforAddXlxFileForm import ClassforAddXlxFileForm


##-- Главное окно
class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Main()
        # self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainForm")
        self.ui.csvFile.clicked.connect(self.toCsvForm)
        self.ui.XlxFile.clicked.connect(self.toXLXForm)
        self.ui.fileHandler.clicked.connect(self.toFileHandlerForm)

    def toCsvForm(self):
        from ClassForForm.ClassforXLXForm import csvClassforForm
        self.csvForm = csvClassforForm()
        self.csvForm.show()
        self.close()
        pass

    def toXLXForm(self):
        from ClassForForm.ClassforXLXForm import ClassforXLXForm
        self.xlxForm = ClassforXLXForm()
        self.xlxForm.show()
        self.close()
        pass

    def toFileHandlerForm(self):
        from ClassForForm.ClassforFileHandlerForm import ClassforFileHandlerForm
        self.handlerForm = ClassforFileHandlerForm()
        self.handlerForm.show()
        self.close()
        pass
