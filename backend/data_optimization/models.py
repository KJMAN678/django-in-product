from django.db import models


class IndexedModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["first_name"]),
        ]
