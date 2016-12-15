from rest_framework import serializers
from weather.models import Weather, PrivateWeather

class WeatherSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Weather
        fields = (
            "created",
            "temperature",
            "humidity",
        )

class PrivateWeatherSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = PrivateWeather
        fields = (
            "created",
            "temperature",
            "humidity",
            "owner",
        )
        read_only_fields = ("owner",)
