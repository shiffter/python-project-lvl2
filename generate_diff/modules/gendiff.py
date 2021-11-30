import json


def generate_diff(file_1, file_2):
    sum_keys = []
    result_dict = dict()
    file_1 = json.load(open(file_1))
    file_2 = json.load(open(file_2))
    keys1 = list(file_1.keys())
    keys2 = list(file_2.keys())
    sum_keys.extend(keys1)
    sum_keys.extend(keys2)
    common_keys = sorted(set(sum_keys))
    for key in common_keys:
        if (key in keys1) and (key in keys2):
            if file_1[key] == file_2[key]:
                result_dict['  ' + key] = file_1[key]
            else:
                result_dict['- ' + key] = file_1[key]
                result_dict['+ ' + key] = file_2[key]
        elif key in keys1:
            result_dict['- ' + key] = file_1[key]
        else:
            result_dict['+ ' + key] = file_2[key]
    result_string = json.dumps(result_dict, indent=2, separators=('', ': ')).replace('"', '')
    return result_string


