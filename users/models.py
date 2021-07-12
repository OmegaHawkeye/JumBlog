from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(default="profile_pics/default.jpg",upload_to="profile_pics/")
    newsletter = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False,help_text="Designates whether this user is a supporter and has access to the supporter ticket list view")
