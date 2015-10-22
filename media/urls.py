from django.conf.urls import patterns, url

from media import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getallmedia/$', views.getallmedia, name='getallmedia'),
    url(r'^getallmedia_dt2/$', views.getallmedia_dt2, name='getallmedia_dt2'),  
)