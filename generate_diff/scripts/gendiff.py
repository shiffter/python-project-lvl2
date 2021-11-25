import argparse

parser = argparse.ArgumentParser(description='Generate diff', epilog='Created by shiffter')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output', type=str)
args = parser.parse_args()
