from django.apps import AppConfig


class ModelManagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ch02_orm.model_manager"
