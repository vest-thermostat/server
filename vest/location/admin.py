from django.contrib.gis import admin
from .models import UserLocation, UserNest, UserJourney

admin.site.register(UserLocation, admin. GeoModelAdmin)
admin.site.register(UserNest, admin. GeoModelAdmin)
admin.site.register(UserJourney, admin. GeoModelAdmin)
