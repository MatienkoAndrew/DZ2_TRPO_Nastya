from contextlib import closing
import psycopg2


class FileHandler:
    def __init__(self):
        self.id = None
        self.named = None
        self.code = None
        self.data = None
        self.result = None


class FileHandlerMapper:
    def Create(self, FileHandler):
        conn_string = "host='localhost' dbname='mydb' user='postgres' password='MAtienko9999'"
        with closing(psycopg2.connect(conn_string)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO FileHandler (named, code, data, result)
                                    VALUES ('{name}', {code}, '{date}', '{result}')
                                """)
                pass
        pass

    def Delete(self, id):
        pass

    def GetById(self, id):
        pass

    def Update(self, id, FileHandler):
        pass