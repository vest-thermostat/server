from django.conf.urls import include, url

from .views import (change_password, profile,
                    send_reset_password_link, reset_password,
                    register, verify_registration,
                    register_email, verify_email)
import users.views as views

urlpatterns = [
    url('register/$', views.Register.as_view(), name='register'),
    url('verify-registration/$', verify_registration),

    url('send-reset-password-link/$', send_reset_password_link),
    url('reset-password/$', reset_password, name='reset-password'),

    url('login/$', views.Login.as_view(), name='login'),
    url('logout/$', views.Logout.as_view(), name='logout'),
    url('profile/$', profile),

    url('change-password/$', change_password),

    url('register-email/$', register_email),
    url('verify-email/$', verify_email),
]
