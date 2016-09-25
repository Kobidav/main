from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.units, name='units'),
    url(r'^people$', views.people, name='people'),
    url(r'^inv$', views.inv, name='inv'),
 #    url(r'^table$', views.table, name='table'),
]
