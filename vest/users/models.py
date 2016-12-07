from django.core.urlresolvers import reverse
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class VestUser(AbstractUser):
    """
    """
    home = models.PointField(null=True)

    def get_absolute_url(self):
        return reverse('profile')
