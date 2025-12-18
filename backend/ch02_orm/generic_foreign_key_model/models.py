from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q

from ch02_orm.author.models import Author
from ch02_orm.blog.models import Blog


class GenericForeignKeyModel(models.Model):
    name = models.CharField(max_length=100)
    # target_content_type = ContentType.objects.get_for_models(Blog, Author)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            # モデル名を小文字にする必要あり
            # https://stackoverflow.com/questions/6335986/how-can-i-restrict-djangos-genericforeignkey-to-a-list-of-models
            "model__in": ["blog", "author"],
        },
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.name
