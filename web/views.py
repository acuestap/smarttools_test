import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

from django.shortcuts import render
from rest_framework import serializers

from web.business_logic import login_request_from_model, tareas

# Create your views here.
from web.models import Competition, Video


def index(request):
    return render(request, 'inicio.html')


'''
    REST Service performing login
'''


@csrf_exempt
def login_request(request):
    if request.method == 'POST':
        response = login_request_from_model(request)
        print("Exito")
        print(response)

    else:
        response = {
            'username': '',
            'status': 'NO POST',
            'message': 'Error de metodo.',
        }
    return JsonResponse(response)


'''
    Check if user is logged
'''


@csrf_exempt
def is_logged_user(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False

    print("ENTRO.")
    return JsonResponse({'logged': logged})


'''
    Logout user
'''


@csrf_exempt
def logout_user(request):
    logout(request)
    print("Cerrando sesión....")
    return JsonResponse({'logout': True})


'''
    Add video to competition
'''


@csrf_exempt
def add_video(request):
    if request.method == 'POST':
        new_video = Video(name=request.POST.get('name'),
                          state='En proceso',
                          user_email=request.POST.get('user_email'),
                          message=request.POST.get('message'),
                          original_video=request.FILES['original_video'],
                          uploadDate=datetime.datetime.now(),
                          competition=Competition.objects.filter(id=1).get()
                          )
        new_video.save()

    return HttpResponse(serializers.serialize("json", [new_video]))
