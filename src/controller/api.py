from flask import Blueprint, request, jsonify
from src.service.api_service import ApiService
import os


api = Blueprint("api", __name__, url_prefix='')

service = ApiService()

response = {
    'code': 200,
    'data': '',
    'msg': 'success'
}


@api.route('/insert',  methods=['post'])
def insert():
    body = request.json
    value = (body['key'], body['name'], int(body['number']), body['answer'])
    result = service.insert(value)
    response['data'] = result
    print(result)
    if(result):
        return jsonify(response)

    response['code'] = 400
    response['msg'] = 'error'
    return jsonify(response)


@api.route('/wordcloud', methods=['get'])
def wordcloud():
    return service.get_wordcloud().decode()


@api.route('/upload', methods=['post'])
def upload():
    if 'file' not in request.files:
        response['code'] = 400
        response['msg'] = '上传失败'
        return jsonify(response)
    file = request.files['file']
    if file.filename == '':
        response['code'] = 400
        response['msg'] = '文件出错'
        return jsonify(response)
    file.save(os.path.join('./tmp/', file.filename))

    return jsonify(response)



@api.route('/wordcloud', methods=['get'])
def count():
    return service.get_wordcloud().decode()
