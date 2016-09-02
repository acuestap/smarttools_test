from django.contrib import admin
from .models import Competition, Video


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'image', 'startingDate', 'deadline', 'user', 'active')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'user_email', 'competition', 'original_video', 'converted_video')
