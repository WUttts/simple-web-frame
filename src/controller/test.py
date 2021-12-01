from flask import Blueprint,render_template

test = Blueprint("test", __name__, url_prefix='')


@test.route('/')
def test_hello():
    return '<h1>hello</h1>'

@test.route('/index')
def hello():
    return render_template("index.html")
