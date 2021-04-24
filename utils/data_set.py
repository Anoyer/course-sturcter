
import sys
import os
import pandas
from utils import common


class DataSet:
    def __init__(self, data_file=None, default_data=None):
        self.data = default_data
        if data_file:
            self.data = common.write_data_to_csv(data_file)

    def get_special_data(self):
        # todo: 扫一遍BJMC数据 重建一个DataSet
        pass



