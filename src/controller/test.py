from flask import Blueprint,render_template,request
from src.service.test_service import TestService

test = Blueprint("test", __name__, url_prefix='')


@test.route('/')
def test_hello():
    return '<h1>hello</h1>'

# 测试页面  
@test.route('/index')
def hello():
    name = request.args.get("name")
    result = TestService().test()
    return render_template("test.html",name=name,result=result)
