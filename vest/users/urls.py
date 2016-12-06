from django.conf.urls import include, url
from .views import Registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', Registration.as_view(), name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
]
