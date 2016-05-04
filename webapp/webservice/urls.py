from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^countries/', views.countries, name='countries'),
    url(r'^regions/(?P<country_id>[0-9]{6})/$', views.regions_select, name='regions'),
    url(r'^cities/(?P<region_id>[0-9]{6})', views.countries, name='cities'),
]