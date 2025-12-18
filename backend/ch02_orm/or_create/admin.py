from django.contrib import admin

# Register your models here.
from ch02_orm.or_create.models import OrCreateModel

admin.site.register(OrCreateModel)
