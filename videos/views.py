import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from web.models import Video, Competition


@csrf_exempt
def get_video_by_competition(request, competitionName, competition_id):
    if request.method == 'GET':
        print("Listando videos de: " + competitionName + "/" + competition_id)
        print("url del concurso:" + request.path)
        print("url del concurso:" + request.path_info)
        competition = Competition.objects.get(id=competition_id)
        enlace_publico = competition.url

        if enlace_publico == competitionName:
            response = get_videos_from_model(request, competition_id)
        else:
            response = {'url_valida': 'NO'}

        return JsonResponse(response, safe=False)


@csrf_exempt
def add_video_by_competition(request):
    if request.method == 'POST':
        print("Llego al servicio y se revisa llegada de id competition")
        competition_id = request.POST.get('competition_id');
        new_video = Video(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            state=False,
            user_email=request.POST.get('user_email'),
            message=request.POST.get('message'),
            original_video=request.FILES['original_video'],
            uploadDate=datetime.datetime.now(),
            competition=Competition.objects.filter(id=competition_id).get()
        )

        new_video.save()

        return JsonResponse({'ok': 'video guardado'}, status=200)


'''
    Method returning all videos
'''


def get_videos_from_model(request, competition_id):
    videos = []
    competition = Competition.objects.get(id=competition_id)

    # Si el usuario no se encuentra autenticado solo se le mostraran los videos que ya esten convertidos.

    lista_videos = Video.objects.filter(competition=competition, state=1).all().order_by('uploadDate').reverse()

    if request.user.is_authenticated():
        lista_videos = Video.objects.filter(competition=competition).all().order_by('uploadDate').reverse()

    for c in lista_videos:
        videos.append(video_to_json(c))

    return videos


'''
    Transform product to json format
'''


def video_to_json(video):

    if video.converted_video=='':
        object = {
            'id': video.id,
            'name': video.name,
            'surname': video.surname,
            'user_email': video.user_email,
            'message': video.message,
            'original_video': video.original_video.url,
            #'converted_video': video.converted_video.url,
            'state': video.state,
            # 'competition': video.competition.pk,
            'uploadDate': video.uploadDate
        }
    else:
        object = {
            'id': video.id,
            'name': video.name,
            'surname': video.surname,
            'user_email': video.user_email,
            'message': video.message,
            'original_video': video.original_video.url,
            'converted_video': video.converted_video.url,
            'state': video.state,
            # 'competition': video.competition.pk,
            'uploadDate': video.uploadDate
        }

    return object
