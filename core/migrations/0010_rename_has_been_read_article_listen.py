# Generated by Django 3.2 on 2021-04-23 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210422_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='has_been_read',
            new_name='listen',
        ),
    ]
