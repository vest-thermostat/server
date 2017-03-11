from rest_framework import serializers
from location.models import UserLocation
import rest_framework_gis.serializers as gserializers

class LocationSerializer(gserializers.GeoFeatureModelSerializer):
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

class JourneySerializer(serializers.ModelSerializer):
    """
    """
    start = serializers.SerializerMethodField()
    finish = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    def get_start(self, obj):
        return LocationSerializer(obj.start).data

    def get_finish(self, obj):
        return LocationSerializer(obj.finish).data

    def get_data(self, obj):
        return LocationSerializer(obj.get_set(), many=True).data

    class Meta:
        model = UserLocation
        fields = (
            "owner",
            "created",
            'start',
            'finish',
            'data',
        )
        read_only_fields = (
            "created",
            "owner",
        )
