```sh
# 最初の1回
$ touch .envrc
# for Mac
$ brew install direnv

# 環境変数
$ cp .envrc.example .envrc
$ direnv allow

$ ./docker-remake.sh
- 下記を実行
$ docker compose up -d
$ docker compose down
$ docker compose build
$ docker compose exec web uv run task start-django
```
http://localhost:8000/v1/api/hello-world/
http://localhost:8000/admin/


### 保留 backend
```sh
$ docker compose exec web uv add Django==5.2.8
$ docker compose exec web uv add --dev Django==5.2.8

# 最初の1回のみ プロジェクト作成
$ mkdir backend
$ docker compose exec web uv run django-admin startproject config backend/api/

# app 追加
$ mkdir backend/util
$ docker compose exec web uv run django-admin startapp util util

$ docker compose exec web uv run task start-django
- 以下を実行
$ docker compose exec web uv run python manage.py makemigrations
$ docker compose exec web uv run python manage.py flush --no-input
$ docker compose exec web uv run python manage.py migrate
$ docker compose exec web uv run manage.py createsuperuser --noinput
```

```sh
$ docker compose exec web uv run task check

- 以下を実行する
$ docker compose exec web uv run ruff check . --fix
$ docker compose exec web uv run ruff format .
$ docker compose exec web uv run pyrefly check 
$ docker compose exec web uv run pytest

# mypy は pyrefly に移行中
$ docker compose exec web uv run mypy .
```

### ダミーデータ作成
```sh
$ docker compose exec web uv run python manage.py make_dummy_blog_author
```

```sh
$ docker compose exec web uv run python manage.py get_query_blog
$ docker compose exec web uv run python manage.py get_query_author
# 生のクエリを出力
$ docker compose exec web uv run python manage.py get_by_raw_query
# count を取得
$ docker compose exec web uv run python manage.py get_count
```

### pyrefly を試す

```sh
$ docker compose exec web uv run pyrefly init

$ docker compose exec web uv run pyrefly check --suppress-errors
$ docker compose exec web uv run pyrefly check --remove-unused-ignores
```
