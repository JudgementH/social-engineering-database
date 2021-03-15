#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 8:49

'后端入口'

__author__ = 'Judgement'

from flask import Flask, request, jsonify
from flask_cors import CORS

from database.qqgroup import query_qq_from_qqmember

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True, resources=r"/*")


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/query/qq', methods=['GET'])
def query_qq():
    """
    code = 0 参数不合法
    code = 1 正常返回
    """
    qq_num = str(request.args.get('qq'))
    if qq_num:
        res = query_qq_from_qqmember(qq_num)
        print(res)
        return_dict = {"code": '1', "res": str(res)}
        return jsonify(return_dict)
    return jsonify(code='0')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2333)
