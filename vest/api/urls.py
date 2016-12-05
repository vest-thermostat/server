from django.conf.urls import url, include
from rest_framework import routers

from weather.views import WeatherList, PrivateWeatherList
from location.views import LocationList

router = routers.DefaultRouter()
router.register(r'weather/own', PrivateWeatherList, 'weather_own')
router.register(r'weather/public', WeatherList, 'weather_public')
router.register(r'location', LocationList, 'location')

urlpatterns = [
    url(r'^', include(router.urls)),
]
