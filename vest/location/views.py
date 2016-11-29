from rest_framework import viewsets
from rest_framework import permissions

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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
