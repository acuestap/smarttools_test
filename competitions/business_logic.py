import os
import json
import time
import base64

from django.core.files.base import ContentFile
from django.db.models.fields.files import ImageFieldFile
from django.views.decorators.csrf import csrf_exempt

from web.models import Competition, User



'''
    Transform product to json format
'''


def competition_to_json(competition):
    image_path = '/static/img/profile.png'
    if isinstance(competition.image, ImageFieldFile):
        try:
            image_path = competition.image.path
        except ValueError as e:
            image_path = '/static/img/profile.png'

    object = {
        'id': competition.id,
        'name': competition.name,
        'image': image_path,
        'url': competition.url,
        'startingDate': competition.startingDate,
        'deadline': competition.deadline,
        'active': competition.active
    }
    return object

'''
    Method returning all competitions
'''


def get_competitions_from_model(request):

    competitions = []
    if request.user.is_authenticated():
        idUser = request.user.id
        user = User.objects.get(id=idUser)

    for c in Competition.objects.filter(user=user).all():
        competitions.append(competition_to_json(c))

    return competitions


def handle_uploaded_file(f):
    with open('/upload_files/competitions/images/noborrar.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def create_competition_in_model(request):
    status = 'Error'

    if request.method == 'POST':
        json_competition = json.loads(request.body.decode('utf-8'))

        name = json_competition.get('name')
        url = json_competition.get('url')
        startingdate = json_competition.get('startingDate')
        deadline = json_competition.get('deadline')
        description = json_competition.get('description')
        fileString = json_competition.get('fileString')
        # print(json_competition)

        print("FIN _ STRING")
        #Para el manejo de la imagen o archivos tipo upload

        base64_string = fileString.encode('utf-8')
        filename = str(time.time())+".png"

        # decoding base string to image and saving in to your media root folder
        fh = open(os.path.join("upload_files/competitions/images/", filename), "wb")
        # fh.write(bytes(base64_string.decode('base64')))
        # fh.write(base64.b64decode(bytes(base64_string.decode('base64'), 'utf-8', '')))
        fh.write(bytes(base64_string))
        '''
        with open(os.path.join("upload_files/competitions/images/", filename), 'wb+') as fh:
            for chunk in json_competition['image'].chunks():
                fh.write(chunk)
        '''
        fh.close()
        # saving decoded image to database
        # decoded_image = base64_string.decode('base64')
        decoded_image = base64_string.decode('utf-8')
        # Fin del manejo de archivos tipo upload

        # Se verifica si el usuario actual se encuentra auteticado.

        if request.user.is_authenticated():
            idUser = request.user.id

            # Se verifica si todos los datos obligatorios fueron ingresados.'
            if idUser > 0 and name != "" and url != "" and startingdate != "" and deadline != "" and description != "":

                user = User.objects.get(id=idUser)
                # Se verifica que no exista una competencia igual.
                existcompetition = Competition.objects.filter(name=name, url=url, user=user)

                if existcompetition.count() > 0:
                    status = 'El concurso ya existe.'
                else:

                    # formcompetition = CompetitionForm(request.POST, request.FILES)
                    print("INICIO.....")
                    # http://blog.josephmisiti.com/how-to-upload-a-photo-to-django-using-ios
                    # if formcompetition.is_valid():
                    # print(request.FILES)
                    # handle_uploaded_file(request.FILES['image', ''])
                    print("FIN.....")

                    '''
                    new_competition = Competition(name=request.POST.get('name'),
                                                  url=request.POST.get('url'),
                                                  startingDate=request.POST.get('startingDate'),
                                                  deadline=request.POST.get('deadline'),
                                                  image=formcompetition.cleaned_data['image'],
                                                  description=request.POST.get('description'),
                                                  user=user)
                    new_competition.save()
                    '''

                    competitionmodel = Competition()
                    competitionmodel.name = name
                    competitionmodel.url = url
                    competitionmodel.startingDate = startingdate
                    competitionmodel.deadline = deadline
                    competitionmodel.description = description
                    competitionmodel.user = user
                    competitionmodel.imagen = ContentFile(decoded_image, filename)
                    competitionmodel.save()

                    status = 'OK'
                    # else:
                        # status = 'Campos incompletos.'
            else:
                status = 'Todos los campos son obligatorios.'
        else:
            status = 'Cliente no autenticado'
    else:
        status = 'Metodo no POST.'

    return {'status': status}
