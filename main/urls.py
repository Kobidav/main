from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inv, name='inv'),
    url(r'^inv$', views.inv, name='inv'),
    url(r'^main/(?P<stype>\S+)/(?P<svalue>\S+)/(?P<lst_srt>\S+)/(?P<fsname>\S+)/(?P<shw_data>\S+)/$', views.sort_n, name='sort_n'),
]
