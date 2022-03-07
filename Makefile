rebuild: uninstall build package-install

build:
	poetry build

uninstall:
	pip uninstall python-lvl2

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	python3 flake8 generate_diff

gendiff:
	poetry run gendiff

test:
	poetry run pytest