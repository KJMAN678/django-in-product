from django.core.management.base import BaseCommand

from blog.models import Blog


class Command(BaseCommand):
    help = "Get explain"

    def handle(self, *args, **options):
        # https://www.postgresql.org/docs/current/sql-explain.html
        print(
            Blog.objects.filter(title__contains="中世").explain(
                verbose=True, analyze=True
            ),
            flush=True,
        )

        print(
            Blog.objects.filter(id__in=[1, 2, 3]).explain(verbose=True, analyze=True),
            flush=True,
        )
