from django.contrib.auth.password_validation import validate_password
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.decorators import permission_classes, api_view

from users.utils import get_ok_response


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate_old_password(self, old_password):
        user = self.context['request'].user
        if not user.check_password(old_password):
            raise serializers.ValidationError('Old password is not correct')
        return old_password

    def validate_password(self, password):
        user = self.context['request'].user
        validate_password(password, user=user)
        return password

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords don\'t match')
        return data


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def change_password(request):
    '''
    Change the user password.
    ---
    serializer: ChangePasswordSerializer
    '''
    serializer = ChangePasswordSerializer(data=request.data,
                                          context={'request': request})
    serializer.is_valid(raise_exception=True)

    user = request.user
    user.set_password(serializer.data['password'])
    user.save()
    return get_ok_response('Password changed successfully')
