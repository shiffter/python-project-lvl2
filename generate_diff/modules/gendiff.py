import json
import yaml
from pprint import pprint


def search_way(file_name):
    if 'json' in file_name:
        return json.load(open(file_name))
    if 'yaml' in file_name:
        with open(file_name) as f:
            file = yaml.safe_load(f)
        return file
    elif 'yml' in file_name:
        with open(file_name) as f:
            file = yaml.safe_load(f)
        return file
    else:
        return -1


def refactor_name(diction):
    keys = list(diction.keys())
    for node in keys:
        if isinstance(diction[node], dict):
            refactor_name(diction[node])
        elif (str(node)[-1] == '+') or (str(node)[-1] == '-') or (str(node)[-1] == ' '):
            continue
        else:
            value = diction.pop(node)
            diction[node + ' '] = value
    return diction


def generate_diff(diction, stra, depth=0):
    if depth == 0:
        stra.extend('{\n')
        depth += 1
    keys = diction.keys()
    # length = len(keys)
    for node in keys:
        # length -= 1
        if isinstance(diction[node], dict):
            ma_str = '    ' * depth
            length = len(ma_str)
            ma_str = ma_str[2:length] + str(node)[-1] + ' ' + node[0:len(node)-1]# + ma_str[0:len(node)-1]
            stra.extend(ma_str)
            stra.extend(': {\n')
            depth += 1
            generate_diff(diction[node], stra, depth)
            depth -= 1
            stra.extend('    ' * depth + '}\n')
        else:
            # if str(node)[0] == ' ' or '+' or '-'
            if str(node)[-1] == '+':
                ma_str = '    ' * depth
                length = len(ma_str)
                ma_str = ma_str[2:length] + '+ ' + node[0:len(node)-1]
                stra.extend(ma_str)
                stra.extend(': ')
                stra.extend(list(str(diction[node])))
                stra.extend('\n')
            elif str(node)[-1] == '-':
                ma_str = '    ' * depth
                length = len(ma_str)
                ma_str = ma_str[2:length] + '- ' + node[0:len(node)-1]
                stra.extend(ma_str)
                stra.extend(': ')
                stra.extend(list(str(diction[node])))
                stra.extend('\n')
            elif str(node)[-1] == ' ':
                ma_str = '    ' * depth
                length = len(ma_str)
                ma_str = ma_str[2:length] + '  ' + node[0:len(node)-1]
                stra.extend(ma_str)
                stra.extend(': ')
                stra.extend(list(str(diction[node])))
                stra.extend('\n')
            # if length < 1:
            #     depth -= 1
    return stra, depth


def difference(file1, file2, depth=1):
    result = dict()
    main1 = set(file1.keys())
    main2 = set(file2.keys())
    file_1set = sorted(main1 - main2)
    file_2set = sorted(main2 - main1)
    common_keys = sorted(main1 | main2)
    for node3 in common_keys:
        if node3 in (main1 & main2):
            if isinstance(file1[node3], dict) and (isinstance(file2[node3], dict)):
                depth += 1
                result[node3 + ' '] = difference(file1[node3], file2[node3], depth=depth)
            elif file1[node3] == file2[node3]:
                result[node3 + ' '] = file2[node3]
            elif file2[node3] != file1[node3]:
                result[node3 + '-'] = file1[node3]
                result[node3 + '+'] = file2[node3]
        elif node3 in file_1set:
            result[node3 + '-'] = file1[node3]
        elif node3 in file_2set:
            result[node3 + '+'] = file2[node3]
    return result
