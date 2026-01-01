from django.core.management.base import BaseCommand

from ch03_drf_serialize.model_serializer.models import BlogSerializer


class Command(BaseCommand):
    help = "Create by serializer"

    def handle(self, *args, **options):
        input_data = {
            "title": "new blog title",
            "content": "this is content",
            "author": 1,
        }
        new_blog = BlogSerializer(data=input_data)
        new_blog.is_valid()
        new_blog.save()
        self.stdout.write(self.style.SUCCESS(f"{new_blog}"))
