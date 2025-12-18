from django.core.management.base import BaseCommand
from django.db import connection

from ch02_orm.author.models import Author


class Command(BaseCommand):
    help = "Get count"

    def handle(self, *args, **options):
        # 〜.count() が int 担ってしまうので、 〜.count().query はエラーになる
        # クエリは取得できない
        # author_count = (
        #     Author.objects.filter(email__endswith="example.net").count().query
        # )
        # print(author_count, flush=True)

        # 下記のようにすると、クエリを取得できる
        # ただし、デバッグモードの時のみ
        author_count = Author.objects.filter(email__endswith="example.net").count()
        print(connection.queries[-1], flush=True)
