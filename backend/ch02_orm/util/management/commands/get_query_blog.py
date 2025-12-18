from django.core.management.base import BaseCommand, CommandError

from ch02_orm.blog.models import Blog


class Command(BaseCommand):
    help = "Get query"

    def handle(self, *args, **options):
        try:
            author = Blog.objects.get(id=1).author
        except Blog.DoesNotExist:
            raise CommandError("Blog does not exist")

        self.stdout.write(self.style.SUCCESS(author))
