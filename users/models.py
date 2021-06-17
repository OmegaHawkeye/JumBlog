from django.db import models
from django.contrib.auth.models import AbstractUser#,AbstractBaseUser,PermissionsMixin,BaseUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(default="profile_pics/default.jpg",upload_to="profile_pics/")
    newsletter = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False,help_text="Designates whether this user is a supporter and has access to the supporter ticket list view")


# class CustomUserManager(BaseUserManager):

#     def create_user(self,email,username,password,**other_fields):
#         if not email:
#             raise ValueError("You must provide an email address")

#         email = self.normalize_email(email)
#         user = self.model(email=email,username=username,**other_fields)

#         user.set_password(password)
#         user.save()

#         return user

#     def create_sueruser(self,email,username,password,**other_fields):
#         other_fields.setdefault("is_staff",True)
#         other_fields.setdefault("is_supporter",True)
#         other_fields.setdefault("is_superuser",True)
#         other_fields.setdefault("is_active",True)

#         if other_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must be assigned to is_staff=True.")
        
#         if other_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must be assigned to is_superuser=True.")
        
#         if other_fields.get("is_supporter") is not True:
#             raise ValueError("Superuser must be assigned to is_supporter=True.")

#         return self.create_user(email,username,password,**other_fields)


# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     username = models.CharField(max_length=150,unique=True)
#     image = models.ImageField(default="profile_pics/default.jpg",upload_to="profile_pics/")
#     newsletter = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_supporter = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     object = CustomUserManager()

#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
