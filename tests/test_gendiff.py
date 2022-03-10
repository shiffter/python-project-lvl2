from generate_diff.modules import gendiff


def test_generate_diff_plain():
    diff = open('tests/fixtures/plain_diff.txt')
    assert gendiff.generate_diff('tests/fixtures/file3_plain.json', 'tests/fixtures/file4_plain.json') == diff.read()
    diff.close()


def test_generate_diff_incorrect():
    assert gendiff.generate_diff('tests/fixtures/file3_plain.json', 'tests/fixtures/file4_plain.json') != 'cheker'


def test_generate_diff_empty():
    assert gendiff.generate_diff('tests/fixtures/empty.json', 'tests/fixtures/empty.json') == '{}'


def test_generate_diff_for_string():
    diff = gendiff.generate_diff('tests/fixtures/plain_file1.yml', 'tests/fixtures/plain_file2.yaml')
    assert type(diff) == str


def test_generate_diff_yaml_plain():
    diff = open('tests/fixtures/plain_diff.txt')
    assert gendiff.generate_diff('tests/fixtures/plain_file1.yml', 'tests/fixtures/plain_file2.yaml') == diff.read()
    diff.close()


def test_generate_diff_incorrect_filename():
    assert gendiff.generate_diff('tfI$le1.yl', 'false') == -1
