build:
	poetry build

uninstall:
	pip uninstall python-lvl2

package-install:
	pip install dist/python_lvl2-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 generate_diff
