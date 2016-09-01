from __future__ import absolute_import
import subprocess

from celery import task


@task
def convert_video(param):
    pathConverted = 'upload_files\\competitions\\videos\\convertido.mp4'
    path = 'upload_files\\competitions\\videos\\video3.avi'
    print('Ejecutando conversión ...')
    resultado = subprocess.call('ffmpeg -i ' + path + '  -b 1500k -vcodec libx264 -g 30 ' + pathConverted)

    if resultado != 0:
        print('Algo falló en la conversión del video %s', resultado)
    else:
        print('Video convertido ok')

    return 'La tarea de conversion de video esta ok. %s ' % resultado


@task
def send_confirmation_video(param):
    from django.core.mail import send_mail
    try:
        send_mail(
            'Confirmación de video',
            'Hola, tu video ha sido procesado y se encuentra publicado en el home del concurso. Gracias por participar en el concurso.',
            'smarttoolscloud@gmail.com',
            ['yego23@gmail.com'],
            fail_silently=False,
        )
    except:
        print
        "Error enviando el mail"

    return 'Ok tarea 2 y el parametro es:  "%s" ' % param
