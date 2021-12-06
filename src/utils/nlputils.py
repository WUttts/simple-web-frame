# 你可以在这里写你的 自然语言处理代码，下面是一个示例

def nlp(keys, question):
    """
    这里只是简单的替换，将问题里的关键字加了个颜色
    """
    question = str(question)
    for key in keys:
        befor = renderStr(str(key))
        print(befor)
        q = question.replace(str(key), befor)
        print(q)

    return q



def renderStr(key):
    _key = str(key)
    return """<span style="color: darkorange;">{key}</span>""".format(key=_key)
