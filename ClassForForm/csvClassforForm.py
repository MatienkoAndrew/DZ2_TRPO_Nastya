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
        self.ui.changeButton.clicked.connect(self.change)
        self.ui.back.clicked.connect(self.back)
        pass

    def connect(self):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM csv_file")
                rows = cursor.fetchall()

                self.ui.tableWidget.setRowCount(len(rows))
                tablerow = 0
                for row in rows:
                    print(row)
                    self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

                    self.btn = QtWidgets.QPushButton(self.ui.centralwidget)
                    self.btn.setObjectName(f'{row[0]}')
                    self.btn.setText("Удалить")
                    self.ui.tableWidget.setCellWidget(tablerow, 5, self.btn)
                    self.btn.clicked.connect(self.del_row)
                    tablerow += 1
                    pass
                pass
            pass
        pass

    def del_row(self):
        clicked_btn = self.sender()
        click_btn_obj_name = clicked_btn.objectName()
        print(f"DELETE {click_btn_obj_name} button")

        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM csv_file WHERE id='{click_btn_obj_name}'")
                cursor.execute(f"DELETE FROM csv_to_fileh WHERE csvid='{click_btn_obj_name}'")
                conn.commit()
                pass
            pass

        ##-- закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.csvFileForm = csvClassforForm()
        self.csvFileForm.show()

        pass

    def openAddForm(self):
        self.AddFormforCSV = ClassforAddCSVFileForm()
        self.AddFormforCSV.show()

    def change(self):

        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                for row in range(self.ui.tableWidget.rowCount()):
                    cursor.execute(f"""
                    UPDATE csv_file 
                    SET name='{self.ui.tableWidget.item(row, 1).text()}',
                        quantity={self.ui.tableWidget.item(row, 2).text()},
                        designation='{self.ui.tableWidget.item(row, 3).text()}',
                        standart={self.ui.tableWidget.item(row, 4).text()}
                    WHERE ID={self.ui.tableWidget.item(row, 0).text()}
                    """)
                conn.commit()
        # ##-- закрытие всех окон и открытие FileHandler обновленного
        # app = QtGui.QGuiApplication.instance()
        # app.closeAllWindows()
        # self.FileHandler = ClassforFileHandlerForm()
        # self.FileHandler.show()
        pass

    def back(self):
        from ClassForForm.MainForm import MainForm
        self.MainForm = MainForm()
        self.MainForm.show()
        self.close()
    pass
