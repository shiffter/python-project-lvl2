import argparse
from generate_diff.modules import gendiff
import os

def main():
    parser = argparse.ArgumentParser(description='Generate diff', epilog='Created by shiffter')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output', type=str)
    args = parser.parse_args()
    print(args.first_file, args.second_file)
    dif = gendiff.generate_diff(os.path.abspath(args.first_file), (os.path.abspath(args.second_file)))
    print(dif)  


if __name__ == '__main__':
    main()



