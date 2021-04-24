#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 hch All Rights Reserved.
# Author: chuanhuihuang@foxmail.com


import os
import csv
from utils import common
from config import configer


def get_run_path():
    return os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":
    print("ok")
    configer.load_data(get_run_path())
    print(configer.__global_dict["special"])

