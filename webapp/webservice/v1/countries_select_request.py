import json

from django.http import HttpResponse, HttpRequest
from django.template.response import TemplateResponse
from django.views.generic import View

from webapp.dbmodel.models import Country

class CountriesReq(View):
    model = Country
    def get(self, request, *args, **kwargs):
        print("POST REQ CALLED")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['content']
        return content

    def post(self, request, *args, **kwargs):
        print("POST REQ CALLED")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['content']
        return content

