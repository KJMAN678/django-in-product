from django.db import models
from rest_framework import serializers

from ch02_orm.blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    # create メソッドをオーバーライドして、独自処理を追加する
    def create(self, validated_data):
        print("***カスタム作成メソッド***")
        return super(BlogSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        print("***カスタム更新メソッド***")
        return super(BlogSerializer, self).update(instance, validated_data)

    class Meta:  # pyrefly: ignore [bad-override]
        model = Blog
        fields = "__all__"
