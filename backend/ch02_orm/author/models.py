from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}-{self.id}"


class Author2(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def get_author_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_short_bio(self) -> str:
        return f"{self.bio[:200]}..."
