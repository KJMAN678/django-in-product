from django.contrib import admin

from author.models import Author, Author2


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "bio")


@admin.register(Author2)
class Author2Admin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "bio")
