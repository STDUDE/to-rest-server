from django.conf.urls import url

from webapp import views
from webapp.webservice.v1.countries_request_handler import CountriesReqHandler

urlpatterns = [
    url(r'^countries/', CountriesReqHandler.as_view(), name='countries'),
    url(r'^regions/(?P<country_id>[0-9]{6})/$', views.countries, name='regions'),
    url(r'^cities/(?P<region_id>[0-9]{6})', views.countries, name='cities'),
]

