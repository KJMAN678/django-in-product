from django.apps import AppConfig
from django.core.signals import request_finished


class BulkCreateTroubleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ch02_orm.bulk_create_trouble"

    def ready(self):
        from ch02_orm.bulk_create_trouble import handlers
