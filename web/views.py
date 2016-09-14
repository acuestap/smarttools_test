import datetime
from celery import chain
from .tasks import *
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .serializers import VideoSerializer
from django.shortcuts import render
from rest_framework.authtoken import serializers


from web.business_logic import login_request_from_model

# Create your views here.
from web.models import Competition, Video
from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework import status
from rest_framework.response import Response


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
    return JsonResponse({'logged': logged})


'''
    Logout user
'''


@csrf_exempt
def logout_user(request):
    logout(request)
    print("Cerrando sesión....")
    return JsonResponse({'logout': True})

