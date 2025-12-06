from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from author.models import Author, Author2
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
            Author2.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                bio=faker.text(max_nb_chars=500),
            )
        self.stdout.write(self.style.SUCCESS("3件のブログと著者を作成しました"))
