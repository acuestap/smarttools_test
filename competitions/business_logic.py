from django.db.models.fields.files import ImageFieldFile
from web.models import Competition, User


'''
    Transform product to json format
'''


def competition_to_json(competition):
    image_path = '/static/img/profile.png'
    if isinstance(competition.image, ImageFieldFile):
        try:
            image_path = competition.image.url
        except ValueError as e:
            image_path = '/static/img/profile.png'

    object = {
        'id': competition.id,
        'name': competition.name,
        'image': image_path,
        'url': competition.url,
        'startingDate': competition.startingDate,
        'deadline': competition.deadline,
        'active': competition.active
    }
    return object

'''
    Method returning all competitions
'''


def get_competitions_from_model(request):
    competitions = []
    if request.user.is_authenticated():
        iduser = request.user.id
        user = User.objects.get(id=iduser)

    for c in Competition.objects.filter(user=user).all():
        competitions.append(competition_to_json(c))

    return competitions
