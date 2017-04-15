from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^write/?$', views.write, name='write'),
    url(r'^(?P<abc>[0-9]+)/$', views.detail, name='detail'),
    url(r'^collect/?$', views.collect, name='collect'),
    url(r'^send/?$', views.send, name='send'),
]
