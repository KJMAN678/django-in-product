from django.core.management.base import BaseCommand

from ch03_drf_serialize.model_serializer.models import BlogSerializer


class Command(BaseCommand):
    help = "Show serializer"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f"{BlogSerializer()}"))
