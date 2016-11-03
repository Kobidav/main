from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^warr$', views.warr, name='warr'),
    url(r'^inv3$', views.inv3, name='inv3'),
    url(r'^mainn/(?P<ffname>\S+)/(?P<fvalue>\S+)/$', views.inv3, name='inv3'),
    url(r'^inv$', views.inv, name='inv'),
    url(r'^main/(?P<stype>\S+)/(?P<svalue>\S+)/(?P<lst_srt>\S+)/(?P<fsname>\S+)/$', views.sort_n, name='sort_n'),
]
