from django.core.urlresolvers import reverse
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from home.models import HeatTypeDefinition, HomeDaySchedule, HEAT_TYPE, DAYS_OF_WEEK

class VestUser(AbstractUser):
    """
    """
    home = models.PointField(null=True)

    def get_absolute_url(self):
        return reverse('profile')


@receiver(post_save, sender=VestUser)
def create_default_preference(sender, instance, **kwargs):
    for i, ht in HEAT_TYPE:
        tmp = HeatTypeDefinition(owner=instance, type=ht, temperature=20)
        tmp.save()

    for i, day in DAYS_OF_WEEK:
        tmp = HomeDaySchedule(owner=instance, day=day)
        tmp.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
