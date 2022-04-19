import json
from os.path import abspath


def json_reader(file_path):
    """
    Reads a json file and returns a dictionary.
    """
    with open(abspath(file_path), 'r') as f:
        return json.load(f)


def load_json(file_name):
    """
    Loads json files for the api tests
    :param file_name:
    :return:
    """
    file_abs_path = abspath(f"test_data/api_test_data/{file_name}")
    with open(file_abs_path, 'r') as f:
        return json.load(f)
