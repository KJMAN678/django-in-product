from django.contrib import admin

from uuid_model.models import MyUUIDModel


# Register your models here.
@admin.register(MyUUIDModel)
class MyUUIDModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
