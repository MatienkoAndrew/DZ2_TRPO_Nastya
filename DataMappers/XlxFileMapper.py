from contextlib import closing
import psycopg2


class XlxFile:
    def __init__(self):
        self.idx = None
        self.name = None
        self.quantity = None
        self.type = None
        self.standart = None
        self.designation = None
        self.idhand = None

    def Create(self):
        return XlxFileMapper().Create(self)

    def Delete(self, id):
        return XlxFileMapper().Delete(id)

    def GetAll(self):
        return XlxFileMapper().GetAll()

    def GetById(self, id):
        return XlxFileMapper().GetById(id)

    def Update(self, id):
        return XlxFileMapper().Update(id, self)


class XlxFileMapper:
    def Create(self, XlxFile):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO Xlx_file (name, quantity, type, standart, designation, idhand)
                                    VALUES ('{XlxFile.name}', {XlxFile.quantity}, '{XlxFile.type}', '{XlxFile.standart}', 
                                    '{XlxFile.designation}', {XlxFile.idhand})
                                """)
                conn.commit()
                pass
        return

    def Delete(self, id):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM Xlx_file WHERE idx='{id}'")
                conn.commit()
                pass
        return


    def GetAll(self):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" SELECT * FROM Xlx_file """)
                XlxFileRows = cursor.fetchall()
        return XlxFileRows


    def GetById(self, id):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" SELECT * FROM Xlx_file WHERE idx={id}""")
                XlxFileRows = cursor.fetchone()

                XlxFileClass = XlxFile()
                XlxFileClass.idx = XlxFileRows[0]
                XlxFileClass.name = XlxFileRows[1]
                XlxFileClass.quantity = XlxFileRows[2]
                XlxFileClass.type = XlxFileRows[3]
                XlxFileClass.standart = XlxFileRows[4]
                XlxFileClass.designation = XlxFileRows[5]
                XlxFileClass.idhand = XlxFileRows[6]
        return XlxFileClass

    def Update(self, id, XlxFile):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" UPDATE Xlx_file 
                                    SET name='{XlxFile.name}',
                                        quantity={XlxFile.quantity},
                                        type='{XlxFile.type}',
                                        standart='{XlxFile.standart}',
                                        designation='{XlxFile.designation}',
                                        idhand={XlxFile.idhand}
                                    WHERE idx={id}
                                """)
                conn.commit()
        return
