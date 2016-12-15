from django.conf.urls import include, url
from .views import Registration, UserProfileView, UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', Registration.as_view(), name='register'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'},
        name='login'
    ),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'logout.html'},
        name='logout'
    ),
    # url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^edit/$', UserEditView.as_view(), name='edit'),
]
