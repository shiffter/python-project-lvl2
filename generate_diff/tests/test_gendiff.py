import os
from generate_diff.modules import gendiff


diff = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
path_1 = os.path.abspath('generate_diff/tests/fixtures/file1.json')
path_2 = os.path.abspath('generate_diff/tests/fixtures/file2.json')


def test_generate_diff():
    assert gendiff.generate_diff(path_1, path_2) == diff
