from django.db import models


# Create your models here.
class SignalTriggerModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SampleModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChildModel(BaseModel):
    name_child_only = models.CharField(max_length=100)


class OneModel(models.Model):
    name = models.CharField(max_length=100)


class ManyToManyModel(models.Model):
    name = models.CharField(max_length=100)
    many_to_many = models.ManyToManyField(OneModel)
