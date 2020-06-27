# Generated by Django 3.0.7 on 2020-06-21 06:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Content'),
        ),
    ]