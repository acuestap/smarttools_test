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

    print(json_user)

    username = 'admin'  # json_user.get('username')
    password = 'admin123'  # json_user.get('password')

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
    Method returning all videos
'''


def get_videos_from_model():
    videos = []

    allVideos = Video.objects.all()

    if allVideos is None:
        return videos
    else:
        for c in allVideos:
            videos.append(video_to_json(c))

    return videos


'''
    Transform product to json format
'''


def video_to_json(video):
    object = {
        'id': video.id,
        'name': video.name,
        'state': video.state,
        'user_email': video.user_email,
        'uploadDate': video.uploadDate,
        'message': video.message,
        'original_video': video.original_video
    }
    return object


def tareas(originPath, user_email):
    workflow = chain(convert_video.s(originPath))
    workflow.delay()

    workflow2 = chain(send_confirmation_video.s(user_email))
    workflow2.delay()


def validateConvert(user_email, original_video):
    tareas(original_video, user_email)
    print(user_email)
    print(original_video)
