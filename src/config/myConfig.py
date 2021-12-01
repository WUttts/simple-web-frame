import os


class Dev:
    # 待添加数据源配置

    # 通用配置
    SECRET_KEY = 'ac#$ds8911'
    CSRF_ENABLED = True
    WHOOSH_PATH = os.path.join(os.getcwd(), 'whoosh_indexes')
    WTF_CSRF_ENABLED = False

    # redis 配置待定
    # USE_CACHE = True
    # CACHE_TYPE = 'redis'
    # CACHE_REDIS_HOST = '127.0.0.1'
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_PASSWORD = ''
    # CACHE_REDIS_DB = '0'


class Pro:
    pass


config = {
    "Dev": Dev,
    "Pro": Pro
}
