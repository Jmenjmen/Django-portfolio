# Generated by Django 4.1.6 on 2023-05-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
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
        migrations.AddField(
            model_name='posts',
            name='comments',
            field=models.ManyToManyField(to='app.comment'),
        ),
        migrations.AddField(
            model_name='posts',
            name='liked',
            field=models.ManyToManyField(to='app.like'),
        ),
    ]
