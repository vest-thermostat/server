import json
import logging
logger = logging.getLogger(__name__)
import numpy as np
from sklearn.cluster import DBSCAN

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.geos import Point

from .models import UserLocation, UserNest, UserJourney
from channels import Group
from .serializers import LocationSerializer

def send_notification(notification, owner):
    Group("location-%s" % (owner)).send({'text': json.dumps(notification)})

@receiver(post_save, sender=UserLocation)
def new_location_notification(sender, instance, created, **kwargs):
    if created:
        s = LocationSerializer(instance)
        send_notification(s.data, instance.owner)


def detect_nest(datas):
    """
    @desc: A cluster return labels if no cluster was found the array is set
        to -1 everywhere.

    @param{datas}: Cluster labels
    """
    for x in datas:
        if x == 0:
            return True

    return False


@receiver(post_save, sender=UserLocation)
def verify_journey(sender, instance, created, **kwargs):
    lastJourney = instance.owner.get_last_journey()
    dataset = None
    first = None
    if lastJourney:
        dataset = UserLocation.objects.filter(
            owner=instance.owner,
            created__gte=lastJourney.finish.created
        )
        first = lastJourney.finish
    else:
        dataset = UserLocation.objects.filter(owner=instance.owner)
        first = dataset[0]

    x = list(map(lambda x: x.position[0], dataset))
    y = list(map(lambda x: x.position[1], dataset))
    X = np.array(list(zip(x, y)))

    db = DBSCAN(eps=0.0003, min_samples=12, metric='euclidean')
    y_db = db.fit_predict(X)

    if (detect_nest(y_db)):
        longitude = sum(X[y_db == 0, 0]) / float(len(X[y_db == 0, 0]))
        latitude = sum(X[y_db == 0, 1]) / float(len(X[y_db == 0, 1]))
        logger.info("New nest detected !")
        UserNest(owner=instance.owner, position=Point(longitude, latitude)).save()
        UserJourney(owner=instance.owner, start=first, finish=instance).save()
