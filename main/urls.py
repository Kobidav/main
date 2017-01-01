from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inv, name='inv'),
    url(r'^inv$', views.inv, name='inv'),
    url(r'^hard/(?P<hwtype>\S+)/(?P<hwvalue>\S+)/$', views.hard, name='hard'),
    url(r'^main/(?P<stype>\S+)/(?P<svalue>\S+)/$', views.sort_n, name='sort_n'),
]
