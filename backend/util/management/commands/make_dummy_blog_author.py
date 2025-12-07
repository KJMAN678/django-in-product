from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from author.models import Author, Author2
from blog.models import Blog


class Command(BaseCommand):
    help = "Make dummy data for blog and author"

    def handle(self, *args, **options):
        faker = Faker(["ja_JP"])

        # まず全てのオブジェクトをリストに作成
        authors = []
        blogs = []
        author2s = []

        for _ in range(1000):
            authors.append(
                Author(
                    name=faker.name(),
                    email=faker.email(),
                    bio=faker.text(),
                )
            )
            author2s.append(
                Author2(
                    first_name=faker.first_name(),
                    last_name=faker.last_name(),
                    email=faker.email(),
                    bio=faker.text(max_nb_chars=500),
                )
            )

        # Authorを一括作成
        created_authors = Author.objects.bulk_create(authors)

        # Blogを作成（AuthorのIDを使用）
        for _, author in enumerate(created_authors):
            blogs.append(
                Blog(
                    title=faker.sentence(),
                    content=faker.text(),
                    author=author,
                )
            )

        # BlogとAuthor2を一括作成
        Blog.objects.bulk_create(blogs)
        Author2.objects.bulk_create(author2s)

        self.stdout.write(self.style.SUCCESS("1000件のブログと著者を作成しました"))
