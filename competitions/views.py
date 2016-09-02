import json

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from competitions.business_logic import get_competitions_from_model
from web.models import Competition, User


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
        respuesta = 'Error'
        status_code = 500
        if request.method == 'POST':
            if request.user.is_authenticated():
                id_user = request.user.id
                user = User.objects.get(id=id_user)

                name = request.POST.get('name')
                url = request.POST.get('url')

                # Se verifica que no exista una competencia igual.
                existcompetition = Competition.objects.filter(name=name, url=url, user=user)

                if existcompetition.count() <= 0:
                    new_competition = Competition(
                        name=name,
                        url=url,
                        image=request.FILES['image'],
                        startingDate=request.POST.get('startingDate'),
                        deadline=request.POST.get('deadline'),
                        description=request.POST.get('description'),
                        active=request.POST.get('active'),
                        user=user
                    )
                    new_competition.save()

                    respuesta = 'OK'
                    status_code = 200
                else:
                    respuesta = 'El concurso ya existe.'
            else:
                 respuesta = 'Usuario no autenticado'
        print(respuesta)

        return JsonResponse({'message': respuesta}, status=status_code)

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
        return JsonResponse({"status": "OK"})

    if request.method == 'DELETE':
        jsonData = json.loads(request.body.decode('utf-8'))
        competition = Competition.objects.get(id=jsonData['pk'])
        competition.delete()
        return JsonResponse({"status": "OK"})