import logging
logger = logging.getLogger('location.signals')

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.geos import Point

from .models import UserLocation, UserNest, UserJourney
from home.models import ThermostatState

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

def prepare_data(journeys):
    # Getting all location included in a journey.
    details = list(map(lambda x: list(
        map(lambda y: [y.position[0], y.position[1]], x.get_set())
    ), journeys))

    indexes = []
    X = []
    for i, x in enumerate(details):
        indexes.extend(list([i] * len(x)))
        X.extend(x)

    return np.array(X), indexes


def analyze_route(locations, journeys):
    """
    @args{locations}: Locations in progress for the current journey.
    @args{journeys}: Journeay that started from the same location as the one in
        progress to multiple destination.
    """
    X, indexes = prepare_data(journeys)

    match = dict()

    nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(X)
    for loc in locations:
        distances, indices = nbrs.kneighbors(np.array([loc.position[0], loc.position[1]]))
        d = journeys[indexes[indices[0][0]]].destination
        if (match.get(d)):
            match[d] += 1
        else:
            match[d] = 1

    owner = locations[0].owner

    last = ThermostatState.objects.filter(owner=owner).latest()

    for destination, value in match.items():
        print(destination.is_home(), destination.position.coords, value / len(locations))


        if destination.is_home() and (value / len(locations)) > 0.50:
            if last and not last.state:
                ThermostatState(owner=owner, state="On").save()
            return

    if last and last.state:
        ThermostatState(owner=owner, state="Off").save()

@receiver(post_save, sender=UserLocation)
def verify_journey(sender, instance, created, **kwargs):
    lastJourney = instance.owner.get_last_journey()
    dataset = None
    first = None
    departure = None
    if lastJourney:
        dataset = UserLocation.objects.filter(
            owner=instance.owner,
            created__gte=lastJourney.finish.created
        )
        first = lastJourney.finish
        departure = lastJourney.destination
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
        nest = UserNest(
            owner=instance.owner,
            position=Point(longitude, latitude)
        ).save()

        if departure is None:
            departure = UserNest(owner=first.owner, position=first.position).save()

        UserJourney(
            owner=instance.owner,
            start=first,
            finish=instance,
            departure=departure,
            destination=nest,
        ).save()
    else:
        journeySet = UserJourney.objects.filter(departure=departure)
        if len(journeySet) == 0:
            journeySet = UserJourney.objects.filter(owner=first.owner)

        if len(dataset) and len(journeySet):
            analyze_route(dataset, journeySet)
