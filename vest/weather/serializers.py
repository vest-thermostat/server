from rest_framework import serializers
from weather.models import Weather, PrivateWeather, PersonalTemperature
from home.models import ThermostatState

class PersonalTemperatureSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = PersonalTemperature
        fields = (
                "created",
                "temperature",
                "owner",
        )
        read_only_fields = (
                "created",
                "owner",
        )

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
    current_temperature = serializers.SerializerMethodField()
    thermostat_state = serializers.SerializerMethodField()

    def get_current_temperature(self, obj):
        tmp = PersonalTemperature.objects.all().filter(owner=obj.owner).latest()
        if tmp:
            return tmp.temperature
        else:
            return 20.0

    def get_thermostat_state (self, obj):
        tmp = ThermostatState.objects.all().filter(owner=obj.owner).latest()
        if tmp:
            return tmp.state == "On"

        return False

    class Meta:
        model = PrivateWeather
        fields = (
            "created",
            "temperature",
            "humidity",
            "owner",
            "current_temperature",
            "thermostat_state",
        )
        read_only_fields = ("owner",)
