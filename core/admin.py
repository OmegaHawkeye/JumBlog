from django.contrib import admin
from django.db import models
from .models import Article,Task
from martor.widgets import AdminMartorWidget

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
admin.site.register(Article,ArticleAdmin)

admin.site.register(Task)

