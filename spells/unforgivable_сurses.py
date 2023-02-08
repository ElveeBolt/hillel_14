import os
import json


def avada_kedavra(path: str):
    """
    Remove empty folder is path

    :param path: str of path
    :return:
    """
    dirs = list(os.walk(path))[1:]

    for root, dir, files in dirs:
        if len(dir) > 0 and len(files) == 0:
            continue

        if len(files) == 0:
            os.rmdir(root)


def imperius(path: str):
    """
    Modify award type in json file

    :param path: str of json file
    :return:
    """
    with open(path, 'r') as file:
        data = json.load(file)

    for i, film in enumerate(data):
        for k, result in enumerate(film['results']):
            data[i]['results'][k]['type'] = 'Winner'

    with open(path, 'w') as file:
        json.dump(data, file)


def save_json(data: list, path: str):
    """
    Save data to json file

    :param data: list of data
    :param data: str of path

    :return:
    """
    with open(path, "w") as file:
        json.dump(data, file)
