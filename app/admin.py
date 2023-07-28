from django.contrib import admin
from app.models import *

# Register your models here.

@admin.register(Posts)
class post(admin.ModelAdmin):
    search_fields = ['header', 'key']
    list_display = ['header']
    list_display_links = ['header']

@admin.register(Like)
class like(admin.ModelAdmin):
    search_fields = ['post']
    list_display = ['post']
    list_display_links = ['post']

    def post(self, obj):
        obj.post.header

@admin.register(Comment)
class comment(admin.ModelAdmin):
    search_fields = ['post']
    list_display = ['post']
    list_display_links = ['post']

    def post(self, obj):
        obj.post.header

@admin.register(Profile)
class Prof(admin.ModelAdmin):
    search_fields = ['post']
    list_display = ['post']
    list_display_links = ['post']

    def post(self, obj):
        obj.user.username

@admin.register(Subscribe)
class sbc(admin.ModelAdmin):
    search_fields = ['post']
    list_display = ['post']
    list_display_links = ['post']

    def post(self, obj):
        obj.user.username