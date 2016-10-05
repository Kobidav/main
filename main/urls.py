from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.units, name='units'),
    url(r'^people$', views.people, name='people'),
    url(r'^inv2$', views.inv2, name='inv2'),
    url(r'^inv3$', views.inv3, name='inv3'),
   # url(r'^main/new/$', views.comp_inv, name='comp_inv'),
    url(r'^main/cm/(?P<pk>\S+)/$', views.inv2, name='inv2'),
    url(r'^main/um/(?P<pk>\S+)/(?P<num>\S+)/$', views.inv3, name='inv3'),
    url(r'^inv$', views.inv, name='inv'),
    url(r'^main/sort_by/sort_by/(?P<pk>\S+)/$', views.sort, name='sort'),
 #    url(r'^table$', views.table, name='table'),

]
