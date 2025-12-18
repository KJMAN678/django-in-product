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
    -> [Djnago 6.0 でも非対応](https://docs.djangoproject.com/ja/6.0/topics/async/#:~:text=%E3%83%88%E3%83%A9%E3%83%B3%E3%82%B6%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AF%E9%9D%9E%E5%90%8C%E6%9C%9F%E3%83%A2%E3%83%BC%E3%83%89%E3%81%A7%E3%81%AF%E3%81%BE%E3%81%A0%E6%A9%9F%E8%83%BD%E3%81%97%E3%81%BE%E3%81%9B%E3%82%93%E3%80%82%E3%82%82%E3%81%97%E3%83%88%E3%83%A9%E3%83%B3%E3%82%B6%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E5%8B%95%E4%BD%9C%E3%81%8C%E5%BF%85%E8%A6%81%E3%81%AA%E3%82%B3%E3%83%BC%E3%83%89%E3%81%8C%E3%81%82%E3%82%8B%E5%A0%B4%E5%90%88%E3%81%AF%E3%80%81%E3%81%9D%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%921%E3%81%A4%E3%81%AE%E5%90%8C%E6%9C%9F%E7%9A%84%E3%81%AA%E9%96%A2%E6%95%B0%E3%81%A8%E3%81%97%E3%81%A6%E6%9B%B8%E3%81%84%E3%81%A6%E3%80%81sync_to_async()%20%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%99%E3%81%93%E3%81%A8%E3%82%92%E3%81%8A%E3%81%99%E3%81%99%E3%82%81%E3%81%97%E3%81%BE%E3%81%99%E3%80%82)
    - コードを1つの同期的な関数として書いて、sync_to_async() を使用して呼び出す必要あり
    - [select_for_update](https://docs.djangoproject.com/ja/6.0/ref/models/querysets/#select-for-update)は、トランザクションが終了するまで行をロックし、サポートされているデータベース上で SELECT ... FOR UPDATE SQL 文を生成する QuerySet を返す
