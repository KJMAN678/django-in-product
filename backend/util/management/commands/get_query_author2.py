from django.core.management.base import BaseCommand, CommandError

from author.models import Author2


class Command(BaseCommand):
    help = "Get query"

    def handle(self, *args, **options):
        try:
            # モデルインスタンス
            author = Author2.objects.get(id=1)
            print(author.get_author_name(), flush=True)
            print(author.get_short_bio(), flush=True)
        except Author2.DoesNotExist:
            raise CommandError("Blog does not exist")

        # pyrefly: ignore [bad-argument-type]
        self.stdout.write(self.style.SUCCESS(author))
