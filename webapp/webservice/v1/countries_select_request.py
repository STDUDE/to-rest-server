import json

from django.http import StreamingHttpResponse, JsonResponse
from django.views.generic import View

from webapp.dbmodel.models import Country

class CountriesReq(View):
    model = Country
    def get(self, request, *args, **kwargs):
        print("GET REQ CALLED")
        request = json.loads(request.GET.body)
        if request['req'] is 'country':
            return JsonResponse({
                'message': 'Bad Request',
                'status': 'error'
            })
        else :
            responce_data = Country.objects.all()
            responce = {}
            responce['status'] = 'success'
            responce['body'] = responce_data
            return JsonResponse(responce)

    def post(self, request, *args, **kwargs):
        print("POST REQ CALLED")
        request = json.loads(request.POST.body)
        if request['req'] is 'country':
            return JsonResponse({
                'message': 'Bad Request',
                'status': 'error'
            })
        else :
            responce_data = Country.objects.all()
            responce = {}
            responce['status'] = 'success'
            responce['body'] = responce_data
            return JsonResponse(responce)

