from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, ImageField
from rest_framework import serializers


class Competition(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='static/upload_files/competitions/images', null=True)
    url = models.CharField(max_length=200, null=False)
    startingDate = models.DateTimeField(null=False)
    deadline = models.DateTimeField(null=False)
    description = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(User, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

'''
# class CompetitionForm(serializers.ModelSerializer):
class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        # read_only_fields = ('name', 'url', 'description', 'startingDate', 'deadline')
        fields = ['name', 'url', 'description', 'startingDate', 'deadline']
'''


class Video(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=True)
    state = models.BooleanField(null=False)
    user_email = models.CharField(max_length=60, null=False)
    uploadDate = models.DateTimeField(null=True)
    message = models.CharField(max_length=1000, null=False)
    competition = models.ForeignKey(Competition, null=False)
    original_video = models.FileField(upload_to='static/upload_files/competitions/videos', null=True)
    converted_video = models.FileField(upload_to='static/upload_files/competitions/videos', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['uploadDate']


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'user_email', 'message','original_video']
