from flask import Blueprint, render_template, request, jsonify
from src.service.test_service import TestService
from src.db import DB

api = Blueprint("api", __name__, url_prefix='')




# 测试页面  
@api.route('/index')
def hello():
    # name = request.args.get("name")
    # result = TestService().test()
    return render_template("index.html")


@api.route('/subKeys',  methods=['post'])
def sub_keys():
    key = request.form["key"]
    name = request.form["name"]
    number = request.form["number"]
    text = request.form["text"]
    if not all([key, name, number, text]):
        return jsonify(code=400, message="missing parameter")
    sql = 'INSERT INTO keys ( key, name, number, answer ) VALUES( key, name, number, text )'
    DB().save()
    return jsonify(code=200, message="ok!")


