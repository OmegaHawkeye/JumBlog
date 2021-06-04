from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/default.jpg",upload_to="profile_pics/")
    newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username