#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 8:49

'后端入口'

__author__ = 'Judgement'

from flask import Flask, request, jsonify
from flask_cors import CORS

from database.qqgroup import query_qq_from_qqmember, query_qun_from_qqmember, query_relation_from_qqmember

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
    qq_num = str(request.args.get('num'))
    if qq_num:
        res = query_qq_from_qqmember(qq_num)
        print('/query/qq', res)
        return_dict = {"code": '1', "res": res}
        return jsonify(return_dict)
    return jsonify(code='0')


@app.route('/query/qqgroup', methods=['GET'])
def query_qqgroup():
    """
    code = 0 参数不合法
    code = 1 正常返回
    """
    qqgroup_num = str(request.args.get("num"))
    if qqgroup_num:
        res = query_qun_from_qqmember(qqgroup_num)
        print('/query/qqgroup', res)
        return_dict = {"code": "1", "res": res}
        return jsonify(return_dict)
    return jsonify(code='0')


@app.route('/query/relation', methods=['GET'])
def query_relation():
    qqNum = str(request.args.get("qqnum"))
    if qqNum:
        graph_dict = query_relation_from_qqmember(qqNum)
        graph_dict["type"] = "force"
        graph_dict["categories"] = [{"name": "群主"}, {"name": "管理员"}, {"name": "一般成员"}, {"name": "查询用户"}]
        return jsonify(code='1', graph=graph_dict)
    return jsonify(code='0')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2333)
