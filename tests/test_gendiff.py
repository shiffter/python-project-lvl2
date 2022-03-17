import gendiff.gendiff_m
import tests.fixtures.right_answer
from gendiff import formaters, gendiff_m


def test_formaters_convert_to_json():
    diction = dict()
    assert formaters.convert_to_json(diction) == dict()
    diction = {1: False, 2: None, 3: True}
    assert formaters.convert_to_json(diction) == {1: 'false', 2: 'null', 3: 'true'}


def test_formaters_stylish():
    diction = dict()
    assert formaters.stylish(diction, 'json') == '"{\\n}"'
    diction = {1: 2, 3: 3}
    assert formaters.stylish(diction, 'json') == '"{\\n  1 : 2\\n  3 : 3\\n}"'


def test_formaters_search_way():
    assert gendiff_m.search_way('tests/fixtures/empty.json') == {}


def test_formaters_format_string():
    new_value = 2
    path = 'root'
    node = 'node'
    action = 'update'
    result = []
    old_value = 'two'
    result = formaters.format_string(new_value, path, node, action, result, old_value)
    assert result == tests.fixtures.right_answer.right_format_string[0]
    action = 'add'
    result.clear()
    result = formaters.format_string(new_value, path, node, action, result, old_value)
    assert result == tests.fixtures.right_answer.right_format_string[1]
    action = 'delete'
    result.clear()
    result = formaters.format_string(new_value, path, node, action, result, old_value)
    assert result == tests.fixtures.right_answer.right_format_string[2]


def test_formaters_status_node():
    list_of_node = ['node1', 'node2', 'node2', 'node4']
    assert formaters.status_node(list_of_node, 'node1', ' ') == "not change"
    assert formaters.status_node(list_of_node, 'node2', '-') == 'update'
    assert formaters.status_node(list_of_node, 'node3', '+') == 'status'
    assert formaters.status_node(list_of_node, 'node4', '-') == 'delete'
    assert formaters.status_node(list_of_node, 'node1', '+') == 'add'


def test_formaters_separate_status():
    list_of_node = ['node1+', 'node2-', 'node2 ', 'node4*']
    assert formaters.separate_status_of_name(list_of_node) == ['node1', 'node2', 'node2', 'node4']


def test_formaters_status_key():
    path_1 = gendiff.gendiff_m.search_way('tests/fixtures/file1.json')
    path_2 = gendiff.gendiff_m.search_way('tests/fixtures/file2.json')
    diction = gendiff_m.difference(path_1, path_2)
    assert formaters.status_key(diction, []) == tests.fixtures.right_answer.status_key


def test_formaters_convert_list_to_dict():
    diction = {1: 'one', 2: 2, 'three': 3, 'doggy': False}
    result = []
    assert formaters.convert_dict_to_list(diction, result) == (tests.fixtures.right_answer.right_plain_list, 1)
    diction = dict()
    result.clear()
    assert formaters.convert_dict_to_list(diction, result, depth=0) == ([], 0)
    diction = gendiff_m.search_way('tests/fixtures/empty.json')
    result.clear()
    assert formaters.convert_dict_to_list(diction, result) is not True


def test_formaters_convert_string():
    assert formaters.convert_str('!!@#asd', 3) == '          d !!@#as'
    assert formaters.convert_str('    ', 0) == '     '


def test_gendiff_m_recursive():
    diction = gendiff_m.search_way('tests/fixtures/file1.json')
    result = []
    assert formaters.convert_dict_to_list(diction, result) == (tests.fixtures.right_answer.right_recursive_list_json, 1)
    diction = gendiff_m.search_way('tests/fixtures/r_file1.yaml')
    result = []
    assert formaters.convert_dict_to_list(diction, result) == (tests.fixtures.right_answer.right_recursive_list_yaml, 1)


def test_gendiff_m_difference():
    diction1 = gendiff_m.search_way('tests/fixtures/file1.json')
    diction2 = gendiff_m.search_way('tests/fixtures/file2.json')
    result = gendiff_m.difference(diction1, diction2)
    assert result == tests.fixtures.right_answer.right_recursive_dict


def test_gendiff_m_refactor_name():
    diction = dict()
    assert gendiff_m.refactor_keys(diction) == dict()
    diction = {'1': 3}
    assert gendiff_m.refactor_keys(diction) == {'1 ': 3}
