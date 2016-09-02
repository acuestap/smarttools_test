from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.manage_competition),
    url(r'^(?P<competition_id>\d+)/$', views.get_competition),
    url(r'^competition/create/', login_required(views.create_competition), name='createCompetition'),
    #url(r'^crud/competition/?$', CompetitionCrudView.as_view(), name='crud_competition'),
    #url(r'^competitions/', login_required(WebIndexView.as_view()), name='competitions'),
    #url(r'^home/(?P<company_name>\w+)', HomeView.as_view(), name='home'),
    #url(r'^competition/(?P<company_name>\w+)', CompetitionView.as_view(), name='competition'),
    #url(r'^video/add', AddVideoView.as_view(), name='addvideo'),
]
