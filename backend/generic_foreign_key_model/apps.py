from django.apps import AppConfig


class GenericForeignKeyModelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "generic_foreign_key_model"
