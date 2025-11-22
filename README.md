
```sh
$ uv add Django==5.2.8
$ uv add --dev Django==5.2.8
$ uv sync

$ mkdir backend
$ uv run django-admin startproject config backend/api/

$ mkdir backend/api
$ uv run django-admin startapp api backend/api

$ uv run python backend/manage.py makemigrations
$ uv run python backend/manage.py migrate

$ uv run python backend/manage.py runserver
```
http://127.0.0.1:8000/

```sh
$ uv run ruff check . --fix
$ uv run ruff format .
$ uv run mypy .
$ uv run pytest
```
