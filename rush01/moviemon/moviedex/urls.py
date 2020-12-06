from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^\/(?P<encryptedId>[-\W\w]+)$', views.detail, name='detail'),
]