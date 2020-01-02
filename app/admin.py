from django.contrib import admin

# Register your models here.
from .models import Event, Comment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'
