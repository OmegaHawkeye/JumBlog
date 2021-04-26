from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = RichTextField()
    image_url = models.URLField(null=True,blank=True)
    needed_xp = models.PositiveIntegerField(default=10)
    gained_xp = models.PositiveIntegerField(default=5)
    listen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} created by {self.author}'
