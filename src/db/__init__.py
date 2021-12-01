import pymysql
import threading
from DBUtils.PooledDB import PooledDB


class DB:
    _instance_lock = threading.Lock()
    HOST = '127.0.0.1'
    PORT = 3306
    USER = 'root'
    # PASSWORD='wtp164614'
    PASSWORD = '356615'
    DATABSE = 'my_project'

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
            host=self.HOST,
            port=self.PORT,
            user=self.USER,
            password=self.PASSWORD,
            database=self.DATABSE,
            charset='utf8'
        )
        self.__result = []

    # 插入多条数据
    def save(self, sql):
        """
        :param sql:
        :param param: 单个插入
        :return:
        """
        conn = self.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
            _id = cursor.lastrowid
            if _id == 0:
                return True
            return _id
        except Exception as e:
            conn.rollback()
            print('insert except'+str(e.args))
        finally:
            cursor.close()
            conn.close()

    # 插入多条数据
    def save_many(self, sql, params):
        """
        :param sql:
        :param param: 必须是元组或列表[(),()]或（（），（））
        :return:
        """
        conn = self.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, (params))
            conn.commit()
            _id = cursor.lastrowid
            if _id == 0:
                return True
            return _id
        except Exception as e:
            conn.rollback()
            print('insert except'+str(e.args))
        finally:
            cursor.close()
            conn.close()

    def query(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            col_info = [tuple[0] for tuple in cursor.description]
            self.__process_result(col_info, data)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def __process_result(self, col_info, data):
        result_map = {}
        for row in data:
            i = 0
            for field in col_info:
                result_map[field] = row[i]
                i = i + 1
            self.__result.append(result_map)

    def result(self):
        return self.__result


db = DB()
if __name__ == '__main__':
    INSERT_SQL = "INSERT INTO `keys` (`key`, `name`, `number`, `answer`) VALUES( %s, %s, %s, %s )"
    values = (("sasa", "wts", 1, "sasasasacsfeg"),
              ("sasa", "wts", 1, "sasasasacsfeg"))
    db.save(INSERT_SQL, values)
