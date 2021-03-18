#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 9:17

'处理QQ群的数据'

__author__ = 'Judgement'

import csv
import os

import pymongo

client = pymongo.MongoClient()
db = client.social_engineering_db
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
    find_result = qqmember_coll.find({"QQNum": qqnum}, {"_id": 0})
    member_list = []
    for item in find_result:
        member_list.append(item)
    return member_list


def query_qun_from_qqmember(qunNum: str):
    find_result = qqmember_coll.find({"QunNum": qunNum}, {"_id": 0})
    member_list = []
    for item in find_result:
        member_list.append(item)
    return member_list


def query_relation_from_qqmember(qqNum: str):
    joined_group = qqmember_coll.find({"QQNum": qqNum}, {"QunNum": 1, "Nick": 1, "_id": 0})
    group_num_list = []
    for item in joined_group:
        group_num_list.append(item["QunNum"])
    graph_params = {}
    graph_params["nodes"] = [{"name": "QQ:" + qqNum, "value": 1, "category": 3}]
    graph_params["links"] = []

    for group_num in group_num_list:
        master_index = -1
        for member in qqmember_coll.find({"QunNum": group_num}, {"_id": 0}):
            if member['Auth'] == '4':
                group_master = member['QQNum']
                graph_params["nodes"].append(
                    {"name": "QQ:" + group_master + "\n昵称：" + member['Nick'] + "\n群号:" + group_num, "value": 1,
                     "category": 0})
                master_index = len(graph_params["nodes"]) - 1
                graph_params["links"].append({"source": 0, "target": master_index})
        for member in qqmember_coll.find({"QunNum": group_num}, {"_id": 0}):
            category = 2
            if member['Auth'] == "2":
                category = 1
            elif member['Auth'] == '1':
                category = 2
            graph_params["nodes"].append({"name": "QQ:" + member["QQNum"] + "\n昵称：" + member['Nick'], "value": 1, "category": category})
            index = len(graph_params["nodes"]) - 1
            graph_params["links"].append({"source": master_index, "target": index})
    return graph_params


if __name__ == '__main__':
    # 入库
    # root = "E:\STUDIO\大三下\系统安全\QQ群\GroupData"
    # files = os.listdir(root)
    # filepath_list = [os.path.join(root, file) for file in files]
    # for file in filepath_list:
    #     insert_csv_to_mongodb(file, qqmember_coll)

    # 查询测试
    # l1 = query_qq_from_qqmember("100000")
    # print(l1)
    #
    # l2 = query_qun_from_qqmember("30084997")
    # print(l2)

    # l3 = query_relation_from_qqmember("100000")
    # print(l3)

    l4 = query_relation_from_qqmember("100000")
    print(l4)
