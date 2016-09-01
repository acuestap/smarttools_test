from web.models import Competition
'''
    Transform product to json format
'''


def competition_to_json(competition):
    object = {
        'id': competition.id,
        'name': competition.name,
        'image': competition.image,
        'url': competition.url,
        'startingDate': competition.startingDate,
        'deadline': competition.deadline
        #'user_id': competition.user_id
    }
    return object

'''
    Method returning all competitions
'''


def get_competitions_from_model():

    competitions = []

    for c in Competition.objects.all():
        competitions.append(competition_to_json(c))

    return competitions
