from django.db import models


# Create your models here.
class WebUser(models.Model):
    name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WebUserProfile(models.Model):
    user = models.OneToOneField(WebUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_images/")
    bio = models.TextField()

    def __str__(self):
        return self.user.name
