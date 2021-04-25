#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 hch All Rights Reserved.
# Author: chuanhuihuang@foxmail.com


import os
import csv
from utils import common
from config import configer
from utils.data_set import DataSet, get_important_subject


def get_run_path():
    return os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":
    configer.load_data(get_run_path())
    # 获取专业数据
    A = DataSet("2014-2015_计科.csv")
    B = DataSet("2016-2017_计科.csv")
    C = DataSet("2018-2019_计科.csv")
    A.get_special_data()
    B.get_special_data()
    C.get_special_data()

    # 获取课程交集
    important = get_important_subject(A.get_column("ZWMC"), B.get_column("ZWMC"), C.get_column("ZWMC"))
    with open(os.path.join(configer.get_value("dataset_path"), "csv/important_sub.txt"), "w+") as w:
        w.write(str(important))
    print("ok")

    # 获取班级课程成绩
    A.get_courses_data(important)
    B.get_courses_data(important)
    C.get_courses_data(important)

