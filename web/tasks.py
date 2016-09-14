from __future__ import absolute_import

import datetime
import random
import subprocess
from celery import task
from celery.decorators import periodic_task
from web.business_logic import all_video_to_convert, update_to_state_video


@periodic_task(run_every=datetime.timedelta(seconds=60), name="convert_video", ignore_result=True)
def convert_video():

    videos = []

    videos = all_video_to_convert()

    if not videos:
        print("No se puede convertir, No hay videos aún.... Esperando....")
    else:

        num = random.randrange(1000000000)

        for video in videos:

            path_converted = 'static\\upload_files\\competitions\\videos\\video_' + str(num) + '_' + str(video.id) + '.mp4'

            print('Ejecutando conversión de video ')

            resulted = subprocess.call(
                'ffmpeg -i ' + str(video.original_video) + '  -b 1500k -vcodec libx264 -g 30 ' + str(path_converted))

            if resulted != 0:
                print('Algo falló en la conversión del video %s', resulted)
            else:
                print('Video convertido ok')
                print(video.id)
                video.converted_video = path_converted
                update_to_state_video(video)
                send_confirmation_video(str(video.user_email), str(video.name))
            return 'Conversion de video Ok %s ' % resulted
        videos = []


def send_confirmation_video(user_email, name):
    from django.core.mail import send_mail

    try:
        send_mail(
            'Confirmación de video',
            'Hola, ' + name + ' tu video ha sido procesado y se encuentra publicado en el home del concurso. Gracias por participar en el concurso.',
            'smarttoolscloud@gmail.com',
            [user_email],
            fail_silently=False,
        )
    except:
        print
        "Error enviando el mail"

    return 'Correo enviado correctamente como tarea'
