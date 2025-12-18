from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from ch02_orm.uuid_model.models import MyUUIDModel


class Command(BaseCommand):
    help = "Make dummy data for invoice"

    def handle(self, *args, **options):
        faker = Faker(["ja_JP"])
        for _ in range(3):
            MyUUIDModel.objects.create(
                name=faker.name(),
            )

        self.stdout.write(self.style.SUCCESS("3件のUUIDモデルデータを作成しました"))
