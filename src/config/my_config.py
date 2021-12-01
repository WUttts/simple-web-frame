import os


class Dev:
    # 待添加数据源配置
    

    # 通用配置
    SECRET_KEY = 'ac#$ds8911'
    CSRF_ENABLED = True
    WHOOSH_PATH = os.path.join(os.getcwd(), 'whoosh_indexes')
    WTF_CSRF_ENABLED = False


class Pro:
    pass


config = {
    "Dev": Dev,
    "Pro": Pro
}
