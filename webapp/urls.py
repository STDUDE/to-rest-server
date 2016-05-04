from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^page/', views.home_page, name='home_page'),
    url(r'^countries/', views.countries, name='countries'),
    url(r'^webservice/', include('webapp.webservice.urls')),
]