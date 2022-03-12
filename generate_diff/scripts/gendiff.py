import argparse
from generate_diff.modules import gendiff, formaters
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
    diff = gendiff.difference(file1, file2, depth=1)
    if args.format == 'json':
        diff_with_right_name = gendiff.refactor_keys(diff)
        result = gendiff.convert_to_json(diff_with_right_name)
        finally_ = gendiff.stylish(result)
    if args.format == 'plain':
        result = []
        finally_list = formaters.status_key(diff, result)
        finally_ = ''
        for i in finally_list:
            finally_ += i
    print(finally_)


if __name__ == '__main__':
    main()
