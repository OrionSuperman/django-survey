from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
  url(r'^', include('apps.impression.urls')), # we inserted this line!!!
  # url(r'admin/', include(admin.site.urls)),
)
