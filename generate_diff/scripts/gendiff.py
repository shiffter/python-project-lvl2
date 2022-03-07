import argparse
from generate_diff.modules import gendiff
import os
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff', epilog='Created by shiffter')
    parser.add_argument('file_1', type=str)
    parser.add_argument('file_2', type=str)
    parser.add_argument('-f', '--format', help='set format of output', type=str)
    args = parser.parse_args()
    path_1 = os.path.abspath(args.file_1)
    path_2 = os.path.abspath(args.file_2)
    file_1 = json.load(open(path_1))
    file_2 = json.load(open(path_2))
    print(f'file_1 = {file_1}\nfile_2={file_2}')
    dif = gendiff.generate_diff(path_1, path_2)
    return print(dif)


if __name__ == '__main__':
    main()
