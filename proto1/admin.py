from django.contrib import admin
from .models import Event, Comment, Attend

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Attend)
class AttendAdmin(admin.ModelAdmin):
    pass

