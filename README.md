## CLI app "Diff":


[![Actions Status](https://github.com/shiffter/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/shiffter/python-project-lvl2/actions)
[![Linter](https://github.com/shiffter/python-project-lvl2/actions/workflows/linter_test.yml/badge.svg?event=push)](https://github.com/shiffter/python-project-lvl2/actions/workflows/linter_test.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e7cfe31a172845184a57/maintainability)](https://codeclimate.com/github/shiffter/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e7cfe31a172845184a57/test_coverage)](https://codeclimate.com/github/shiffter/python-project-lvl2/test_coverage)


##This project was built using these tools:


| Tool                                        | Description                                            |
|---------------------------------------------|--------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)        | "Python dependency management and packaging made easy" |
| [Py.Test](https://pytest.org)               | "A mature full-featured Python testing tool"           |
| [flake8](https://github.com/PyCQA/flake8) | "used linter"                                          |


###Diff is a CLI utility for finding differences between configuration files.


####Supported format: JSON, YAML


####Formate report as json, plain or structured text


###Usage as external library


```python
from gendiff import generate_diff
diff = generate_diff(path_to_file1, path_to_file2)
```

### as CLI tool


```
>gendiff -h
usage: gendiff [-h] [-f FORMAT] file_1 file_2

Generate diff

positional arguments:
  file_1
  file_2

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output

Created by shiffter
```


###installation


```bash
python3 -m pip install hexlet-code-at-shiffter
```

[![asciicast](https://asciinema.org/a/477793.svg)](https://asciinema.org/a/477793)


###compare flat json files


```bash
gendiff path1 path2
```

[![asciicast](https://asciinema.org/a/477795.svg)](https://asciinema.org/a/477795)


###compare nested files, you can set output in plain format


```bash
gendiff -f plain path1 path2
```
[![asciicast](https://asciinema.org/a/477800.svg)](https://asciinema.org/a/477800)

