# Generated by Django 4.1.6 on 2023-05-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_posts_comments_remove_posts_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='key',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
