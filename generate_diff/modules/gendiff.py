import json
import yaml


def search_way(file_name: str):
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


def stylish(diction):
    result_list = []
    generate_diff(diction, result_list)
    finally_str = '{\n'
    for sym in result_list:
        finally_str += sym
    finally_str += '}'
    return finally_str


def convert_to_json(diction: dict):
    keys = list(diction.keys())
    for node in keys:
        if isinstance(diction[node], dict):
            convert_to_json(diction[node])
        else:
            value = diction[node]
            if value is False:
                value = 'false'
            elif value is None:
                value = 'null'
            elif value is True:
                value = 'true'
            diction[node] = value
    return diction


def refactor_name(diction: dict):
    keys = list(diction.keys())
    for node in keys:
        flag = str(node)[-1]
        list_of_flag = [' ', '-', '+']
        if isinstance(diction[node], dict):
            if flag in list_of_flag:
                refactor_name(diction[node])
            else:
                value = diction.pop(node)
                diction[node + ' '] = value
                refactor_name(diction[node + ' '])
        elif flag in list_of_flag:
            continue
        else:
            value = diction.pop(node)
            diction[node + ' '] = value
    return diction


def convert_str(string, depth):
    convert = '    ' * depth
    length = len(convert)
    convert = convert[2:length] + string[-1] + ' ' + string[0:len(string) - 1]
    return convert


def generate_diff(diction, result_list, depth=1):
    keys = diction.keys()
    for node in keys:
        if isinstance(diction[node], dict):
            ma_str = convert_str(str(node), depth)
            result_list.extend(ma_str)
            result_list.extend(': {\n')
            depth += 1
            generate_diff(diction[node], result_list, depth)
            depth -= 1
            result_list.extend('    ' * depth + '}\n')
        else:
            ma_str = convert_str(str(node), depth)
            result_list.extend(ma_str)
            result_list.extend(': ')
            result_list.extend(list(str(diction[node])))
            result_list.extend('\n')
    return result_list, depth


def difference(dict1, dict2, depth=1):
    result = dict()
    main1, main2 = set(dict1.keys()), set(dict2.keys())
    file_1set, file_2set = (main1 - main2), (main2 - main1)
    common_keys = sorted(main1 | main2)
    for node in common_keys:
        if node in (main1 & main2):
            if isinstance(dict1[node], dict) and (isinstance(dict2[node], dict)):
                depth += 1
                result[node + ' '] = difference(dict1[node], dict2[node], depth=depth)
            elif dict1[node] == dict2[node]:
                result[node + ' '] = dict2[node]
            elif dict2[node] != dict1[node]:
                result[node + '-'] = dict1[node]
                result[node + '+'] = dict2[node]
        elif node in file_1set:
            result[node + '-'] = dict1[node]
        elif node in file_2set:
            result[node + '+'] = dict2[node]
    return result
