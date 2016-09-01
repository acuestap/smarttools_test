from django.contrib.auth import authenticate, login
import json
from celery import chain
from .tasks import *

'''
    Perform login
'''


def login_request_from_model(request):
    json_user = json.loads(request.body.decode('utf-8'))

    print(json_user)

    username = 'admin' #json_user.get('username')
    password = 'admin123'#json_user.get('password')

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

def tareas():

    workflow = chain(convert_video.s('Convirtiendo videos.'))
    workflow.delay()

    workflow2 = chain(send_confirmation_video.s('Enviando confirmación de video.'))
    workflow2.delay()