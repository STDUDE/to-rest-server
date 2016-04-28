from django.db import models

class RegionManager(models.Manager):
    def all(self, country_id):
        return super(RegionManager, self).get_queryset().filter(country=country_id)


