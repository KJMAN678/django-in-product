from django.core.management.base import BaseCommand, CommandError
from django.db import DatabaseError, transaction
from faker import Faker

from transaction_model.models import WebUser, WebUserProfile


class Command(BaseCommand):
    help = "Make dummy data for transaction model"

    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker(["ja_JP"])

        WebUser.objects.create(
            name=faker.name(),
            is_staff=faker.boolean(),
        )

        raise ValueError("test")

        WebUserProfile.objects.create(
            user=WebUser.objects.get(id=id),
            profile_image=faker.image_url(),
            bio=faker.text(),
        )

        self.stdout.write(self.style.SUCCESS("1件のUUIDモデルデータを作成しました"))
