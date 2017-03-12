import logging
logger = logging.getLogger(__name__)

from django.contrib.gis.db import models
from django.contrib.gis.measure import D
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import VestUser

class UserLocation(models.Model):
    """
    """
    owner = models.ForeignKey('users.VestUser', related_name='location', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    position = models.PointField()

    class Meta:
        ordering = ("-created",)
        get_latest_by = "created"

class UserNest(models.Model):
    """
    A Nest is a place where a user would stay more than an hour during a journey.
    """
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)
    position = models.PointField()

    # def find(owner, point):
    #     nest = UserNest.objects.filter(owner=owner)

    def save(self, *args, **kwargs):
        x = UserNest.objects.filter(owner=self.owner, position__distance_lte=(self.position, D(m=30)))
        # Find close Nest for the same owner

        if (x):
            logger.info("Nest already exist for user " + self.owner.username)
            return x[0]

        return super(UserNest, self).save(*args, **kwargs)


class UserJourney(models.Model):
    """
    UserJourney define a user travel to a point to another. A journey always
    finish by staying 60 minute in a nest.
    """
    owner = models.ForeignKey('users.VestUser', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    start = models.ForeignKey('location.UserLocation', related_name="start_location", on_delete=models.CASCADE)
    finish = models.ForeignKey('location.UserLocation', related_name="finish_location", on_delete=models.CASCADE)
    departure = models.ForeignKey('location.UserNest', related_name="start_nest", on_delete=models.CASCADE)
    destination = models.ForeignKey('location.UserNest', related_name="finish_nest", on_delete=models.CASCADE)

    def get_set(self):
        return UserLocation.objects.filter(
            owner=self.owner,
            created__gte=self.start.created,
            created__lte=self.finish.created
        )

    def save(self, *args, **kwargs):
        if (self.start.created > self.finish.created):
            return

        instance = super(UserJourney, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = "created"

from location import signals
