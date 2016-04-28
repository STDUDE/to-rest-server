from django.http import HttpResponse
from django.template.response import TemplateResponse

from webapp.dbmodel.models import *


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_page(request):
    return HttpResponse("Hello, second page.")

def countries(request):
    countries_info = Country.objects.all()
    print(countries_info)
    return TemplateResponse(request, 'index.html', {"countries": countries_info})
