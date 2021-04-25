
__all__ = [
    "load_data",
    "get_value",
    "set_key"
]

import os
import sys
import json
from utils.common import read_json_from_file

__global_dict = {}


def load_data(run_path):
    global __global_dict
    __global_dict.update(read_json_from_file(os.path.join(run_path, "config/config.json")))
    set_key("run_path", run_path)
    set_key("dataset_path", os.path.join(run_path, 'dataset'))


def set_key(key, value):
    global __global_dict
    __global_dict[key] = value


def get_value(key, default=None):
    global __global_dict
    return __global_dict.get(key, default)
