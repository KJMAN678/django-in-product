from django.core.management.base import BaseCommand

from or_create.models import OrCreateModel


class Command(BaseCommand):
    help = "Get | Update or Create"

    def handle(self, *args, **options):
        object1, created1 = OrCreateModel.objects.get_or_create(
            # 検索条件
            first_name="John",
            last_name="Doe",
            # defaults は作成時にのみ使用される
            defaults={
                "birthday": "1990-01-01",
            },
        )
        self.stdout.write(
            self.style.SUCCESS(f"object1: {object1}, created1: {created1}")
        )

        object2, created2 = OrCreateModel.objects.get_or_create(
            # 検索条件
            first_name="John",
            last_name="Doe",
            # defaults は作成時にのみ使用される
            defaults={
                "birthday": "1990-01-01",
            },
        )
        self.stdout.write(
            self.style.SUCCESS(f"object2: {object2}, created2: {created2}")
        )

        object3, created3 = OrCreateModel.objects.update_or_create(
            # 検索条件
            first_name="John",
            last_name="Doe",
            birthday="1990-01-01",
            # defaults は更新 or 作成に使用される
            defaults={
                "first_name": "Charlie",
                "last_name": "Brown",
                "birthday": "1995-05-15",
            },
        )
        self.stdout.write(
            self.style.SUCCESS(f"object3: {object3}, created3: {created3}")
        )
