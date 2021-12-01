from src.db import db

class ApiService:
    INSERT_SQL = '''INSERT INTO keys ( key, name, number, answer ) 
    VALUES( %s, %s, %s, %s )'''

    def insert(self,value):
        values =(value)
        return db.save(self.INSERT_SQL,values) 

