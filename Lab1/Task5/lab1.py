import os
from datetime import datetime
import json
import sys


def log_err(mes: str):
    print(f'{datetime.now()} ERROR : {mes}')


def log_info(mes: str):
    print(f'{datetime.now()} : {mes}')


def log_debug(mes: str):
    print(f'{datetime.now()} : {mes}')


def generate_out_file_name(filename: str):
    return ".".join(filename.split('.')[0:len(filename.split('.')) - 1]) + '.xip'


def create_out_file(name: str):
    try:
        if os.path.exists(name):
            log_err(f'name {name} exist')
    finally:
        pass

    file = open(name, "w+")
    log_debug('out file was created')
    return file


def check_path_to_zip(path: str):
    try:
        if not os.path.exists(path):
            log_err(f'zip path {path} not exist')
            return False
    except:
        return False

    return True


def get_file_str(file_from):
    log_debug(f'get  str from {file_from}')
    with open(file_from, 'r') as file_r:
        return file_r.read()


def zip_loop(file_path):
    data = dict()

    for root, dirs, files in os.walk(file_path):
        data[root] = []
        for file in files:
            buf = get_file_str(os.path.join(root, file))
            data[root] += [{file: buf}]

    return data


def check_sig(file):
    return True


def read_data(filename):
    with open(filename, 'r') as file:
        return file.read()


def parse_data(filename):
    data_str = read_data(filename)
    return json.loads(data_str)


def unzip_loop(data, file_path):
    work_dir = file_path

    def to_work(path):
        return os.path.join(work_dir, path)

    for root, files in data.items():
        work = to_work(root)
        print(root, files)

        try:
            os.mkdir(work)
        except:
            log_err(f'root {work} exists')

        for file in files:
            print(file)
            work_file = os.path.join(work, list(file.keys())[0])

            with open(work_file, 'w+') as open_file:
                open_file.write(list(file.values())[0])


def main():
    if check_path_to_zip(PATH_TO_ZIP):
        fd = create_out_file(OUT_FILE_NAME)
        data = zip_loop(PATH_TO_ZIP)
        json.dump(data, fd)
        fd.close()

        data = parse_data(OUT_FILE_NAME)
        unzip_loop(data, '.\\unzip')


PATH_TO_ZIP = "test.test.ste"
NAME_TO_ZIP = "test.test.ste"
OUT_FILE_NAME = generate_out_file_name(NAME_TO_ZIP)
main()
