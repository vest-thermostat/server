import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels import Group
from .models import PrivateWeather
from .serializers import PrivateWeatherSerializer

def send_notification(notification, owner):
    # logger.info('send_notification. notification = %s', notification)
    Group("weather-%s" % (owner)).send({'text': json.dumps(notification)})

@receiver(post_save, sender=PrivateWeather)
def new_weather_notification(sender, instance, created, **kwargs):
    if created:
        send_notification(PrivateWeatherSerializer(instance).data, instance.owner)
