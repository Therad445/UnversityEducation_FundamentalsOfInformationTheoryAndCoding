import math
import os
import struct
import sys
import pandas
from datetime import datetime

from compression import huffman as h


def log_warn(mes: str):
    print(f'{datetime.now()} [WARN] : {mes}')


def log_err(mes: str):
    print(f'{datetime.now()} [ERROR] : {mes}')


def sort_by_symb(data):
    return data['data'].sort(key=lambda x: x[0])


def sort_by_v(data):
    return data['data'].sort(key=lambda x: x[1], reverse=True)


def print_statistic(data):
    print(f"Общая длина: {data['len']}")
    df = pandas.DataFrame(data=data['data'], index=data['index'], columns=['Символ', 'Количество вхождений', 'Вероятность', 'Количество информации ai'])
    print(df)
    print(f"I(X) = {sum([i[3] for i in data['data']])}")


def collect_statistic(filepath, filedata):
    res = dict()
    res['counts'] = dict()
    res['data'] = []

    res['len'] = len(filedata)

    for symb in filedata:
        if symb not in res['counts']:
            res['counts'][symb] = 1
        else:
            res['counts'][symb] += 1

    for symb in res['counts'].keys():
        p_i = res['counts'][symb]/res['len']
        res['data'] += [(symb, res['counts'][symb], p_i, -math.log2(p_i))]

    res['index'] = [i for i in range(len(res['counts'].keys()))]

    return res


def collect_bin_statistic(filepath):
    filedata = b''

    with open(filepath, "rb") as file:
        filedata = file.read()

    return collect_statistic(filepath, filedata)


def collect_sym_statistic(filepath):
    filedata = ''

    with open(filepath, "r") as file:
        filedata = file.read()

    return collect_statistic(filepath, filedata)


def generate_out_file_name(filename: str):
    return ".".join(filename.split('.')[0:len(filename.split('.')) - 1]) + '.xip'


CODE_1 = 0x01
CODE_2 = 0x02
CODE_3 = 0x04
CODE_4 = 0x08


def parse_codes(codes: int):
    return codes & CODE_4, codes & CODE_3, codes & CODE_2, codes & CODE_1


SIGNATURE_NAME = 0x1111
SIGNATURE_ALLOWED_VERSION = (1, 0)
SIGNATURE_UNPACK_STR = 'hBBBQ'
SIGNATURE_SIZE = 16


def generate_signature(version: tuple = (1, 0), codes: int = 0, data_size: int = 0):
    name = SIGNATURE_NAME
    res_size = SIGNATURE_SIZE + data_size
    return struct.pack(SIGNATURE_UNPACK_STR, name, version[0], version[1], codes, res_size)


def unpack_signature(signature):
    return struct.unpack(SIGNATURE_UNPACK_STR, signature)


def check_signature(signature):
    check = unpack_signature(signature)
    if check[0] != SIGNATURE_NAME or (check[1], check[2]) != SIGNATURE_ALLOWED_VERSION:
        return False
    return True


def create_out_file(name: str):
    try:
        if os.path.exists(name):
            log_warn(f'name {name} exist')
    finally:
        pass

    file = open(name, "wb+")
    return file


def check_path_to_zip(path: str):
    try:
        if not os.path.exists(path):
            log_warn(f'zip path {path} not exist')
            return False
    except:
        return False

    return True


def get_file_str(file_from):
    with open(file_from, 'rb') as file_r:
        return file_r.read()


def zip_loop(file_path):
    data = dict()

    for root, dirs, files in os.walk(file_path):
        data[root] = []
        for file in files:
            buf = get_file_str(os.path.join(root, file))
            data[root] += [{file: buf}]

    return data


def parse_len(it):
    value, buf = '', next(it)
    while chr(buf[1]) != ';':
        value += str(buf[1] - 48)
        buf = next(it)

    assert (value.isdigit())
    value = int(value)

    for i in range(value + 1):
        next(it)

    return value, buf[0] + 1


def parse_file(it, d):
    filename_len, last = parse_len(it)
    filename = d[last:last + filename_len]

    data_len, last = parse_len(it)
    data = d[last:last + data_len]

    return {filename.decode(): data}, chr(d[data_len + last])


def parse_dir_name(it, d):
    dir_len, last = parse_len(it)
    dir_name = d[last:last + dir_len]

    return dir_name.decode()


def read_dir(d):
    it = iter(enumerate(d))
    data = dict()
    buf = ''

    try:
        while 1:
            cur_dir = parse_dir_name(it, d)
            data[cur_dir] = []
            while buf != '}':
                file, buf = parse_file(it, d)
                data[cur_dir].append(file)
            buf = ''
    except StopIteration:
        return data


def unzip_loop(data, file_path):
    for root, files in data.items():
        work = os.path.join(file_path, root)

        try:
            os.mkdir(work)
        except:
            log_warn(f'dir {work} exists')

        for file in files:
            work_file = os.path.join(work, list(file.keys())[0])
            file_data = list(file.values())[0]

            with open(work_file, 'wb+', encoding=None) as open_file:
                open_file.write(file_data)


def fill_file_tittle(pair):
    tittle = b''

    file = list(pair.items())[0][0]
    value = list(pair.items())[0][1]

    tittle += str(len(file)).encode() + b';'
    tittle += file.encode() + b';'
    tittle += str(len(value)).encode() + b';'
    tittle += value

    return tittle


def fill_files_tittles(data):
    tittle = b''

    pre_last_index = len(data) - 1
    for i in range(pre_last_index):
        pair = data[i]
        tittle += fill_file_tittle(pair)
        tittle += b'|'
    pair = data[pre_last_index]
    tittle += fill_file_tittle(pair)

    return tittle


def write_from_dict(data):
    new_data = b''

    for dirs in data.keys():
        new_data += str(len(dirs)).encode() + b';'
        new_data += dirs.encode() + b'{'

        if len(data[dirs]):
            new_data += fill_files_tittles(data[dirs])

        new_data += b'}'

    return new_data


def zip_without_compress(filepath):
    fd = create_out_file(OUT_FILE_NAME)
    data = write_from_dict(zip_loop(filepath))
    fd.write(generate_signature(data_size=sys.getsizeof(data)))
    fd.write(data)
    fd.close()


def unzip_item(filepath, output):
    with open(filepath, 'rb') as file:
        signature = file.read(SIGNATURE_SIZE)
        if check_signature(signature):
            codes = unpack_signature(signature)
            check_compress_code(filepath, output, signature)

def decode_no_compressed(file):
    data = read_dir(file.read())
    unzip_loop(data, os.path.join('.', 'unzip'))


def decode_huffman(filepath, output):
    h.decode_file(filepath, output)


def decode_ariph(filepath, output):



def check_compress_code(filepath, output, code):
    codes = parse_codes(code)
    if codes[0]:
        decode_huffman(filepath, output)
    elif codes[1]:



def task1():
    statistic = collect_bin_statistic('test-koi8.txt')
    sort_by_v(statistic)
    print_statistic(statistic)


def task2():
    statistic = collect_sym_statistic('test-utf8.txt')
    sort_by_v(statistic)
    print_statistic(statistic)


def task3():
    statistic = collect_bin_statistic('Main.java')
    sort_by_v(statistic)
    buf = [i for i in statistic['data'] if chr(i[0]).isalpha()][0:4]
    buf += [i for i in statistic['data'] if not chr(i[0]).isalpha()][0:4]
    statistic['data'] = buf
    statistic['index'] = [i for i in range(8)]
    print_statistic(statistic)

    data = ''
    with open('6.txt', 'r', encoding='utf-16le') as file:
        data = file.read()

    data = data.encode('utf-16le')
    print(data)
    for i in range(0, len(data), 2):
        print(data[i:i+1], end=',')


def main():
    task1()
    task2()
    # task3()
    # try:
    #     zip_item(PATH_TO_ZIP)
    #     unzip_item(OUT_FILE_NAME)
    # except Exception as e:
    #     log_err(str(e))


PATH_TO_ZIP = "test.test.ste"
NAME_TO_ZIP = "test.test.ste"
OUT_FILE_NAME = generate_out_file_name(NAME_TO_ZIP)
main()
