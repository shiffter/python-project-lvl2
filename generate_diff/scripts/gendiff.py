import argparse
from generate_diff.modules import gendiff
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff', epilog='Created by shiffter')
    parser.add_argument('file_1', type=str)
    parser.add_argument('file_2', type=str)
    parser.add_argument('-f', '--format', help='set format of output', type=str)
    args = parser.parse_args()
    path_1 = os.path.abspath(args.file_1)
    path_2 = os.path.abspath(args.file_2)
    file1 = gendiff.search_way(path_1)
    file2 = gendiff.search_way(path_2)
    dif = gendiff.difference(file1, file2, depth=0)
    right_name = gendiff.refactor_name(dif)
    s = []
    result = gendiff.generate_diff(right_name, s)
    print(result)
    result = ''
    for i in s:
        result += i
    result += '}'
    print(result)
    # if dif != -1:
    #     print(result)
    #     return 0
    # else:
    #     print('incorrect path or file name')
    #     return -1


if __name__ == '__main__':
    main()
