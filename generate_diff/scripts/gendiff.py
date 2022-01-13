import argparse
from generate_diff.modules import gendiff
import os


def main():
    parser = argparse.ArgumentParser(description='Generate diff', epilog='Created by shiffter')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output', type=str)
    args = parser.parse_args()
    path_1 = os.path.abspath(args.first_file)
    path_2 = os.path.abspath(args.second_file)
    dif = gendiff.generate_diff(path_1, path_2)
    return print(dif)


if __name__ == '__main__':
    main()
