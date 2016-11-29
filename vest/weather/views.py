from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from weather.models import Weather, PrivateWeather
from weather.serializers import WeatherSerializer
from users.models import VestUser
from users.permissions import IsOwner

class WeatherList(viewsets.ModelViewSet):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (
            permissions.IsAuthenticated,
    )

class PrivateWeatherList(WeatherList):
    """
    """
    queryset = PrivateWeather.objects.all()
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
