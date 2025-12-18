from datetime import datetime

from django.db import models

from ch02_orm.author.models import Author


class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseTimeStampModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("author.Author", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class CoverImage(BaseTimeStampModel):
    image_link = models.URLField()
    # 1対1
    blog = models.OneToOneField(
        "Blog", related_name="blog_ci", on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.image_link


# class BlogTag(models.Model):
#     blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
#     tag = models.ForeignKey("Tag", on_delete=models.CASCADE)


# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#     blog = models.ManyToManyField("Blog", related_name="blog_tags", through="BlogTag")


class Tag(BaseTimeStampModel):
    name = models.CharField(max_length=100)
    blog = models.ManyToManyField("Blog", related_name="blog_tags")

    def __str__(self) -> str:
        return self.name


# マルチテーブル継承
class BlogAuthor(Author):
    # Proxy モデル: データベースにテーブルを作成しない。
    # Author モデルをラップする
    class Meta:
        proxy = True

    def perform_something(self):
        pass
