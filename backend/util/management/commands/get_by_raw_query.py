from django.core.management.base import BaseCommand

from author.models import Author


class Command(BaseCommand):
    help = "Get by raw query"

    def handle(self, *args, **options):
        all_authors = (
            Author.objects.filter(email__endswith="example.net")
            .values_list("name")
            .query
        )
        print(all_authors, flush=True)
