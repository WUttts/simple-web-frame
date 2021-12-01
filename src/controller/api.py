from flask import Blueprint,render_template,request
from src.service.test_service import TestService

api = Blueprint("api", __name__, url_prefix='')



# 测试页面  
@api.route('/index')
def hello():
    name = request.args.get("name")
    result = TestService().test()
    return render_template("test.html",name=name,result=result)


@api.route('/subKeys')
def subKeys():
    pass


