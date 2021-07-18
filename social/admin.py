from django.contrib import admin
from .models import Post, ThreadModel, UserProfile, Comment, Notification

# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(ThreadModel)