#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 16:27

'工具人'

__author__ = 'Judgement'

import csv
import os
import re
import time

import pandas as pd


def read_csv_to_list(filepath_root):
    files = os.listdir(filepath_root)
    filepath_list = [os.path.join(filepath_root, file) for file in files]
    all_list = []
    for filepath in filepath_list:
        print("now reading file:" + str(filepath))
        with open(filepath, 'r', errors='ignore') as f:
            lines = csv.reader(f)
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                all_list.append(line)
    return all_list


def read_csv_to_pandas(filepath):
    # with open(filepath,'r',encoding='GB2312') as f:
    data = pd.read_csv(filepath, sep=',', encoding='utf-8', engine='python')
    return data


def delete_error_char(filepath, savepath):
    with open(filepath, 'r', errors='ignore') as f, open(savepath, 'w', encoding='utf-8', newline='') as f2:
        lines = csv.reader(f)
        write = csv.writer(f2)
        for line in lines:
            temp = []
            for col in line:
                temp.append(col)
            write.writerow(temp)



if __name__ == '__main__':
    # PATH = "E:\STUDIO\大三下\系统安全\QQ群\GroupData\GroupData01.csv"
    # data = read_csv_to_pandas(PATH)
    # print(data)
    t1 = time.time()
    list = read_csv_to_list('E:\STUDIO\大三下\系统安全\QQ群\GroupData')
    QQnumber = '57994217'
    print(list)
    t2 = time.time()
    print('用时:' + str((t2 - t1) / 1000) + 's')
