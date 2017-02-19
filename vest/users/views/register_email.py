from django.http import Http404

from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from users.notifications import send_verification
from users.utils import (
        get_ok_response,
        get_user_model_class,
        get_user_setting,
        verify_signer_or_bad_request
)
from users.settings import registration_settings
from users.verification import URLParamsSigner


class RegisterEmailSigner(URLParamsSigner):
    salt = 'register-email'
    use_timestamp = True

    @property
    def base_url(self):
        return registration_settings.REGISTER_EMAIL_VERIFICATION_URL

    @property
    def valid_period(self):
        return registration_settings.REGISTER_EMAIL_VERIFICATION_PERIOD


class RegisterEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_email(request):
    '''
    Register new email.
    ---
    serializer: RegisterEmailSerializer
    '''
    user = request.user

    serializer = RegisterEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.data['email']

    template_config = (
        registration_settings.REGISTER_EMAIL_VERIFICATION_EMAIL_TEMPLATES)
    if registration_settings.REGISTER_EMAIL_VERIFICATION_ENABLED:
        signer = RegisterEmailSigner({
            'user_id': user.pk,
            'email': email,
        }, request=request)
        send_verification(user, signer, template_config)
    else:
        email_field = get_user_setting('EMAIL_FIELD')
        setattr(user, email_field, email)
        user.save()

    return get_ok_response('Register email link email sent')


class VerifyEmailSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    timestamp = serializers.IntegerField(required=True)
    signature = serializers.CharField(required=True)


@api_view(['POST'])
def verify_email(request):
    '''
    Verify email via signature.
    ---
    serializer: VerifyEmailSerializer
    '''
    if not registration_settings.REGISTER_EMAIL_VERIFICATION_ENABLED:
        raise Http404()
    user_class = get_user_model_class()
    serializer = VerifyEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.data
    signer = RegisterEmailSigner(data, request=request)
    verify_signer_or_bad_request(signer)

    email_field = get_user_setting('EMAIL_FIELD')
    user = get_object_or_404(user_class.objects.all(), pk=data['user_id'])
    setattr(user, email_field, data['email'])
    user.save()

    return get_ok_response('Email verified successfully')
