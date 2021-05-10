from django.contrib import admin
from django.db import models
from .models import Article
from martor.widgets import AdminMartorWidget
from image_cropping import ImageCroppingMixin

class ArticleAdmin(ImageCroppingMixin,admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
admin.site.register(Article,ArticleAdmin)