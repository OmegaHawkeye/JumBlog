# Generated by Django 3.2.3 on 2021-05-27 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_article_likedcounter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likedCounter',
        ),
    ]
