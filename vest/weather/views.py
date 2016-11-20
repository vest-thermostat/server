

from rest_framework import generics
from rest_framework import permissions

from weather.models import Weather
from weather.serializers import WeatherSerializer
from weather.permissions import IsOwner

class WeatherList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )

class WeatherDetail(generics.RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )
