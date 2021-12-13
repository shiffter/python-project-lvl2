import json
import os
path_1 = os.path.abspath('file1.json')
path_2 = os.path.abspath('file2.json')


def generate_diff(path_1, path_2):
    sum_keys = []
    result_dict = dict()
    dict_1 = json.load(open(path_1))
    dict_2 = json.load(open(path_2))
    keys1 = list(dict_1.keys())
    keys2 = list(dict_2.keys())
    sum_keys.extend(keys1)
    sum_keys.extend(keys2)
    common_keys = sorted(set(sum_keys))
    for key in common_keys:
        if (key in keys1) and (key in keys2):
            if dict_1[key] == dict_2[key]:
                result_dict['  ' + key] = dict_1[key]
            else:
                result_dict['- ' + key] = dict_1[key]
                result_dict['+ ' + key] = dict_2[key]
        elif key in keys1:
            result_dict['- ' + key] = dict_1[key]
        else:
            result_dict['+ ' + key] = dict_2[key]
    diff = json.dumps(result_dict, indent=2, separators=('', ': ')).replace('"', '')
    return diff
