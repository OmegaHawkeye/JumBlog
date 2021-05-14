# Generated by Django 3.2.3 on 2021-05-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_ticket_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]