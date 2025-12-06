from django.contrib import admin

from blog.models import Blog, CoverImage, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author")


@admin.register(CoverImage)
class CoverImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_link", "blog")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
