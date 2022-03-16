import tests.fixtures.right_answer
from gendiff import formaters, gendiff_m


def test_generate_diff():
    diction = {1: 'one', 2: 2, 'three': 3, 'doggy': False}
    result = []
    assert formaters.convert_dict_to_list(diction, result) == (tests.fixtures.right_answer.right_plain_list, 1)
    diction = dict()
    result = []
    assert formaters.convert_dict_to_list(diction, result, depth=0) == ([], 0)
    diction = gendiff_m.search_way('tests/fixtures/empty.json')
    result = []
    assert formaters.convert_dict_to_list(diction, result) is not True


def test_generate_diff_recursive():
    diction = gendiff_m.search_way('tests/fixtures/file1.json')
    result = []
    assert formaters.convert_dict_to_list(diction, result) == (tests.fixtures.right_answer.right_recursive_list_json, 1)
    diction = gendiff_m.search_way('tests/fixtures/r_file1.yaml')
    result = []
    assert formaters.convert_dict_to_list(diction, result) == (tests.fixtures.right_answer.right_recursive_list_yaml, 1)


# def test_difference():
#     diction1 = gendiff_m.search_way('tests/fixtures/file1.json')
#     diction2 = gendiff_m.search_way('tests/fixtures/file2.json')
#     result = gendiff_m.difference(diction1, diction2)
#     assert result == tests.fixtures.right_answer.right_recursive_dict


def test_convert_string():
    assert formaters.convert_str('!!@#asd', 3) == '          d !!@#as'
    assert formaters.convert_str('    ', 0) == '     '


def test_refactor_name():
    diction = dict()
    assert gendiff_m.refactor_keys(diction) == dict()
    diction = {'1': 3}
    assert gendiff_m.refactor_keys(diction) == {'1 ': 3}


def test_convert_to_json():
    diction = dict()
    assert formaters.convert_to_json(diction) == dict()
    diction = {1: False, 2: None, 3: True}
    assert formaters.convert_to_json(diction) == {1: 'false', 2: 'null', 3: 'true'}


def test_stylish():
    diction = dict()
    assert formaters.stylish(diction, 'json') == '{\n}'
    diction = {1: 2, 3: 3}
    assert formaters.stylish(diction, 'json') == '{\n  1 : 2\n  3 : 3\n}'


def test_search_way():
    assert gendiff_m.search_way('tests/fixtures/empty.json') == {}
