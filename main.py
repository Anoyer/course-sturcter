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
    print("ok")
    configer.load_data(get_run_path())
    print(configer.__global_dict["special"])
    print(get_important_subject([1, 4], [2, 4], [4, 5], [4, 5]))

    # A = DataSet("1.csv")
    # # A.get_special_data()
    # data = A.get_column("ZWMC")
    # print(data)
    #common.write_data_to_csv(data, os.path.join(configer.get_value("dataset_path"), "csv/2.csv"))

