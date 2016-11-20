from django.conf.urls import url
from weather import views

urlpatterns = [
    url(r'^weathers/$', views.weather_list),
    url(r'^weathers/(?P<pk>[0-9]+)/$', views.weather_detail),
]
