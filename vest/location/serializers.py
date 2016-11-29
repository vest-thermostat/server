from rest_framework import serializers
from location.models import UserLocation

class LocationSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UserLocation
        fields = (
            "created",
            "latitude",
            "longitude",
        )
