from contextlib import closing
import psycopg2


class FileHandler:
    def __init__(self):
        self.id = None
        self.named = None
        self.code = None
        self.data = None
        self.result = None

    def Create(self):
        return FileHandlerMapper().Create(self)

    def Delete(self, id):
        return FileHandlerMapper().Delete(id)

    def GetAll(self):
        return FileHandlerMapper().GetAll()

    def GetById(self, id):
        return FileHandlerMapper().GetById(id)

    def Update(self, id):
        return FileHandlerMapper().Update(id, self)


class FileHandlerMapper:
    def Create(self, FileHandler):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO FileHandler (named, code, data, result)
                                    VALUES ('{FileHandler.named}', {FileHandler.code}, '{FileHandler.data}', '{FileHandler.result}')
                                """)
                conn.commit()
                pass
        return

    def Delete(self, id):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(f"DELETE FROM xlx_file WHERE idhand='{id}'")
                    cursor.execute(f"DELETE FROM csv_to_fileh WHERE handid='{id}'")
                    cursor.execute(f"""DELETE FROM FileHandler WHERE id={id}""")
                except Exception as e:
                    cursor.execute(f"DELETE FROM FileHandler WHERE ID='{id}'")
                conn.commit()
                pass
        return


    def GetAll(self):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" SELECT * FROM FileHandler """)
                fileHandlerRows = cursor.fetchall()
        return fileHandlerRows


    def GetById(self, id):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" SELECT * FROM FileHandler WHERE id={id}""")
                fileHandlerRow = cursor.fetchone()

                fileHandlerClass = FileHandler()
                fileHandlerClass.id = fileHandlerRow[0]
                fileHandlerClass.named = fileHandlerRow[1]
                fileHandlerClass.code = fileHandlerRow[2]
                fileHandlerClass.data = fileHandlerRow[3]
                fileHandlerClass.result = fileHandlerRow[4]
        return fileHandlerClass

    def Update(self, id, FileHandler):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f""" UPDATE FileHandler 
                                    SET named='{FileHandler.named}',
                                        Code={FileHandler.code},
                                        Data='{FileHandler.data}',
                                        result={FileHandler.result}
                                    WHERE ID={id}
                                """)
                # FileHandler.id = id
                conn.commit()
        return
        # return FileHandler
