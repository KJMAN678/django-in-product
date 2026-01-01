from django.core.management.base import BaseCommand

from ch02_orm.blog.models import Blog
from ch03_drf_serialize.model_serializer.models import BlogSerializer


class Command(BaseCommand):
    help = "Create by serializer"

    def handle(self, *args, **options):
        update_input_data = {
            "title": "updated blog title",
        }
        existing_blog = Blog.objects.get(id=1000)
        updated_blog = BlogSerializer(
            instance=existing_blog, data=update_input_data, partial=True
        )
        updated_blog.is_valid()
        updated_blog.save()
        self.stdout.write(self.style.SUCCESS(f"{updated_blog}"))
