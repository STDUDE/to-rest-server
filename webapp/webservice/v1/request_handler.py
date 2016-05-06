from django.views.generic import View


class RequestHandler(View):
    COUNTRIES_REQ = 'countries'
    REGIONS_REQ = 'regions'
    CITIES_REQ = 'cities'
    RESORTS_REQ = 'resorts'
    HOTELS_REQ = 'hotels'
    HOTTOURS_REQ = 'hottours'
