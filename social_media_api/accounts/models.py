from django.contrib.auth.models import AbstractUser
from django.db import models
from taggit.managers import TaggableManager

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
