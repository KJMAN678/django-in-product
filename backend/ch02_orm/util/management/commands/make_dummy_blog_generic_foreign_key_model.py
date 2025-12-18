import random

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from faker import Faker

from ch02_orm.author.models import Author
from ch02_orm.blog.models import Blog
from ch02_orm.generic_foreign_key_model.models import GenericForeignKeyModel


class Command(BaseCommand):
    help = "Make dummy data for generic foreign key model"

    def handle(self, *args, **options):
        faker = Faker(["ja_JP"])
        for _ in range(3):
            choiced_object = random.choice([Blog, Author])
            choiced_object_id = None

            if choiced_object == Blog:
                blog = Blog.objects.create(
                    title=faker.sentence(),
                    content=faker.text(),
                    author=Author.objects.get(id=1),
                )
                choiced_object_id = blog.id
            else:
                author = Author.objects.create(
                    name=faker.name(),
                    email=faker.email(),
                    bio=faker.text(),
                )
                choiced_object_id = author.id

            GenericForeignKeyModel.objects.create(
                name=faker.name(),
                content_type=ContentType.objects.get_for_model(choiced_object),
                object_id=choiced_object_id,
            )

        self.stdout.write(
            self.style.SUCCESS("3件のジェネリックフォーリンキーモデルを作成しました")
        )
