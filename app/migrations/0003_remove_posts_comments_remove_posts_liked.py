# Generated by Django 4.1.6 on 2023-05-10 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_posts_comments_remove_posts_liked_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='liked',
        ),
    ]
