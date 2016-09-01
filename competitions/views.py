from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from competitions.business_logic import get_competitions_from_model, create_competition_in_model


@csrf_exempt
def get_all_competitions(request):
    if request.method == 'GET':
        response = get_competitions_from_model()
        return JsonResponse(response,safe=False)


@csrf_exempt
def create_competition(request):
    if request.method == 'POST':
        response = create_competition_in_model(request)

        return JsonResponse(response)


