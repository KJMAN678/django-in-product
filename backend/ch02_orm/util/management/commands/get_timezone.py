from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from ch02_orm.blog.models import Blog


class Command(BaseCommand):
    help = "Get timezone"

    def handle(self, *args, **options):
        print(timezone.now(), flush=True)
        print(datetime.now(), flush=True)
