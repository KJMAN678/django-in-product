from django.apps import AppConfig
from django.core.signals import request_finished


class BulkCreateTroubleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bulk_create_trouble"

    def ready(self):
        from bulk_create_trouble import handlers
