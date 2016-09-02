from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from web.views import index, login_request, logout_user, is_logged_user,add_video, VideosListView

urlpatterns = [
    url(r'^$', index, name='inicio'),
    url(r'^web/', index, name='inicio'),
    url(r'^login', login_request, name='login'),
    url(r'^logout/', logout_user, name='logout'),
    url(r'^islogged/', is_logged_user, name='isLoggedUser'),

    # Prueba del video
    url(r'^videos', VideosListView.as_view(), name='videos'),
    url(r'^video/add', add_video, name='addvideo'),
    url(r'^api/videos/', VideosListView.as_view(), name='videos'),

]
