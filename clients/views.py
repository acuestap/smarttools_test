import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from clients.business_logic import register_client_in_model
from web.models import User

@csrf_exempt
def register_client(request):
    if request.method == 'POST':
        response = register_client_in_model(request)

        return JsonResponse(response)


@csrf_exempt
def get_info_client(request):
    if request.user.is_authenticated():
        id_user = request.user.id
        user = User.objects.get(id=id_user)
        first_name = user.first_name
        last_name = user.last_name
        email = user.email

        jsonData = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        return JsonResponse(jsonData)
'''
@csrf_exempt
def manage_clients(request):
    if request.method == 'GET':
        jsonData = json.loads(request.body.decode('utf-8'))
        client = User.objects.get(id=jsonData['pk'])
        client.first_name = jsonData.get('first_name')
        client.last_name = jsonData.get('last_name')
        client.username = jsonData.getname('')
        client.email = jsonData.get('email')

        return JsonResponse({"data": client})
'''
