from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from clients.business_logic import register_client_in_model

@csrf_exempt
def register_client(request):
    if request.method == 'POST':
        response = register_client_in_model(request)

        return JsonResponse(response)
