from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.decorators import serializer_class_getter
from users.settings import registration_settings


@serializer_class_getter(
    lambda: registration_settings.PROFILE_SERIALIZER_CLASS)
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def profile(request):
    '''
    Get or set user profile.
    '''
    serializer_class = registration_settings.PROFILE_SERIALIZER_CLASS
    if request.method == 'GET':
        serializer = serializer_class(instance=request.user)
    elif request.method in ['POST', 'PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = serializer_class(
            instance=request.user,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

    return Response(serializer.data)
