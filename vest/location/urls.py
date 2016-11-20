from django.conf.urls import url
from location import views

urlpatterns = [
    url(r'^api/$', views.LocationList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
]
