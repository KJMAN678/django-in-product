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


- 同期処理
http://localhost:8000/async/get-blog/
- 非同期処理
http://localhost:8000/async/get-blog-async/

- 非同期処理でトランザクションを使用する
http://localhost:8000/async/async-view-with-transaction/

### 保留 backend
```sh
$ docker compose exec web uv add Django==5.2.8
$ docker compose exec web uv add --dev Django==5.2.8

# 最初の1回のみ プロジェクト作成
$ mkdir backend
$ docker compose exec web uv run django-admin startproject config backend/api/

# app 追加
$ mkdir backend/ch0x_xxx/async
$ docker compose exec web uv run django-admin startapp async ch0x_xxx/async

$ docker compose exec web uv run task start-django
- 以下を実行
$ docker compose exec web uv run python manage.py makemigrations
$ docker compose exec web uv run python manage.py flush --no-input
$ docker compose exec web uv run python manage.py migrate
$ docker compose exec web uv run manage.py createsuperuser --noinput
```

### 逆 migration
```sh
# blog app を 0001 適用時の状態に戻す
$ docker compose exec web uv run python manage.py migrate blog 0001
```

### fake migration
- DB 構築済みの場合に、Django の履歴上、migrate 適用済みと認識させる処理
```sh
$ docker compose exec web uv run python manage.py migrate blog 0002 --fake
```

### lint, formatter, test

```sh
$ docker compose exec web uv run task check

- 以下を実行する
$ docker compose exec web uv run ruff check . --fix
$ docker compose exec web uv run ruff format .
$ docker compose exec web uv run pyrefly check 
$ docker compose exec web uv run pytest
$ docker compose exec web uv run djlint templates --extension html --reformat
```

### ダミーデータ作成
```sh
$ docker compose exec web uv run python manage.py make_dummy_blog_author
$ docker compose exec web uv run python manage.py make_transaction_dummy_model
$ docker compose exec web uv run python manage.py make_dummy_blog_generic_foreign_key_model
```

### pyrefly を試す

```sh
$ docker compose exec web uv run pyrefly init

$ docker compose exec web uv run pyrefly check --suppress-errors
$ docker compose exec web uv run pyrefly check --remove-unused-ignores
```

