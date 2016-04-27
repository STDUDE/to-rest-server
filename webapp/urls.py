from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^page/', views.home_page, name='home_page'),
    url(r'^countries/', views.countries, name='countries'),
]