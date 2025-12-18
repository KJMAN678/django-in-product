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

### 保留 backend
```sh
$ docker compose exec web uv add Django==5.2.8
$ docker compose exec web uv add --dev Django==5.2.8

# 最初の1回のみ プロジェクト作成
$ mkdir backend
$ docker compose exec web uv run django-admin startproject config backend/api/

# app 追加
$ mkdir backend/async
$ docker compose exec web uv run django-admin startapp async async

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
```

### ダミーデータ作成
```sh
$ docker compose exec web uv run python manage.py make_dummy_blog_author
$ docker compose exec web uv run python manage.py make_transaction_dummy_model
$ docker compose exec web uv run python manage.py make_dummy_blog_generic_foreign_key_model
```

```sh
$ docker compose exec web uv run python manage.py get_query_blog
$ docker compose exec web uv run python manage.py get_query_author
# 生のクエリを出力
$ docker compose exec web uv run python manage.py get_by_raw_query
# count を取得
$ docker compose exec web uv run python manage.py get_count
# datetime.datetime は出来ないが、django.utils.timezone.now なら timezone 情報を取得できる
$ docker compose exec web uv run python manage.py get_timezone

$ docker compose exec web uv run python manage.py get_query_author2

$ docker compose exec web uv run python manage.py get_invoice_count

$ docker compose exec web uv run python manage.py get_explain
$ docker compose exec web uv run python manage.py get_queryset

# あまりクエリに違いがなかった
$ docker compose exec web uv run python manage.py get_bad_query

# N+1 問題
$ docker compose exec web uv run python manage.py get_n_plus_1

# bulk create はシグナル pre_save が実行されない
$ docker compose exec web uv run python manage.py do_bulk_create_no_signal
# bulk create は Baseモデルを継承したモデルでは動作しない
$ docker compose exec web uv run python manage.py do_bulk_create_no_multi_table_inheritance

$ docker compose exec web uv run python manage.py do_bulk_create_many_to_many_model

$ docker compose exec web uv run python manage.py get_update_or_create
```

### pyrefly を試す

```sh
$ docker compose exec web uv run pyrefly init

$ docker compose exec web uv run pyrefly check --suppress-errors
$ docker compose exec web uv run pyrefly check --remove-unused-ignores
```

### FSM による状態管理
- [django-fsm-2](https://github.com/django-commons/django-fsm-2)
- [django-fsm-2-admin](https://github.com/coral-li/django-fsm-2-admin)
- [django-fsm を使って Django の状態遷移を管理する](https://joseph-fox.co.uk/tech/manage-state-transitions-django-fsm-guide)

### インデックスの使用
- デフォルトの id フィールドはインデックス作成済み
- 主キー、ForeignKey、OneToOneField はデフォルトでインデックス作成済み
- インデックスを作成すると、データの取得が高速化されるが、テーブルの書き込み速度が低下する
- クラスター化インデックスは、データアクセスパターンを分析した後に使用すべき

### Database 設定

- [持続的 (persistent) な接続](https://docs.djangoproject.com/ja/5.2/ref/databases/#persistent-connections)
  - `CONN_MAX_AGE` を設定することで、接続を保持する時間を設定できる
    - デフォルトは 0 で、接続を保持しない
