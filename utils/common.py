# -*- coding: utf-8 -*-
#
# Copyright 2021 hch All Rights Reserved.
# Author: chuanhuihuang@foxmail.com
# Author 自己改

__all__ = [
    "read_csv_from_file",
    "write_data_to_csv",
    "read_json_from_file"
]


import os
import sys
import csv
import json
import pandas as pd


# 支持从execl、xlsx、csv中读取数据
def read_data_from_file(path_of_file: str):
    if not os.path.exists(path_of_file):
        return pd.DataFrame({})

    try:
        with open(path_of_file) as file:
            data = eval(f"pd.read_{path_of_file.split('.')[-1]}(file)")
        return data
    except Exception as e:
        print(str(e))
        return pd.DataFrame({})


def write_data_to_csv(data: pd, path):
    try:
        data.to_csv(path)
    except Exception as e:
        print(str(e))


def read_json_from_file(path_of_file):
    if not os.path.exists(path_of_file):
        return {}

    try:
        with open(path_of_file, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError as jde:
        print("ReadJsonFromFile: ", jde)

        return {}
    except IOError as ioe:
        print("ReadJsonFromFile: ", ioe)
        return {}


