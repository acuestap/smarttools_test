from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
'''
urlpatterns = [
    url(r'^$', views.manage_video),
]
'''

urlpatterns = [
    url(r'^(\w+)/(\d+)$', views.get_video_by_competition),
    url(r'^add/', views.add_video_by_competition),
]
