# Generated by Django 3.2.3 on 2021-08-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210812_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='price',
            field=models.PositiveBigIntegerField(default=10),
        ),
    ]