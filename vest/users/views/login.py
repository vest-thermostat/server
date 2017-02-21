from django.contrib import auth
from rest_framework import serializers
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.settings import api_settings
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)

from users.exceptions import BadRequest
from users.settings import registration_settings
from users.utils import get_user_model_class, get_ok_response


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()


class Login(generics.RetrieveAPIView):
    """
    Logs in the user via given login and password.
    ---
    serializer: LoginSerializer
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request, format=None):
        return Response({})

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        user_class = get_user_model_class()
        login_fields = (registration_settings.USER_LOGIN_FIELDS or
                        getattr(user_class, 'LOGIN_FIELDS', None) or
                        [user_class.USERNAME_FIELD])

        for field_name in login_fields:
            kwargs = {
                field_name: data['login'],
                'password': data['password'],
            }
            user = auth.authenticate(**kwargs)
            if user:
                break

        if not user:
            raise BadRequest('Login or password invalid.')

        if should_authenticate_session():
            auth.login(request, user)

        extra_data = {}

        if should_retrieve_token():
            token, _ = Token.objects.get_or_create(user=user)
            extra_data['token'] = token.key

        return get_ok_response('Login successful', extra_data=extra_data)


class Logout(generics.RetrieveAPIView):
    '''
    Logs out the user. returns an error if the user is not
    authenticated.
    '''

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'logout.html'

    def get(self, request):
        if not request.user.is_authenticated():
            raise BadRequest('Not logged in')

        auth.logout(request)

        return get_ok_response('Logout successful')


def should_authenticate_session():
    result = registration_settings.LOGIN_AUTHENTICATE_SESSION
    if result is None:
        result = rest_auth_has_class(SessionAuthentication)
    return result


def should_retrieve_token():
    result = registration_settings.LOGIN_RETRIEVE_TOKEN
    if result is None:
        result = rest_auth_has_class(TokenAuthentication)
    return result


def rest_auth_has_class(cls):
    return cls in api_settings.DEFAULT_AUTHENTICATION_CLASSES
