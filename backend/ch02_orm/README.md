### カスタムコマンド実行
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

### 非同期処理

- [非同期サポート](https://docs.djangoproject.com/ja/5.2/topics/async/)
- [非同期クエリ](https://docs.djangoproject.com/ja/5.2/topics/db/queries/#asynchronous-queries)
- [トランザクション](https://docs.djangoproject.com/ja/6.0/topics/db/queries/#transactions)
  - トランザクションは現在、非同期クエリや更新ではサポートされていない

- [Python 非同期処理](https://docs.python.org/ja/3.14/library/asyncio-task.html)

- メモ
  - Django 非同期処理が活きるパターンとは
  - Django 非同期処理 でなんとかトランザクションするには
