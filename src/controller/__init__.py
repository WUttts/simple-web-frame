from .test import test

# 蓝图映射
DEFAULT_BLUEPRINT = (
    # (蓝图，前缀)
    (test, '/test'),
    
)


# 封装蓝图
def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)