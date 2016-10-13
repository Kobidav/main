from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.units, name='units'),
    #url(r'^inv2$', views.inv2, name='inv3'),
    url(r'^inv3$', views.inv3, name='inv3'),
    url(r'^main/(?P<ffname>\S+)/(?P<fvalue>\S+)/$', views.inv3, name='inv3'),
    url(r'^inv$', views.inv, name='inv'),
    url(r'^mainn/(?P<stype>\S+)/(?P<svalue>\S+)/(?P<fsname>\S+)/$', views.sort_n, name='sort_n'),

]
