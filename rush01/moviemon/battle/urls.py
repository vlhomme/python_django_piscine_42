from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<moviemon_id>[-\W\w]+)$', views.index),
]