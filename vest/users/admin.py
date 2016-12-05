from django.contrib.gis import admin
from .models import VestUser

admin.site.register(VestUser, admin.GeoModelAdmin)
