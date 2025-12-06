from django.core.management.base import BaseCommand

from model_manager.models import Invoice


class Command(BaseCommand):
    help = "Get invoice data count"

    def handle(self, *args, **options):
        # pyrefly: ignore [missing-attribute]
        invoice_data_count = Invoice.objects.get_invoice_data_count()
        print(invoice_data_count, flush=True)
