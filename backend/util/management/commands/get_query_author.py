from django.core.management.base import BaseCommand, CommandError

from author.models import Author


class Command(BaseCommand):
    help = "Get query"

    def handle(self, *args, **options):
        try:
            # モデルインスタンス
            author = Author.objects.get(id=1)
            # Queryset
            all_blogs_by_author = author.blog_set.all()
            # Queryset
            selected_blog = author.blog_set.filter(title__contains="中世")
        except Author.DoesNotExist:
            raise CommandError("Blog does not exist")

        self.stdout.write(self.style.SUCCESS(author))
        self.stdout.write(self.style.SUCCESS(all_blogs_by_author))
        self.stdout.write(self.style.SUCCESS(selected_blog))
