from django.contrib import admin

from post.models import Category, Comment, Post, Tag

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
