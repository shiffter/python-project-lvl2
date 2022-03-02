import copy
import json
import yaml


def search_way(file_name):
    if 'json' in file_name:
        return json.load(open(file_name))
    if 'yaml' or 'yml' in file_name:
        file = open(file_name, 'r')
        return yaml.load(file, yaml.SafeLoader)


def generate_diff(path_1, path_2):
    sum_keys, result_dict = [], dict()
    dict_1 = search_way(path_1)
    dict_2 = search_way(path_2)
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


chek_json = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}

chek1_json = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}


chek_yaml = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}

chek1_yaml = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}


# def difference(file1, file2):
#     result = dict()
#     main1 = set(file1.keys())
#     main2 = set(file2.keys())
#     file_1set = sorted(main1 - main2)
#     file_2set = sorted(main2 - main1)
#     common_keys = sorted(main1 & main2)
#     for node3 in common_keys:
#         if isinstance(file1[node3], dict) and (isinstance(file2[node3], dict)):
#             result[node3] = difference(file1[node3], file2[node3])
#         elif file1[node3] == file2[node3]:
#             result['  ' + node3] = file2[node3]
#         else:
#             result['- ' + node3] = file1[node3]
#             result['+ ' + node3] = file2[node3]
#     for node in file_1set:
#         result['- ' + node] = file1[node]
#     for node2 in file_2set:
#         result['+ ' + node2] = file2[node2]
#     return result


# def generate_diff1(dict_1, dict_2):
#     sum_keys, result_dict = [], dict()
#     keys1 = list(dict_1.keys())
#     keys2 = list(dict_2.keys())
#     for node in keys1:
#         if isinstance(dict_1[node], dict) and isinstance(dict_2[node], dict):
#             generate_diff1(dict_1[node], dict_2[node])
#         else:
#             sum_keys.extend(keys1)
#             sum_keys.extend(keys2)
#             common_keys = sorted(set(sum_keys))
#             for key in common_keys:
#                 if (key in keys1) and (key in keys2):
#                     if dict_1[key] == dict_2[key]:
#                         result_dict['' + key] = dict_1[key]
#                     else:
#                         result_dict['- ' + key] = dict_1[key]
#                         result_dict['+ ' + key] = dict_2[key]
#                 elif key in keys1:
#                     result_dict['- ' + key] = dict_1[key]
#                 else:
#                     result_dict['+ ' + key] = dict_2[key]
#             diff = json.dumps(result_dict, indent=7, separators=('', ': ')).replace('"', '')
#             return diff


def stylish_diff1(diction):
    diff = json.dumps(diction, indent=2, separators=('', ': ')).replace('"', '')
    return diff
#
#
# def stylish(diction):
#     result = []
#     keys = sorted(diction.keys())
#     for node in keys:
#         if isinstance(diction[node], dict):
#             stylish(diction[node])
#         else:
#             result.append(str(diction))
#     return result
#
#
def difference(file1, file2):
    result = dict()
    main1 = set(file1.keys())
    main2 = set(file2.keys())
    file_1set = sorted(main1 - main2)
    file_2set = sorted(main2 - main1)
    common_keys = sorted(main1 | main2)
    for node3 in common_keys:
        if node3 in (main1 & main2):
            if isinstance(file1[node3], dict) and (isinstance(file2[node3], dict)):
                result[node3] = difference(file1[node3], file2[node3])
            elif file1[node3] == file2[node3]:
                result['  ' + node3] = file2[node3]
            elif file2[node3] != file1[node3]:
                result['- ' + node3] = file1[node3]
                result['+ ' + node3] = file2[node3]
        elif node3 in file_1set:
            result['- ' + node3] = file1[node3]
        elif node3 in file_2set:
            result['+ ' + node3] = file2[node3]
    return result


result = difference(chek_json, chek1_json)
# print(result)
# print(stylish_diff1(result))
