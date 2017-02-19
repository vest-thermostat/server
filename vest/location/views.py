from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from location.models import UserLocation
from location.serializers import LocationSerializer
from users.permissions import IsOwner

class LocationList(viewsets.ModelViewSet):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = UserLocation.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (
            permissions.IsAuthenticated,
            IsOwner,
    )

    def get_queryset(self):
        return UserLocation.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        if not serializer.is_valid():
            raise ValidationError()

        serializer.save(owner=self.request.user)
