from django.conf.urls import url
from weather import views

urlpatterns = [
    url(r'^api/$', views.weather_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.weather_detail),
]
