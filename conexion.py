import sqlite3 as sql
class ConexionDB():
    def __init__(self,database):
        self.connect = sql.connect(database)
        self.cursor = self.connect.cursor()
    def db_close(self):
        self.connect.close()
    def request(self,request):
        self.cursor.execute(request)
    def commit(self):
        self.connect.commit()