import pymysql
import threading
from loguru import logger
from DBUtils.PooledDB import PooledDB


class DB:
    _instance_lock = threading.Lock()

    QUERY = "SELECT"
    WHERE = "WHERE"
    UPDATE = "UPDATE"
    SET = "SET"
    FROM = "FROM"

    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=10,
            mincached=2,
            maxcached=5,
            maxshared=3,
            blocking=True,
            maxusage=None,
            setsession=[], 
            ping=0,
            host='127.0.0.1',
            port=3306,
            user='root',
            password='356615',
            database='my_project',
            charset='utf8'
        )
        self.__result = []

    def execute(self,sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            col_info = [tuple[0] for tuple in cursor.description]
            self.process_result(col_info,data)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def process_result(self,col_info,data):
        result_map = {}
        for row in data:
            i = 0
            for field in col_info:
                result_map[field] = row[i]
                i = i + 1
            self.__result.append(result_map)

    def result(self):
        return self.__result

