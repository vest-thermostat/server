from rest_framework import serializers
from location.models import UserLocation
import rest_framework_gis.serializers as serializers

class LocationSerializer(serializers.GeoFeatureModelSerializer):
    """
    """
    class Meta:
        model = UserLocation
        geo_field = "position"
        fields = (
            "created",
            "owner",
        )
        read_only_fields = (
            "created",
            "owner",
        )
