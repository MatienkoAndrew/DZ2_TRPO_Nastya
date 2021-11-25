from contextlib import closing
import psycopg2


class CsvFile:
    def __init__(self):
        self.id = None
        self.name = None
        self.quantity = None
        self.designation = None
        self.standart = None

    def Create(self):
        return CsvFileMapper().Create(self)

    def Delete(self, id):
        return CsvFileMapper().Delete(id)

    def GetAll(self):
        return CsvFileMapper().GetAll()

    def GetById(self, id):
        return CsvFileMapper().GetById(id)

    def Update(self, id):
        return CsvFileMapper().Update(id, self)


class CsvFileMapper:
    def Create(self, CsvFile):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO csv_file (name, quantity, designation, standart)
                                    VALUES ('{CsvFile.name}', {CsvFile.quantity}, '{CsvFile.designation}', '{CsvFile.standart}')
                                """)
                conn.commit()
                pass
        return

    def Delete(self, id):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM csv_file WHERE id='{id}'")
                cursor.execute(f"DELETE FROM csv_to_fileh WHERE csvid='{id}'")
                conn.commit()
                pass
        return


    def GetAll(self):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" SELECT * FROM csv_file """)
                csvFileRows = cursor.fetchall()
        return csvFileRows


    def GetById(self, id):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" SELECT * FROM csv_file WHERE id={id}""")
                csvFileRow = cursor.fetchone()

                csvFileClass = CsvFile()
                csvFileClass.id = csvFileRow[0]
                csvFileClass.name = csvFileRow[1]
                csvFileClass.quantity = csvFileRow[2]
                csvFileClass.designation = csvFileRow[3]
                csvFileClass.standart = csvFileRow[4]
        return csvFileClass

    def Update(self, id, CsvFile):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" UPDATE csv_file 
                                    SET name='{CsvFile.name}',
                                        quantity={CsvFile.quantity},
                                        designation='{CsvFile.designation}',
                                        standart='{CsvFile.standart}'
                                    WHERE ID={id}
                                """)
                conn.commit()
        return
