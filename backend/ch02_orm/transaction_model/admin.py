from django.contrib import admin

from ch02_orm.transaction_model.models import WebUser, WebUserProfile

# Register your models here.
admin.site.register(WebUser)
admin.site.register(WebUserProfile)
