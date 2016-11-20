from django.db import models

class UserLocation(models.Model):
    """
    """
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.VestUser', related_name='location', on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
