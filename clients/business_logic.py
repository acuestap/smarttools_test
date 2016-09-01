from django.contrib.auth import authenticate, login
import json

from django.contrib.auth.models import User

def register_client_in_model(request):
    status = 'Error'

    if request.method == 'POST':
        json_client = json.loads(request.body.decode('utf-8'))

        first_name = json_client.get('first_name')
        last_name = json_client.get('last_name')
        username = json_client.get('username')
        password = json_client.get('password1')
        password2 = json_client.get('password2')
        email = json_client.get('email')

        if(username != "" and password != "" and password2 != ""
           and email != "" and first_name != "" and last_name != ""):
            existUser = User.objects.filter(username=username)

            if existUser.count() > 0:
                status = 'Cliente ya existe.'
            else:
                if(password != password2):
                    status = 'Las contraseñas no coinciden.'
                else:
                    userModel = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    userModel.save()
                    status = 'OK'
        else:
            status = 'Todos los campos son obligatorios.'
    else:
        status = 'Metodo no POST.'

    return {'status': status}
