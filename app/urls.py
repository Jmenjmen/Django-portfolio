from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', main, name="home"),
    path('posts/', posts.as_view(), name='posts'),
    path('posts/<str:slug>/', post.as_view(), name="post"),
    path('MyProfile/', MyProfile, name='myProfile'),
    path('make/', MakePost, name='make'),
    path('like/', like),
    path('comment/', comment),
    path('delete_comment/', delete_comment),
    path('profile/', include('allauth.urls'), name="acc"),
    path('subscribe/', subscribe),
]