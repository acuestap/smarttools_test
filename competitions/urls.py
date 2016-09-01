from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from competitions.views import get_all_competitions


urlpatterns = [
    url(r'^competitions/', login_required(get_all_competitions), name='competitions'),
    #url(r'^competitions/', login_required(WebIndexView.as_view()), name='competitions'),
    #url(r'^home/(?P<company_name>\w+)', HomeView.as_view(), name='home'),
    #url(r'^competition/(?P<company_name>\w+)', CompetitionView.as_view(), name='competition'),
    #url(r'^video/add', AddVideoView.as_view(), name='addvideo'),
]
