# Generated by Django 3.2.3 on 2021-08-16 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210815_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='image',
            new_name='badge',
        ),
    ]