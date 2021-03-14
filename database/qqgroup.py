#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 9:17

'处理QQ群的数据'

__author__ = 'Judgement'

import csv
import os

import pymongo

client = pymongo.MongoClient()
db = client.social_work_db
qqmember_coll = db.qqmember
qqgroup_coll = db.qqgroup


def insert_csv_to_mongodb(file_path, collection):
    print("now insert file:", file_path)
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = csv.reader(f)
        item_dict = {}
        col_names = []
        for i, line in enumerate(lines):
            line = line[1:]  # 去除第一列id列
            if i == 0:
                for col_name in line:
                    col_names.append(col_name)
                continue
            if len(col_names) != len(line):
                continue
            for j in range(len(col_names)):
                item_dict[col_names[j]] = line[j] if j != len(col_names) - 1 else "".join(line[j:])
            collection.insert_one(item_dict.copy())
            item_dict = {}


def query_qq_from_qqmember(qqnum: str):
    find_result = qqmember_coll.find({"QQNum": qqnum})
    member_list = []
    for item in find_result:
        member_list.append(item)
    return member_list


def query_qun_from_qqmember(qunNum: str):
    find_result = qqmember_coll.find({"QunNum": qunNum})
    member_list = []
    for item in find_result:
        member_list.append(item)
    return member_list


if __name__ == '__main__':
    # 入库
    root = "E:\STUDIO\大三下\系统安全\QQ群\QunInfo"
    files = os.listdir(root)
    filepath_list = [os.path.join(root, file) for file in files]
    for file in filepath_list:
        insert_csv_to_mongodb(file, qqgroup_coll)

    # 查询测试
    # l1 = query_qq_from_qqmember("3131033")
    # print(l1)
    #
    # l2 = query_qun_from_qqmember("900002")
    # print(l2)
