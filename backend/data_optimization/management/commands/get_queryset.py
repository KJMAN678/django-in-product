from django.core.management.base import BaseCommand

from blog.models import Blog


class Command(BaseCommand):
    help = "Get queryset"

    def handle(self, *args, **options):
        # print文を実行する際に、下記３つのクエリが一度に実行される
        some_query = Blog.objects.filter(author__id=1)
        another_query = some_query.filter(title__startswith="中世")
        yet_another_query = another_query.filter(title__endswith="世界")
        print(yet_another_query, flush=True)
