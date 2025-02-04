rebuild: uninstall build package-install

build:
	poetry build

uninstall:
	pip uninstall hexlet-code

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 tests gendiff

test-cover:
	poetry run pytest --cov=gendiff --cov-report xml

gendiff:
	poetry run gendiff

test:
	poetry run pytest