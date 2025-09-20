from django.db import models
from django.contrib.auth.models import AbstractUser

class Wish(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    pass

