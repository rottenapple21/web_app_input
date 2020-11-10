from django.contrib import admin
from .models import Kurasi, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]

admin.site.register(Kurasi, BlogAdmin)
