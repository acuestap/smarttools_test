import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from competitions.business_logic import get_competitions_from_model
from web.models import Competition, User


@csrf_exempt
def getUrlCompetition(request,competitionName,competition_id):
    print("Redireccionando el concurso:"+competitionName+"/"+competition_id)

    competition = Competition.objects.get(id=competition_id)
    enlace_publico = competition.url

    if enlace_publico == competitionName:
        return HttpResponseRedirect("/#/"+competitionName+"/"+competition_id)
    else:
        return HttpResponseRedirect("/#/")





@csrf_exempt
def get_competition(request, competition_id):
    if request.method == 'GET':
        print("Consultando la info de competition en REST:")
        competition = Competition.objects.get(id=competition_id)
        return HttpResponse(serializers.serialize("json", [competition]))

'''
Edicion de competition que se separo de manage para poder garantizar que las imagenes se guardaran.
'''
@csrf_exempt
def update_competition(request):
    if request.method == 'POST':
        print("Entra a servicios REST de editar un concurso:")
        respuesta = 'Error'
        status_code = 500

        if request.user.is_authenticated():
            id_user = request.user.id
            user = User.objects.get(id=id_user)

            name = request.POST.get('name')
            url = request.POST.get('url')

            # Se verifica que no exista una competencia igual.
            existcompetition = Competition.objects.filter(name=name, url=url, user=user)

            if existcompetition.count() <= 0:
                competition_id = request.POST.get('hdCompetitionId')

                competition = Competition.objects.get(id=competition_id)
                competition.name = name
                competition.url = url
                competition.image = request.FILES['image']
                competition.startingDate = request.POST.get('startingDate')
                competition.deadline = request.POST.get('deadline')
                competition.description = request.POST.get('description')
                competition.active = request.POST.get('active')

                competition.save()

                respuesta = 'OK'
                status_code = 200
            else:
                respuesta = 'El concurso ya existe.'
        else:
             respuesta = 'Usuario no autenticado'

        return JsonResponse({'message': respuesta}, status=status_code)



@csrf_exempt
def manage_competition(request):
    if request.method == 'GET':
        response = get_competitions_from_model(request)
        return JsonResponse(response, safe=False)
    if request.method == 'POST':
        print("Entra a servicios REST de crear concurso:")
        respuesta = 'Error'
        status_code = 500

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

        return JsonResponse({'message': respuesta}, status=status_code)

    if request.method == 'DELETE':
        jsonData = json.loads(request.body.decode('utf-8'))
        competition = Competition.objects.get(id=jsonData['pk'])
        competition.delete()
        return JsonResponse({"status": "OK"})
