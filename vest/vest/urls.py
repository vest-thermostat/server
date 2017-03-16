"""vest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib.gis import admin
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view

from weather.views import WeatherList, PrivateWeatherList, PersonalTemperatureList, TemperatureView
from location.views import LocationList, JourneyList, NestList
from home.views import HomeView
# from users.views import UserProfileView

router = routers.DefaultRouter()
router.register(r'weather/own', PrivateWeatherList, base_name='weather_own')
router.register(r'weather/public', WeatherList, base_name='weather_public')
router.register(r'weather/set', PersonalTemperatureList, base_name='weather_set')
router.register(r'location/journey', JourneyList, base_name='journey')
router.register(r'location/nest', NestList, base_name='nest')
router.register(r'location', LocationList, base_name='location')
router.register(r'home', HomeView, base_name='home')
# router.register(r'users', UserProfileView, base_name='users')

urlpatterns = [
    url(r'^api-auth/$', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'users/', include('users.urls')),
    url(r'weather/$', TemperatureView.as_view({'get': 'list'})),
    url(r'docs/$', get_swagger_view(title='VEST API')),
    url(r'^', include(router.urls)),
]
