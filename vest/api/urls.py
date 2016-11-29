from django.conf.urls import url, include
from rest_framework import routers

from weather.views import WeatherList, PrivateWeatherList
from location.views import LocationList

router = routers.DefaultRouter()
router.register(r'weather/own', PrivateWeatherList)
router.register(r'weather/public', WeatherList)
router.register(r'location', LocationList)

urlpatterns = [
    url(r'^', include(router.urls)),
]
