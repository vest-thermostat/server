from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import VestUser

class UserLocation(models.Model):
    """
    """
    owner = models.ForeignKey('users.VestUser', related_name='location', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    position = models.PointField()

from location import signals
