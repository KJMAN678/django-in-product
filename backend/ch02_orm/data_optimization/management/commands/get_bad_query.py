from django.core.management.base import BaseCommand

from ch02_orm.author.models import Author
from ch02_orm.blog.models import Blog


def filtered_authors():
    # 何か複雑な条件で絞り込む
    return Author.objects.filter(name__startswith="鈴木", email__endswith="example.net")


def filtered_authors_2():
    return Author.objects.filter(
        name__startswith="鈴木", email__endswith="example.net"
    ).values_list("id", flat=True)


class Command(BaseCommand):
    help = "Get bad query"

    def handle(self, *args, **options):
        # DB によって JOIN になったり、WHERE user_id IN (SELECT ...) のサブクエリになったりします。
        # もし Blog.objects.filter(author__in=...) の author__in にインデックスが無かったり、
        # サブクエリ側もインデックスをうまく使えていない
        # と、巨大なテーブル同士の結合 / サブクエリになり、パフォーマンスが落ちる可能性がある
        qs = Blog.objects.filter(author__in=filtered_authors())
        # print(qs.explain(verbose=True, analyze=True), flush=True)
        print(qs.query, flush=True)

        print("--------------------------------")

        # クエリセットを評価してから使う
        # active_author_ids() を呼んだ時点で 1 回目の SELECT が発行され、
        # 結果（id のリスト）が Python 側に取ってこられる
        # そのあと Blog.objects.filter(author__in=...) で 2 回目の SELECT が発行される
        qs = Blog.objects.filter(author__in=filtered_authors_2())
        # print(qs.explain(verbose=True, analyze=True), flush=True)
        print(qs.query, flush=True)
