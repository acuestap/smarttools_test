from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from web.views import index, login_request, logout_user, is_logged_user


urlpatterns = [
    url(r'^$', index, name='inicio'),
    url(r'^web/', index, name='inicio'),
    url(r'^login', login_request, name='login'),
    url(r'^logout/', logout_user, name='logout'),
    url(r'^islogged/', is_logged_user, name='isLoggedUser'),
]
