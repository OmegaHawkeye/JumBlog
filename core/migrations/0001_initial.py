# Generated by Django 3.2.3 on 2021-08-23 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('content', tinymce.models.HTMLField()),
                ('image_thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='article_pics/')),
                ('category', models.CharField(blank=True, choices=[('WebDevelopment', 'Web Development'), ('Covid19', 'Covid-19'), ('Entertainment', 'Entertainment'), ('Music', 'Music'), ('News', 'News'), ('Movies', 'Movies')], max_length=155, null=True)),
                ('bookmarked', models.BooleanField(default=False)),
                ('allow_comments', models.BooleanField(default=True)),
                ('published', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='article_likes', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
