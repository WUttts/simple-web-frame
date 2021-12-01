from flask import Flask
from src.config.my_config import config
from src.controller import config_blueprint
from src.db import DB


def app_run(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config_blueprint(app)
    print('================主程序已启动  ^_^!!===================')
    return app
