from generate_diff.modules import gendiff


def test_generate_diff_plain():
    diff = open('tests/fixtures/plain_diff.txt')
    assert gendiff.generate_diff('tests/fixtures/file3_plain.json', 'tests/fixtures/file4_plain.json') == diff.read()
    diff.close()


def test_generate_diff_incorrect():
    assert gendiff.generate_diff('tests/fixtures/file3_plain.json', 'tests/fixtures/file4_plain.json') != 'cheker'


def test_generate_diff_empty():
    assert gendiff.generate_diff('tests/fixtures/empty.json', 'tests/fixtures/empty.json') == '{}'
