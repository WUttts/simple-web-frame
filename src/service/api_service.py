from src.db import db

class ApiService:
    INSERT_SQL = "INSERT INTO `keys`(`key`, \
       `name`, `number`, `answer`) \
       VALUES ('%s', '%s',  %s,  '%s')"

    def insert(self,value):
        self.INSERT_SQL % value
        return db.save(self.INSERT_SQL) 

