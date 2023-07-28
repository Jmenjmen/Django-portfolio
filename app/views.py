import random

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView
from app.models import *
from django.core import serializers


# Create your views here.

def main(request):
    try:
        profile1 = Profile.objects.get(user=request.user)
        context = {
            'profile': profile1
        }
        return render(request, 'index.html', context=context)
    except Exception:
        return render(request, 'index.html')

class posts(ListView):
    model = Posts
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            profile = Profile.objects.get(user=self.request.user)
            context['profile'] = profile
        except Exception:
            pass
        return context

    def get_queryset(self):
        posts = Posts.objects.all()
        p = Paginator(posts, 7)
        current_page = self.request.GET.get('p')
        p_page = p.get_page(current_page)
        return p_page

class post(ListView):
    model = Posts
    template_name = 'post.html'
    context_object_name = 'post'

    def get_queryset(self):
        key = self.request.GET.get('k')
        post_name = self.kwargs['slug']
        post = Posts.objects.get(header=post_name, key=key)
        return post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            profile = Profile.objects.get(user=self.request.user)
            context['profile'] = profile
        except Exception:
            pass
        key = self.request.GET.get('k')
        post_name = self.kwargs['slug']
        post = Posts.objects.get(header=post_name, key=key)
        subsc = Subscribe.objects.filter(subscribed__username=post.owner.username)
        try:
            test = Subscribe.objects.get(user=self.request.user, subscribed=post.owner)
            context['test'] = test
        except Exception:
            pass
        context['subsc'] = subsc
        context['like'] = Like.objects.filter(post=post)
        context['comments'] = Comment.objects.filter(post=post)
        context['total_likes'] = Like.objects.filter(post=post)
        return context

def MyProfile(request):
    profile = Profile.objects.get(user=request.user)
    myPosts = Posts.objects.filter(owner=request.user)
    likes = Like.objects.filter(post__owner=request.user)
    subscribers = Subscribe.objects.filter(subscribed=request.user)
    subscribed = Subscribe.objects.get(user=request.user)
    context = {
        'profile': profile,
        'myPosts': myPosts,
        'likes': likes,
        'subscribers': subscribers,
        'subsribed': subscribed
    }
    return render(request, 'profile.html', context=context)

def MakePost(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        avatar = request.FILES.get('avatar')
        text = request.POST.get('text')
        key = random.randint(1, 99999999999)
        Posts.objects.create(post_avatar=avatar, header=header, text=text, owner=request.user, key=key)
        return redirect('post', slug=header)
    else:
        return render(request, 'make.html')

def like(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        key = request.POST.get('key')
        post = Posts.objects.get(header=header, key=key)

        like, created = Like.objects.get_or_create(post=post, owner=request.user)
        total_likes = Like.objects.filter(post=post)

        if not created:
            like.delete()

        content = {
            'post': created,
            'total_likes': str(total_likes.count())
        }

        return JsonResponse(content)

def comment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        header = request.POST.get('header')
        key = request.POST.get('key')
        post = Posts.objects.get(header=header, key=key)
        key1 = random.randint(0, 99999999999)

        com = Comment.objects.create(owner=request.user, post=post, comment=text, key=key1)

        com.save()

        content = {
            'key': com.key,
            'owner': request.user.username,
            'post': post.header,
        }

        return JsonResponse(content)

def delete_comment(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        header = request.POST.get('header')
        comment_text = request.POST.get('text')
        owner = request.user

        com = Comment.objects.get(owner=owner, key=key, comment=comment_text, post__header=header)

        com.delete()

        context = {
            'access': 'ok!!!'
        }

        return JsonResponse(context)

def subscribe(request):
    if request.method == 'POST':
        s, created = Subscribe.objects.get_or_create(user=request.user)
        val = request.POST.get('sbc')

        try:
            Subscribe.objects.get(user=request.user, subscribed__username=val)
            s.subscribed.remove(User.objects.get(username=val))
        except Exception:
            s.subscribed.add(User.objects.get(username=val))
        s.save()

        subsc = Subscribe.objects.filter(subscribed__username=val).count()

        context = {
            'success': str(subsc)
        }
        return JsonResponse(context)