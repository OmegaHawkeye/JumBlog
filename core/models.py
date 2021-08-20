from django.urls import reverse
from django.db import models
from imagekit.models.fields import ProcessedImageField
from taggit.managers import TaggableManager
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
from imagekit.processors import ResizeToFill
import datetime
from django_project.settings import AUTH_USER_MODEL
from tinymce.models import HTMLField

CATEGORY_CHOICES = (
    ('WebDevelopment','Web Development'),
    ('Covid19','Covid-19'),
    ('Entertainment','Entertainment'),
    ('Music','Music'),
    ('News','News'),
    ('Movies','Movies'),
)

class Article(models.Model):
    title = models.CharField(max_length=100,unique=True)
    subtitle = models.CharField(max_length=100,null=True,blank=True)
    author = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    # content = MartorField()
    content = HTMLField()
    image_thumbnail = ProcessedImageField(blank=True,upload_to="article_pics/",processors=[ResizeToFill(400,400)],format='JPEG', options={'quality': 80})
    category = models.CharField(max_length=155,choices=CATEGORY_CHOICES,null=True,blank=True)
    tags = TaggableManager()
    bookmarked= models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    likes = models.ManyToManyField(AUTH_USER_MODEL,related_name="article_likes",blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} created by {self.author}'

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
    
    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def status(self):
        if self.published:
            return "Published"
        else:
            return "Drafted"

class ArticleCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'created_at'
    moderate_after = 365

moderator.register(Article, ArticleCommentModerator)

class Task(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} created by {self.creator}'

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('task-update', kwargs={'pk': self.pk})

    def get_deletion_url(self):
        return reverse('task-delete', kwargs={'pk': self.pk})

    @property
    def getStatus(self):
        if self.completed == False and ((self.end - datetime.datetime.now()) > datetime.timedelta(seconds=1)):
            return "Uncompleted"
        elif self.completed == False and (self.end - datetime.datetime.now()) < datetime.timedelta(seconds=1):
            return "Outdated"
        else:
            return "Completed"

