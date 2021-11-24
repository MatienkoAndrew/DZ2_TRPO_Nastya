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
from ClassForForm.ClassforAddFileHandlerForm import *



class ClassforAddCSVFileForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AddCsvFileForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ClassforAddCSVFileForm")
        self.ui.saveButton.clicked.connect(self.save)

    def save(self):
        name = self.ui.nameEdit.text()
        quantity = self.ui.quantityEdit.text()
        designation = self.ui.designationEdit.text()
        standart = self.ui.standartBox.currentText()

        ##-- сохранение в БД
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO csv_file (name, quantity, designation, standart)
                                    VALUES ('{name}', {quantity}, '{designation}', '{standart}')
                                """)
                conn.commit()

        ##-- закрытие всех окон и открытие FileHandler обновленного
        QtWidgets.QMessageBox.about(self, "Предупреждение", "Запись сохранена в БД")
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        from ClassForForm.csvClassforForm import csvClassforForm
        self.CsvFileForm = csvClassforForm()
        self.CsvFileForm.show()
        pass
    pass