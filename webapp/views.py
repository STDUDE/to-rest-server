from django.http import HttpResponse
from django.shortcuts import render
from webapp.models import Country
from django.template.response import TemplateResponse

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_page(request):
    return HttpResponse("Hello, second page.")

def countries(request):
    countries_info = Country.objects.is_active()
    print(countries_info)
    #return render_to_response('index.html', countries_info, context_instance=RequestContext(request))
    return TemplateResponse(request, 'index.html', {"countries": countries_info})