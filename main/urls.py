from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.units, name='units'),
]
