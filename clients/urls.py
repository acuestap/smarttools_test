from django.conf.urls import url
from .views import register_client

urlpatterns = [
    url(r'^client/create', register_client, name='clientCreate'),
]
