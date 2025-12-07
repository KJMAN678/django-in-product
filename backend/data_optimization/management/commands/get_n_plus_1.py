from django.core.management.base import BaseCommand
from django.db import connection, reset_queries

from author.models import Author
from blog.models import Blog


def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func(*args, **kwargs)
        query_info = connection.queries
        print(f"function_name:  {func.__name__}")
        print(f"query_count: {len(query_info)}", flush=True)
        query = [f"{query['sql']}\n" for query in query_info]
        # クエリを出力すると、大量のクエリが出力されるので、コメントアウト
        # print(f"query: \n{''.join(query)}")
        return results

    return inner_func


@database_debug
def regular_query():
    blogs = Blog.objects.all()

    return [blog.author.name for blog in blogs]


@database_debug
def select_related_query():
    # select_related は、JOIN を使用して、関連するモデルを１度のクエリで取得する
    blogs = Blog.objects.select_related("author").all()

    return [blog.author.name for blog in blogs]


@database_debug
def prefetch_related_query():
    # prefetch_related は、モデルごとにクエリを実行し、Python 側で結合する
    blogs = Blog.objects.prefetch_related("author").all()
    return [blog.author.name for blog in blogs]


class Command(BaseCommand):
    help = "Get N+1 query"

    def handle(self, *args, **options):
        regular_query()
        select_related_query()
        prefetch_related_query()
