from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
from martor.models import MartorField

class Category(models.Model):

    CATEGORIES = [
        ("Web Development","Web Development"),
        ("Covid-19","Covid-19")
    ]

    name = models.CharField(max_length=50,choices=CATEGORIES)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # content = RichTextField()
    content = MartorField()
    image = models.ImageField(upload_to="pics")
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = TaggableManager()
    bookmarked= models.BooleanField(default=False)
    liked = models.ManyToManyField(User,related_name="article_likes",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} created by {self.author}'

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

class ArticleCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'publish'
    moderate_after = 365


moderator.register(Article, ArticleCommentModerator)