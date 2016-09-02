from __future__ import absolute_import
import subprocess

from celery import task


@task
def convert_video(originPath,user_email):
    pathConverted = 'upload_files\\competitions\\videos\\convertido'+user_email+'.mp4'
    path = 'upload_files\\competitions\\videos\\video1.avi'
    print('Ejecutando conversión ...')
    resultado = subprocess.call('ffmpeg -i ' + originPath + '  -b 1500k -vcodec libx264 -g 30 ' + pathConverted)

    if resultado != 0:
        print('Algo falló en la conversión del video %s', resultado)
    else:
        print('Video convertido ok')

    return 'La tarea de conversion de video esta ok. %s ' % resultado


@task
def send_confirmation_video(user_email,name):
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

    return 'Ok tarea 2 y el parametro es:  "%s" ' % param
