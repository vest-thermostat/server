from django.contrib.gis.db import models

class UserLocation(models.Model):
    """
    """
    owner = models.ForeignKey('users.VestUser', related_name='location', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
