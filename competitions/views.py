from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from competitions.business_logic import get_competitions_from_model, create_competition_in_model
# from djng.views.crud import NgCRUDView

from web.models import Competition, User
import json


@csrf_exempt
def create_competition(request):
    if request.method == 'POST':
        response = create_competition_in_model(request)

        return JsonResponse(response)


@csrf_exempt
def get_competition(request, competition_id):
    if request.method == 'GET':
        competition = Competition.objects.get(id=competition_id)
        return HttpResponse(serializers.serialize("json", [competition]))


@csrf_exempt
def manage_competition(request):
    if request.method == 'GET':
        response = get_competitions_from_model(request)
        return JsonResponse(response, safe=False)
        '''
        NO ME TRAE LOS REGISTOS AUN...
        competitions = Competition.objects.all()
        return HttpResponse(serializers.serialize("json", competitions))
        '''
    if request.method == 'POST':
        status = 'OK'
        if request.user.is_authenticated():
            idUser = request.user.id
            user = User.objects.get(id=idUser)

            jsonData = json.loads(request.body.decode('utf-8'))
            name = jsonData.get('name')
            url = jsonData.get('url')
            startingdate = jsonData.get('startingDate')
            deadline = jsonData.get('deadline')
            description = jsonData.get('description')
            active = jsonData.get('active')

            # Se verifica que no exista una competencia igual.
            existcompetition = Competition.objects.filter(name=name, url=url, user=user)


            print("Creando concurso...")
            if existcompetition.count() <= 0:
                jsonData = json.loads(request.body.decode('utf-8'))
                competition = Competition()
                competition.name = name
                competition.url = url
                competition.startingDate = startingdate
                competition.deadline = deadline
                competition.description = description
                competition.active = active
                competition.user = user

                competition.save()
                print("Concursi creado.....")
            else:
                status = 'El concurso ya existe.'
        else:
            status = 'Usuario no autenticado'

        # return HttpResponse(serializers.serialize("json", [competition]))
        return JsonResponse({"status": status})

    if request.method == 'PUT':
        jsonData = json.loads(request.body.decode('utf-8'))
        competition = Competition.objects.get(id=jsonData['pk'])
        competition.name = jsonData.get('name')  # jsonData['name']
        competition.url = jsonData.get('url')  # jsonData['url']
        competition.startingDate = jsonData.get('startingDate')  # jsonData['startingDate']
        competition.deadline = jsonData.get('deadline')  # jsonData['deadline']
        competition.description = jsonData.get('description')  # jsonData['description']
        competition.active = jsonData.get('active')  # jsonData['description']

        competition.save()
        # return HttpResponse(serializers.serialize("json", {competition}))
        return JsonResponse({"status": "OK"})

    if request.method == 'DELETE':
        jsonData = json.loads(request.body.decode('utf-8'))
        competition = Competition.objects.get(id=jsonData['pk'])
        competition.delete()
        return JsonResponse({"status": "OK"})

'''
# Vista para gestionar el CRUD del modelo Competition ---PERO AUN NO ME FUNCIONA
class CompetitionCrudView(NgCRUDView):
    model = Competition
'''
