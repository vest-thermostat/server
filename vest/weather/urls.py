from django.conf.urls import url
from weather import views

urlpatterns = [
    url(r'^api/$', views.WeatherList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.WeatherDetail.as_view()),
]
