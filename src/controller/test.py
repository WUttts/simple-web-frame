from flask import Blueprint

test = Blueprint("test", __name__, url_prefix='')


@test.route('/')
def test_hello():
    return 'hello test'

@test.route('/hello')
def hello():
    return 'hello'
