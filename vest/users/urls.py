from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

# from .views import Registration, UserProfileView, UserEditView
from .views import (change_password, login, logout, profile,
                    send_reset_password_link, reset_password,
                    register, verify_registration,
                    register_email, verify_email)

urlpatterns = [
    url('register/$', register),
    url('verify-registration/$', verify_registration),

    url('send-reset-password-link/$', send_reset_password_link),
    url('reset-password/$', reset_password),

    url('login/$', login),
    url('logout/$', logout),

    url('profile/$', profile),

    url('change-password/$', change_password),

    url('register-email/$', register_email),
    url('verify-email/$', verify_email),
]

# urlpatterns = [
#     url(r'^register/$', Registration.as_view(), name='register'),
#     url(r'', include('rest_registration.api.urls')),
#     url(r'^login/$', auth_views.login,
#         {'template_name': 'login.html'},
#         name='login'
#     ),
#     url(r'^logout/$', auth_views.logout,
#         {'template_name': 'logout.html'},
#         name='logout'
#     ),
#     url(r'^edit/$', UserEditView.as_view(), name='edit'),
# ]
