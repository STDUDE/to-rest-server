from django.http import JsonResponse

def page_not_found(request):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })

