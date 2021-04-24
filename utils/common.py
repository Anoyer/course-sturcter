# -*- coding: utf-8 -*-
#
# Copyright 2021 hch All Rights Reserved.
# Author: chuanhuihuang@foxmail.com
# Author 自己改

__all__ = [
    "read_csv_from_file",
    "write_data_to_csv"
]


import os
import sys
import csv
import pandas as pd


def read_csv_from_file(path_of_file):
    if not os.path.exists(path_of_file):
        return pd.DataFrame({})

    try:
        with open(path_of_file) as file:
            data = pd.read_csv(file)
        return data
    except Exception as e:
        print(str(e))
        return pd.DataFrame({})


def write_data_to_csv(data: pd, path):
    try:
        data.to_csv(path)
    except Exception as e:
        print(str(e))


