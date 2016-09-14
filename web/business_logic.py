import random

from django.contrib.auth import authenticate, login
import json
from celery import chain
from .tasks import *
from .models import Video

'''
    Perform login
'''


def login_request_from_model(request):
    json_user = json.loads(request.body.decode('utf-8'))

    print("Autenticando...")
    print(json_user)
    username = json_user.get('username')
    password = json_user.get('password')
    print("username..." + username + "--password:" + password)

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        message = 'El usuario ha iniciado sesion'
        status = 'OK'

    else:
        message = 'Usuario o Clave incorrecta'
        status = 'ERROR'

    return {
        'username': username,
        'status': status,
        'message': message,
    }


'''
    Get all videos for convert
'''


def all_video_to_convert():
    videos_to = []
    videos = []

    videos = Video.objects.all()

    if not videos:
        print("Aún no hay videos")
    else:
        for video in videos:

            if video.state is False:

                videos_to.append(video)

    return videos_to

'''
    Update video after this was converted
'''


def update_to_state_video(video):

    video.state = True

    video.save()
