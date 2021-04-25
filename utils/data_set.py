
import sys
import os
import pandas as pd
from utils import common
from config import configer


class DataSet:
    def __init__(self, data_file=None, default_data=pd.DataFrame):
        self.data = default_data
        if data_file:
            self.data_file_path = os.path.join(configer.get_value("dataset_path"), data_file)
            self.data_file_name = data_file.split('.')[0].split('_')[0]
            self.data = common.read_data_from_file(self.data_file_path)
        self.special = configer.get_value("special")
        self.college = configer.get_value("college")

    def get_special_data(self):
        # todo: 扫一遍BJMC数据 重建一个DataSet
        self.data = self.data.loc[lambda x: x['BJMC'].str.startswith(self.special)]
        self.data = self.data.loc[lambda x: x['ZWMC_1'].str.startswith(self.college)]
        common.write_data_to_csv(
            self.data, os.path.join(configer.get_value("dataset_path"),
                                    f'csv/{self.data_file_name}_{configer.get_value("special")}.csv'))
        print(f"ok {self.data_file_name}")

    def get_column(self, index):
        try:
            return list(self.data[index].values)
        except Exception as e:
            print(str(e))
            return []

    def get_courses_data(self, courses):
        for course in courses:
            data = self.data.loc[self.data["ZWMC"] == course]
            grades = set(grade[:-2] for grade in list(data["BJMC"].values))
            for grade in grades:
                grade_data = data.loc[lambda x: x["BJMC"].str.startswith(grade)]
                common.write_data_to_csv(
                    grade_data, os.path.join(configer.get_value("dataset_path"),
                                             f'csv/{self.data_file_name}_{grade}_{course}.csv'))


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



