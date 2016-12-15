from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer

from weather.models import Weather, PrivateWeather
from weather.serializers import WeatherSerializer, PrivateWeatherSerializer
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

class PrivateWeatherList(viewsets.ModelViewSet):
    """
    """
    queryset = PrivateWeather.objects.all()
    serializer_class = PrivateWeatherSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'weather_overview.html'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
