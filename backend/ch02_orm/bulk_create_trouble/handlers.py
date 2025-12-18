from django.db.models.signals import pre_save
from django.dispatch import receiver

from ch02_orm.bulk_create_trouble.models import SampleModel, SignalTriggerModel


@receiver(pre_save, sender=SignalTriggerModel)
def my_handler(sender, **kwargs):
    SampleModel.objects.create(name="signal fired!")
