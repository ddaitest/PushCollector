from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<msg_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<abc>[0-9]+)/$', views.detail, name='detail'),
    url(r'^collect/?$', views.collect, name='collect'),
    url(r'^abc/?$', views.abc, name='abc'),
]
