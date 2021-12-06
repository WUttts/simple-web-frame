from flask import Blueprint, json, request, jsonify
from src.service.api_service import ApiService
import uuid
import os


api = Blueprint("api", __name__, url_prefix='')

service = ApiService()

response = {
    'code': 200,
    'data': '',
    'msg': 'success'
}


TMP_PATH = './tmp/'

@api.route('/insert',  methods=['post'])
def insert():
    body = request.json
    value = (body['name'], int(body['number']), body['question'])
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


@api.route('/list', methods=['get'])
def list():
    response['data'] = service.list()
    return jsonify(response)


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
    filename = str(uuid.uuid1()) + file.filename
    file.save(os.path.join(TMP_PATH,filename) )

    service.parse_file(TMP_PATH+filename)
    
    response['data'] = file.filename
    response['msg'] = '上传成功'
    return jsonify(response)


@api.route('/count', methods=['post'])
def count():
    body = request.json
    keys = body['keys']
    data = service.count(keys)
    response['data'] = data
    return jsonify(response)
