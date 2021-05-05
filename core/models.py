from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
from martor.models import MartorField

CATEGORY_CHOICES = (
    ('WebDevelopment','Web Development'),
    ('Covid19','Covid-19'),
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # content = RichTextField()
    content = MartorField()
    image = models.ImageField(upload_to="article_pics/")
    category = models.CharField(max_length=155,choices=CATEGORY_CHOICES)
    tags = TaggableManager()
    bookmarked= models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    liked = models.ManyToManyField(User,related_name="article_likes",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} created by {self.author}'

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

class ArticleCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'created_at'
    moderate_after = 365


moderator.register(Article, ArticleCommentModerator)