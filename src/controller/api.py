from flask import Blueprint, request, jsonify
from src.service.api_service import ApiService


api = Blueprint("api", __name__, url_prefix='')


@api.route('/insert',  methods=['post'])
def sub_keys():
    key = request.form["key"]
    name = request.form["name"]
    number = request.form["number"]
    text = request.form["text"]
    if not all([key, name, number, text]):
        return jsonify(code=400, message="missing parameter")
    service = ApiService()
    value = (key, name, number, text)
    result = service.insert(value)
    if result:
        return jsonify(code=200, message="ok!")
    return jsonify(code=400, message="missing parameter")
