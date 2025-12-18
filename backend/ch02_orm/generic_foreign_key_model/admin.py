from django.contrib import admin

from ch02_orm.generic_foreign_key_model.models import GenericForeignKeyModel

# Register your models here.
admin.site.register(GenericForeignKeyModel)
