import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserLocation
from channels import Group
from .serializers import LocationSerializer

def send_notification(notification, owner):
    Group("location-%s" % (owner)).send({'text': json.dumps(notification)})

@receiver(post_save, sender=UserLocation)
def new_location_notification(sender, instance, created, **kwargs):
    if created:
        s = LocationSerializer(instance)
        send_notification(s.data, instance.owner)

# @receiver(post_save, sender=UserLocation)
# def handle_new_location(sender, instance, **kwargs):
#     home = instance.owner.home
#     if home is null:
#         return

#     distance = Distance(instance.location, home)
#     if (distance.km < 10):
#         print("ON")
