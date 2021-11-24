from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui
import psycopg2
from ui.CSVFileForm import CSVFileForm
from ui.Main import Main
from ui.FileHandlerForm import FileHandlerForm
from ui.XLXForm import XLXForm
from ui.AddFileHandlerForm import AddFileHandlerForm
from ui.AddCsvFileForm import AddCsvFileForm
from ui.AddXlxFileForm import AddXlxFileForm
from contextlib import closing



##-- Форма добавления записей в XLX-file
class ClassforAddXlxFileForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = AddXlxFileForm()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ClassforAddXlxFileForm")
        self.ui.saveButton.clicked.connect(self.save)

    def save(self):
        name = self.ui.nameEdit.text()
        quantity = self.ui.quantityEdit.text()
        type = self.ui.typeEdit.text()
        standart = self.ui.standartBox.currentText()
        designation = self.ui.designationEdit.text()
        idhand = self.ui.idHandEdit.text()

        ##-- сохранение в БД
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(f"""INSERT INTO xlx_file (name, quantity, type, standart, designation, idhand)
                                        VALUES ('{name}', {quantity}, '{type}', '{standart}', '{designation}', {idhand})
                                    """)
                    conn.commit()

                    ##-- закрытие всех окон и открытие FileHandler обновленного
                    QtWidgets.QMessageBox.about(self, "Предупреждение", "Запись сохранена в БД")
                    app = QtGui.QGuiApplication.instance()
                    app.closeAllWindows()

                    self.XlxFileForm = ClassforXLXForm()
                    self.XlxFileForm.show()
                except Exception:
                    QtWidgets.QMessageBox.about(self, "Предупреждение", "Нет такого FileHandler")

        pass
    pass



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
        self.ui.changeButton.clicked.connect(self.change)

    def connect(self):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM xlx_file")
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
                    self.ui.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.ui.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))

                    ##-- добавление кнопок "Удалить"
                    self.btn = QtWidgets.QPushButton(self.ui.centralwidget)
                    self.btn.setObjectName(f'{row[0]}')
                    self.btn.setText("Удалить")
                    self.ui.tableWidget.setCellWidget(tablerow, 7, self.btn)
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
                cursor.execute(f"DELETE FROM xlx_file WHERE idx='{click_btn_obj_name}'")
                conn.commit()
                pass
            pass

        ##-- закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.XlxForm = ClassforXLXForm()
        self.XlxForm.show()

        pass

    def openAddForm(self):
        self.AddFormforXlx = ClassforAddXlxFileForm()
        self.AddFormforXlx.show()

    def change(self):

        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                for row in range(self.ui.tableWidget.rowCount()):
                    cursor.execute(f"""
                    UPDATE xlx_file 
                    SET name='{self.ui.tableWidget.item(row, 1).text()}',
                        quantity='{self.ui.tableWidget.item(row, 2).text()}',
                        type='{self.ui.tableWidget.item(row, 3).text()}',
                        standart={self.ui.tableWidget.item(row, 4).text()},
                        designation='{self.ui.tableWidget.item(row, 5).text()}',
                        idhand={self.ui.tableWidget.item(row, 6).text()}
                    WHERE IDX={self.ui.tableWidget.item(row, 0).text()}
                    """)
                conn.commit()
        # ##-- закрытие всех окон и открытие FileHandler обновленного
        # app = QtGui.QGuiApplication.instance()
        # app.closeAllWindows()
        # self.FileHandler = ClassforFileHandlerForm()
        # self.FileHandler.show()
        pass
    pass


##-- Форма добавления записей в CSV-file
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

        self.CsvFileForm = csvClassforForm()
        self.CsvFileForm.show()
        pass
    pass



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
    pass






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

        ##-- сохранение в БД
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO FileHandler (named, code, data, result)
                                    VALUES ('{name}', {code}, '{date}', '{result}')
                                """)
                conn.commit()

        ##-- закрытие всех окон и открытие FileHandler обновленного
        QtWidgets.QMessageBox.about(self, "Предупреждение", "Запись сохранена в БД")
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.FileHandler = ClassforFileHandlerForm()
        self.FileHandler.show()
        pass
    pass




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
        self.ui.changeButton.clicked.connect(self.change)
        pass

    def connect(self):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM filehandler")
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
                try:
                    cursor.execute(f"DELETE FROM xlx_file WHERE idhand='{click_btn_obj_name}'")
                    cursor.execute(f"DELETE FROM FileHandler WHERE ID='{click_btn_obj_name}'")
                    cursor.execute(f"DELETE FROM csv_to_fileh WHERE handid='{click_btn_obj_name}'")
                except Exception as e:
                    cursor.execute(f"DELETE FROM FileHandler WHERE ID='{click_btn_obj_name}'")
                conn.commit()
                pass
            pass

        ##-- закрытие всех окон и открытие FileHandler обновленного
        app = QtGui.QGuiApplication.instance()
        app.closeAllWindows()

        self.FileHandler = ClassforFileHandlerForm()
        self.FileHandler.show()

        pass

    def openAddForm(self):
        self.AddForm = ClassforAddFileHandlerForm()
        self.AddForm.show()

    def change(self):

        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                for row in range(self.ui.tableWidget.rowCount()):
                    cursor.execute(f"""
                    UPDATE FileHandler 
                    SET named='{self.ui.tableWidget.item(row, 1).text()}',
                        Code={self.ui.tableWidget.item(row, 2).text()},
                        Data='{self.ui.tableWidget.item(row, 3).text()}',
                        result={self.ui.tableWidget.item(row, 4).text()}
                    WHERE ID={self.ui.tableWidget.item(row, 0).text()}
                    """)
                conn.commit()
        # ##-- закрытие всех окон и открытие FileHandler обновленного
        # app = QtGui.QGuiApplication.instance()
        # app.closeAllWindows()
        # self.FileHandler = ClassforFileHandlerForm()
        # self.FileHandler.show()
        pass
    pass


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
        self.csvForm = csvClassforForm()
        self.csvForm.show()
        pass

    def toXLXForm(self):
        self.xlxForm = ClassforXLXForm()
        self.xlxForm.show()
        pass

    def toFileHandlerForm(self):
        self.handlerForm = ClassforFileHandlerForm()
        self.handlerForm.show()
        pass



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())
