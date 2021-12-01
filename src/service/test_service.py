from src.db import DB

class TestService:
    def __init__(self) -> None:
        self.db = DB()
    

    def test(self):
        sql = "select * from test"
        self.db.execute(sql)
        return self.db.result()
