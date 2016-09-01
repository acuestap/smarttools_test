from django.db.models.fields.files import ImageFieldFile

from web.models import Competition, User, CompetitionForm
import json

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
        'deadline': competition.deadline
    }
    return object

'''
    Method returning all competitions
'''


def get_competitions_from_model():

    competitions = []

    for c in Competition.objects.all():
        competitions.append(competition_to_json(c))

    return competitions


def handle_uploaded_file(f):
    with open('/upload_files/competitions/images/noborrar.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def create_competition_in_model(request):
    status = 'Error'

    if request.method == 'POST':
        json_competition = json.loads(request.body.decode('utf-8'))

        name = json_competition.get('name')
        url = json_competition.get('url')
        startingdate = json_competition.get('startingDate')
        deadline = json_competition.get('deadline')
        description = json_competition.get('description')


        # Se verifica si el usuario actual se encuentra auteticado.

        if request.user.is_authenticated():
            idUser = request.user.id

            # Se verifica si todos los datos obligatorios fueron ingresados.'




            if name != "" and url != "" and startingdate != "" and deadline != "" and description != "":

                # Se verifica que no exista una competencia igual.
                existcompetition = Competition.objects.filter(name=name, url=url,
                                                              startingDate=startingdate,
                                                              deadline=deadline)

                if existcompetition.count() > 0:
                    status = 'El concurso ya existe.'
                else:

                    formcompetition = CompetitionForm(request.POST, request.FILES)
                    print("INICIO.....")
                    # http://blog.josephmisiti.com/how-to-upload-a-photo-to-django-using-ios
                    # if formcompetition.is_valid():
                    user = User.objects.get(id=idUser)
                    print(request.FILES)
                    handle_uploaded_file(request.FILES['image',''])
                    print(request.FILES['image'])
                    print("FIN.....")
                    new_competition = Competition(name=request.POST.get('name'),
                                                  url=request.POST.get('url'),
                                                  startingDate=request.POST.get('startingDate'),
                                                  deadline=request.POST.get('deadline'),
                                                  image=formcompetition.cleaned_data['image'],
                                                  description=request.POST.get('description'),
                                                  user=user)
                    new_competition.save()
                    '''
                    competitionModel = Competition()
                    competitionModel.name = name
                    competitionModel.url = url
                    competitionModel.image = image
                    competitionModel.startingDate = startingDate
                    competitionModel.deadline = deadline
                    competitionModel.description = description
                    user = User.objects.get(id=idUser)

                    competitionModel.user = user
                    competitionModel.save()
                    '''
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
