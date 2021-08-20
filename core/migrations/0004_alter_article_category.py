# Generated by Django 3.2.3 on 2021-08-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('WebDevelopment', 'Web Development'), ('Covid19', 'Covid-19'), ('Entertainment', 'Entertainment'), ('Music', 'Music'), ('News', 'News'), ('Movies', 'Movies')], max_length=155, null=True),
        ),
    ]
