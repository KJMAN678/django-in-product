from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from author.models import Author
from blog.models import Blog


class Command(BaseCommand):
    help = "Make dummy data for blog and author"

    def handle(self, *args, **options):
        faker = Faker(["ja_JP"])
        for _ in range(3):
            author = Author.objects.create(
                name=faker.name(),
                email=faker.email(),
                bio=faker.text(),
            )
            Blog.objects.create(
                title=faker.sentence(),
                content=faker.text(),
                author=author,
            )
        self.stdout.write(self.style.SUCCESS("3件のブログと著者を作成しました"))
