from django.conf.urls import url, include
from rest_framework import routers

from weather.views import WeatherList, PrivateWeatherList
from location.views import LocationList
from users.views import UserProfileView

router = routers.DefaultRouter()
# router.register(r'weather/own', PrivateWeatherList, base_name='weather_own')
# router.register(r'weather/public', WeatherList, base_name='weather_public')
# router.register(r'location', LocationList, base_name='location')
# router.register(r'users', UserProfileView, base_name='users')

router.register(r'weather/own', PrivateWeatherList)
router.register(r'weather/public', WeatherList)
router.register(r'location', LocationList)
router.register(r'users', UserProfileView)



urlpatterns = [
    url(r'^', include(router.urls)),
]
