from django.db import models
from rest_framework import serializers

from ch02_orm.blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    # pyrefly: ignore [bad-override]
    class Meta:
        model = Blog
        fields = "__all__"
