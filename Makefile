rebuild: uninstall build package-install

build:
	poetry build

uninstall:
	pip uninstall python-lvl2

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 tests generate_diff

test-cover:
	poetry run pytest --cov=generate_diff --cov-report xml

gendiff:
	poetry run gendiff

test:
	poetry run pytest