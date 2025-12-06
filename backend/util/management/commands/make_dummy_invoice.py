from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from model_manager.models import Invoice


class Command(BaseCommand):
    help = "Make dummy data for invoice"

    def handle(self, *args, **options):
        faker = Faker(["ja_JP"])
        for _ in range(3):
            Invoice.objects.create(
                invoice_number=faker.ean(),
                invoice_date=faker.date_time(),
                invoice_amount=faker.pyint(min_value=1, max_value=99),
            )

        self.stdout.write(self.style.SUCCESS("3件の請求書データを作成しました"))
