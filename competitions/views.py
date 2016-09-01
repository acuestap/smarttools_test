from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from competitions.business_logic import get_competitions_from_model

@csrf_exempt
def get_all_competitions(request):
    if request.method == 'GET':
        response = get_competitions_from_model()
        return JsonResponse(response,safe=False)
