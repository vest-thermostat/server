from django.contrib.gis import admin
from .models import UserLocation

admin.site.register(UserLocation, admin. GeoModelAdmin)
