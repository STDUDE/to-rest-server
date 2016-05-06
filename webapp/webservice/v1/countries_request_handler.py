import json

from django.core import serializers
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse
from django.views.generic import View

from webapp.dbmodel.models import Country
from webapp.webservice.v1.request_handler import RequestHandler


class CountriesReqHandler(View):

    def get(self, request, *args, **kwargs):
        print("GET REQ CALLED")
        responce = {}
        results = [ob.as_json() for ob in Country.objects.all()]
        responce["status"] = "success"
        responce["body"] = results
        print(json.dumps(responce))
        return HttpResponse(json.dumps(responce), content_type="application/json")

    def post(self, request, *args, **kwargs):
        print("POST REQ CALLED")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        req = body['req']

        if req is not RequestHandler.COUNTRIES_REQ:
            return JsonResponse({
                'message': 'Bad Request',
                'status': 'error'
            })
        else:
            responce = {}
            results = [ob.as_json() for ob in Country.objects.all()]
            responce["status"] = "success"
            responce["body"] = results
            print(json.dumps(responce))
            return HttpResponse(json.dumps(responce), content_type="application/json")
