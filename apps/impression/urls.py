from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^submit/$', views.submit, name='svy-submit'),
  url(r'^results/$', views.results, name='svy-results'),
)
