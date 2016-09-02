from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^info', views.get_info_client, name='info_client'),
    url(r'^create', views.register_client, name='clientCreate'),
]
