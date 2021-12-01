from src.db import db
from src.utils import wordcloud_util

class ApiService:
    INSERT_SQL = "INSERT INTO `keys`(`key`, \
       `name`, `number`, `answer`) \
       VALUES ('%s', '%s',  %s,  '%s') \ "

    def insert(self,value):
        self.INSERT_SQL % value
        return db.save(self.INSERT_SQL) 

    def get_wordcloud(self):
        tmp = ['''
     Generally speaking, long holidays are good for us college students. 
     On the one hand, we have a lot of time to study by ourselves 
     and thus improve weaknesses and further develop strengths. On the other hand, 
     we can take part-time jobs, which can make us realize responsibility and make ourselves better prepared for social life.''']
        wc = wordcloud_util.generate(tmp)
        return wordcloud_util.convert_img_to_b64(wc)


