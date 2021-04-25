
import sys
import os
import pandas as pd
from utils import common
from config import configer


class DataSet:
    def __init__(self, data_file=None, default_data=pd.DataFrame):
        self.data = default_data
        if data_file:
            self.data_file = os.path.join(configer.get_value("dataset_path"), data_file)
            self.data = common.read_data_from_file(self.data_file)
        self.special = configer.get_value("special")

    def get_special_data(self):
        # todo: 扫一遍BJMC数据 重建一个DataSet
        self.data = self.data.loc[lambda x: x['BJMC'].str.startswith(self.special)]

    def get_column(self, index):
        try:
            return self.data[index].values
        except Exception as e:
            print(str(e))
            return []


# 计算数据交集
def get_important_subject(*args):
    important_subject = set()
    if len(args):
        if isinstance(args[0], list):
            important_subject = set(args[0])
        else:
            print("args is not list")
            return []
    for enum in args:
        if isinstance(args[0], list):
            important_subject = important_subject & set(enum)
        else:
            print("args is not list")
            return []
    return list(important_subject)

