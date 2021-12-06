from src.db import db
from src.utils import nlputils, fileutils, wordcloud_util


class ApiService:
    INSERT_SQL = "INSERT INTO `keys`(\
       `name`, `number`, `question`) \
       VALUES (%s,  %s,  %s) "

    LIST_SQL = "SELECT * FROM `keys` ORDER BY `id` DESC"

    def insert(self, value):
        r = db.save(self.INSERT_SQL, value)
        return r

    def list(self):
        db.query(self.LIST_SQL)
        return db.result()

    def get_wordcloud(self):
        tmp = ['''
     Generally speaking, long holidays are good for us college students. 
     On the one hand, we have a lot of time to study by ourselves 
     and thus improve weaknesses and further develop strengths. On the other hand, 
     we can take part-time jobs, which can make us realize responsibility and make ourselves better prepared for social life.''']
        wc = wordcloud_util.generate(tmp)
        return wordcloud_util.convert_img_to_b64(wc)

    def count(self, keys):
        """
            nlp 就是 经过自然语言处理后的 文字
        """
        keys = keys.split(",")
        print(keys)
        questions = self.list()
        for question in questions:
            nlp_result = nlputils.nlp(keys, question['question'])
            question['answer'] = nlp_result
        return questions

    def parse_file(self, path):
        data = fileutils.read_file(path)
        return db.save_many(self.INSERT_SQL, data)
