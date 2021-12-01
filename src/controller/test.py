from flask import Blueprint,render_template,request

test = Blueprint("test", __name__, url_prefix='')


@test.route('/')
def test_hello():
    return '<h1>hello</h1>'

# 测试页面  
@test.route('/index')
def hello():
    name = request.args.get("name")
    return render_template("index.html",name=name)
