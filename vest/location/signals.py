import json
import logging
logger = logging.getLogger('location.signals')

from django.db.models.signals import post_save
from django.dispatch import receiver

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

def notificate(message, owner):
    send_notification({
        'type': 'notifications',
        'message': message,
    }, owner)

@receiver(post_save, sender=UserNest)
def notificate_nest(sender, instance, created, **kwargs):
    if created:
        logger.info('notificating new nest')
        notificate("New nest saved.", instance.owner)

@receiver(post_save, sender=UserJourney)
def notificate_journey(sender, instance, created, **kwargs):
    if created:
        logger.info('notificating new journey')
        notificate("New journey saved.", instance.owner)
