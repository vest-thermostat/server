import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ThermostatState
from .serializers import StateSerializer

def send_notification(notification, owner):
    Group("home-%s" % (owner)).send({'text': json.dumps(notification)})

@receiver(post_save, sender=ThermostatState)
def new_state_notification(sender, instance, created, **kwargs):
    if created:
        s = StateSerializer(instance)
        send_notification(s.data, instance.owner)
