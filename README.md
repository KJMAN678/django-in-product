```sh
# 最初の1回
$ touch .envrc
# for Mac
$ brew install direnv

# 環境変数
$ cp .envrc.example .envrc
$ direnv allow

$ docker compose up -d
$ docker compose down
$ docker compose build
```
http://localhost:8000/v1/api/hello-world/


### 保留 backend
```sh
$ docker compose exec web uv add Django==5.2.8
$ docker compose exec web uv add --dev Django==5.2.8

# 最初の1回のみ プロジェクト作成
$ mkdir backend
$ docker compose exec web uv run django-admin startproject config backend/api/

# app 追加
$ mkdir backend/blog
$ docker compose exec web uv run django-admin startapp blog blog

$ docker compose exec web uv run python manage.py makemigrations
$ docker compose exec web uv run python manage.py migrate
$ docker compose exec web uv run manage.py createsuperuser --noinput
```

```sh
$ docker compose exec web uv run ruff check . --fix
$ docker compose exec web uv run ruff format .
$ docker compose exec web uv run mypy .
$ docker compose exec web uv run pytest
```
