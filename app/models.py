from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.

class Posts(models.Model):
    post_avatar = models.ImageField('Avatar', upload_to='post-avatar/')
    header = models.CharField('Header', max_length=30)
    text = models.TextField('Text', max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField('Post key(generate automat)', max_length=20)

    def __str__(self):
        return self.header

class Like(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.header

class Comment(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    key = models.CharField(max_length=20)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_avatar/', default='default_avatar/user.png')

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed = models.ManyToManyField(User, blank=True, related_name='My_Subscribed')
