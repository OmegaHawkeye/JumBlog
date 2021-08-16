from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# class Badge(models.Model):
#     image = models.ImageField(upload_to="badge_pics/")

class Role(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Feature(models.Model):
    # badge = models.ForeignKey(Badge,on_delete=models.CASCADE,null=True,blank=True)
    badge = models.ImageField(upload_to="badge_pics/")
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(default=10)

    def __str__(self):
        return f'{self.name} for {self.price} XP Points'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(default="profile_pics/default.jpg",upload_to="profile_pics/")
    newsletter = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False,help_text="Designates whether this user is a supporter and has access to the supporter ticket list view")
    xp = models.PositiveBigIntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
    features = models.ManyToManyField(Feature,related_name="users_features")