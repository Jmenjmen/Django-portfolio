# Generated by Django 4.2.1 on 2023-05-13 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_userprofile_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='us',
            new_name='user',
        ),
    ]